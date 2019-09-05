import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class GetModelInfoByStrategy(unittest.TestCase):
    """查询路由模板信息接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/usercenter/sys/h5/getModelInfoByStrategy")
        self.channelId = 'mdwdk001'
        self.code = 200
        self.msg = "ok"

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("查询页面模板信息接口(下载页)", 1003, 100020101, 2, 1),
        ("查询页面模板信息接口(注册页)", 1003, 100020101, 1, 1)
    ])
    # @unittest.skip("pass")
    def test_getModelInfoByStrategy(self, name, productId, abconfigsid, type, deviceType):
        """{}""".format(name)
        self.params = {"productId": productId, "abconfigsid": abconfigsid, "type": type, "deviceType": deviceType}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result['msg'], self.msg)
        self.assertEqual(self.result['code'], self.code)


if __name__ == "__mani__":
    unittest.main()
