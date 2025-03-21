# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

def list_applications():
    config = oci.config.from_file()


    # Initialize service client with default config file
    functions_client = oci.functions.FunctionsManagementClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    get_application_response = functions_client.list_applications(
        compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq")

    # Get the data from response
    print(get_application_response.data)

def create_application():
    config = oci.config.from_file()


    # Initialize service client with default config file
    functions_client = oci.functions.FunctionsManagementClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    create_application_response = functions_client.create_application(
    create_application_details=oci.functions.models.CreateApplicationDetails(
        compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq",
        display_name="application_from_sdk",
        subnet_ids=["ocid1.subnet.oc1.ap-singapore-1.aaaaaaaar52xo6nji5vauz3bev24rdeioiq6s6ciixwav7wtrqaepungibva"]))

    # Get the data from response
    print(create_application_response.data)


#list_applications()

create_application()