import requests
import unittest
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class GetMainLinkBySublink(unittest.TestCase):
    "修改密码提交"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/mofidyPassByCode')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        (
        "修改密码提交",  "555555", "867910035562539", "2.6.0", "15", "1003",
        "1", "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_getMainLinkBySublink(self, case, code, deviceId, ver, verno,
                                  productId, deviceType, channelId, deviceToken, mjbname):
        username = 18127813601
        password = "de8b02de3a4f16ffa1e56ffd30b0349d"
        pa = {"username": username, "password": password, "code": code, "deviceId": deviceId, "ver": ver,
              "verno": verno, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
              "mjbname": mjbname, "deviceType": deviceType}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], '200')
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
