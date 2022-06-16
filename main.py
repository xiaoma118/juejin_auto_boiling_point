import random
import time

import requests
from requests_html import HTMLSession
import re


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
    son_url = label_urls[random.randint(0, len(label_urls))]
    # 请求标签链接

    son_rep = session.get(url=son_url, timeout=3)
    time.sleep(1)
    # 解析标签链接 获取多个文案文章url
    article_urls = son_rep.html.xpath('/html/body/div[5]/div[2]/li/a/@href')
    # 随机一个文章
    wz_url = article_urls[random.randint(0, len(article_urls))]
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
    if len(' '.join(content)) < 16:  # 小于15字的不要
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
        'cookie': 'cookie: _ga=GA1.2.1811657961.1642139615; MONITOR_WEB_ID=4e97a8a5-642f-4940-8938-678c61b529cd; __tea_cookie_tokens_2608=%257B%2522user_unique_id%2522%253A%25227052935898246088232%2522%252C%2522web_id%2522%253A%25227052935898246088232%2522%252C%2522timestamp%2522%253A1642555869527%257D; passport_csrf_token=ed96303b1b77b4d80a754ae29983b677; passport_csrf_token_default=ed96303b1b77b4d80a754ae29983b677; n_mh=CIUBtfW4A8DOGakAhyYLrNIn199dcNF_dDOoGJQq1B8; sid_guard=6d2ac110446bbd783d13744383bafc65%7C1652665064%7C31536000%7CTue%2C+16-May-2023+01%3A37%3A44+GMT; uid_tt=eb8528e3b7c47ccfe1c780636dc88052; uid_tt_ss=eb8528e3b7c47ccfe1c780636dc88052; sid_tt=6d2ac110446bbd783d13744383bafc65; sessionid=6d2ac110446bbd783d13744383bafc65; sessionid_ss=6d2ac110446bbd783d13744383bafc65; sid_ucp_v1=1.0.0-KDY3NjU5ZTZiN2NkYWNiZWNiZDFmNjZhNWE5NDgyZWZjZjBiOTNhMDAKFwjX6vDA_fXlBhDo1YaUBhiwFDgCQPEHGgJsZiIgNmQyYWMxMTA0NDZiYmQ3ODNkMTM3NDQzODNiYWZjNjU; ssid_ucp_v1=1.0.0-KDY3NjU5ZTZiN2NkYWNiZWNiZDFmNjZhNWE5NDgyZWZjZjBiOTNhMDAKFwjX6vDA_fXlBhDo1YaUBhiwFDgCQPEHGgJsZiIgNmQyYWMxMTA0NDZiYmQ3ODNkMTM3NDQzODNiYWZjNjU; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _gid=GA1.2.1364460869.1655083088'
    }
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
        # if reqs.json()['err_msg'] != 'success':
        #     auto_juejin()
        print(params)
        # 3秒后再发
        time.sleep(3)


if __name__ == '__main__':
    auto_juejin()

