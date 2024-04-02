# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import time

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info

def create_oke(name, compartment_id, endpoint_subnet_id, vcn_id, subnet_id):
    # Initialize service client with default config file
    config = oci.config.from_file()
    container_engine_client = oci.container_engine.ContainerEngineClient(config)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    create_cluster_response = container_engine_client.create_cluster(
        create_cluster_details=oci.container_engine.models.CreateClusterDetails(
            name=name,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            kubernetes_version="v1.28.2",
            endpoint_config=oci.container_engine.models.CreateClusterEndpointConfigDetails(
                subnet_id=endpoint_subnet_id,
                is_public_ip_enabled=True),
            options=oci.container_engine.models.ClusterCreateOptions(
                service_lb_subnet_ids=[subnet_id],
                kubernetes_network_config=oci.container_engine.models.KubernetesNetworkConfig(
                    pods_cidr="10.244.0.0/16",
                    services_cidr="10.96.0.0/16"),
                add_ons=oci.container_engine.models.AddOnOptions(
                    is_kubernetes_dashboard_enabled=False,
                    is_tiller_enabled=False),
                admission_controller_options=oci.container_engine.models.AdmissionControllerOptions(
                    is_pod_security_policy_enabled=False)),
            cluster_pod_network_options=[
                oci.container_engine.models.OciVcnIpNativeClusterPodNetworkOptionDetails(
                    cni_type="OCI_VCN_IP_NATIVE")],
            type="ENHANCED_CLUSTER"))

    # Get the data from response
    header = create_cluster_response.headers
    opc_work_request_id = header.get("opc-work-request-id")
    print(header)
    print("=============================================")
    print("the opc_work_request_id is {0}".format(opc_work_request_id))
    return opc_work_request_id
