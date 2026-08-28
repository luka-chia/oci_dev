# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()
security_list_ocid = "ocid1.securitylist.oc1.ap-singapore-1.aaaaaaaaz54cgqps4egarwylaf6dweyei7oxaba3p7eumgmi7pyivulyez5a"

# Initialize service client with default config file
core_client = oci.core.VirtualNetworkClient(config)

get_security_list_response = core_client.get_security_list(
    security_list_id=security_list_ocid)

egress_security_rules = get_security_list_response.data.egress_security_rules
ingress_security_rules = get_security_list_response.data.ingress_security_rules

add_ingress_security_rule = oci.core.models.IngressSecurityRule(
                protocol="6",
                source="80.80.80.0/24",
                is_stateless=False,
                source_type="CIDR_BLOCK",
                tcp_options=oci.core.models.TcpOptions(
                    destination_port_range=oci.core.models.PortRange(
                        max=4000,
                        min=4000),
                    ))

ingress_security_rules.append(add_ingress_security_rule)



# Send the request to service, some parameters are not required, see API
# doc for more info
update_security_list_response = core_client.update_security_list(
    security_list_id=security_list_ocid,
    update_security_list_details=oci.core.models.UpdateSecurityListDetails(
        ingress_security_rules=ingress_security_rules
        )
    )

# Get the data from response
print(update_security_list_response.data)
