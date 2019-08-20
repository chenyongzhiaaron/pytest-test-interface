import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class GetBusinessProductList(unittest.TestCase):
    '''查询大王贷款列表接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/dwdk/getBusinessProductList.do")

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("参数正确，查询大王贷款列表成功", "", 2001, 1, "NPL81820181011105344100"),
    ])
    def test_get_business_product_list_success(self, name, userId, productId, clientType, cfgId):
        parms = {"cfgId": cfgId, "userId": userId, "productId": productId, "clientType": clientType}
        self.result = requests.get(url=self.url, params=parms).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], "ok")



if __name__ == "__main__":
    unittest.main()
