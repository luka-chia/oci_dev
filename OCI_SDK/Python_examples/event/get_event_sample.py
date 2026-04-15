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
config.update({"region": "us-phoenix-1"})


# Initialize service client with default config file
events_client = oci.events.EventsClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
get_rule_response = events_client.get_rule(
    rule_id="ocid1.eventrule.oc1.phx.amaaaaaaak7gbriaxmgpwmhnxbtm5kswxftplqauedgfcenugd2g5pfgq2jq",
    opc_request_id="3CRKID6SVM4LS1GYAJUG<unique_ID>")

# Get the data from response
print(get_rule_response.data)
