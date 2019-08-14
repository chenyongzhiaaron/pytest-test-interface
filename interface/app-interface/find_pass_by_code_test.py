import requests
import unittest
from Global_base import global_base
from Global_base import phone_create
from parameterized import parameterized


class SendPhoneCode(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/findPassByCode')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("找回密码成功", "8ff15b24341602becdf011679ec383c1", "2.6.0", "15", "867910035562539", "1", "1003",
         "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_send_phone_code(self, case, password, ver, verno, deviceId, deviceType, productId, channelId,
                             deviceToken, mjbname):
        phone_new = "18888888888"
        code = "1234512dd"
        pa = {"username": str(phone_new), "password": password, "code": code, "verno": verno, "deviceId": deviceId, "ver": ver, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        value = global_base.DefTool.sign(self, **pa)
        sign = {"sign": value}
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except AssertionError as  e:
            print(e)


if __name__ == '__main__':
    unittest.main()
