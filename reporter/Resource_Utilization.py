import oci
from datetime import datetime
import matplotlib.pyplot as plt

def get_resource_utilization_report(compartment_id, resource_utilization):
    config = oci.config.from_file()
    config.update({"region": "ap-seoul-1"})


    # Initialize service client with default config file
    opsi_client = oci.opsi.OperationsInsightsClient(config)

    # get cpu statistics
    cpu_statistics = opsi_client.summarize_host_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric="CPU",
        analysis_time_interval="P30D",
        limit=207,
        sort_order="DESC",
        sort_by="utilizationPercent",
        opc_request_id="B5EG7RA4QQS76JRGMROY<unique_ID>",
        compartment_id_in_subtree=True)

    # Get the data from response
    cpu_items = cpu_statistics.data.items
    topN_by_cpu = {}
    print("=============================== cpu statistics ==============================")
    for item in cpu_items:
        resource_name = deal(item.host_details.host_display_name)
        utilization_percent = item.current_statistics.utilization_percent
        topN_by_cpu[resource_name] = utilization_percent
        #print("host[name=%s] cpu_usage_percent=%s"%(item.host_details.host_display_name,item.current_statistics.utilization_percent))
    print(topN_by_cpu)

    # get mem statistics
    memory_statistics = opsi_client.summarize_host_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric="LOGICAL_MEMORY",
        analysis_time_interval="P30D",
        limit=207,
        sort_order="DESC",
        sort_by="utilizationPercent",
        opc_request_id="B5EG7RA4QQS76JRGMROY<unique_ID>",
        compartment_id_in_subtree=True)

    # Get the data from response
    memory_items = memory_statistics.data.items
    topN_by_memory = {}
    print("=============================== memory statistics ==============================")
    for item in memory_items:
        resource_name = deal(item.host_details.host_display_name)
        utilization_percent = item.current_statistics.utilization_percent
        topN_by_memory[resource_name] = utilization_percent
        #print("host[name=%s] memory_usage_percent=%s"%(item.host_details.host_display_name,item.current_statistics.utilization_percent))
    print(topN_by_memory)

    # get storage statistics
    storage_statistics = opsi_client.summarize_host_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric="STORAGE",
        analysis_time_interval="P30D",
        limit=207,
        sort_order="DESC",
        sort_by="utilizationPercent",
        opc_request_id="B5EG7RA4QQS76JRGMROY<unique_ID>",
        compartment_id_in_subtree=True)

    # Get the data from response
    storage_items = storage_statistics.data.items
    topN_by_storage = {}
    print("=============================== storage statistics ==============================")
    for item in storage_items:
        resource_name = deal(item.host_details.host_display_name)
        utilization_percent = item.current_statistics.utilization_percent
        topN_by_storage[resource_name] = utilization_percent
        #print("host[name=%s] storage_usage_percent=%s"%(item.host_details.host_display_name,item.current_statistics.utilization_percent))
    print(topN_by_storage)

    # generate pdf report
    generate_pdf(topN_by_cpu=topN_by_cpu, topN_by_memory=topN_by_memory, topN_by_storage=topN_by_storage, 
                 resource_utilization=resource_utilization)

def deal(string):
    return string.split(".")[0]

def generate_pdf(topN_by_cpu, topN_by_memory, topN_by_storage, resource_utilization):    
    plt.figure(figsize=(24, 6), dpi=100)

    # step1 draw cpu top n
    resource_name = [key for key in topN_by_cpu]
    cpu_percent = [value for value in topN_by_cpu.values()]
    resource_name.reverse()
    cpu_percent.reverse()
    plt.subplot(1,3,1)
    plt.barh(resource_name, cpu_percent, color = "#4CAF50", height=0.1)
    plt.yticks(rotation=45, fontsize=15)

    for i, v in enumerate(cpu_percent):
        plt.text(v, i, str(v), 
                color = 'red', fontweight = 'bold', fontsize=12)
    
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("CPU使用率TOP_N", fontsize=24)

    # step2 draw memory top n
    resource_name = [key for key in topN_by_memory]
    memory_percent = [value for value in topN_by_memory.values()]
    resource_name.reverse()
    memory_percent.reverse()
    plt.subplot(1,3,2)
    plt.barh(resource_name, memory_percent, color = "#4CAF50", height=0.1)
    plt.yticks(rotation=45, fontsize=15)

    for i, v in enumerate(memory_percent):
        plt.text(v, i, str(v), 
                color = 'red', fontweight = 'bold', fontsize=12)
    

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("内存使用率TOP_N", fontsize=24)

    # step3 draw storage top n
    resource_name = [key for key in topN_by_storage]
    storage_percent = [value for value in topN_by_storage.values()]
    resource_name.reverse()
    storage_percent.reverse()
    plt.subplot(1,3,3)
    plt.barh(resource_name, storage_percent, color = "#4CAF50", height=0.1)
    plt.yticks(rotation=45, fontsize=15)

    for i, v in enumerate(storage_percent):
        plt.text(v, i, str(v), 
                color = 'red', fontweight = 'bold', fontsize=12)
    

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("存储使用率TOP_N", fontsize=24)

    # 保存图表到pdf文档
    plt.savefig(resource_utilization, bbox_inches='tight', pad_inches=0.1)

