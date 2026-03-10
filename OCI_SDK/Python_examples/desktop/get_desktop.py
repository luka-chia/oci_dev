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
get_desktop_response = desktops_client.get_desktop(
    desktop_id="ocid1.desktoppooldesktop.oc1.ap-seoul-1.anuwgljrmpkgznyacftizhoeq46uskrxrjydkx2q3wigwtdpzk76453aomfa",
    opc_request_id="AA9TL1PGLVQDQI07ITOB<unique_ID>")

# Get the data from response
print(get_desktop_response.data)
