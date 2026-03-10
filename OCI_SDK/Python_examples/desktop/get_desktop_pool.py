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


# Initialize service client with default config file
desktops_client = oci.desktops.DesktopServiceClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
get_desktop_pool_response = desktops_client.get_desktop_pool(
    desktop_pool_id="ocid1.desktoppool.oc1.ap-seoul-1.amaaaaaampkgznyari2io7hzpe5s7mdos5slyxjpb5ztlovpchqfhnhaphma",
    opc_request_id="EINR2URFU9KBJTQN5Z4B<unique_ID>")

# Get the data from response
print(get_desktop_pool_response.data)
