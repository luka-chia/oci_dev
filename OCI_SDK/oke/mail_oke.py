import oke_cluster
import node_pool
import opc_work_request

compartment_id = "ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"
vcn_id = "ocid1.vcn.oc1.iad.amaaaaaaak7gbriahxr6lpvdrck6uh2x37643hqe2ptl5vgowln2v4rs36da"
endpoint_subnet_id = "ocid1.subnet.oc1.iad.aaaaaaaaylkwuvbup6fcdxekfy5lexp5jzhhrycve57apsoxtlkyqgp6jqda"
lb_subnet_id = "ocid1.subnet.oc1.iad.aaaaaaaapivwaqubkxx6gcd6jq2lm7673vrqpzqecqgnivwhyhbu2vexnlkq"
node_subnet_id = "ocid1.subnet.oc1.iad.aaaaaaaaafgdxf3bruk44vdgziprhrx5iclsh22n56b46pz6vwp2fy23au6q"
image_id = "ocid1.image.oc1.iad.aaaaaaaam6zxgcfwlyahvzmg32r526ckcosvkamzkb4vxceh7ywjslntbjmq"

node_shape = "VM.Standard.E3.Flex"
ssh_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC02p4H1pjNUDEPORETpkHLpG9wkSMAXg0ZiOYgyIlnDwY9rWbPwlro1Ve42Sl7o2gZuyDvxptj3rJhs11h3l2q62AknA47noPMclGgLed0Pf5WYRGvhywAnx8PxCbkdmXAWyVWovyUSlti8iHmB4PgEW595YAElMPAjBtnenBk/YbGMJPBtaBfp37B1QFMuW/1jNkpJHpcGigR1RDKmanDMRO8BpsCw15N6GKLOahM5MQmLcCxL/a55zwt+cr3pbHvpUWGXL9jWvnPaI8DfaUKR2hxLqvvsZLWDzwFmvrYiJKDcjF/sxfrCfhd+PdLMsgLqgg4gQJ/VU7GYx+gbA/C8QrA5G1XkrVd+iHqk1c1h6YrzrgAhE8Ba6aGa6N2R8W5vRwn5yRAWWCk79ZHWKLz+XeVrOaSg5miqrGdXFYz1P8ipkEtaeBrIz6opJ5VWffHX/XVyPCi0wd+OLxrfi56txmFHkCUlMKW5vfSVQrW0sQ3c9lAN3tnrRoQiIqtfM8= lulujia@LULUJIA-7420"

oke_cluster_name = "sdk_oke_1"
node_pool_name = "sdk_nodepool_1"

opc_request_work_id = oke_cluster.create_oke(name=oke_cluster_name, endpoint_subnet_id=endpoint_subnet_id,
                                             compartment_id=compartment_id, vcn_id=vcn_id, subnet_id=lb_subnet_id)

result_status, resource_id = opc_work_request.get_request_result(opc_work_request_id=opc_request_work_id)
print("current request when create oke cluster is in status [{0}]".format(result_status))
if("succeeded" == result_status.lower()):
    print("successfully create oke cluster")
else:
    print("failed to create oke cluster")

opc_request_work_id = node_pool.create_node_pool(
    name=node_pool_name, compartment_id=compartment_id, subnet_id=node_subnet_id, 
    ssh_key=ssh_key, cluster_id=resource_id, image_id=image_id, node_shape=node_shape)

result_status, _ = opc_work_request.get_request_result(opc_work_request_id=opc_request_work_id)
print("current request when create node pool is in status [{0}]".format(result_status))
if("succeeded" == result_status.lower()):
    print("successfully create oke node pool")
else:
    print("failed to create oke node pool")
