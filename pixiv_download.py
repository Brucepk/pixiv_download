import requests
import json
import random
import re
import time


class DownloadPixiv():
    # 设置 UA 列表
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

    # 获取插画列表插画的id，headers信息我做了处理，你记得替换成自己的再运行代码
    def get_ids(self, p):
        UA = random.choice(self.user_agent_list)
        headers = {
            'authority': 'www.pixiv.net',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': UA,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'xxxxxxxxxxx',  # 此处需替换成真实的
        }

        params = (
            ('mode', 'daily'),
            ('content', 'illust'),
            ('p', p),
            ('format', 'json'),
        )

        response = requests.get(
            'https://www.pixiv.net/ranking.php',
            headers=headers,
            params=params).text
        info = json.loads(response)
        illust_ids = []
        for i in range(50):
            illust_id = info['contents'][i]['illust_id']
            illust_ids.append(illust_id)
        return illust_ids

    # 下载图片，file_path目录记得替换成你电脑的目录
    def download_pic(self, illust_id):
        file_path = '/Users/brucepk/pixiv/{}.png'.format(illust_id)
        with open(file_path, 'wb+') as f:
            pic_url = 'https://embed.pixiv.net/decorate.php?illust_id={}&mode=sns-automator'.format(
                illust_id)
            try:
                f.write(requests.get(pic_url).content)
                print('成功下载图片：{}.png'.format(illust_id))
            except Exception:
                print('成功下载图片：{}.png'.format(illust_id))


if __name__ == '__main__':
    download = DownloadPixiv()
    for p in range(1, 11):
        illust_ids = download.get_ids(p)
        time.sleep(int(format(random.randint(10, 20))))  # 随机等待时间
        for illust_id in illust_ids:
            download.download_pic(illust_id)
