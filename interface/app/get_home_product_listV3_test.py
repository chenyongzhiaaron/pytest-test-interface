import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class IndexInterface(unittest.TestCase):
    """首页接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getHomeProductListV3.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ('未登录访问首页接口', "1", "1003", "", "15", "1", "sinaif", "867910035562539"),
    ])
    def test_index_interfacec(self, name, clientType, productId, token, recommendSize, dataType, channelId, deviceId):
        """首页接口"""
        pa = {"clientType": clientType, "productId": productId, "token": token, "recommendSize": recommendSize,
              "dataType": dataType, "channelId": channelId, "deviceId": deviceId}
        self.params = global_base.DefTool().payload(**pa)
        # self.result = global_base.RunMain("get", self.url, params).re
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], "200")


if __name__ == "__main__":
    unittest.main()
