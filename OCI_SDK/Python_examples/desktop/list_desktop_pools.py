
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
list_desktop_pools_response = desktops_client.list_desktop_pools(
    compartment_id="ocid1.compartment.oc1..aaaaaaaatiruzu2mgma7lwclgwkp7xs3qcmzdyx3dx4bbfmmfb72sc7oxr5a")

# Get the data from response
print(list_desktop_pools_response.data)
