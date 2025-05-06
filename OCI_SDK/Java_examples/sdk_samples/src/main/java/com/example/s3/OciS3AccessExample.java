package com.example.s3;

import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.S3ObjectSummary;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class OciS3AccessExample {

    // AES解密方法
    private static String decrypt(String key, String encrypted) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        byte[] decodedBytes = Base64.getDecoder().decode(encrypted);
        byte[] decryptedBytes = cipher.doFinal(decodedBytes);
        return new String(decryptedBytes, StandardCharsets.UTF_8);
    }

    public static void main(String[] args) {
        // 配置参数
        String accessKey = "30bf43cef8ff248f21b7d4f9128385b285e012e3";
        String secretKey = "your-secret-key";
        String namespace = "sehubjapacprod";
        String region = "eu-frankfurt-1";
        String bucketName = "Luka-bucket";

        try {
            
            // 构建endpoint
            String endpoint = String.format("https://%s.compat.objectstorage.%s.oraclecloud.com", 
                                          namespace, region);
            
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
                .withPathStyleAccessEnabled(true)  // OCI需要路径风格访问
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