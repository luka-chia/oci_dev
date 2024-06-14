# kbot aka knowledge based chatbot


## operating system

os should be linux with g++, gcc, cmake

## download the code

add deploy key https://gitee.com/munger1985/ai/deploy_keys/new

git clone git@gitee.com:munger1985/ai.git

cd ai/kbot/


## install python env

```commandline
conda create -n kbot python=3.10 -y
conda activate kbot
```

## install deps

```commandline
pip install -r req*.txt
```

## config

config oci api key, and config.py
make sure your home directory, e.g. KB_ROOT_PATH should make it right.
or auth using instance principal without api key
need to add policy below

```commandline
allow dynamic-group <xxxx> to manage generative-ai-family in tenancy
xxxx is your dynamic-group that indicated your vm or other resources
```

## python start 

```commandline
python main.py  --port 8899 
python main.py  --port 8899 --hf_token xxx
python main.py  --port 8899 --ssl_keyfile tls.key --ssl_certfile tls.crt
python main.py  --port 443 --ssl_keyfile /home/ubuntu/qq/dev.oracle.k8scloud.site.key  --ssl_certfile /home/ubuntu/qq/dev.oracle.k8scloud.site.pem
```

## Docker approach


### build

```commandline
docker build -t kbot .
```

### docker start

if you don't need oss llm, ignore --hf_token xxx
if you dont have gpu, ignore --gpus all

#### docker with gpu

```commandline
docker run --gpus all  -e port=8899  -p 8899:8899  kbot  --hf_token <your huggingface token> --port 8899
```

#### docker with cpu

```commandline
docker run  -e port=8899    -p 8899:8899  kbot  --hf_token <your huggingface token> --port 8899
```

#### oci prebuilt docker

```commandline
docker run  -e port=8899   -p 8899:8899  sin.ocir.io/sehubjapacprod/munger:kbot   --port 8899
```



#### Auto Start
##### remember open port in linux, for instance 443

* -A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT

```commandline
the script is in autoStart.sh 
crontab -e
@reboot /bin/bash /home/ubuntu/kbot/autoStart.sh
```