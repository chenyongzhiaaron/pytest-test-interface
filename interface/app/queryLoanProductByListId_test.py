import requests
import unittest
import json
from Global_base import global_base, login, globa_phone
from parameterized import parameterized


class QueryLoanProductByListId(unittest.TestCase):
    """轻松借模块列表接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/queryLoanProductByListId.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("查询模块列表", "NPL6320190619171559100", "", "1003", "1", "true", "2.6.0", 1, 1, "867910035562539"),
    ])
    # @unittest.skip("pass")
    def test_queryLoanProductByListId(self, name, id, tags, productId, clientType, queryRecProduct, versionName,
                                      queryType, dataType, deviceId):
        """轻松借模块列表接口"""
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        userId = values[0]
        token = values[1]
        pa = {"id": id, "tags": tags, "deviceId": deviceId,
              "productId": productId, "userId": userId, "token": token, "clientType": clientType,
              "queryRecProduct": queryRecProduct, "versionName": versionName, "queryType": queryType,
              "dataType": dataType}
        self.params = global_base.DefTool().payload(**pa)
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
