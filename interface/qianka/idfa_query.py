# coding=utf-8
import unittest
import requests
import json
from parameterized import parameterized


class IdfaQuery(unittest.TestCase):
    ''' 对接信息流查询接口 '''
    def setUp(self):
        self.url = "http://k8s-qsj-test-jie.iask.cn/spread/idfa/query"

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(self.params))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("appid为空", "", "test", "10101", "1562234911895", "appid错误", 100002),
        ("idfa为空", "1467866510", "", "10101", "1562234911895", "idfa错误", 100002),
        ("channel为空", "1467866510", "test", "", "1562234911895", "channel错误", 100002),
        ("appid错误", "1467866510tesj发", "test", "10101", "1562234911895", "无效的appid", 100002),
        ("appid传null", "null", "test", "10101", "1562234911895", "appid错误", 100002),
        ("appid小于5", "1234", "test", "10101", "1562234911895", "appid错误", 100002),
        ("appid大于32", "123456789012345678901234567890123", "test", "10101", "1562234911895", "appid错误", 100002),
        ("channel错误", "1467866510", "test001", "10101UUU", "1562234911895", "渠道错误", 100002),
        ("channel小于5", "1467866510", "test001", "aaaa", "1562234911895", "channel错误", 100002),
        ("channel大于20", "1467866510", "test001", "123456789012345678901", "1562234911895", "channel错误", 100002),

    ])
    @unittest.skip("pass")
    def test_idfaQuery_fault(self, case, appid, idfa, channel, timestamp, msg, code):
        ''' 对接信息流查询接口 '''
        self.params = {"appid": appid, "idfa": idfa, "channel": channel, "timestamp": timestamp}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], msg)
        self.assertEqual(self.result['code'], code)
    @unittest.skip("pass")
    def test_idfaQuery_success_0(self):
        '''idfa 不在数据库，返回0;idfa 存在数据库，返回1;{"appid": "1467866510", "idfa": "interfacetest,auto_test_init01", "channel": "10101", "timestamp": "1562234911895"}'''
        self.params = {"appid": "1467866510", "idfa": "interfacetest,auto_test_init01", "channel": "10101",
                 "timestamp": "1562234911895"}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["interfacetest"], 0)
        self.assertEqual(self.result["auto_test_init01"], 1)
    @unittest.skip("pass")
    def test_idfaQuery_success_1(self):
        ''' 传入多个 idfa，返回多个 idfa 对应值;{"appid": "1467866510", "idfa": "auto_test_001,auto_test_002,auto_test_003,auto_test_004,auto_test_005", "channel": "10101", "timestamp": "1562234911895"} '''
        self.params = {"appid": "1467866510", "idfa": "auto_test_001,auto_test_002,auto_test_003,auto_test_004,auto_test_005",
                "channel": "10101", "timestamp": "1562234911895"}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["auto_test_001"], 0)
        self.assertEqual(self.result["auto_test_002"], 0)
        self.assertEqual(self.result["auto_test_003"], 0)
        self.assertEqual(self.result["auto_test_004"], 0)
        self.assertEqual(self.result["auto_test_005"], 0)


if __name__ == "__main__":
    unittest.main()
