# coding=utf-8
import unittest
import requests
import json
from Global_base import global_base
from Global_base import phone_create
from parameterized import parameterized

'''
channelId	渠道ID(大王贷款/mdwdk001)	string	非空、必传
deviceType	设备类型(1/安卓，2/iOS)	number	非空、必传
phone	手机号	string	非空、必传
productId	产品ID(大王贷款/2001)	string	非空、必传
'''


class CheckUser(unittest.TestCase):
    '''查询路由用户注册状态及下载地址'''

    def setUp(self):
        self.url = global_base.DefTool.url(self, "/usercenter/sys/h5/checkUser")
        self.channelId = 'mdwdk001'
        self.code = 200
        self.msg = "ok"

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(self.params))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("验证安卓手机号输入正确手机号，有路由结果，返回路由链接", 1, "mdwdk001", 2001, int(phone_create.create_phone()), False),
        ("验证安卓手机号输入正确手机号，无路由结果，返回默认链接", 1, "mdwdk001", 2001, 18127813600, False),
        ("验证IOS手机号输入正确手机号，无路由结果，返回默认链接", 2, "mdwdk001", 2001, 18127813600, False),
        ("验证IOS手机号输入正确手机号，有路由结果，返回路由链接", 2, "mdwdk001", 2001, int(phone_create.create_phone()), False),
    ])
    def test_cehckUser(self, case, deviceType, channelId, productId, phone, isRegisted):
        self.params = {"deviceType": deviceType, "channelId": channelId, "productId": productId, "phone": phone}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["code"], self.code)


if __name__ == "__main__":
    unittest.main()
