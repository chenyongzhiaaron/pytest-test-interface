import requests
import unittest
from Global_base import global_base
from Global_base import phone_create
from parameterized import parameterized


class SendPhoneCode(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/sendPhoneCode')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("发送短信验证码成功", "2", "15", "867910035562539", "2.6.0", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_send_phone_code(self, case, type, verno, deviceId, ver, deviceType, productId, channelId, deviceToken,
                             mjbname):
        phone_new = phone_create.create_phone()
        pa = {"phone": str(phone_new), "type": type, "verno": verno, "deviceId": deviceId, "ver": ver,
              "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        value = global_base.DefTool.sign(self, **pa)
        sign = {"sign": value}
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
