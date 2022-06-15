def juejin_auto():
    herder = {
        'referer': 'https://juejin.cn/',
        'origin': 'https://juejin.cn',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'cookie': 'cookie: _ga=GA1.2.1811657961.1642139615; MONITOR_WEB_ID=4e97a8a5-642f-4940-8938-678c61b529cd; __tea_cookie_tokens_2608=%257B%2522user_unique_id%2522%253A%25227052935898246088232%2522%252C%2522web_id%2522%253A%25227052935898246088232%2522%252C%2522timestamp%2522%253A1642555869527%257D; passport_csrf_token=ed96303b1b77b4d80a754ae29983b677; passport_csrf_token_default=ed96303b1b77b4d80a754ae29983b677; n_mh=CIUBtfW4A8DOGakAhyYLrNIn199dcNF_dDOoGJQq1B8; sid_guard=6d2ac110446bbd783d13744383bafc65%7C1652665064%7C31536000%7CTue%2C+16-May-2023+01%3A37%3A44+GMT; uid_tt=eb8528e3b7c47ccfe1c780636dc88052; uid_tt_ss=eb8528e3b7c47ccfe1c780636dc88052; sid_tt=6d2ac110446bbd783d13744383bafc65; sessionid=6d2ac110446bbd783d13744383bafc65; sessionid_ss=6d2ac110446bbd783d13744383bafc65; sid_ucp_v1=1.0.0-KDY3NjU5ZTZiN2NkYWNiZWNiZDFmNjZhNWE5NDgyZWZjZjBiOTNhMDAKFwjX6vDA_fXlBhDo1YaUBhiwFDgCQPEHGgJsZiIgNmQyYWMxMTA0NDZiYmQ3ODNkMTM3NDQzODNiYWZjNjU; ssid_ucp_v1=1.0.0-KDY3NjU5ZTZiN2NkYWNiZWNiZDFmNjZhNWE5NDgyZWZjZjBiOTNhMDAKFwjX6vDA_fXlBhDo1YaUBhiwFDgCQPEHGgJsZiIgNmQyYWMxMTA0NDZiYmQ3ODNkMTM3NDQzODNiYWZjNjU; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _gid=GA1.2.1364460869.1655083088'
    }
    url = 'https://api.juejin.cn/content_api/v1/short_msg/publish?aid=2608&uuid=7052935898246088232'
    params = {
        'content': 'xdm,摸鱼的一天结束啦',
        'topic_id': '6824710203301167112',
        'sync_to_org': False
    }
    reqs = requests.post(url=url, headers=herder, json=params)
    print(reqs.json())
if __name__ == '__main__':
    juejin_auto()
