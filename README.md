# OCI Dev Samples

这个目录收集了一组 Oracle Cloud Infrastructure (OCI) 开发、运维和集成示例，覆盖 OCI CLI、OCI SDK、Functions、对象存储 S3 兼容 API、自动化脚本和若干实践文档。代码主要用于演示和二次开发参考，建议先在测试环境验证，再按实际租户、区域、网络、IAM 策略和资源命名进行调整。

## 免责声明

- 本目录中的脚本和示例仅供学习、验证和参考，不代表 Oracle 官方交付或服务承诺。
- 部分脚本会创建、修改或删除云资源，可能产生费用或影响现有业务；执行前请仔细阅读代码并确认目标 compartment、region、resource OCID、tag、policy 等参数。
- 示例中的配置、密钥、endpoint、bucket、namespace、用户名等需要替换为你自己的环境信息；不要提交真实密钥或生产凭据。

## 前置准备

按需准备以下工具和权限：

- OCI CLI：配置 `~/.oci/config`、API key、tenancy/user fingerprint，并确保当前 profile 有对应权限。
- OCI SDK：根据语言安装 Python、Java、Go、.NET 或 Node.js 依赖，并配置 OCI 认证信息。
- Cloud Shell：大多数 CLI/SDK 示例也可以在 OCI Cloud Shell 中运行。
- Functions：需要已配置 Fn Project CLI、Docker、OCI Registry、Functions application、dynamic group 和 IAM policy。
- S3 兼容 API：需要 Object Storage namespace、bucket、customer secret key、region endpoint 等信息。

参考文档：

- OCI CLI setup: <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm>
- OCI SDK setup: <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm>
- OCI Cloud Shell: <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/devcloudshellintro.htm>
- OCI Functions: <https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm>

## 目录结构

| 路径 | 内容 |
| --- | --- |
| [`OCI-Auto-Scripts/`](./OCI-Auto-Scripts) | OCI 自动化脚本集合，包含资源批量操作、查询、备份、压测、OpenShift、RMS stack、AI/LLM 示例等。 |
| [`OCI_Functions/`](./OCI_Functions) | OCI Functions 示例，覆盖 Python、JavaScript、.NET，以及通知、队列、Kafka、证书监控、数据库扩缩容等场景。 |
| [`OCI_SDK/`](./OCI_SDK) | OCI SDK 示例代码，包含 Python、Java、Go 的 Object Storage、Events、Functions、Desktop 等 API 调用。 |
| [`AWS_S3_SDK/`](./AWS_S3_SDK) | 使用 AWS S3 SDK 或前端代码访问 OCI Object Storage S3 兼容接口的示例。 |
| [`Documents/`](./Documents) | OCI 实践文档和 PDF，例如 Ubuntu 添加副网卡、Libreswan IPsec VPN、Cloud Guard 等。 |

## 重点用例索引

### OCI Auto Scripts

- [Create VMs and Attach New Block Volumes](./OCI-Auto-Scripts/oci%20create%20vms%20attached%20bvs)：创建 VM 并挂载 Block Volume。
- [OpenShift Automatic Deployment on OCI VMs](./OCI-Auto-Scripts/openshift/README.md)：在 OCI VM 上部署 OpenShift 的 Terraform/脚本示例。
- [Add/update tags to OCI Resources](./OCI-Auto-Scripts/oci%20batch%20add%20tags/README.md)：批量给 OCI 资源添加或更新标签。
- [Format Block Volume Disks](./OCI-Auto-Scripts/ssh%20remote%20run%20cmd%20and%20format%20blockvolume/README.md)：通过 SSH 远程执行命令并格式化数据盘。
- [Query Resources Across Regions](./OCI-Auto-Scripts/Query%20Resources%20Across%20Regions/README.md)：跨区域查询资源并导出结果。
- [Create Bastion Session](./OCI-Auto-Scripts/create_bastion_session.sh)：创建 OCI Bastion session。
- [Autobackup All Block Volumes](./OCI-Auto-Scripts/autobackup%20all%20block%20volumes/README.MD)：自动备份 Block Volume。
- [OCI Bucket Statistics](./OCI-Auto-Scripts/oci%20bucket%20statistics/README.MD)：统计 Object Storage bucket 使用情况。
- [OCI IP Finder](./OCI-Auto-Scripts/oci%20ip%20finder/README.md)：查找 OCI 资源公网/私网 IP。
- [Test Region Capacity for a Shape](./OCI-Auto-Scripts/test%20if%20a%20region%20has%20capacity%20for%20a%20specified%20shape/README.MD)：测试指定 region/shape 是否可能容量不足。
- [OCI Exporter](./OCI-Auto-Scripts/oci_exporter/README.md)：Prometheus OCI exporter 示例。
- [OCI Small Clean GUI](./OCI-Auto-Scripts/oci%20small%20clean%20gui/README.md)：清理资源的小型 GUI 工具。
- [RMS Stack](./OCI-Auto-Scripts/rms%20stack)：Resource Manager stack/job 操作示例。
- [K6 Stress Test](./OCI-Auto-Scripts/k6%20stress%20test)：k6 API 压测脚本。
- [OCI LLM Example Code](./OCI-Auto-Scripts/oci%20llm%20example%20code)：Cohere、Llama、Grok 等模型 streaming 调用示例。
- [Grok4 as VLM](./OCI-Auto-Scripts/Grok4%20as%20VLM)：Grok4 多模态调用示例。
- [Speech ASR / Summary / Sentiment](./OCI-Auto-Scripts/speech%20asr%20%7Csummary%7C%20sentiment%20analysis/README.MD)：语音识别、摘要、情感分析示例。
- [OCI Document Understanding](./OCI-Auto-Scripts/oci%20document%20understanding)：Document Understanding OCR 示例。
- [Python Auth Without OCI SDK](./OCI-Auto-Scripts/python%20auth%20without%20oci%20sdk)：不依赖 OCI SDK 的 Python API 签名示例。
- [Use OCI API in OpenResty](./OCI-Auto-Scripts/openresty%20oci%20api)：OpenResty/Lua 调用 OCI API 示例。
- [Many Tools OCI Image](./OCI-Auto-Scripts/Many%20Useful%20Tools%20Custom%20Image--%20Gold%20Hundun/README.MD)：包含常用工具的自定义镜像说明。
- [Auto Install Management Agent in Windows](./OCI-Auto-Scripts/auto%20install%20management%20agent%20in%20windows/README.MD)：Windows 自动安装 Management Agent 示例。
- [Java Connect ADW](./OCI-Auto-Scripts/java_connect_adw)：Java 连接 Autonomous Data Warehouse 示例。

