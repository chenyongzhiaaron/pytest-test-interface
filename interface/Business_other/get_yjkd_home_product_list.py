import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class GetHomeProdcutList(unittest.TestCase):
    """查询有借卡贷TAB1首页接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/loan/getHomeProductList.do")

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("参数正确获取有借卡贷Tab1首页成功", 1001, 1, "NPL56820190110110515100"),
    ])
    def test_get_home_product_list(self, name, productId, clientType, id):
        """{}""".format(name)
        self.params = {"name": name, "productId": productId, "clientType": clientType, "id": id, }
        r = requests.get(url=self.url, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], "ok")
        self.result = r.text
        # self.assertIn("新浪有借", self.result)


if __name__ == "__main__":
    unittest.main()
