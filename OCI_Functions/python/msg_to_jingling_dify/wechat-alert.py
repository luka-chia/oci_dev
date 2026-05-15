#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
author:yangzai
project:
DATE:2024/8/05
说明：接收aws通知并将到的消息调阿里通义api接口将消息进行总结归纳后再发出告警，不要将所有英文都消息都发送出去，会被屏蔽的
'''
import json
import requests
import os
from http import HTTPStatus
from dashscope import Application
# 新增阿里通义API调用函数
'''def summarize_with_tongyi(text):

    print("开始调用阿里通义接口")
    print(text)
    # 设置API Key
    api_key = os.environ['api_key']
    app_id = os.environ['app_id']
    
    # 调用百炼的文本总结API,使用qwen-plus-latst
    response = Application.call(
        api_key=api_key,
        app_id=app_id,
        async_timeout=100,
        prompt=f"请将此段内容用中文并进行简洁总结，只要将总结后的500内字发我即可，不要将所有内容都发出来格式为：来自AI提炼后内容，如有问题请查看AWS原始信息：{text}",
    )
    # 处理响应
    if response.status_code == HTTPStatus.OK:
        print("API调用成功")
        print("总结后的文本：", response.output.text)
        return response.output.text
    else:
        print(f"API调用失败，状态码：{response.status_code}")
        print(f"错误信息：{response.output}")
        return text  # 如果API调用失败，返回原始文本
'''
# dify密钥
DIFI_APIKEY = os.environ['DIFI_APIKEY']
DIFI_APIURL = os.environ['DIFI_APIURL']
USER_IDENTIFIER = "awsxh_wechat_lambda"
def is_json(s: str) -> bool:
    """判断字符串是否为 JSON"""
    try:
        json.loads(s)
        return True
    except:
        return False
def lambda_handler(event, context):
    qywx_robot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="
    token = os.environ['mytoken']
    send_url = qywx_robot_url + token
    headers = {
        'Content-Type': 'application/json'
    }

    context = ""
    #print("event:")
    print(event)
    #try:
        #subject = event['Records'][0]['Sns']['Subject']
    record = event['Records'][0]
    json_msg = "初始空"
    #timestamp = event['Records'][0]['Sns']['Timestamp']
    if 'Records' in event and len(event['Records']) > 0:
        if 'Sns' in record:
            message = record['Sns']['Message'] 
            json_msg = json.dumps(json.loads(message), ensure_ascii=False) if is_json(message) else message
        else:
            json_msg = record
    else:
        json_msg = record
    headers = {"Authorization": f"Bearer {DIFI_APIKEY}","Content-Type": "application/json"}        
    payload = {
    "inputs": {
        "AWS_MSG": json_msg
    },
    "response_mode": "blocking",
    "user": USER_IDENTIFIER
    }
    #调dify
    print(DIFI_APIURL)
    response = requests.post(DIFI_APIURL,json=payload,headers=headers,timeout=30)
    if response.status_code == 200:
        result = response.json()
        if result.get("data", {}).get("status") == "succeeded":
            print("✅ Dify 工作流执行成功")
        else:
            print("😭 Dify 工作流执行失败")
    else:
        print(response.text)
    #解析失败，直接调企微发aws原始信息
    '''except Exception as e:
        Records = event['Records'][0]
        title = '<font color=\"info\">[Aws 通知--告警代码解析异常]</font>'
        content = title + "\n> <font color=green>Records:</font>" + str(Records)

    msg = {
        "msgtype": 'markdown',
        "markdown": {'content': content}
    }
    response = requests.post(url=send_url, data=json.dumps(msg), headers=headers)
    print('已发送消息到企业微信')
    return response.text'''


