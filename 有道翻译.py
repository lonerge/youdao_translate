# r = "" + (new Date).getTime()
# i = r + parseInt(10 * Math.random(), 10);
#
# salt: i,
# sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")

# salt: 16429880942724        # 时间戳加一个随机整数
# sign: ad5e13199086cc615511a4499d313e51      # 输入值加salt加两个字符串
# lts: 1642988094272      # 时间戳





import requests

from requests.cookies import cookiejar_from_dict
import hashlib
import time
import random
import re
import json


class Youdao(object):
    def __init__(self):
    # url
        self.session = requests.session()
        self.url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # headers
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Referer': 'https://fanyi.youdao.com/'
        }
    # cookies
        cookies = {
        'OUTFOX_SEARCH_USER_ID': '1730686703@10.110.96.158',
        'JSESSIONID': 'aaarIOt7g8Pg6__B0Wj6x',
        'OUTFOX_SEARCH_USER_ID_NCOO': '511912186.32251394',
        '___rl__test__cookies': '1642995000839'
    }
        self.session.cookies = cookiejar_from_dict(cookies)

    def dataform(self, target):
        lts = str(int(time.time()*1000))      # 获取13位时间戳
        salt = str(int(time.time()*1000)) + str(random.randint(0, 10))
        old_sign = "fanyideskweb" + target + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        # 用hashlib.md5()    将sign进行哈希加密
        md5 = hashlib.md5()
        md5.update(old_sign.encode())
        sign = md5.hexdigest()
        data = {
            'i': target,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': '30202777336adaadd34a49a7c732df71',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
        }
        return data

    # dataform
    # 发送请求,获取响应
    # 解析响应,获取目标数据
    def get(self, dataform):
        res = self.session.post(self.url, data=dataform)
        return res.content.decode()

    def parse(self, data):
        try:
            old_result = re.search(r'"tgt":"(.*?)"', data)
            result = old_result.group(1)
        except:
            result = None
        return result
        # result_dict = json.loads(data)
        # result = result_dict["translateResult"][0][0]["tgt"]
        # return result

    def run(self):
        target = input("输入要翻译的内容:")
        dataform = self.dataform(target)
        res = self.get(dataform)
        print(self.parse(res))


if __name__ == '__main__':
    youdao = Youdao()
    youdao.run()




