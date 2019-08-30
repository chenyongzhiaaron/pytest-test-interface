import requests
import unittest
from Global_base import global_base,globa_phone
from parameterized import parameterized
from Global_base import login


class QueryLoanProductByListIdV2(unittest.TestCase):
    "贷款大全"
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/queryLoanProductByListIdV2.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))

    @parameterized.expand([
        ("用户未登陆查询贷款大全成功", "1003", "16", 1, "sinaif", "867910035562539", 1, 8, ""),
        ("用户登陆查询贷款大全成功", "1003", "16", 1, "sinaif", "867910035562539", 1, 8, ""),
    ])
    @unittest.skip("pass")
    def test_queryLoanProductByListIdV2(self, case, productId, id, clientType, channelId, deviceId, dataType,
                                        hotProductSize, searchKey):
        userId_null = ""
        token_null = ""
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        userId = values[0]
        token = values[1]
        if case == "用户未登陆查询贷款大全成功":
            self.params = {"productId": productId, "id": id, "clientType": clientType, "channelId": channelId, "deviceId": deviceId,
              "dataType": dataType, "hotProductSize": hotProductSize, "searchKey": searchKey, "token":token_null, "userId": userId_null}
            self.result = requests.post(url=self.url, data=self.params).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], '200')

        elif case == "用户登陆查询贷款大全成功":
            self.params = {"productId": productId, "id": id, "clientType": clientType, "channelId": channelId,
                  "deviceId": deviceId,
                  "dataType": dataType, "hotProductSize": hotProductSize, "searchKey": searchKey, "token": userId,
                  "userId": token}
            self.result = requests.post(url=self.url, data=self.params).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
