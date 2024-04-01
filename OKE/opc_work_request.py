# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import time

def get_request_result(opc_work_request_id):
    config = oci.config.from_file()
    # Initialize service client with default config file
    container_engine_client = oci.container_engine.ContainerEngineClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    get_work_request_response = container_engine_client.get_work_request(
        work_request_id=opc_work_request_id)

    # Get the data from response
    result = get_work_request_response.data
    resource_id = result.resources[0].identifier
    result_status = result.status
    while("in_progress" == result_status.lower() or "accepted" == result_status.lower()):
        print("current request is in status [{0}], please waiting for a moment".format(result_status))
        time.sleep(30)
        get_work_request_response = container_engine_client.get_work_request(work_request_id=opc_work_request_id)
        result = get_work_request_response.data
        result_status = result.status
    
    return result_status, resource_id
