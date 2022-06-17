import requests
import sys

herder = {
    'referer': 'https://juejin.cn/',
    'origin': 'https://juejin.cn',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'cookie': sys.argv[1]
}


def get_latest_dynamic():
    """
    获取沸点最新动态列表
    :return:
    """
    url = 'https://api.juejin.cn/recommend_api/v1/short_msg/recommend?aid=2608&uuid=7052935898246088232'

    params = {
        'cursor': '0',
        'id_type': 4,
        'limit': 100,
        'sort_type': 300
    }
    rep = requests.post(url=url, json=params, headers=herder)
    data_list = rep.json()['data']
    for data in data_list:
        digg_user_list = data['digg_user']
        user_name_list = [item['user_name'] for item in digg_user_list]
        if '贤菜' not in user_name_list:
            run_like(data['msg_id'])


def run_like(msg_id):
    url = 'https://api.juejin.cn/interact_api/v1/digg/save?aid=2608&uuid=7052935898246088232'
    params = {
        'item_type': 4,
        'item_id': msg_id,
        'client_type': 2608
    }
    resp = requests.post(url=url, headers=herder, json=params)
    if resp.json()['err_msg'] == 'success':
        print('点赞成功')


if __name__ == '__main__':
    get_latest_dynamic()
