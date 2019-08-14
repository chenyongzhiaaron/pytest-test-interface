import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class Login():
    @parameterized.expand([
        ('初始成功', "8ff15b24341602becdf011679ec383c1", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3",
         "qsj",),
    ])
    def test_init(self, username):
        username = username
        pa = {"ver": 2.6.0, "password": 8ff15b24341602becdf011679ec383c1,
              "verno": 15, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname, "username": username}
        values = global_base.DefTool.sign(self, **pa)
        sign = {"sign": values}
        params = dict(pa, **sign)
        try:
            self.result = requests.post(url=self.url, data=params).json()
        except Exception as e:
            print(e)
        accountid = self.result['data']['accountid']
        token = self.result['token']
        return accountid, token
