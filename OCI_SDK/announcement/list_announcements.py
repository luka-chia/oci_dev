# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).
# refer to https://docs.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/AnnouncementsCollection/ListAnnouncements

from datetime import datetime
import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
announcements_service_client = oci.announcements_service.AnnouncementClient(
    config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_announcements_response = announcements_service_client.list_announcements(
    compartment_id="ocid1.compartment.oc1..aaaaaaaahr7aicqtodxmcfor6pbqn3hvsngpftozyxzqw36gj4kh3w3kkj4q")

# Get the data from response
print(list_announcements_response.data.items)
