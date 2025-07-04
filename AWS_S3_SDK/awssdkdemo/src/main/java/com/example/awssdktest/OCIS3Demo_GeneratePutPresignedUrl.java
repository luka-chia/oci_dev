package com.example.awssdktest;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.model.*;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.PresignedPutObjectRequest;
import software.amazon.awssdk.services.s3.presigner.model.PutObjectPresignRequest;

import java.io.File;
import java.io.FileInputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;

public class OCIS3Demo_GeneratePutPresignedUrl{
    public static void main(String[] args) {
        // OCI S3 兼容配置
        String ociEndpoint = "https://sehubjapacprod.compat.objectstorage.us-ashburn-1.oraclecloud.com";
        String accessKey = "286f20dee8de157e55b63cd56b828b401753b28b";  // OCI 生成的 S3 兼容访问密钥
        String secretKey = "H9P1j3I/oOtKpixXk7wuwdf5r8LCH0JjZ6UJlpBToss=";  // OCI 生成的 S3 兼容密钥
        String bucketName = "Luka-bucket-ashburn";

        // 0. 创建 S3Client（适配 OCI）
        S3Client s3Client = S3Client.builder()
                .endpointOverride(URI.create(ociEndpoint))  // OCI S3 兼容端点
                .serviceConfiguration(
                    S3Configuration.builder()
                    .pathStyleAccessEnabled(true) // 关键：强制使用 Path Style
                    .build())
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(accessKey, secretKey)))
                .region(Region.of("us-ashburn-1"))  // 任意值（OCI 会忽略，但 SDK 要求必填）
                .build();

        // 1. 生成上传预签名 URL
        generatePutPresignedUrl(s3Client, bucketName);
        s3Client.close();
    }

    // 生成上传预签名URL（有效期15分钟）
    private static void generatePutPresignedUrl(S3Client s3Client, String bucket) {
        String filePath = "/Users/luka/Downloads/Oracle_Document.pdf";
        S3Presigner presigner = S3Presigner.builder()
                .endpointOverride(s3Client.serviceClientConfiguration().endpointOverride().orElse(null))
                .credentialsProvider(s3Client.serviceClientConfiguration().credentialsProvider())
                .region(s3Client.serviceClientConfiguration().region())
                .build();

        PresignedPutObjectRequest presignedRequest = presigner.presignPutObject(
            PutObjectPresignRequest.builder()
                .signatureDuration(Duration.ofMinutes(15))
                .putObjectRequest(PutObjectRequest.builder()
                    .bucket(bucket)
                    .key("Oracle_Document.pdf_by_presignPutObject")
                    .contentType("application/octet-stream") // 强制二进制流类型
                    .build())
                .build());

        String presignedUrl = presignedRequest.url().toString();
        System.out.println("OCI 预签名上传URL: \n" + presignedUrl);

        Path file = Paths.get(filePath);
        try {
            File file1 = file.toFile();
            URL url = new URL(presignedUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            
            // 配置请求
            conn.setRequestMethod("PUT");
            conn.setDoOutput(true);
            conn.setRequestProperty("Content-Type", "application/octet-stream");
            
            // 上传文件流
            try (FileInputStream fis = new FileInputStream(file1);
                 OutputStream os = conn.getOutputStream()) {
                byte[] buffer = new byte[8192];
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead);
                }
            }
            // 获取响应状态码
            int statusCode = conn.getResponseCode();
            System.out.println("上传状态码: " + statusCode); // 成功返回 200
        } catch (Exception e) {
            e.printStackTrace();
        }

        //验证上传本地文件（需安装 curl）curl -X PUT --upload-file "localfile.txt" -H "Content-Type: application/octet-stream" url
        presigner.close();
    }
}