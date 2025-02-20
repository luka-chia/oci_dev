# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).
# refer to https://docs.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/Service/ListServices

import oci


config = oci.config.from_file()


# Initialize service client with default config file
announcements_service_client = oci.announcements_service.ServiceClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_services_response = announcements_service_client.list_services(
    compartment_id="ocid1.compartment.oc1..aaaaaaaahr7aicqtodxmcfor6pbqn3hvsngpftozyxzqw36gj4kh3w3kkj4q",
    limit=564,
    sort_by="serviceName",
    sort_order="DESC",
    opc_request_id="OUI7CUYLL9CH7F5FMBBG<unique_ID>")

# Get the data from response
print(list_services_response.data)

for item in list_services_response.data.items:
    print(item.service_name)

