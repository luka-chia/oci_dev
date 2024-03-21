# coding=utf-8
# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import datetime
import numpy as np
import matplotlib.pyplot as plt

def get_cost_report(tenant_id, cost_pdf):
    # Initialize service client with default config file
    config = oci.config.from_file()
    usage_api_client = oci.usage_api.UsageapiClient(config)

    first_day_last_month = datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)
    last_day_last_month = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)


    # Send the request to service, some parameters are not required, see API
    # doc for more info
    request_summarized_usages_response = usage_api_client.request_summarized_usages(
        request_summarized_usages_details=oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            time_usage_started=datetime.datetime.strptime(str(first_day_last_month), "%Y-%m-%d"),
            time_usage_ended=datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d"),
            granularity="MONTHLY",
            group_by=["compartmentName"],
            query_type="COST",
            compartment_depth=1))

    # Get the data from response
    items = request_summarized_usages_response.data.items
    compartment_costs = dict()
    for item in items:
        if("INR"==item.currency):
            month = item.time_usage_started.strftime('%Y-%#m')
            cost = round(item.computed_amount,2)
            if(item.compartment_name in compartment_costs):
                compartment_costs.get(item.compartment_name)[month] = cost
            else:
                month_cost = {month:cost}
                compartment_costs[item.compartment_name] = month_cost
    print(compartment_costs)
    generate_pdf(compartment_costs=compartment_costs, cost_pdf=cost_pdf)

def get_this_month():
	# 获取当前日期
    now_time = datetime.datetime.now()
    # 返回本月份
    return now_time.strftime('%Y-%#m')

def get_last_month():
	# 获取当前日期
    now_time = datetime.datetime.now()
    # 获取本月的第一天
    end_day_in_mouth = now_time.replace(day=1)
    # 获取上月的最后一天
    last_mouth = end_day_in_mouth - datetime.timedelta(days=1)
    # 返回上月的月份
    return last_mouth.strftime('%Y-%#m')

def parse_data(compartment_costs):
    compartment_names = [key for key in compartment_costs][0:10]

    last_month_cost = list()
    this_month_cost = list()

    for compartment_name in compartment_names:
        cost = compartment_costs.get(compartment_name)
        last_month_cost.append(cost.get(get_last_month()))
        this_month_cost.append(cost.get(get_this_month()))
    #print("===================================")
   # print(compartment_names)
    #print(last_month_cost)
    #print(this_month_cost)
    return compartment_names, last_month_cost, this_month_cost

def generate_pdf(compartment_costs, cost_pdf):
    # 分别处理并提取数据到不同的数组中（图表中需要用到）
    compartment_names, last_month_cost, this_month_cost = parse_data(compartment_costs=compartment_costs)
    last_month = get_last_month()
    this_month = get_this_month()
    
    colors = plt.cm.tab10(range(len(compartment_names)))
    rows = [this_month, last_month]

    x = np.arange(len(compartment_names))
    width=0.4
    #x1 = x - width/2
    #x2 = x + width/2

    fig, ax = plt.subplots(layout='constrained')
    rects_x1 = plt.bar(x, last_month_cost, label=last_month, width=width, color='#FF7F0E')
    ax.bar_label(rects_x1, padding=1, fontsize=5, color='#FF7F0E')
    rects_x2 = plt.bar(x + width, this_month_cost, label=this_month, width=width, color='#2CA02C')
    ax.bar_label(rects_x2, padding=1, fontsize=5, color='#2CA02C')

    plt.xticks(x + width/2, compartment_names, fontsize=6, rotation=45)
    plt.yticks(rotation=45, fontsize=6)
    plt.ylabel(u'费用成本', fontsize=6)
    
    # 在柱状图上显示数字
    '''
    for i, v in enumerate(this_month_cost):
        plt.text(i, v, str(v), color='#2CA02C', fontsize=5, ha='left', va='bottom')
    
    for i, v in enumerate(last_month_cost):
        plt.text(i, v, str(v), color='#FF7F0E', fontsize=5, ha='left', va='bottom')
    '''
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='upper right', ncols=1)


    # Add a table at the bottom of the axes
    table = plt.table(cellText=[this_month_cost,last_month_cost], 
              rowLabels=rows,
              rowColours=colors,
              colLabels=compartment_names,
              loc='bottom', 
              cellLoc='center',
              rowLoc='center',
              bbox=[0, -0.6, 1, 0.24])
    table.auto_set_font_size(False)
    table.set_fontsize(5)
    # Adjust layout to make room for the table:
    # plt.subplots_adjust(left=0.2, bottom=0.2)

    
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(u"各区间近期费用支出详情")
    
    # 保存图表到pdf文档
    plt.savefig(cost_pdf, bbox_inches='tight', pad_inches=0.1)
