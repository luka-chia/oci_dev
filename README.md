# Disclaimer

This repo is for collecting scripts when you use Oracle Cloud Infrastructure (OCI), including sdk samples, functions, and s3 compatibility api, especially when you need to operate mutliple resources at once or automatically.

The script could be writen based on OCI CLI command, or python/C#/Java code based on OCI SDK. 

For the record, those tools and code are all for your reference, please test it and then fit in your environment, we have ***NO*** resposibility when you apply those tools or code.

# Prerequisites

You have to setup related OCI CLI or SDK envrionment before running the code directly.
Follow the Oracle Offical documents about how to setup related envrionment.

CLI setup: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm

SDK setup: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm

You could also run these on CloudShell instead your own workstation/laptop.

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/devcloudshellintro.htm


# Usecase List

Here are the usecases covered by the scripts, we list these as scripts examples, and hope to give some rough idea on how to adjust the code to fit your real usecases.
please search in this page by ctl+f, will not be listed below in the future.

- [Create VMs and Attach New Block Volumes](./OCI-Auto-Scripts-main/oci%20create%20vms%20attached%20bvs)
- [Openshift Automatic Deployment on OCI VMs](./OCI-Auto-Scripts-main/openshift/README.md)
- [Add/update tags to OCI Resources ](./OCI-Auto-Scripts-main/oci%20batch%20add%20tags)
- [Format Block Volume Disks](./OCI-Auto-Scripts-main/ssh%20remote%20run%20cmd%20and%20format%20blockvolume)
- [OCI SDK .Net Sample Code](./OCI-Auto-Scripts-main/oci%20.net%20sdk%20demo)
- [Query Resources across OCI regions](./OCI-Auto-Scripts-main/Query%20Resources%20Across%20Regions)
- [Test uploading files to oci with s3 compatible API](./OCI-Auto-Scripts-main/curl%20upload%20file%20to%20oci%20s3%20compatible%20bucket)
- [Python auth without oci sdk](./OCI-Auto-Scripts-main/python%20auth%20without%20oci%20sdk)
- [Use oci api in Openresty](./OCI-Auto-Scripts-main/openresty%20oci%20api)
- [oci small clean gui ](./OCI-Auto-Scripts-main/oci%20small%20clean%20gui)
- [prometheus oci exporter ](./OCI-Auto-Scripts-main/oci_exporter)
- [Many Tools OCI Image](./OCI-Auto-Scripts-main/Many%20Useful%20Tools%20Custom%20Image--%20Gold%20Hundun)
- [auto install management agent in windows](./OCI-Auto-Scripts-main/auto%20install%20management%20agent%20in%20windows)
- [java connect to adw ](./OCI-Auto-Scripts-main/java_connect_adw)
- [OCI Functions .NET Samples](./OCI_Functions/dotnet)
- [OCI Functions Python Samples](./OCI_Functions/python)
- [OCI Functions Template](./OCI_Functions/function_template)
- [OCI SDK Go Examples](./OCI_SDK/Go_examples)
- [OCI SDK Java Examples](./OCI_SDK/Java_examples)
- [OCI SDK Python Examples](./OCI_SDK/Python_examples)
- [AWS S3 SDK Demo](./AWS_S3_SDK/awssdkdemo)
- [Vue Example with AWS S3](./AWS_S3_SDK/vue-example)
- [Check Client HTML Tool](./check_client.html)
- [Create Bastion Session](./OCI-Auto-Scripts-main/create_bastion_session.sh)
- [Monitor Disk Usage](./OCI-Auto-Scripts-main/monitor%20disk%20usage)
- [OSS Python Script](./OCI-Auto-Scripts-main/OSS.py)
- [Autobackup All Block Volumes](./OCI-Auto-Scripts-main/autobackup%20all%20block%20volumes)
- [AWS S3 Java SDK Example](./OCI-Auto-Scripts-main/aws%20s3%20java%20sdk%20example)
- [Bucket Usage Statistics](./OCI-Auto-Scripts-main/bucket%20usage%20statistics)
- [CPP S3 Compatible API in OCI Buckets](./OCI-Auto-Scripts-main/cpp%20s3%20compatible%20api%20in%20oci%20buckets)
- [Grok4 as VLM](./OCI-Auto-Scripts-main/Grok4%20as%20VLM)
- [K6 Stress Test](./OCI-Auto-Scripts-main/k6%20stress%20test)
- [OCI Bucket PAR for C Language HTTP Client](./OCI-Auto-Scripts-main/oci%20bucket%20par%20for%20C%20language%20http%20client)
- [OCI Bucket Statistics](./OCI-Auto-Scripts-main/oci%20bucket%20statistics)
- [OCI Document Understanding](./OCI-Auto-Scripts-main/oci%20document%20understanding)
- [OCI IP Finder](./OCI-Auto-Scripts-main/oci%20ip%20finder)
- [OCI LLM Example Code](./OCI-Auto-Scripts-main/oci%20llm%20example%20code)
- [RMS Stack](./OCI-Auto-Scripts-main/rms%20stack)
- [S3 Presigned URL Create and Upload Files to OCI Bucket](./OCI-Auto-Scripts-main/s3%20pesigned%20url%20create%20and%20upload%20files%20to%20oci%20bucket)
- [Speech ASR | Summary | Sentiment Analysis](./OCI-Auto-Scripts-main/speech%20asr%20|summary|%20sentiment%20analysis)
- [Test if a Region Has Capacity for a Specified Shape](./OCI-Auto-Scripts-main/test%20if%20a%20region%20has%20capacity%20for%20a%20specified%20shape)



# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.  The repo is maintained by Oracle China SEHub Solutions employees, but not related with Oracle offical obligation. 

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

# Contact
You could also contact us by mail, lu.jia@oracle.com
