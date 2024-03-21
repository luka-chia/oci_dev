# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import matplotlib.pyplot as plt

def get_advisor_report(compartment_id, cloud_advisor):
    # Initialize service client with default config file
    config = oci.config.from_file()
    optimizer_client = oci.optimizer.OptimizerClient(config)


    list_categories_response = optimizer_client.list_categories(
        compartment_id=compartment_id,
        compartment_id_in_subtree=True,
        # include_organization=True,
        opc_request_id="MSSQUNK7PGJX2EVRVUZM<unique_ID>")

    high_availability_advisor = dict()
    performance_advisor = dict()
    cost_advisor = dict()
    estimated_cost_saving = None
    # Get the data from response
    items = list_categories_response.data.items
    for item in items:
        name = item.name
        recommendation_data = {}
        for recommendation in item.recommendation_counts:
            recommendation_data[recommendation.importance] = recommendation.count
        
        resource_data = {}
        for resource in item.resource_counts:
            resource_data[resource.status] = resource.count

        if("high-availability" in name):
            # get high availability data
            high_availability_advisor["recommendation"] = recommendation_data
            high_availability_advisor["resource"] = resource_data
        elif("performance" in name):
            # get performance data
            performance_advisor["recommendation"] = recommendation_data
            performance_advisor["resource"] = resource_data
        elif("cost-management" in name):
            # get cost data
            cost_advisor["recommendation"] = recommendation_data
            cost_advisor["resource"] = resource_data
            estimated_cost_saving = item.estimated_cost_saving
    print(high_availability_advisor)
    print(performance_advisor)
    print(cost_advisor)

    generate_pdf(high_availability_advisor=high_availability_advisor, performance_advisor=performance_advisor,
                 cost_advisor=cost_advisor, estimated_cost_saving=estimated_cost_saving,
                 cloud_advisor=cloud_advisor)

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

def transit_level(recommendation_level):
    en_cn_map = {
        "CRITICAL": u"严重",
        "HIGH":u"高",
        "MODERATE":u"中",
        "LOW":u"低",
        "MINOR":u"次要"
    }
    return en_cn_map.get(recommendation_level)

def generate_pdf(high_availability_advisor, performance_advisor, cost_advisor, estimated_cost_saving, cloud_advisor):
    plt.figure(figsize=(24, 32), dpi=100)

    # draw cost_advisor
    plt.subplot(3,1,1)
    recommendation_level = [transit_level(key) for key in cost_advisor.get("recommendation")]
    recommendation_count = [value for value in cost_advisor.get("recommendation").values()]
    plt.pie(recommendation_count, labels=recommendation_level, autopct=autopct_format(recommendation_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("成本管理建议数", fontsize=32)
    cost_saving = "预计节省%s" % (estimated_cost_saving)
    text = u'''
    成本管理建议通过查找和调整未充
    分利用的资源为您节省成本。例如，
    成本管理建议帮助您查找未充分利
    用的计算实例、过度预配的自治数
    据仓库实例、未附加的块存储卷或
    引导卷，以及没有生命周期策略规
    则对象存储存储桶'''
    plt.text(1.3, 0.7, cost_saving, fontdict={'size': 40, 'color': 'red'}, ha='left', va='center')
    plt.text(1, 0, text, fontdict={'size': 32, 'color': 'black'}, ha='left', va='center')

    '''
    plt.subplot(3,2,6)
    resource_level = [key for key in cost_advisor.get("resource")]
    resource_count = [value for value in cost_advisor.get("resource").values()]
    plt.pie(resource_count, labels=resource_level, autopct=autopct_format(resource_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("成本建议处理进展", fontsize=24)
    '''

    # draw high_availability_advisor
    plt.subplot(3,1,2)
    recommendation_level = [transit_level(key) for key in high_availability_advisor.get("recommendation")]
    recommendation_count = [value for value in high_availability_advisor.get("recommendation").values()]
    plt.pie(recommendation_count, labels=recommendation_level, autopct=autopct_format(recommendation_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("高可用性建议数", fontsize=32)
    text = u'''
    高可用性建议有助于改进系统弹性。
    例如，通过在不同的可用性域中使
    用冗余计算节点来支持故障转移功
    能并正确地利用容错域，可以提高
    在OCI上运行的应用程序的可用性。。'''
    plt.text(1, 0, text, fontdict={'size': 32, 'color': 'black'}, ha='left', va='center')


    '''
    plt.subplot(3,2,2)
    resource_level = [key for key in high_availability_advisor.get("resource")]
    resource_count = [value for value in high_availability_advisor.get("resource").values()]
    plt.pie(resource_count, labels=resource_level, autopct=autopct_format(resource_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("高可用性建议处理进展", fontsize=24)
    '''

    # draw performance_advisor
    plt.subplot(3,1,3)
    recommendation_level = [transit_level(key) for key in performance_advisor.get("recommendation")]
    recommendation_count = [value for value in performance_advisor.get("recommendation").values()]
    plt.pie(recommendation_count, labels=recommendation_level, autopct=autopct_format(recommendation_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("性能建议数", fontsize=32)
    text = u'''
    性能建议通过查找和调整过度利用
    的资源来改进性能。例如，通过调
    整过度利用的计算实例和负载平衡
    器来改进性能，并通过查找未使用
    自动优化功能的块存储卷和引导卷
    来优化性能设置。'''
    plt.text(1, 0, text, fontdict={'size': 32, 'color': 'black'}, ha='left', va='center')

    '''
    plt.subplot(3,2,4)
    resource_level = [key for key in performance_advisor.get("resource")]
    resource_count = [value for value in performance_advisor.get("resource").values()]
    plt.pie(resource_count, labels=resource_level, autopct=autopct_format(resource_count),
            textprops={'fontsize': 25}, labeldistance=None)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("性能建议处理进展", fontsize=24)
    '''

    plt.savefig(cloud_advisor, bbox_inches='tight', pad_inches=0.1)

