# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import time

from datetime import datetime

config = oci.config.from_file()
config.update({"region": "ap-singapore-1"})


certificates_management_client = oci.certificates_management.CertificatesManagementClient(config)
# Send the request to service, some parameters are not required, see API doc for more info
list_certificates_response = certificates_management_client.list_certificates(
    compartment_id="ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"
    )

# Get the data from response
certificates = list_certificates_response.data.items

imported_certificates = list()

for certificate in certificates:
    if certificate.config_type == "IMPORTED":
        imported_certificates.append(certificate)
print(imported_certificates)

format_string = "%Y-%m-%d"
for import_cert in imported_certificates:
    str_date = import_cert.current_version_summary.validity.time_of_validity_not_after
    #cert_date_expire = datetime.strptime(str_date, format_string)

    today = datetime.now().date()

    remaining_days = str_date.date()-today
    if remaining_days.days < int('1000'):
        print("expiry soon")
    print(remaining_days)
