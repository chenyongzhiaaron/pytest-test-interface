import requests
import unittest
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class RecordAdd(unittest.TestCase):
    "助贷工具接口"
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/credit/getCreditHelper.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取助贷工具接口成功", "1003", "1")
    ])
    def test_record_add(self, case, productId, clientType):
        pa = {"productId": productId, "clientType": clientType}
        self.result = requests.post(url=self.url, data=pa).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')



if __name__ == '__main__':
    unittest.main()
