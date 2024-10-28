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
#config.update({"region": "ap-singapore-1"})


# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
def list_bucket():
    list_buckets_response = object_storage_client.list_buckets(
    namespace_name="sehubjapacprod",
    compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq")

    # Get the data from response
    print(list_buckets_response.data)

def put_o():
    put_object_response = object_storage_client.put_object(
    namespace_name="sehubjapacprod",
    bucket_name="Luka-bucket-ashburn",
    object_name="luka/canton",
    put_object_body=b"",
    )

    print(put_object_response.headers)

put_o()