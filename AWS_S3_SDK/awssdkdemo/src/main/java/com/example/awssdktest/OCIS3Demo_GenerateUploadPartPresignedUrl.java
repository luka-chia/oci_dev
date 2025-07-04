package com.example.awssdktest;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.model.*;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.PresignedUploadPartRequest;
import software.amazon.awssdk.services.s3.presigner.model.UploadPartPresignRequest;

import java.io.File;
import java.io.FileInputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class OCIS3Demo_GenerateUploadPartPresignedUrl {
    public static void main(String[] args) {
        // OCI S3 兼容配置
        String ociEndpoint = "https://sehubjapacprod.compat.objectstorage.us-ashburn-1.oraclecloud.com";
        String accessKey = "286f20dee8de157e55b63cd56b828b401753b28b";
        String secretKey = "H9P1j3I/oOtKpixXk7wuwdf5r8LCH0JjZ6UJlpBToss=";
        String bucketName = "Luka-bucket-ashburn";
        String objectKey = "test_part_upload.pptx";

        // 创建 S3Client
        S3Client s3Client = S3Client.builder()
                .endpointOverride(URI.create(ociEndpoint))
                .serviceConfiguration(
                    S3Configuration.builder()
                    .pathStyleAccessEnabled(true)
                    .build())
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(accessKey, secretKey)))
                .region(Region.of("us-ashburn-1"))
                .build();
        
        try {
            // 1. 初始化分片上传
            String uploadId = initMultipartUpload(s3Client, bucketName, objectKey);
            System.out.println("Upload ID: " + uploadId);

            // 2. 生成分片预签名URL
            int partNumber = 1;
            String presignedUrl = generatePartPresignedUrl(
                s3Client, 
                bucketName, 
                objectKey, 
                uploadId, 
                partNumber, 
                1, // 有效期1小时
                TimeUnit.HOURS
            );
            System.out.println("Part " + partNumber + " Presigned URL: \n" + presignedUrl);

            // 3. 实际上传分片并获取真实ETag
            String eTag = uploadPartAndGetETag(presignedUrl);
            System.out.println("Part " + partNumber + " ETag: " + eTag);

            // 4. 验证分片是否上传成功
            if (verifyPartUpload(s3Client, bucketName, objectKey, uploadId, partNumber, eTag)) {
                // 5. 完成分片上传
                List<CompletedPart> completedParts = new ArrayList<>();
                completedParts.add(CompletedPart.builder()
                    .partNumber(partNumber)
                    .eTag(eTag)
                    .build());

                completeMultipartUpload(s3Client, bucketName, objectKey, uploadId, completedParts);
            } else {
                System.err.println("分片验证失败，请检查上传情况");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            s3Client.close();
        }
    }

    private static String initMultipartUpload(S3Client s3Client, String bucket, String key) {
        CreateMultipartUploadRequest request = CreateMultipartUploadRequest.builder()
            .bucket(bucket)
            .key(key)
            .build();
        return s3Client.createMultipartUpload(request).uploadId();
    }

    private static String generatePartPresignedUrl(
            S3Client s3Client, String bucket, String key, 
            String uploadId, int partNumber, 
            long expiry, TimeUnit timeUnit) {
        
        S3Presigner presigner = S3Presigner.builder()
            .endpointOverride(s3Client.serviceClientConfiguration().endpointOverride().orElse(null))
            .credentialsProvider(s3Client.serviceClientConfiguration().credentialsProvider())
            .region(s3Client.serviceClientConfiguration().region())
            .build();

        UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
            .bucket(bucket)
            .key(key)
            .uploadId(uploadId)
            .partNumber(partNumber)
            .build();

        PresignedUploadPartRequest presignedRequest = presigner.presignUploadPart(
            UploadPartPresignRequest.builder()
                .signatureDuration(Duration.ofHours(expiry))
                .uploadPartRequest(uploadPartRequest)
                .build());

        presigner.close();
        return presignedRequest.url().toString();
    }

    private static String uploadPartAndGetETag(String presignedUrl) {
        String filePath = "/Users/luka/Downloads/test_part_upload.pptx";
        Path file = Paths.get(filePath);
        
        try {
            URL url = new URL(presignedUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            
            // 配置请求
            conn.setRequestMethod("PUT");
            conn.setDoOutput(true);
            conn.setRequestProperty("Content-Type", "application/octet-stream");
            
            // 上传文件流
            try (FileInputStream fis = new FileInputStream(file.toFile());
                 OutputStream os = conn.getOutputStream()) {
                byte[] buffer = new byte[8192];
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead);
                }
            }
            
            // 获取响应状态码和ETag
            int statusCode = conn.getResponseCode();
            String eTag = conn.getHeaderField("ETag");
            
            if (statusCode == 200 && eTag != null) {
                // 移除ETag中的双引号
                return eTag.replace("\"", "");
            } else {
                throw new RuntimeException("上传失败，状态码: " + statusCode);
            }
        } catch (Exception e) {
            throw new RuntimeException("分片上传失败", e);
        }
    }

    private static boolean verifyPartUpload(S3Client s3Client, String bucket, String key, 
                                         String uploadId, int partNumber, String expectedETag) {
        try {
            ListPartsRequest listRequest = ListPartsRequest.builder()
                .bucket(bucket)
                .key(key)
                .uploadId(uploadId)
                .build();

            List<Part> parts = s3Client.listParts(listRequest).parts();
            for (Part part : parts) {
                if (part.partNumber() == partNumber) {
                    String actualETag = part.eTag().replace("\"", "");
                    if (actualETag.equals(expectedETag)) {
                        System.out.println("分片验证成功");
                        return true;
                    } else {
                        System.err.println("ETag不匹配，预期: " + expectedETag + "，实际: " + actualETag);
                        return false;
                    }
                }
            }
            System.err.println("未找到指定分片");
            return false;
        } catch (Exception e) {
            System.err.println("验证分片时出错: " + e.getMessage());
            return false;
        }
    }

    private static void completeMultipartUpload(
            S3Client s3Client, String bucket, String key, 
            String uploadId, List<CompletedPart> parts) {
        
        try {
            CompletedMultipartUpload completedUpload = CompletedMultipartUpload.builder()
                .parts(parts)
                .build();

            CompleteMultipartUploadRequest completeRequest = CompleteMultipartUploadRequest.builder()
                .bucket(bucket)
                .key(key)
                .uploadId(uploadId)
                .multipartUpload(completedUpload)
                .build();

            CompleteMultipartUploadResponse response = s3Client.completeMultipartUpload(completeRequest);
            System.out.println("分片上传完成！对象ETag: " + response.eTag());
        } catch (S3Exception e) {
            System.err.println("完成分片上传失败: " + e.awsErrorDetails().errorMessage());
            throw e;
        }
    }
}