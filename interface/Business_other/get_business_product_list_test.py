import pytest
import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class GetBusinessProductList(unittest.TestCase):
    """查询大王贷款列表接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/dwdk/getBusinessProductList.do")

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("参数正确，查询大王贷款列表成功", "", 2001, 1, "NPL81820181011105344100"),
    ])
    def test_get_business_product_list_success(self, name, userId, productId, clientType, cfgId):
        """{}""".format(name)
        self.params = {"cfgId": cfgId, "userId": userId, "productId": productId, "clientType": clientType}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], "ok")


if __name__ == "__main__":
    unittest.main()
