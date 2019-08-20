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
        params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], "200")

    def tearDown(self):
        print(self.result)


if __name__ == "__main__":
    unittest.main()
