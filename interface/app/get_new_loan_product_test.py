import unittest
import requests
import json
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class NewLoanProduct(unittest.TestCase):
    """最新口子接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getNewLoanProduct.do')

    @parameterized.expand([
        ('获取最新口子列表成功', "1003", "1", "1", "20", "1", "867910035562539"),
    ])
    # @unittest.skip("pass")
    def test_get_new_loan_product(self, name, productId, clientType, pageIndex, pageSize,dataType, deviceId):
        """{}""".format(name)
        token = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))[1]
        self.params = {"deviceId": deviceId, "productId": productId, "token": token, "pageIndex": pageIndex, "pageSize": pageSize, "clientType": clientType}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], '200')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == '__main__':
    unittest.main()
