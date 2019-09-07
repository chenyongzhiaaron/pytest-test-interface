import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized

'''
cfgId	列表ID	string	
cfgType	产品类型：固定为2	number	
clientType	客户端类型(1/安卓，2/iOS)	number	
listType	列表类型：固定为101	number	
productId	产品ID(有借/1001,卡贷/1002,闪贷/1005)	string	
'''


class GetYkdHomePageInfo(unittest.TestCase):
    """有借、卡贷、闪贷 APP改版首页请求"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/loan/getYkdHomePageInfo.do")

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ["获取有借首页成功", "NPL62420190509175804100", 2, 1, 101, 1001],
        ["获取卡贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1002],
        ["获取闪贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1005],
        # ("产品类型错误,返回400", "NPL62420190509175804100", "12d3", 1, 101, 1005),

    ])
    def test_getYkdHomePageInfo(self, name, cfgId, cfgType, clientType, listType, productId):
        """有借、卡贷、闪贷 APP改版首页请求"""
        self.params = {"cfgId": cfgId, "cfgType": cfgType, "clientType": clientType, "listType": listType,
                  "productId": productId}
        self.result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')


if __name__ == '__main__':
    unittest.main()
