import requests
import unittest
from Global_base import global_base,login
from parameterized import parameterized


class GetSmartMatchList(unittest.TestCase):
    '''智能推荐接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getSmartMatchList.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("智能推荐", "16", "1003", 1)
    ])
    def test_getSmartMatchList(self, case, id, productId, clientType):
        values = login.LoginByPassWord().login_by_password(18127813601)
        accountid = values[0]
        params = {"id": id, "clientType": clientType,
                  "productId": productId, "accountid": accountid}
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
