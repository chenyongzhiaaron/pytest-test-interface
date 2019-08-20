import time
import unittest
import requests
from Global_base import global_base, send_code
from db_fixture import test_db
from parameterized import parameterized


class LoginByCode(unittest.TestCase):
    '''通过验证码登陆接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/loginByCode')

    @parameterized.expand([
        ("输入正确手机号及验证码，登陆成功", 1003, "MJBIOS015", 1566281892, "52f505fc8d9d5412e1e253e4a82e7dd2","1ED714DC-8B19-4AD9-9EC7-8507AD23C454", "Q001", 2, "yjwy", "2.5.2", 12),
        # ("验证码过期，登陆失败", 1003, "MJBIOS015", 1566281892, "52f505fc8d9d5412e1e253e4a82e7dd2","1ED714DC-8B19-4AD9-9EC7-8507AD23C454", "Q001", 2, "yjwy", "2.5.2", 12),
    ])
    def test_login_by_code_success(self, name, productId, channelId, timestamp, deviceToken, deviceId, source, deviceType, mjbname, ver, verno):
        phone = "18127813603"
        if name == '输入正确手机号及验证码，登陆成功':
            code = send_code.SendPhoneCode().send_phone_code(phone)
            payload = {'username': phone, "code": code, "productId": productId, "channelId": channelId, "timestamp": timestamp,
              "deviceToken": deviceToken, "deviceId": deviceId,
              "source": source, "deviceType": deviceType, "mjbname": mjbname, "ver": ver, "verno": verno}
            params = global_base.DefTool().payload(**payload)
            self.result = requests.post(url=self.url, data=params).json()
            self.assertEqual(self.result['code'], 200)
            self.assertEqual(self.result['msg'], 'ok')

    def tearDown(self):
        print(self.result)


if __name__ == "__main__":
    unittest.main()
