import requests
import json
import random
import re
import time
from fake_useragent import UserAgent

'''
Author：pk哥
Date：2021/1/24
公众号：Python知识圈
代码详细解析可在公众号「Python知识圈」找到对应文章
你也可以在B站找到视频讲解，B站账号：「菜鸟程序员的日常」

如有疑问或需要获取插画图，请联系微信号RookieProM：，备注来意，谢谢。
'''


class DownloadPixiv():
    def get_proxy(self):
        result = []
        # 读取代理池ip并随机返回一个
        with open('ip_pool_foreign.txt', 'r') as f:
            for line in f:
                result.append(line.strip('\n'))
        ips = list(filter(None, result))
        proxies = {'http': random.choice(ips)}
        return proxies

    # 获取插画列表插画的id，headers信息我做了处理，你记得替换成自己的再运行代码
    def get_ids(self, p):
        headers = {
            'authority': 'www.pixiv.net',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': UserAgent(verify_ssl=False).random,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'xxxxx',     # 此处需替换成真实的，换成你自己的cookie
        }

        params = (
            ('mode', 'rookie'),
            ('content', 'illust'),
            ('p', p),
            ('format', 'json'),
        )

        proxies = self.get_proxy()
        try:
            response = requests.get('https://www.pixiv.net/ranking.php', headers=headers, params=params, proxies=proxies).text
            info = json.loads(response)
            illust_ids = []
            for i in range(50):
                try:
                    illust_id = info['contents'][i]['illust_id']
                    illust_ids.append(illust_id)
                except IndexError:
                    print('爬取已完成')
            return illust_ids
        except:
            proxies = self.get_proxy()
            response = requests.get('https://www.pixiv.net/ranking.php', headers=headers, params=params,
                                    proxies=proxies).text
            info = json.loads(response)
            illust_ids = []
            for i in range(50):
                try:
                    illust_id = info['contents'][i]['illust_id']
                    illust_ids.append(illust_id)
                except IndexError:
                    print('爬取已完成')
            return illust_ids

    # 下载图片，file_path目录记得替换成你电脑的目录
    def download_pic(self, illust_id):
        file_path = '/Users/brucepk/pixiv-rookie/{}.png'.format(illust_id)
        with open(file_path, 'wb+') as f:
            pic_url = 'https://embed.pixiv.net/decorate.php?illust_id={}&mode=sns-automator'.format(illust_id)
            try:
                f.write(requests.get(pic_url).content)
                print('成功下载图片：{}.png'.format(illust_id))
            except Exception:
                print('成功下载图片：{}.png'.format(illust_id))


download = DownloadPixiv()
for p in range(1, 11):
    try:
        illust_ids = download.get_ids(p)
        time.sleep(random.randint(10, 20))  # 随机等待时间
        for illust_id in illust_ids:
            download.download_pic(illust_id)
    except IndexError:
        print('所有图片已爬取完成')

