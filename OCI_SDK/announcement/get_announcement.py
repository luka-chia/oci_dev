# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).
# refer to https://docs.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/Announcement/GetAnnouncement

import oci

config = oci.config.from_file()


# Initialize service client with default config file
announcements_service_client = oci.announcements_service.AnnouncementClient(
    config)


# Send the request to service, some parameters are not required, see API
# doc for more info
get_announcement_response = announcements_service_client.get_announcement(
    announcement_id="ocid1.announcement.oc1..aaaaaaaaarr4d3bhbnwn6efunbbhztzdfbbuid7ezbwakivk2qpx7ea6gtrq")

# Get the data from response
print(get_announcement_response.data)
