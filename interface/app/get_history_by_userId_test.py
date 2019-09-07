import unittest
import requests
import json
from Global_base import global_base,globa_phone
from Global_base import login
from parameterized import parameterized


class HistoryByUserId(unittest.TestCase):
    """查询历史纪录接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/productRecord/getHistoryByUserId.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ('查询历史纪录成功', "867910035562539", "1003", "1", "1", "1", "50"),
    ])
    # @unittest.skip("pass")
    def test_get_history_by_userId(self, name, deviceId, productId, deviceType, actType, pageIndex, pageSize):
        """查询历史纪录接口"""
        value = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        token = value[1]
        accountId = value[0]
        self.params = {"deviceId": deviceId, "accountId": accountId, "productId": productId, "deviceType": deviceType,
                  "actType": actType, "token": token, "pageIndex": pageIndex, "pageSize": pageSize}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], '200')


if __name__ == '__main__':
    unittest.main()
