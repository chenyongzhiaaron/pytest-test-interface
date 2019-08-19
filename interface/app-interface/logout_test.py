import requests
import unittest
from Global_base import global_base,login
from parameterized import parameterized


class Logout(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/logout')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("退出登录", "868777047018746", "2.6.0", "15", "1003", "1","sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_logout(self, case, deviceId, ver, verno, productId, deviceType, channelId, deviceToken,
                             mjbname):
        pa = {"type": type, "verno": verno, "deviceId": deviceId, "ver": ver,
              "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        token = login.LoginByPassWord().login_by_password(18127813601)[1]
        header = {"token":token}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
