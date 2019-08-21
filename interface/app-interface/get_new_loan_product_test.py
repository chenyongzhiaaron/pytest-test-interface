import unittest
import requests
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class NewLoanProduct(unittest.TestCase):
    "最新口子接口"
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getNewLoanProduct.do')

    @parameterized.expand([
        ('获取最新口子列表成功', "1003", "1", "1", "20", "1", "867910035562539"),
    ])
    def test_get_new_loan_product(self, caase, productId, clientType, pageIndex, pageSize,dataType, deviceId):
        token = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))[1]
        params = {"deviceId": deviceId, "productId": productId, "token": token, "pageIndex": pageIndex, "pageSize": pageSize, "clientType": clientType}
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], '200')

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
