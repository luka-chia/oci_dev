# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import time

from datetime import datetime

config = oci.config.from_file()
# Init a default client via default profile
client = oci.identity.IdentityClient(config)


# Get all subscribed regions
subscribedRegionList = client.list_region_subscriptions(config["tenancy"]).data

rootCompartment = client.get_compartment(compartment_id=config["tenancy"]).data
print(rootCompartment)

topCompartmentPayloadList = client.list_compartments(compartment_id=rootCompartment.id,
            compartment_id_in_subtree=True,
            access_level='ANY').data
print(len(topCompartmentPayloadList))
compartments = [{"id": c.id, "name": c.name} for c in topCompartmentPayloadList]

for c in compartments:
    print(c.get("name"))