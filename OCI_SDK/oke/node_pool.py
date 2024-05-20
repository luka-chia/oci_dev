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

def create_node_pool(name, compartment_id, subnet_id, ssh_key, cluster_id, image_id, node_shape):
    # Initialize service client with default config file
    config = oci.config.from_file()
    container_engine_client = oci.container_engine.ContainerEngineClient(config)

    # Send the request to service, some parameters are not required, see API doc for more info
    create_node_pool_response = container_engine_client.create_node_pool(
        create_node_pool_details=oci.container_engine.models.CreateNodePoolDetails(
            compartment_id=compartment_id,
            cluster_id=cluster_id,
            name=name,
            node_shape=node_shape,
            kubernetes_version="v1.28.2",
            node_metadata={},
            node_image_name=image_id,
            node_source_details=oci.container_engine.models.NodeSourceViaImageDetails(
                source_type="IMAGE",
                image_id=image_id,
                boot_volume_size_in_gbs=968),
            node_shape_config=oci.container_engine.models.CreateNodeShapeConfigDetails(
                ocpus=1, memory_in_gbs=4),
            ssh_public_key=ssh_key,
            node_config_details=oci.container_engine.models.CreateNodePoolNodeConfigDetails(
                size=3,
                placement_configs=[
                    oci.container_engine.models.NodePoolPlacementConfigDetails(
                        availability_domain="bxtG:US-ASHBURN-AD-1", subnet_id=subnet_id),
                    oci.container_engine.models.NodePoolPlacementConfigDetails(
                        availability_domain="bxtG:US-ASHBURN-AD-2", subnet_id=subnet_id),
                    oci.container_engine.models.NodePoolPlacementConfigDetails(
                        availability_domain="bxtG:US-ASHBURN-AD-3", subnet_id=subnet_id)],
                is_pv_encryption_in_transit_enabled=False,
                node_pool_pod_network_option_details=oci.container_engine.models.OciVcnIpNativeNodePoolPodNetworkOptionDetails(
                    cni_type="OCI_VCN_IP_NATIVE",
                    pod_subnet_ids=[subnet_id],
                    max_pods_per_node=31))))
    # Get the data from response
    header = create_node_pool_response.headers
    opc_work_request_id = header.get("opc-work-request-id")
    print(header)
    print("=============================================")
    print("the opc_work_request_id is {0}".format(opc_work_request_id))
    return opc_work_request_id
