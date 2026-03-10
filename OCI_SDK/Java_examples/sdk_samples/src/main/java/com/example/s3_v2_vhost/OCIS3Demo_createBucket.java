package com.example.s3_v2_vhost;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.model.*;
import java.net.URI;

import com.example.OCI_Utils;

public class OCIS3Demo_createBucket {

    public static void main(String[] args) {
        // OCI S3 兼容配置
        String ociEndpoint = "https://vhcompat.objectstorage.us-ashburn-1.oci.customer-oci.com";
        String bucketName = "luka-bucket-ashburn-2";
        String accessKey = OCI_Utils.getProperty("oci.accessKey");
        String secretKey = OCI_Utils.getProperty("oci.secretKey");

        // 0. 创建 S3Client（适配 OCI）
        S3Client s3Client = S3Client.builder()
                .endpointOverride(URI.create(ociEndpoint))  // OCI S3 兼容端点
                .serviceConfiguration(
                    S3Configuration.builder()
                    //.pathStyleAccessEnabled(true) // 关键：强制使用 Path Style
                    .build())
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(accessKey, secretKey)))
                .region(Region.of("us-ashburn-1"))  // 任意值（OCI 会忽略，但 SDK 要求必填）
                .build();
        
        createBucket(s3Client,bucketName);
        s3Client.close();
    }

    //上传对象
    private static void createBucket(S3Client s3Client, String bucketName){
        boolean exists;
        try {
            s3Client.headBucket(HeadBucketRequest.builder().bucket(bucketName).build());
            exists = true;
        } catch (Exception ex) {
            exists = false;
        }

        if (exists) {
            System.out.println("Bucket already exists: " + bucketName);
            return;
        }

        // 在 OCI 端通常不需要 LocationConstraint（由端点所属 region 决定）
        s3Client.createBucket(CreateBucketRequest.builder().bucket(bucketName).build());
        s3Client.waiter().waitUntilBucketExists(HeadBucketRequest.builder().bucket(bucketName).build());
        System.out.println("Created OCI bucket: " + bucketName);

    }
}