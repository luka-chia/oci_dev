import os
import Cloud_Guard
import Cost_Management
import Cloud_Advisor
import Resource_Utilization

from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter


compartment_id = "ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba"
tenant_id="ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba"

BYD_Weekly_report = "D://BYD_Weekly_report.pdf"
cost_pdf = "D://cost_report.pdf"
resource_utilization = "D://resource_utilization.pdf"
cloud_guard = "D://cloud_guard.pdf"
cloud_advisor = "D://cloud_advisor.pdf"

# get cost report by compartment from Cost_Management service
print("==== step 1: get cost report by compartment from Cost_Management service ====")
Cost_Management.get_cost_report(tenant_id=tenant_id, cost_pdf=cost_pdf)

# get security report from Cloud_Guard service
print("==== step 2: get security report from Cloud_Guard service ====")
Cloud_Guard.get_cloud_guard_report(compartment_id=compartment_id, cloud_guard=cloud_guard)

# get advisor report from Cloud_Advisor service
print("==== step 3: get advisor report from Cloud_Advisor service ====")
Cloud_Advisor.get_advisor_report(compartment_id=compartment_id, cloud_advisor=cloud_advisor)

# get resource utilization report from operation insight service
print("==== step 4: get resource utilization report from operation insight service ====")
Resource_Utilization.get_resource_utilization_report(compartment_id=compartment_id, 
                                                     resource_utilization=resource_utilization)

def merge_pdf_report():
    print("==== step 5: merge pdf file ====")
    merger = PdfMerger()
    for pdf in [cost_pdf, resource_utilization, cloud_guard, cloud_advisor]:
        merger.append(pdf)
    merger.write(BYD_Weekly_report)
    merger.close()

def del_tmp_file():
    for pdf in [cost_pdf, resource_utilization, cloud_guard, cloud_advisor]:
        os.remove(pdf)

merge_pdf_report()
del_tmp_file()
