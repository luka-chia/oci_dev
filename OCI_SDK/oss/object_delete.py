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


def delete_object():
    delete_object_response = object_storage_client.delete_object(
    namespace_name="sehubjapacprod",
    bucket_name="Luka-bucket",
    object_name="kbot.zip")

    # Get the data from response
    print(delete_object_response.headers)

delete_object()