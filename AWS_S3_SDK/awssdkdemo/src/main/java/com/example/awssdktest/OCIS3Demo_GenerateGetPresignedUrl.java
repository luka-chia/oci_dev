package com.example.awssdktest;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.model.*;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.GetObjectPresignRequest;
import software.amazon.awssdk.services.s3.presigner.model.PresignedGetObjectRequest;

import java.net.URI;
import java.time.Duration;

public class OCIS3Demo_GenerateGetPresignedUrl {

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
        
        // 1. 生成下载预签名 URL
        generateGetPresignedUrl(s3Client, bucketName);

        s3Client.close();
    }

    // 生成下载预签名URL 有效期10分钟
    private static void generateGetPresignedUrl(S3Client s3Client, String bucket) {
        S3Presigner presigner = S3Presigner.builder()
                .endpointOverride(s3Client.serviceClientConfiguration().endpointOverride().orElse(null))
                .credentialsProvider(s3Client.serviceClientConfiguration().credentialsProvider())
                .region(s3Client.serviceClientConfiguration().region())
                .build();

        PresignedGetObjectRequest presignedRequest = presigner.presignGetObject(
                GetObjectPresignRequest.builder()
                        .signatureDuration(Duration.ofMinutes(10))  
                        .getObjectRequest(GetObjectRequest.builder()
                                .bucket(bucket)
                                .key("apache-tomcat.zip")
                                .build())
                        .build());

        presigner.close();
        System.out.println("OCI 预签名下载URL: " + presignedRequest.url().toString());
    }        
}