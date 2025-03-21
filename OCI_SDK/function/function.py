# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

def list_functions():
    config = oci.config.from_file()
    # Initialize service client with default config file
    functions_client = oci.functions.FunctionsManagementClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    get_function_response = functions_client.list_functions(
        application_id="ocid1.fnapp.oc1.ap-singapore-1.aaaaaaaamv6mxvcxsvm5qpt3vdlc5r62t3sn5ltnxoe6uxpi6mrch42oat6a")

    # Get the data from response
    print(get_function_response.data)

def create_function():
    config = oci.config.from_file()
    # Initialize service client with default config file
    functions_client = oci.functions.FunctionsManagementClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    create_function_response = functions_client.create_function(
        create_function_details=oci.functions.models.CreateFunctionDetails(
            display_name="function_from_sdk",
            application_id="ocid1.fnapp.oc1.ap-singapore-1.aaaaaaaaxbz22tffnqnmjmjexwpqondrwrzzvski6u3gq5xmjvlntk5k776q",
            memory_in_mbs=256,
            image="sin.ocir.io/sehubjapacprod/luka/logs_to_kafka:0.0.28"))

    # Get the data from response
    print(create_function_response.data)

#list_functions()

create_function()