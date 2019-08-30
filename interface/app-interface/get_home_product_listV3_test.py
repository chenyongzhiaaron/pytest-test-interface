import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class IndexInterface(unittest.TestCase):
    '''首页接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getHomeProductListV3.do')

    @parameterized.expand([
        ('未登录访问首页接口', "1", "1003", "", "15", "1", "sinaif", "867910035562539"),
    ])
    def test_index_interfacec(self, case, clientType, productId, token, recommendSize, dataType, channelId, deviceId):
        pa = {"clientType": clientType, "productId": productId, "token": token, "recommendSize": recommendSize,
              "dataType": dataType, "channelId": channelId, "deviceId": deviceId}
        self.params = global_base.DefTool().payload(**pa)
        # self.result = global_base.RunMain("get", self.url, params).re
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], "200")

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))


if __name__ == "__main__":
    unittest.main()
