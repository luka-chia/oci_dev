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

public class OCIS3Demo_createBucket {

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
        
        createBucket(s3Client);
        s3Client.close();
    }

    //上传对象
    private static void createBucket(S3Client s3Client){
        String bucket = "new-bucket";
        // OCI 上如果 bucket 已存在同名，会报错，先做个存在性检查
        boolean exists;
        try {
            s3Client.headBucket(HeadBucketRequest.builder().bucket(bucket).build());
            exists = true;
        } catch (Exception ex) {
            exists = false;
        }

        if (exists) {
            System.out.println("Bucket already exists: " + bucket);
            return;
        }

        // 在 OCI 端通常不需要 LocationConstraint（由端点所属 region 决定）
        s3Client.createBucket(CreateBucketRequest.builder().bucket(bucket).build());
        s3Client.waiter().waitUntilBucketExists(HeadBucketRequest.builder().bucket(bucket).build());
        System.out.println("Created OCI bucket: " + bucket);

    }
}