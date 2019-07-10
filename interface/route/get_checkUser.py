# coding=utf-8
import unittest
import requests
import random
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
    def setUp(self):
        self.url = global_base.DefTool.url(self, "usercenter/sys/h5/checkUser")
        self.channelId = 'mdwdk001'
        self.code = 200
        self.msg = "ok"
        # self.defaultDownloadUrl = "https://k8s-qsj-test-jie.iask.cn/pg/qsjRegVTS/iosNav/pages/download/indexAndV2.html?productId=1003"
    def tearDown(self):
        print(self.result)
        # print(int(phone_create.create_phone()))

    @parameterized.expand([
        ("验证安卓手机号输入正确手机号，有路由结果，返回路由链接", 1, "mdwdk001", 2001, int(phone_create.create_phone()), False),
        ("验证安卓手机号输入正确手机号，无路由结果，返回默认链接", 1, "mdwdk001", 2001, 18127813600, True),
        ("验证IOS手机号输入正确手机号，无路由结果，返回默认链接", 2, "mdwdk001", 2001, 18127813600, True),
        ("验证IOS手机号输入正确手机号，有路由结果，返回路由链接", 2, "mdwdk001", 2001, int(phone_create.create_phone()), False),
    ])
    def test_cehckUser(self, case, deviceType, channelId, productId, phone, isRegisted):
        params = {"deviceType": deviceType, "channelId": channelId, "productId": productId, "phone": phone}
        self.result = requests.get(url=self.url, params=params).json()
        self.assertEqual(self.result["code"], self.code)
        self.assertEqual(self.result["data"]["isRegisted"], isRegisted)
        print(phone)

if __name__ == "__main__":
    unittest.main()
