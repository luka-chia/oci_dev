package com.example.storage;

import com.oracle.bmc.ConfigFileReader;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.objectstorage.ObjectStorageClient;
import com.oracle.bmc.objectstorage.requests.PutObjectRequest;
import com.oracle.bmc.objectstorage.responses.PutObjectResponse;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.file.Path;
import java.nio.file.Paths;

public class OciPutObjectExample {

    public static void main(String[] args) throws Exception {

        // 1. Configure Authentication Details
        // Replace with your OCI config file path and profile
        final ConfigFileReader.ConfigFile configFile = ConfigFileReader.parseDefault();
        final AuthenticationDetailsProvider provider = new ConfigFileAuthenticationDetailsProvider(configFile);

        /* Create a service client */
        ObjectStorageClient client = ObjectStorageClient.builder().build(provider);

        client.setRegion("ap-singapore-1");
        // 3. Define Object Details
        String namespaceName = "sehubjapacprod"; // Replace with your Object Storage namespace
        String bucketName = "Luka-bucket";     // Replace with your bucket name
        String objectName = "om_oic_use_case.pdf";  // Desired name for the object in the bucket
        Path filePath = Paths.get("/Users/luka/Downloads/om_oic_use_case.pdf"); // Path to the local file to upload

        // 4. Create PutObjectRequest
        try (InputStream objectContent = new FileInputStream(filePath.toFile())) {
            PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .namespaceName(namespaceName)
                .bucketName(bucketName)
                .objectName(objectName)
                .putObjectBody(objectContent)
                .contentLength(filePath.toFile().length()) // Optional: Set content length for better performance
                .contentType("text/plain") // Optional: Set content type
                .build();

            // 5. Execute the PutObjectRequest
            PutObjectResponse putObjectResponse = client.putObject(putObjectRequest);

            // 6. Handle the Response
            System.out.println("Object uploaded successfully. ETag: " + putObjectResponse.getETag());

        } catch (Exception e) {
            System.err.println("Error uploading object: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // 7. Close the client
            client.close();
        }
    }
}