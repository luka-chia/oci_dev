package com.example.s3_v1_vhost;

import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.S3ObjectSummary;
import com.example.OCI_Utils;

public class OciS3ListObjectsExample {
    public static void main(String[] args) {
        // 配置参数
        String accessKey = OCI_Utils.getProperty("oci.accessKey");
        String secretKey = OCI_Utils.getProperty("oci.secretKey");
        String namespace = "sehubjapacprod";
        String region = "us-ashburn-1";
        String bucketName = "luka-bucket-ashburn-2";

        try {
            
            // 构建endpoint
            String endpoint = String.format("https://vhcompat.objectstorage.%s.oci.customer-oci.com", region);
            
            // 配置客户端
            ClientConfiguration config = new ClientConfiguration()
                .withMaxErrorRetry(3)
                .withConnectionTimeout(10000)
                .withSocketTimeout(30000);
            
            // 创建凭证提供者
            AWSCredentialsProvider credentials = new AWSStaticCredentialsProvider(
                new BasicAWSCredentials(accessKey, secretKey));
            
            // 配置endpoint
            AwsClientBuilder.EndpointConfiguration endpointConfig = 
                new AwsClientBuilder.EndpointConfiguration(endpoint, region);
            
            // 构建S3客户端
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                .withCredentials(credentials)
                .withClientConfiguration(config)
                .withEndpointConfiguration(endpointConfig)
                //.withPathStyleAccessEnabled(true)  // OCI需要路径风格访问
                .disableChunkedEncoding()  // 某些OCI版本需要
                .build();

            // 测试连接
            System.out.println("尝试连接至OCI对象存储...");
            System.out.println("Endpoint: " + endpoint);
            System.out.println("Bucket: " + bucketName);
            
            if (!s3Client.doesBucketExistV2(bucketName)) {
                System.err.println("错误: 存储桶不存在或无权访问");
                return;
            }
            
            // 列出对象
            ObjectListing objectListing = s3Client.listObjects(bucketName);
            System.out.println("\n存储桶内容列表:");
            for (S3ObjectSummary summary : objectListing.getObjectSummaries()) {
                System.out.println(" - " + summary.getKey() + 
                                 " (大小: " + summary.getSize() + " bytes, " +
                                 "最后修改: " + summary.getLastModified() + ")");
            }
            
        } catch (Exception e) {
            System.err.println("\n发生错误:");
            e.printStackTrace();
            
            // 提供更友好的错误提示
            if (e.getMessage().contains("SignatureDoesNotMatch")) {
                System.err.println("\n可能原因:");
                System.err.println("1. 访问密钥或密钥不正确");
                System.err.println("2. 区域配置错误");
                System.err.println("3. 密钥已过期");
            }
        }
    }
}