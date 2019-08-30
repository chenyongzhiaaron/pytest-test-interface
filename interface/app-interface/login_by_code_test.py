import time
import unittest
import requests
from Global_base import global_base, send_code, globa_phone
from parameterized import parameterized


class LoginByCode(unittest.TestCase):
    '''通过验证码登陆接口'''

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/loginByCode')

    @parameterized.expand([
        ("输入正确手机号及验证码，登陆成功", 1003, "MJBIOS015", 1566281892, "52f505fc8d9d5412e1e253e4a82e7dd2",
         "1ED714DC-8B19-4AD9-9EC7-8507AD23C454", "Q001", 2, "yjwy", "2.5.2", 12),
    ])
    def test_login_by_code(self, name, productId, channelId, timestamp, deviceToken, deviceId, source, deviceType,
                           mjbname, ver, verno):
        phone = globa_phone.phone()
        code = send_code.SendPhoneCode().send_phone_code(phone)
        payload = {'username': phone, "code": code, "productId": productId, "channelId": channelId,
                   "timestamp": timestamp,
                   "deviceToken": deviceToken, "deviceId": deviceId,
                   "source": source, "deviceType": deviceType, "mjbname": mjbname, "ver": ver, "verno": verno}
        self.params = global_base.DefTool().payload(**payload)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result['code'], 200)
        self.assertEqual(self.result['msg'], 'ok')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))


if __name__ == "__main__":
    unittest.main()
