import requests
import json
import signature_generator

def generate_upst():
    # API 端点
    url = "https://auth.ap-singapore-1.oraclecloud.com/v1/token/upst/actions/GenerateUpst"

    # 请求体（确保格式正确）
    body = {
        "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtgLQYDwWyL6F9adikcya\niNnLXQh7fEpL2XXmd+lbIVvAO6fcSYmpY1YiPVrwcc1SAoDh7JQ2rDgsi3Axwjls\nKBVnUnqlomUGJOg0sM7EHxbiyn9aSjMLEOS/+YtTlFH56JyH9fOO48nDdzTewLWK\nXZPK1zpmkPkG+Kj0/zebWJg23EApc8f5BlHhxpn7UT2JU35AHCQRwQ5S6pecNbVo\nEO5d1NpDBtygRcY9dMgSaYn4n4ze8jaQXKpW7Bpd+mA3aWDp4fHPJgkhxCVqFDqh\nbTSSi2eOLIvsCslLjnqNf+yzuyIlUhXjq/lMWKGzJA/XmmfbK8zpFuYJqD69O21y\nNQIDAQAB\n-----END PUBLIC KEY-----",
        "sessionExpirationInMinutes": 60
    }


    # 生成签名
    signature, date, body_sha256 = signature_generator.generate_signature(http_method="POST", url=url, body=json.dumps(body))

    # 认证头（使用 OCI 签名）
    headers = {
        "Content-Type": "application/json",
        "Authorization": signature,
        "Date": date
    }

    if body_sha256:
            headers["x-content-sha256"] = body_sha256
            headers["content-type"] = "application/json"


    # 请求体（确保格式正确）
    body = {
        "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtgLQYDwWyL6F9adikcya\niNnLXQh7fEpL2XXmd+lbIVvAO6fcSYmpY1YiPVrwcc1SAoDh7JQ2rDgsi3Axwjls\nKBVnUnqlomUGJOg0sM7EHxbiyn9aSjMLEOS/+YtTlFH56JyH9fOO48nDdzTewLWK\nXZPK1zpmkPkG+Kj0/zebWJg23EApc8f5BlHhxpn7UT2JU35AHCQRwQ5S6pecNbVo\nEO5d1NpDBtygRcY9dMgSaYn4n4ze8jaQXKpW7Bpd+mA3aWDp4fHPJgkhxCVqFDqh\nbTSSi2eOLIvsCslLjnqNf+yzuyIlUhXjq/lMWKGzJA/XmmfbK8zpFuYJqD69O21y\nNQIDAQAB\n-----END PUBLIC KEY-----",
        "sessionExpirationInMinutes": 60
    }

    # 发送请求
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # 查看响应
    print(response.status_code)
    token = json.loads(response.text)
    token_str = token["token"]
    return token_str
    

token_str = generate_upst()
print(token_str)