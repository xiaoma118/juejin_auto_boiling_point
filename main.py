import random
import time

import requests
from requests_html import HTMLSession
import re
import sys

def get_wan():
    """
    获取文案
    :return:
    """
    # 文案地址
    domain_name = 'https://m.wenanwang.com'
    url = 'https://m.wenanwang.com/zt/zhiyu/'
    session = HTMLSession()
    rep = session.get(url=url, timeout=3)
    # 获取多个标签url
    label_urls = rep.html.xpath('//*[@id="wrap"]/a/@href')
    # 随机一个标签
    son_url = label_urls[random.randint(0, len(label_urls)-1)]
    # 请求标签链接
    rep = session.get(url=son_url, timeout=3)
    time.sleep(1)
    # 解析标签链接 获取多个文案文章url
    article_urls = rep.html.xpath('/html/body/div[5]/div[2]/li/a/@href')
    # 随机一个文章
    wz_url = article_urls[random.randint(0, len(article_urls)-1)]
    # 请求文章
    resp = session.get(url=domain_name + wz_url, timeout=3)
    # 解析文章
    content_list = resp.html.xpath('/html/body/div[4]/div[2]/p')
    # 随机两个文案
    wan = []
    for i in range(0, 2):
        content = filter_wan(content_list)
        wan.append(content)

    return wan


def filter_wan(content_list):
    """
    筛选文案
    :return:
    """
    content = content_list[random.randint(0, len(content_list))].text
    if len(''.join(content)) < 16:  # 小于15字的不要
        content = filter_wan(content_list)
    # 去除字符串中的数字
    content = re.sub(r'\d|、|\.', '', content)
    return ''.join(content)


def auto_juejin():
    herder = {
        'referer': 'https://juejin.cn/',
        'origin': 'https://juejin.cn',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'cookie': sys.argv[1]
    }
    print(herder)
    url = 'https://api.juejin.cn/content_api/v1/short_msg/publish?aid=2608&uuid=7052935898246088232'
    params = {
        'content': '还有四个小时下班，哈哈哈',
        'topic_id': '6824710203301167112',
        'sync_to_org': False
    }
    for wan in get_wan():
        params['content'] = wan
        reqs = requests.post(url=url, headers=herder, json=params)
        print(reqs.json()['err_msg'])
        if reqs.json()['err_msg'] != 'success':
            auto_juejin()
        print(params)
        # 3秒后再发
        time.sleep(3)


if __name__ == '__main__':
    auto_juejin()


