import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class GetHomeProdcutList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/loan/getHomeProductList.do")

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("参数正确获取有借卡贷Tab1首页成功", 1001, 1, "NPL56820190110110515100"),
    ])
    def test_get_home_product_list(self, name, productId, clientType, id):
        pamras = {"name": name, "productId": productId, "clientType": clientType, "id": id, }
        r = requests.get(url=self.url, params=pamras)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], '200')
            self.assertEqual(self.result['msg'], "ok")
            self.result = r.text
            self.assertIn("新浪有借", self.result)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
