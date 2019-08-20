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
searchmaps	搜索类型集合，json格式，默认状态下可不传	object	json格式：{"cycleList":"","moneyList":"","sortList":"106022"}，cycleList:"期限类型",moneyList:"额度类型",sortList:"排序类型"
'''


class GetYkdHomePageInfo(unittest.TestCase):
    '''有借、卡贷、闪贷 贷款大全列表'''

    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/loan/getYkdLoanCollection.do")

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取有借首页成功", "NPL62420190509175804100", 2, 1, 101, 1001,
         {"cycleList": "", "moneyList": "", "sortList": "106024"}),
        ("获取卡贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1002,
         {"cycleList": "", "moneyList": "", "sortList": "106024"}),
        ("获取闪贷首页成功", "NPL62420190509175804100", 2, 1, 101, 1005,
         {"cycleList": "", "moneyList": "", "sortList": "106024"}),
        # ("产品类型错误,返回400", "NPL62420190509175804100", "12d3", 1, 101, 1005),

    ])
    def test_getYkdHomePageInfo(self, name, cfgId, cfgType, clientType, listType, productId, searchmaps):
        params = {"cfgId": cfgId, "cfgType": cfgType, "clientType": clientType, "listType": listType,
                  "productId": productId, "searchmaps": searchmaps}
        try:
            self.result = requests.get(url=self.url, params=params).json()
            self.assertEqual(self.result['code'], '200')
            self.assertEqual(self.result['msg'], 'ok')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
