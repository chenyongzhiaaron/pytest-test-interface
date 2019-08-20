import unittest
import requests
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
    '''有借、卡贷、闪贷 APP改版首页请求'''

    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/loan/getYkdHomePageInfo.do")

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取有借首页成功", "NPL62420190509175804100", 2, 1, 101, 1001),
        ("获取卡贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1002),
        ("获取闪贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1005),
        # ("产品类型错误,返回400", "NPL62420190509175804100", "12d3", 1, 101, 1005),

    ])
    def test_getYkdHomePageInfo(self, name, cfgId, cfgType, clientType, listType, productId):
        params = {"cfgId": cfgId, "cfgType": cfgType, "clientType": clientType, "listType": listType,
                  "productId": productId}
        try:
            self.result = requests.get(url=self.url, params=params).json()
            self.assertEqual(self.result['code'], '200')
            self.assertEqual(self.result['msg'], 'ok')
            if productId == 1001:
                self.assertEqual(self.result['data']['morePageUrl'],
                                 'http://k8s-qsj-test-jie.iask.cn/pg/qsj/modular/index.html?cfgId=NPL62420190509175804100&productId=1005')
            elif productId == 1002:
                self.assertEqual(self.result['data']['morePageUrl'],
                                 'http://k8s-qsj-test-jie.iask.cn/pg/yjAppV3/all.html?cfgId=NPL52220190520102424100&productId=1001')
            elif productId == 1005:
                self.assertEqual(self.result['data']['morePageUrl'],
                                 'http://k8s-qsj-test-jie.iask.cn/pg/yjAppV3/all.html?cfgId=NPL52220190520102424100&productId=1001')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
