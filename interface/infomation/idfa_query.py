# coding=utf-8
import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class IdfaQuery(unittest.TestCase):
    """对接信息流查询接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, "/spread/idfa/query")
        # self.url = "https://k8s-qsj-test-jie.iask.cn/spread/idfa/query"

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
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
        ("idfa 不在数据库，返回0;idfa 存在数据库，返回1", "1467866510", "test_in,test_not_in", "10101", "1562234911895", 0, None),
        ("传入多个 idfa，返回多个 idfa 对应值", "1467866510", "auto_test_001,auto_test_002", "10101", "1562234911895", 0, None),

    ])
    @unittest.skip("pass")
    def test_idfaQuery_fault(self, name, appid, idfa, channel, timestamp, msg, code):
        """对接信息流查询接口"""
        if name == "idfa 不在数据库，返回0;idfa 存在数据库，返回1":
            self.params = {"appid": appid, "idfa": idfa, "channel": channel, "timestamp": timestamp}
            self.result = requests.post(url=self.url, data=self.params).json()
            self.assertEqual(self.result["test_in"], 1)
            self.assertEqual(self.result['test_not_in'], msg)
        elif name == "传入多个 idfa，返回多个 idfa 对应值":
            self.params = {"appid": appid, "idfa": idfa, "channel": channel, "timestamp": timestamp}
            self.result = requests.post(url=self.url, data=self.params).json()
            self.assertEqual(self.result["auto_test_001"], msg)
            self.assertEqual(self.result['auto_test_002'], msg)
        else:
            self.params = {"appid": appid, "idfa": idfa, "channel": channel, "timestamp": timestamp}
            self.result = requests.post(url=self.url, data=self.params).json()
            self.assertEqual(self.result["msg"], msg)
            self.assertEqual(self.result['code'], code)


if __name__ == "__main__":
    unittest.main()
