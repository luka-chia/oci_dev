import requests
import urllib
import upst_generator
from datetime import datetime, timezone
# OCI 生成的 UPST 令牌
UPST_TOKEN = upst_generator.generate_upst()
# OCI API 端点（示例：列出 Compute Instances）
compartment_id = "ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"
test_url = f"https://objectstorage.ap-singapore-1.oraclecloud.com/n/sehubjapacprod/b/?compartmentId={compartment_id}"

current_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

# 请求头
headers = {
    "Authorization": f"Bearer {UPST_TOKEN}",
    "Content-Type": "application/json",
    "date": current_date,
    "host": urllib.parse.urlparse(test_url).netloc
}

# 发送请求
response = requests.get(test_url, headers=headers)

# 解析响应
if response.status_code == 200:
    print("成功调用 OCI API")
    print(response.json())  # 输出 JSON 结果
else:
    print(f"调用失败: {response.status_code}, {response.text}")