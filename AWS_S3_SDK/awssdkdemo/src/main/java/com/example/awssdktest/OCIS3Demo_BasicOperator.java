package com.example.awssdktest;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.model.*;
import java.net.URI;
import java.nio.file.Paths;
import java.time.Instant;

public class OCIS3Demo_BasicOperator {

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
        
        // 1. PUT对象
        putObject(s3Client, bucketName);

        // 2. Get对象
        getObject(s3Client, bucketName);

        // 3. 删除对象
        //deleteObject(s3Client, bucketName);
        
        // 4. 查询对象
        listObjects(s3Client, bucketName);

        // 5. 获取对象元数据
        headObject(s3Client, bucketName);

        s3Client.close();
    }

    //上传对象
    private static void putObject(S3Client s3Client, String bucket){
        String filePath = "/Users/luka/Downloads/Oracle_Document.pdf";
        PutObjectResponse response = s3Client.putObject(
                PutObjectRequest.builder()
                .bucket(bucket)
                .key("Oracle_Document.pdf_by_putObject")
                .contentType("text/plain") // 显式设置 MIME 类型
                .build(),
                RequestBody.fromFile(Paths.get(filePath))
            );

            System.out.println("上传成功！ETag: " + response.eTag());

    }
    // 列出对象
    private static void listObjects(S3Client s3Client, String bucket) {
        ListObjectsV2Response response = s3Client.listObjectsV2(ListObjectsV2Request.builder()
                .bucket(bucket)
                .build());
        System.out.println("Bucket 中的对象列表:");
        response.contents().forEach(obj -> System.out.println(" - " + obj.key()));
    }

    // Get对象
    private static void getObject(S3Client s3Client, String bucket) {
        String localFilePath = "/Users/luka/Downloads/abc.yaml";
        s3Client.getObject(
                GetObjectRequest.builder()
                        .bucket(bucket)
                        .key("thumb_k8s.yaml")
                        .build(),
                ResponseTransformer.toFile(Paths.get(localFilePath)) // 保存到本地
        );
        System.out.println("文件下载完成: " + localFilePath);
    }

    // 删除对象
    private static void deleteObject(S3Client s3Client, String bucket) {
        String key = "2025-03.pdf";
        s3Client.deleteObject(DeleteObjectRequest.builder()
                .bucket(bucket)
                .key(key)
                .build());
        System.out.println("删除成功: " + key);
    }

    // 获取对象元数据
    private static void headObject(S3Client s3Client, String bucket){
        // 获取对象元数据
        HeadObjectResponse headResponse = s3Client.headObject(
            HeadObjectRequest.builder()
                .bucket(bucket)
                .key("oss-image-thumbnail-0.0.1-SNAPSHOT.jar")
                .build()
        );

        // 提取元数据
        long fileSize = headResponse.contentLength(); // 文件大小（字节）
        Instant lastModified = headResponse.lastModified(); // 最后修改时间
        String eTag = headResponse.eTag(); // 文件的ETag（哈希值）
        String contentType = headResponse.contentType(); // MIME类型（如text/plain）

        System.out.println("文件元数据:");
        System.out.println(" - 大小: " + fileSize + " bytes");
        System.out.println(" - 最后修改时间: " + lastModified);
        System.out.println(" - ETag: " + eTag);
        System.out.println(" - Content-Type: " + contentType);
    }        
}