import sys

import requests


def get_access_token():
    """
    获取access_token
    :return:
    """
    corpid = sys.argv[2]
    corpsecret = sys.argv[3]
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
    resp = requests.get(url=url)
    return resp.json()['access_token']


def push_content(content='消息推送测试'):
    """
    企业微信应用消息推送
    :return:
    """
    access_token = get_access_token()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token
    params = {
        "touser": "",
        "toparty": "1",
        "totag": "",
        "msgtype": "text",
        "agentid": sys.argv[4],
        "text": {
            "content": content
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0
    }
    resp = requests.post(url=url, json=params)
    print(resp.json())


def webhooks():
    """
    企业微信机器人消息推送
    :return:
    """
    url = sys.argv[5]
    content = {
        "msgtype": "text",
        "text": {
            "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
            "mentioned_list": ["@all"],
            "mentioned_mobile_list": ["@all"]
        }
    }
    resp = requests.post(url=url, json=content)
    print(resp.json())


if __name__ == '__main__':
    push_content()
