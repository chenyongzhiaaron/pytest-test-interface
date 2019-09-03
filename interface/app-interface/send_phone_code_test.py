import requests
import unittest
import json
from Global_base import global_base
from Global_base import phone_create
from parameterized import parameterized


class SendPhoneCode(unittest.TestCase):

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/sendPhoneCode')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("发送短信验证码成功", "2", "15", "867910035562539", "2.6.0", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_send_phone_code(self, case, type, verno, deviceId, ver, deviceType, productId, channelId, deviceToken,
                             mjbname):
        '''发送登陆验证码接口'''
        phone_new = phone_create.create_phone()
        pa = {"phone": str(phone_new), "type": type, "verno": verno, "deviceId": deviceId, "ver": ver,
              "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
