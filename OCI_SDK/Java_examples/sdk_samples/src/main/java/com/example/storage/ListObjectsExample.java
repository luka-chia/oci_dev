package com.example.storage;

/** This is an automatically generated code sample. 
To make this code sample work in your Oracle Cloud tenancy, 
please replace the values for any parameters whose current values do not fit
your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and 
boolean, number, and enum parameters with values not fitting your use case).
*/

import com.oracle.bmc.ConfigFileReader;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.objectstorage.ObjectStorageClient;
import com.oracle.bmc.objectstorage.model.*;
import com.oracle.bmc.objectstorage.requests.*;
import com.oracle.bmc.objectstorage.responses.*;
import java.math.BigDecimal;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Date;
import java.util.UUID;
import java.util.Arrays;


public class ListObjectsExample {
    public static void main(String[] args) throws Exception {

        /**
         * Create a default authentication provider that uses the DEFAULT
         * profile in the configuration file.
         * Refer to <see href="https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>the public documentation</see> on how to prepare a configuration file.
         */
        final ConfigFileReader.ConfigFile configFile = ConfigFileReader.parseDefault();
        final AuthenticationDetailsProvider provider = new ConfigFileAuthenticationDetailsProvider(configFile);

        /* Create a service client */
        ObjectStorageClient client = ObjectStorageClient.builder().build(provider);

            /* Create a request and dependent object(s). */

        ListObjectsRequest listObjectsRequest = ListObjectsRequest.builder()
            .namespaceName("sehubjapacprod")
            .bucketName("Luka-bucket")
            .build();

            /* Send request to the Client */
        ListObjectsResponse response = client.listObjects(listObjectsRequest);
        System.out.println(response);
        }    
}
