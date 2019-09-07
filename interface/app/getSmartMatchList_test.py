import requests
import unittest
import json
from Global_base import global_base, login, globa_phone
from parameterized import parameterized


class GetSmartMatchList(unittest.TestCase):
    """智能推荐接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getSmartMatchList.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("智能推荐", "16", "1003", 1)
    ])
    # @unittest.skip("pass")
    def test_getSmartMatchList(self, name, id, productId, clientType):
        """智能推荐接口"""
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        accountid = values[0]
        self.params = {"id": id, "clientType": clientType, "productId": productId, "accountid": accountid}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
