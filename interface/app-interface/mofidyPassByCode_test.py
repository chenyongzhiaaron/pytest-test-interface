import requests
import unittest
import time
from Global_base import global_base, send_code
from db_fixture import test_db
from parameterized import parameterized
from Global_base import login


class MofidyPassByCode(unittest.TestCase):
    "修改密码提交"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/mofidyPassByCode')

    def tearDown(self):
        try:
            print(self.result)
        except Exception as e:
            print(e)

    @parameterized.expand([
        ("参数正确修改密码成功", "867910035562539", "2.6.0", "15", "1003", "1", "sinaif", "ef70fb3178dccde19df9295a68aca0a3",
         "qsj",
         "123456"),
    ])
    def test_mofidyPassByCode(self, name, deviceId, ver, verno,
                              productId, deviceType, channelId, deviceToken, mjbname, newpassword):
        phone = 18607997979
        value = send_code.SendPhoneCode().send_phone_code_token(phone)
        token = value[0]
        print("2-------------" + token)
        code = value[1]
        print("3-------------" + code)
        pa = {"username": phone, "code": code, "deviceId": deviceId, "ver": ver,
              "verno": verno, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
              "mjbname": mjbname, "deviceType": deviceType, "newpassword": newpassword}
        params = global_base.DefTool().payload(**pa)
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
