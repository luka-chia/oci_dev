# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import datetime
import matplotlib.pyplot as plt

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info

def get_cloud_guard_report(compartment_id, cloud_guard):
    # Initialize service client with default config file
    config = oci.config.from_file()
    cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)


    # Send the request to get the risk_scores
    request_risk_scores_response = cloud_guard_client.request_risk_scores(
        compartment_id=compartment_id,
        limit=49)
    risk_score = request_risk_scores_response.data.items[0].risk_score
    print("Currently the tenancy risk_scores = %s" % risk_score)


    # Send the request to get the security_scores
    request_security_scores_response = cloud_guard_client.request_security_scores(
        compartment_id=compartment_id,
        limit=235)
    security_score = request_security_scores_response.data.items[0].security_score
    print("Currently the tenancy security_scores = %s, and security_rating = %s"
        %(security_score, request_security_scores_response.data.items[0].security_rating))

    # Send the request to get problems
    request_summarized_problems_response = cloud_guard_client.request_summarized_problems(
        list_dimensions=["RISK_LEVEL"],
        compartment_id=compartment_id,
        limit=6910,
        compartment_id_in_subtree=True,
        access_level="ACCESSIBLE")

    problem_items = request_summarized_problems_response.data.items
    problem_data = {}
    for item in problem_items:
        problem_data[item.dimensions_map.get("RISK_LEVEL")] = item.count
    print(problem_data)

    # Send the request to get the SecurityScoreSummarizedTrend
    end = datetime.datetime.now()
    begin = end-datetime.timedelta(days=30)
    request_security_score_summarized_trend_response = cloud_guard_client.request_security_score_summarized_trend(
        compartment_id=compartment_id,
        time_score_computed_greater_than_or_equal_to=begin,
        time_score_computed_less_than_or_equal_to=end)

    trend_items = request_security_score_summarized_trend_response.data.items
    security_score_trend = {}
    for item in trend_items:
        time_stamp = datetime.datetime.fromtimestamp(item.start_timestamp/1000)
        security_score_trend[time_stamp.strftime("%Y-%m-%d")] = item.security_score
        #print("the security_score = %s and security_rating = %s in %s"
        #    %(item.security_score, item.security_rating, datetime.datetime.fromtimestamp(item.start_timestamp/1000)))
    print(security_score_trend)

    # generate pdf report
    generate_pdf(risk_score=risk_score, security_score=security_score,
                 problem_data=problem_data, security_score_trend=security_score_trend,
                 cloud_guard=cloud_guard)

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

def transit_risk_level(risk_level):
    en_cn_map = {
        "CRITICAL": u"严重",
        "HIGH":u"高",
        "MEDIUM":u"中",
        "LOW":u"低",
        "MINOR":u"次要"
    }
    return en_cn_map.get(risk_level)

def generate_pdf(risk_score, security_score, problem_data, security_score_trend, cloud_guard):    
    plt.figure(figsize=(24, 24), dpi=100)

    # step1 draw picture about security_score
    plt.subplot(2,4,1)
    _, labels, _ = plt.pie([security_score], labels=[security_score], autopct='',
            textprops={'fontsize': 100}, labeldistance=0, colors="green")
    # Center-align the labels
    for label in labels:
        label.set_horizontalalignment('center')
    plt.legend(fontsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("当前安全评分等级", fontsize=24)

    text = u'''
    安全评分评级标准
    优秀: (80-100)
    良好: (60-79)
    一般: (40-59)
    差: (0-39)'''
    plt.text(0, -1.5, text, fontdict={'size': 24, 'color': 'red'}, ha='left', va='center')

    # step2 draw picture about risk_score
    plt.subplot(2,4,2)
    _, labels, _ = plt.pie([risk_score], labels=[risk_score], autopct='',
            textprops={'fontsize': 100}, labeldistance=0)
    # Center-align the labels
    for label in labels:
        label.set_horizontalalignment('center')
    plt.legend(fontsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("当前风险评分", fontsize=24)

    text = u'''
    风险评分提供Cloud 
    Guard检测到的问题
    对环境造成的风险级
    别的估计。风险评分
    越低代表越安全。'''
    plt.text(0, -1.5, text, fontdict={'size': 24, 'color': 'red'}, ha='left', va='center')

    # step3 draw pie picture about problem count and risk level
    risk_level = [transit_risk_level(key) for key in problem_data]
    problem_count = [value for value in problem_data.values()]
    plt.subplot(2,2,2)
    plt.pie(problem_count, labels=risk_level, autopct=autopct_format(problem_count),
            textprops={'fontsize': 25}, labeldistance=1.05)
    plt.pie([1], radius=0.7, colors='w')
    plt.legend(fontsize=16)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("不同风险等级问题数量展示", fontsize=24)

    # step4 draw link picture about security score trend
    time_stamp = [key for key in security_score_trend]
    security_score = [value for value in security_score_trend.values()]

    plt.subplot(2,1,2)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(time_stamp, security_score, color="red")
    plt.xticks(rotation=45)
    for x,y in zip(time_stamp,security_score):
        plt.text(x,y,'%.0f' % y,fontdict={'fontsize':24, "color":"red"})

    plt.xlabel("时间/天", fontsize=24)
    plt.ylabel("安全评分", fontsize=24)
    plt.title("近30天安全评分趋势线", fontsize=32)
    plt.grid(alpha=0.5)

    # 保存图表到pdf文档
    plt.savefig(cloud_guard, bbox_inches='tight', pad_inches=0.1)

