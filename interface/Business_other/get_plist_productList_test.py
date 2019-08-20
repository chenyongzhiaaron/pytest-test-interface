import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class PlistProductList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/plist/productList")

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("参数正确，获取有借卡贷列表成功", "NPL94820190117201810100", "101", 2, 1003, 1, ""),
    ])
    def test_get_plist_product_list(self, name, cfgId, listType, cfgType, productId, clientType, userId):
        parma = {"cfgId": cfgId, "listType": listType, "cfgType": cfgType, "productId": productId,
                 "clientType": clientType, "userId": userId}
        r = requests.get(url=self.url, params=parma)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        # self.result = r.text
        # self.assertIn()


if __name__ == "__main__":
    unittest.main()
