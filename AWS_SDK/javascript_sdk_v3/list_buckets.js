// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import { fileURLToPath } from "node:url";
import {fromCognitoIdentityPool} from "@aws-sdk/credential-providers";
import {
  paginateListBuckets,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

function getHtml(template) {
  return template.join("\n");
}

/**
 * List the Amazon S3 buckets in your account.
 */
export const listBuckets = async () => {
  const client = new S3Client({
    region: 'us-east-1',
    credentials: fromCognitoIdentityPool({
      clientConfig: { region: 'us-east-1' }, // Configure the underlying CognitoIdentityClient.
      identityPoolId: 'us-east-1:55a84e2a-19a4-4881-921f-a24ce96fe2c3',
        })
      })

  /** @type {?import('@aws-sdk/client-s3').Owner} */
  let Owner = null;

  /** @type {import('@aws-sdk/client-s3').Bucket[]} */
  const Buckets = [];

  try {
    const paginator = paginateListBuckets({ client }, {});

    for await (const page of paginator) {
      if (!Owner) {
        Owner = page.Owner;
      }

      Buckets.push(...page.Buckets);
    }

    console.log(
      `${Owner.DisplayName} owns ${Buckets.length} bucket${
        Buckets.length === 1 ? "" : "s"
      }:`,
    );
    console.log(`${Buckets.map((b) => ` • ${b.Name}`).join("\n")}`);
  } catch (caught) {
    if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while listing buckets.  ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};
// snippet-end:[s3.JavaScript.buckets.listBucketsV3]

// Invoke main function if this file was run directly.
listBuckets();
