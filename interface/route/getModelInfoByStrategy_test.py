import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class GetModelInfoByStrategy(unittest.TestCase):

    def setUp(self):
        self.url = global_base.DefTool.url(self, "/usercenter/sys/h5/getModelInfoByStrategy")
        self.channelId = 'mdwdk001'
        self.code = 200
        self.msg = "ok"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("查询页面模板信息接口(下载页)", 1003, 100020101, 2, 1),
        ("查询页面模板信息接口(注册页)", 1003, 100020101, 1, 1)
    ])
    def test_getModelInfoByStrategy(self, case, productId, abconfigsid, type, deviceType):
        ''''''
        params = {"productId": productId, "abconfigsid": abconfigsid, "type": type, "deviceType": deviceType}
        try:
            self.result = requests.get(url=self.url, params=params).json()
            self.assertEqual(self.result['msg'], self.msg)
            self.assertEqual(self.result['code'], self.code)
        except Exception as e:
            print(e)


if __name__ == "__mani__":
    unittest.main()
