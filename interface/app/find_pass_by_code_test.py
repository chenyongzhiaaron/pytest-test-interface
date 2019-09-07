import requests
import unittest
import json
from Global_base import global_base, globa_phone
from parameterized import parameterized


class FindPassByCode(unittest.TestCase):
    """找回密码接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/findPassByCode')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("输入错误验证码提示验证码错误", "8ff15b24341602becdf011679ec383c1", "2.6.0", "15", "867910035562539", "1", "1003",
         "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_find_pass_by_code(self, name, password, ver, verno, deviceId, deviceType, productId, channelId,
                               deviceToken, mjbname):
        """找回密码接口"""
        phone_new = int(globa_phone.phone())
        code = "1234512dd"
        pa = {"username": str(phone_new), "password": password, "code": code, "verno": verno, "deviceId": deviceId,
              "ver": ver, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "验证码错误，请重试")
        self.assertEqual(self.result['code'], 1100007)


if __name__ == '__main__':
    unittest.main()
