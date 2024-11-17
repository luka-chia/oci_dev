# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import base64

def decode_b64(text):
    decoded_data = base64.b64decode(text.encode('utf-8'))
    print(f"Encoded: {decoded_data}")
# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
vault_client = oci.vault.VaultsClient(config)

secret_id="ocid1.vaultsecret.oc1.ap-singapore-1.amaaaaaaak7gbriaz6azrtc6r7p2bcaz5nmqln72tk72lcx3lr63coywbphq"

# Send the request to service, some parameters are not required, see API
# doc for more info
get_secret_response = vault_client.get_secret(
    secret_id=secret_id)

# Get the data from response
#print(get_secret_response.data)


get_secret_version_response = vault_client.get_secret_version(
    secret_id=secret_id,
    secret_version_number=1)

# Get the data from response
#print(get_secret_version_response.data)

secrets_client = oci.secrets.SecretsClient(config)
get_secret_bundle_response = secrets_client.get_secret_bundle(
    secret_id=secret_id,
    version_number=1)

# Get the data from response
print(get_secret_bundle_response.data)
decode_b64(get_secret_bundle_response.data.secret_bundle_content.content)