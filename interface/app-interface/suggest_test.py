import requests
import unittest
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class GetMainLinkBySublink(unittest.TestCase):
    "建议提交"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/suggest')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        (
        "建议提交", "A11", "", "867910035562539", "2.6.0", "15", "1003",
        "1", "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_getMainLinkBySublink(self, case, suggestcontent, contactway, deviceId, ver, verno,
                                  productId, deviceType, channelId, deviceToken, mjbname):
        values = login.LoginByPassWord().login_by_password(18127813601)
        token = values[1]
        header = {"token": token}
        pa = {"suggestcontent": suggestcontent, "contactway": contactway, "deviceId": deviceId, "ver": ver,
              "verno": verno, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
              "mjbname": mjbname, "deviceType": deviceType}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
