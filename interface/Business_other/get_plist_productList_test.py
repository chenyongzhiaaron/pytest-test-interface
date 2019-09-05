import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class PlistProductList(unittest.TestCase):
    """查询有借卡贷列表接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/plist/productList")

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


    @parameterized.expand([
        ("参数正确，获取有借卡贷列表成功", "NPL94820190117201810100", "101", 2, 1003, 1, ""),
    ])
    def test_get_plist_product_list(self, name, cfgId, listType, cfgType, productId, clientType, userId):
        """{}""".format(name)
        self.params = {"cfgId": cfgId, "listType": listType, "cfgType": cfgType, "productId": productId,
                 "clientType": clientType, "userId": userId}
        r = requests.get(url=self.url, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        # self.result = r.text
        # self.assertIn()


if __name__ == "__main__":
    unittest.main()
