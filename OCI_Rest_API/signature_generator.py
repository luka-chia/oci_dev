import base64
import hashlib
import urllib.parse
import requests
import json
from OpenSSL import crypto  # 用于加载私钥
from datetime import datetime, timezone
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

# 读取 OCI 配置
OCI_USER_OCID = 'ocid1.user.oc1..aaaaaaaafkg344hepfwbzyrdzbi334q2ncyjforez3pw7kegmyqut5l7eorq'
OCI_TENANCY_OCID = 'ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba'
OCI_FINGERPRINT = 'a2:d1:18:32:c1:ab:73:ba:ec:63:02:d1:69:e1:39:24'
OCI_REGION = 'ap-singapore-1'
OCI_PRIVATE_KEY_PATH = '/Users/luka/.oci/my.pem'

# 🔹 读取私钥
with open(OCI_PRIVATE_KEY_PATH, "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# 🔹 构造 API Key ID
API_KEY_ID = f"{OCI_TENANCY_OCID}/{OCI_USER_OCID}/{OCI_FINGERPRINT}"


def generate_signature(http_method, url, headers=None, body=None):
    """
    生成 OCI API 请求签名
    :param http_method: HTTP 方法 (GET, POST, PUT, DELETE)
    :param url: 请求 URL
    :param headers: 额外的 HTTP 头 (默认 None)
    :param body: 请求体 (仅适用于 POST, PUT, PATCH)
    :return: 认证头部字符串
    """
    headers = headers or {}
    parsed_url = urllib.parse.urlparse(url)

    # 提取 host 和 path
    host = parsed_url.netloc
    path = parsed_url.path or "/"
    query = f"?{parsed_url.query}" if parsed_url.query else ""
    full_path = path + query

    # 获取当前 UTC 时间
    current_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

    # 🔹 必须签名的 Headers (注意顺序)
    required_headers = {
        "(request-target)": f"{http_method.lower()} {full_path}",
        "host": host,
        "date": current_date,
    }

    # 🔹 计算请求体 SHA256 哈希 (仅适用于 POST, PUT, PATCH)
    if body and http_method.upper() in {"POST", "PUT", "PATCH"}:
        body_hash = hashlib.sha256(body.encode("utf-8")).digest()
        body_hash_base64 = base64.b64encode(body_hash).decode("utf-8")
        required_headers["x-content-sha256"] = body_hash_base64
        required_headers["content-type"] = "application/json"
        required_headers["content-length"] = str(len(body))

    # 🔹 组合签名字符串
    signing_string = "\n".join(f"{k}: {v}" for k, v in required_headers.items())
    signature = private_key.sign(signing_string.encode("utf-8"),padding.PKCS1v15(),hashes.SHA256())
    # 转换为 Base64
    signature_base64 = base64.b64encode(signature).decode("utf-8")

    # 🔹 生成 Authorization 头部
    headers_list = " ".join(required_headers.keys())
    authorization_header = (
        f'Signature version="1",keyId="{API_KEY_ID}",algorithm="rsa-sha256",'
        f'headers="{headers_list}",signature="{signature_base64}"'
    )

    return authorization_header, current_date, required_headers.get("x-content-sha256")


# 🔹 示例请求：列出 OCI Object Storage 里的 bucket
if __name__ == "__main__":
    compartment_id = "ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"
    test_url = f"https://objectstorage.ap-singapore-1.oraclecloud.com/n/sehubjapacprod/b/?compartmentId="+compartment_id
    
    # 生成签名
    signature, date, body_sha256 = generate_signature("GET", test_url)

    print(signature)
    # 构造请求头
    headers = {
        "Authorization": signature,
        "date": date,
        "host": urllib.parse.urlparse(test_url).netloc
    }
    if body_sha256:
        headers["x-content-sha256"] = body_sha256
        headers["content-type"] = "application/json"

    # 发送请求
    response = requests.get(test_url, headers=headers)

    # 输出结果
    print("Response Status:", response.status_code)
    try:
        print("Response Body:", response.json())
    except json.JSONDecodeError:
        print("Response Body:", response.text)
