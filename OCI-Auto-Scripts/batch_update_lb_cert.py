import oci

OLD_CERT = "ocid1.certificate.oc1.ap-singapore-1.amaaaaaaak7gbriastucnl6wde2hcvkn42kmsqpkz3ctn3yrendpkfpftqxa"
NEW_CERT = "ocid1.certificate.oc1.ap-singapore-1.amaaaaaaak7gbriabeok6xexvtbkmk5dlb3gelqlqrdwex4sshoh6xfqsihq"
COMPARTMENT_ID = "ocid1.tenancy.oc1..aaaaaaaa3mvsfaushcvhctl7rkiqqavo2so2xqie4rlhjgvm7eq5q3ad35xq"

config = oci.config.from_file()
config.update({"region": "ap-singapore-1"})
lb_client = oci.load_balancer.LoadBalancerClient(config)

lbs = lb_client.list_load_balancers(
    compartment_id=COMPARTMENT_ID
).data

for lb in lbs:
    print(f"Scanning {lb.display_name}")
    detail = lb_client.get_load_balancer(
        lb.id
    ).data

    for listener_name, listener in detail.listeners.items():
        ssl_cfg = listener.ssl_configuration
        if ssl_cfg is None:
            continue
        cert_ids = ssl_cfg.certificate_ids
        if cert_ids is None:
            continue
        if OLD_CERT in cert_ids:
            print(f"Updating listener [{listener_name}] in loadbalance [{lb.display_name}]")

            old_ssl = listener.ssl_configuration

            listener.ssl_configuration.certificate_ids = [NEW_CERT]

            lb_client.update_listener(
                load_balancer_id=lb.id,
                listener_name=listener_name,
                update_listener_details=listener
            )

print("Done")