### OCI Functions

- [Functions 总览](./OCI_Functions/README.md)
- [Function Template](./OCI_Functions/function_template/README.md)：发布 Notification 的 Python function 模板。
- [Python Functions](./OCI_Functions/python)：包含 `notification-publish`、`queue_putmessage`、`logs_to_kafka`、`logs_to_kafka_mtls`、`certificate_expire_monitor`、`scale-dbsystem`、`http_utils_with_auth`、`msg_to_jingling_dify` 等示例。
- [.NET Queue Function](./OCI_Functions/dotnet/queue_putmessage)：.NET 6 Queue put message function。
- [JavaScript Notification Function](./OCI_Functions/js/ocinoti)：JavaScript 通知示例。

### OCI SDK Examples

- [Python Examples](./OCI_SDK/Python_examples)：Object Storage bucket/object、Events、Functions、Desktop API 示例。
- [Java Examples](./OCI_SDK/Java_examples)：Object Storage 原生 SDK、S3 兼容接口、工具类和 Maven 示例。
- [Go Examples](./OCI_SDK/Go_examples)：Application、Bucket、Object 相关 Go SDK 示例。
- [OCI .NET SDK Demo](./OCI-Auto-Scripts/oci%20.net%20sdk%20demo/README.md)：ADB/AJD、Object Storage、Queue、Stream、OpenSearch 等 .NET SDK 示例。

### S3 Compatible API

- [AWS S3 Java SDK Demo](./AWS_S3_SDK/awssdkdemo)：使用 AWS Java S3 SDK 操作 OCI Object Storage 兼容接口。
- [Vue S3 Example](./AWS_S3_SDK/vue-example/readme.txt)：前端 Vue 示例，包含分片、预签名 URL 等相关代码。
- [Curl Upload to OCI S3 Compatible Bucket](./OCI-Auto-Scripts/curl%20upload%20file%20to%20oci%20s3%20compatible%20bucket)：使用 curl 上传到 S3 兼容 bucket。
- [S3 Presigned URL Upload](./OCI-Auto-Scripts/s3%20pesigned%20url%20create%20and%20upload%20files%20to%20oci%20bucket)：生成 S3 预签名 URL 并上传文件。
- [C/C++ S3 Compatible API](./OCI-Auto-Scripts/cpp%20s3%20compatible%20api%20in%20oci%20buckets)：C/C++ 访问 OCI bucket 的 S3 兼容接口示例。
- [PAR for C HTTP Client](./OCI-Auto-Scripts/oci%20bucket%20par%20for%20C%20language%20http%20client)：C 语言 HTTP client 访问 Object Storage PAR 示例。

### Documents

- [OCI 在 Ubuntu 上添加副网卡](./Documents/OCI%20在%20ubuntu%20上添加副网卡.pdf)
- [基于 Libreswan 搭建 IPsec VPN](./Documents/基于liberswan搭建ipsec-vpn.pdf)
- [Enable Cloud Guard](./Documents/Cloud_Guard/enable_cloud_guard.pdf)

## 使用建议

1. 先阅读目标子目录的 README 或源码注释，确认脚本的输入参数、默认 compartment/region/profile 和资源操作范围。
2. 优先在测试 compartment 或 Cloud Shell 中运行，避免直接对生产资源执行批量脚本。
3. 对会修改资源的脚本，建议先增加 dry-run、limit、filter 或输出确认步骤。
4. 执行前检查依赖文件，例如 `requirements.txt`、`pom.xml`、`go.mod`、`package.json`、`func.yaml`。
5. 执行后及时清理测试资源，避免持续计费。

## 常见运行方式

```bash
# Python 示例
python3 script.py

# Shell 脚本
chmod +x script.sh
./script.sh

# Go 示例
go mod tidy
go run main.go

# Java/Maven 示例
mvn clean package
mvn exec:java

# OCI Functions 示例
fn build
fn deploy --app <application-name>
fn invoke <application-name> <function-name>
```

> 具体命令以各子目录 README、源码和 `func.yaml` 为准。

## Contributing

欢迎提交新的脚本、示例和文档。提交前请尽量补充 README、参数说明和安全注意事项，并确保不要包含真实租户信息、私钥、token 或生产环境敏感数据。

## Contact

本仓库由 Oracle China SEHub Solutions 相关成员维护，用于方案沉淀和示例共享，不代表 Oracle 官方义务。
