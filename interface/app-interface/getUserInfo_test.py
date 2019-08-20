import unittest
import requests
from Global_base import global_base, login
from parameterized import parameterized


class GetUserInfo(unittest.TestCase):
    "获取用户信息接口"
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/getUserInfo')

    @parameterized.expand([
        ('获取用户信息成功', "2.6.0", "15", "867910035562539", "1", "1003", "sinaif", "ef70fb3178dccde19df9295a68aca0a3",
         "qsj"),
    ])
    def test_getUserInfo(self, case, ver, verno, deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        params = {"ver": ver, "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
                  "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        token = login.LoginByPassWord().login_by_password(18127813601)[1]
        header = {"token": token}
        params_new = global_base.DefTool().payload(**params)
        self.result = requests.post(url=self.url, headers=header, data=params_new).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
