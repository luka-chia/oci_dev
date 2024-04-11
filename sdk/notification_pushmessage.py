# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import time
import json

from datetime import datetime

config = oci.config.from_file()
config.update({"region": "ap-singapore-1"})

ons_client = oci.ons.NotificationDataPlaneClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info

body = {"default": "Alarm breached", "Email": "Alarm breached: <url>"}
str = json.dumps(body)
print(str)
publish_message_response = ons_client.publish_message(
    topic_id="ocid1.onstopic.oc1.ap-singapore-1.amaaaaaaak7gbriad6fharvjxc4g24ybikxg6dznwi2xpb5gyy3xa4dbvvha",
    message_details=oci.ons.models.MessageDetails(
        body=str,
        title="EXAMPLE-title-Value"),
    message_type="JSON")

# Get the data from response
print(publish_message_response.data)