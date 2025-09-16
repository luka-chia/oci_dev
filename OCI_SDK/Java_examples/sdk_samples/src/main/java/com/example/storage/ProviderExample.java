/**
 * Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
 * This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
 */
package com.example.storage;

import java.io.File;
import java.io.InputStream;
import java.util.function.Supplier;

import com.oracle.bmc.Region;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider;
import com.oracle.bmc.auth.SimplePrivateKeySupplier;
import com.oracle.bmc.auth.StringPrivateKeySupplier;
import com.oracle.bmc.http.signing.internal.PEMFileRSAPrivateKeySupplier;
import com.oracle.bmc.objectstorage.ObjectStorageClient;
import com.oracle.bmc.objectstorage.responses.ListBucketsResponse;

import com.oracle.bmc.objectstorage.requests.*;
import com.oracle.bmc.objectstorage.responses.*;

/** A sample to demonstrate how to use the SimpleAuthenticationDetailsProvider to create a client */
public class ProviderExample {
    public static void main(String[] args) {

        final String tenantId = "ocid1.tenancy.oc1..aaaxxxsc2wbq24l7dzf3kba";
        final String userId = "ocid1.user.oc1..aaaaaaaafkg344cccc7kegmyqut5l7eorq";
        final String fingerprint = "a2:d1:18:32ccc:24";
        String pemFilePath = "/Users/pem";

        Supplier<InputStream> privateKeySupplier = new SimplePrivateKeySupplier(pemFilePath);
        //Supplier<InputStream> privateKeySupplierFromConfigEntry = new SimplePrivateKeySupplier(pemFilePath);

        SimpleAuthenticationDetailsProvider.SimpleAuthenticationDetailsProviderBuilder builder =
                    SimpleAuthenticationDetailsProvider.builder()
                            .privateKeySupplier(privateKeySupplier)
                            .fingerprint(fingerprint)
                            .userId(userId)
                            .region(Region.AP_SINGAPORE_1)
                            .tenantId(tenantId);

        AuthenticationDetailsProvider provider = builder.build();

        /* Create a service client */
        ObjectStorageClient client = ObjectStorageClient.builder().build(provider);

        /* Create a request and dependent object(s). */

	ListBucketsRequest listBucketsRequest = ListBucketsRequest.builder()
        .namespaceName("sehubjapod")
		.compartmentId("ocid1.compartment.oc1..aaaaaaaajyvcxbubwkajwku5hfh4octoq")
		.build();

        /* Send request to the Client */
        ListBucketsResponse response = client.listBuckets(listBucketsRequest);
        System.out.println(response);
    }
}