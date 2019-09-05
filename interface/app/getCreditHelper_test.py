import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class RecordAdd(unittest.TestCase):
    """助贷工具接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/credit/getCreditHelper.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("获取助贷工具接口成功", "1003", "1")
    ])
    def test_record_add(self, name, productId, clientType):
        """{}""".format(name)
        self.params = {"productId": productId, "clientType": clientType}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
