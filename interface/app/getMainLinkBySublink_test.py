import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class GetMainLinkBySublink(unittest.TestCase):
    """获取子链接"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/sublink/getMainLinkBySublink.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("获取子链接成功", "", "1", "", "12345678910QSJ", "", "", "", "", "FRrYbq0", 200, "ok", "https://promotion.billiontech.com/bl-promotion-webapp/register?channelNo=822xla822"),
        ("s参数为空，未找到主链", "", "1", "", "12345678910QSJ", "", "", "", "", "", 300, "子链id和子链短码为空", None)
    ])
    def test_getMainLinkBySublink(self, name, subLink, mobileSystem, appVersion, deviceId, referUrl, linkName,
                                      random,out, s, code, msg, data):
        """获取子链接"""
        pa = {"subLink": subLink, "mobileSystem": mobileSystem, "appVersion": appVersion, "referUrl": referUrl, "linkName": linkName,
              "deviceId": deviceId, "random": random, "out": out, "s": s}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        if name == "获取子链接成功":
            self.assertEqual(self.result["msg"], msg)
            self.assertEqual(self.result['code'], code)
            self.assertEqual(self.result["data"]["mainlink"], data)
        else:
            self.assertEqual(self.result["msg"], msg)
            self.assertEqual(self.result['code'], code)
            self.assertEqual(self.result["data"], data)


if __name__ == '__main__':
    unittest.main()
