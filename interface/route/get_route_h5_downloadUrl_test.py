# coding=utf-8
import unittest
import requests
import random
import json
from Global_base import global_base,globa_phone
from parameterized import parameterized
from Global_base import phone_create


class RouteH5DownLoadUrl(unittest.TestCase):
    """大王贷款接轻松借路由需求，查询轻松借路由下载地址"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/route/h5/getDownloadUrl')
        self.msg = "ok"
        self.code = 200
        self.downloadUrlNone = None
        self.phone = phone_create.create_phone()
        self.deviceType = random.randint(1, 2)

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    def test_get_route_h5_downloadUrl_None(self):
        """手机号正确，没有路由结果返回null"""
        phone = int(globa_phone.phone())
        self.params = {"phone": phone, "productId": 2001, "deviceType": self.deviceType,
                 "channelId": "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc"}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], self.msg)
        self.assertEqual(self.result["code"], self.code)

    def test_get_route_h5_downloadUrl_android_success(self):
        """验证安卓手机号输入正确手机号，有路由结果，返回路由链接"""
        self.params = {"phone": self.phone, "productId": 2001, "deviceType": 1,
                 "channelId": "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc"}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], self.msg)
        self.assertEqual(self.result["code"], self.code)

    def test_get_route_h5_downloadUrl_ios_success(self):
        """验证IOS手机号输入正确手机号，有路由结果，返回路由链接"""
        self.params = {"phone": self.phone, "productId": 2001, "deviceType": 2,
                 "channelId": "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc"}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], self.msg)
        self.assertEqual(self.result["code"], self.code)

    @parameterized.expand([
        ("手机号 phone 为空，提示参数错误", "", 2001, 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请输入手机号码", 100002),
        ("手机号为字符串，提示输入正确手机号", "abc~@#*(中国", 2001, 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请输入正确的手机号码",
         1100006),
        ("手机号多一位，提示输入正确手机号", 181278136001, 2001, 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请输入正确的手机号码",
         1100006),
        ("手机号少一位，提示输入正确手机号", "1812781360", 2001, 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请输入正确的手机号码",
         1100006),
        ("productId错误，提示参数错误", "18127813600", "abc#@中", 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("productId 多一位，提示参数错误", "18127813600", "20010", 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("productId 少一位，提示参数错误", "18127813600", "200", 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("productId 少一位，提示参数错误", "18127813600", "200", 1, "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("deviceType为空，提示参数错误", "18127813600", "200", "", "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("deviceType错误，提示参数错误", "18127813600", "200", "fbz", "qIHgiZmfgM3OxdMnur56Tehk5fW6-LusUYDiFAX7nkc", "请求参数错误",
         100002),
        ("所有参数为空，提示请输入手机号", "", "", "", "", "请输入手机号码",
         100002),
    ])
    def test_get_route_h5_downloadUrl_error(self, name, phone, productId, deviceType, channelId, msg, code):
        """{}""".format(name)
        self.params = {"phone": phone, "productId": productId, "deviceType": deviceType,
                 "channelId": channelId}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], msg)
        self.assertEqual(self.result["code"], code)


if __name__ == "__main__":
    unittest.main()
