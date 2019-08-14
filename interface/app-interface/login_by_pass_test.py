import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class LoginByPassWord(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/loginByPass')

    @parameterized.expand([
        ('初始成功', "8ff15b24341602becdf011679ec383c1", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3",
         "qsj",),
    ])
    def test_login_by_password(self, caase, password, ver, verno, deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        username = 18888888888
        pa = {"ver": ver, "password": password,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname, "username": username}
        values = global_base.DefTool.sign(self, **pa)
        sign = {"sign": values}
        params = dict(pa, **sign)
        try:
            self.result = requests.post(url=self.url, data=params).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result["code"], 200)
            self.assertEqual(self.result['data']['username'], str(username))
            self.assertEqual(self.result['data']['mobile'], str(username))
        except Exception as e:
            print(e)
        accountid = self.result['data']['accountid']
        token = self.result['token']
        return accountid, token

    def tearDown(self):
        print(self.result)
        # print(self.url)


if __name__ == '__main__':
    unittest.main()
