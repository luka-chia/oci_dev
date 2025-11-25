# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import os

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()
# config.update({"region": "us-ashburn-1"})
# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)

bucket_name="Luka-bucket-ashburn",
object_name="test",
local_file_path = "/Users/luka/Downloads/om_oic_use_case.pdf"

try:
    # Open the local file in binary read mode
    with open(local_file_path, 'rb') as f:
        # Call the put_object method
        put_object_response = object_storage_client.put_object(
            namespace_name="sehubjapacprod",
            bucket_name="Luka-bucket-ashburn",
            object_name="test",
            put_object_body=f,
            content_type="text/plain" # Set the appropriate content type for your file
        )
    print(f"Object '{object_name}' uploaded successfully to bucket '{bucket_name}'.")

except oci.exceptions.ServiceError as e:
    print(f"Error uploading object: {e}")
except FileNotFoundError:
    print(f"Error: Local file '{local_file_path}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
