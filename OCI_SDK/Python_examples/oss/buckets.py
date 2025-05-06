# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()
# config.update({"region": "us-ashburn-1"})


# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)

def test_token_authentication():
    # step 1
    # oci session authenticate --no-browser; this command invoke the url=https://auth.ap-singapore-1.oraclecloud.com/v1/token/upst/actions/GenerateUpst
    # oci session refresh --profile token_test
    # oci session authenticate --no-browser --session-expiration-in-minutes <token-persistence-time-in-minutes> --profile <profile_name> --auth security_token
    # config = oci.config.from_file(profile_name='luka')
    token_file = u'C:\\Users\\lulujia\\.oci\\oci_token'
    token = None
    with open(token_file, 'r') as f:
        token = f.read()
    
    # step 2
    private_key = oci.signer.load_private_key_from_file(u'C:\\Users\\lulujia\\.oci\\oci_api_key.pem')
    signer = oci.auth.signers.SecurityTokenSigner(token, private_key) 
    # signer = oci.auth.signers.get_resource_principals_signer()
    # list_region_subscriptions(config['tenancy'])
    client = oci.object_storage.ObjectStorageClient({"region": "ap-singapore-1"}, signer = signer)

    # step 3
    list_objects_response = client.list_objects(
        namespace_name="sehubjapacprod",
        bucket_name="Luka-bucket"
        )

    # Get the data from response
    print(list_objects_response.data)


def list_bucket():
    list_buckets_response = object_storage_client.list_buckets(
    namespace_name="sehubjapacprod",
    compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq")

    # Get the data from response
    print(list_buckets_response.data)

def list_objects():
    list_objects_response = object_storage_client.list_objects(
    namespace_name="sehubjapacprod",
    bucket_name="Luka-bucket-ashburn")

    # Get the data from response
    print(list_objects_response.data)

def put_o():
    put_object_response = object_storage_client.put_object(
    namespace_name="sehubjapacprod",
    bucket_name="Luka-bucket-ashburn",
    object_name="luka/canton",
    put_object_body=b"",
    )

    print(put_object_response.headers)

def create_bucket():
    create_bucket_response = object_storage_client.create_bucket(
    namespace_name="sehubjapacprod",
    create_bucket_details=oci.object_storage.models.CreateBucketDetails(
        name="EXAMPLE-name-Value",
        compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"))

    # Get the data from response
    print(create_bucket_response.data)

# put_o()
#list_objects()
# test_token_authentication()
create_bucket()