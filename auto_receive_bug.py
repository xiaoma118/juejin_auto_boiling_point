import sys
import os
import requests

from message_push import push_content

herder = {
    'referer': 'https://juejin.cn/',
    'origin': 'https://juejin.cn',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    # 'cookie': os.environ.get('cookie') #本地开发工具使用
    'cookie': sys.argv[1]
}


def get_bug_list():
    """
    获取bug数量列表
    :return:
    """

    print('获取待领取的bug列表')
    url = 'https://api.juejin.cn/user_api/v1/bugfix/not_collect?aid=2608&uuid=7052935898246088232'
    params = {}
    resp = requests.post(url=url, headers=herder, json=params)
    data = resp.json()
    print(data)

    if data['err_msg'] == 'success':
        auto_receive_bug(data['data'])
    else:
        print('获取失败，请检查cookie')


def auto_receive_bug(data):
    """
    自动领取掘金BUG
    :return:
    """
    user_own_bug = get_user_own_bug()
    content = '掘金消息：\n本次操作领取了%s个bug\n当前bug数量：%s' % (len(data), user_own_bug)
    if not data:
        print('没有可领取的bug')
        push_content(content)
        return
    print('开始领取bug')
    url = 'https://api.juejin.cn/user_api/v1/bugfix/collect?aid=2608&uuid=7052935898246088232'

    for bug in data:
        params = {
            'bug_time': bug['bug_time'],
            'bug_type': bug['bug_type']
        }
        resp = requests.post(url, json=params, headers=herder)
        print('领取成功', resp.json()['err_msg'])
    push_content(content)


def get_user_own_bug():
    """
    获取当前bug数量
    :return:
    """
    # 先获取competition_id
    params = {
        'competition_id': ''
    }
    url_bugfix = 'https://api.juejin.cn/user_api/v1/bugfix/competition?aid=2608&uuid=7052935898246088232'
    resp = requests.post(url=url_bugfix, headers=herder, json=params)
    params['competition_id'] = resp.json()['data']['competition_id']
    # 使用competition_id获取 账户bug数量
    url = 'https://api.juejin.cn/user_api/v1/bugfix/user?aid=2608&uuid=7052935898246088232'
    response = requests.post(url=url, headers=herder, json=params)
    data = response.json()
    if data['err_msg'] == 'success':
        user_own_bug = data['data']['user_own_bug']
        return user_own_bug
    return False


if __name__ == '__main__':
    get_bug_list()
