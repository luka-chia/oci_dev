# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).
# refer to https://docs.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/AnnouncementSubscription/CreateAnnouncementSubscription

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
announcements_service_client = oci.announcements_service.AnnouncementSubscriptionClient(
    config)


# Send the request to service, some parameters are not required, see API
# doc for more info
create_announcement_subscription_response = announcements_service_client.create_announcement_subscription(
    create_announcement_subscription_details=oci.announcements_service.models.CreateAnnouncementSubscriptionDetails(
        display_name="EXAMPLE-displayName-Value",
        compartment_id="ocid1.test.oc1..<unique_ID>EXAMPLE-compartmentId-Value",
        ons_topic_id="ocid1.test.oc1..<unique_ID>EXAMPLE-onsTopicId-Value",
        description="EXAMPLE-description-Value",
        filter_groups={
            'EXAMPLE_KEY_oPdPj': {
                'filters': [
                    {
                        'type': 'PLATFORM_TYPE',
                        'value': 'EXAMPLE-value-Value'}]}},
        preferred_language="EXAMPLE-preferredLanguage-Value",
        preferred_time_zone="EXAMPLE-preferredTimeZone-Value",
        freeform_tags={
                            'EXAMPLE_KEY_AFPHx': 'EXAMPLE_VALUE_SicVUeo0Uvnsy3tHfSpn'},
        defined_tags={
            'EXAMPLE_KEY_fJHJu': {
                'EXAMPLE_KEY_tIgYV': 'EXAMPLE--Value'}}),
    opc_retry_token="EXAMPLE-opcRetryToken-Value",
    opc_request_id="LUL0HQUB44PXSH5ARUZV<unique_ID>")

# Get the data from response
print(create_announcement_subscription_response.data)
