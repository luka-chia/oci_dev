import io
import json
import logging
import requests

def is_json(s: str) -> bool:
    """判断字符串是否为 JSON"""
    try:
        json.loads(s)
        return True
    except:
        return False

def handler(ctx, data: io.BytesIO = None):
    logging.getLogger().info("begin handle the request" + str(data) )
    cfg = ctx.Config()
    try:
        DIFI_APIKEY = str(cfg["DIFI_APIKEY"])
        DIFI_APIURL = str(cfg["DIFI_APIURL"])
        USER_IDENTIFIER = str(cfg["USER_IDENTIFIER"])
        token = str(cfg["token"])
    except:
        logging.error('Some of the function config keys are not set')
        raise

    try:
        body = json.loads(data.getvalue())
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    headers = {
        'Content-Type': 'application/json'
    }

    json_msg = json.dumps(json.loads(body), ensure_ascii=False) if is_json(body) else body

    headers = {"Authorization": f"Bearer {DIFI_APIKEY}","Content-Type": "application/json"}        
    payload = {
    "inputs": {
        "OCI_MSG": json_msg
    },
    "response_mode": "blocking",
    "user": USER_IDENTIFIER
    }
    #调dify
    logging.getLogger().info(DIFI_APIURL)
    response = requests.post(DIFI_APIURL,json=payload,headers=headers,timeout=30)
    if response.status_code == 200:
        result = response.json()
        if result.get("data", {}).get("status") == "succeeded":
            logging.getLogger().info("✅ Dify 工作流执行成功")
        else:
            logging.getLogger().info("😭 Dify 工作流执行失败")
    else:
        logging.getLogger().info(response.text)
    
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
    logging.getLogger().info('已发送消息到企业微信')
    return response.text
    '''
