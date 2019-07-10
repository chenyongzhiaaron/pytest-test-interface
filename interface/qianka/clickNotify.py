# coding=utf-8
import unittest
import requests
from parameterized import parameterized
from db_fixture import test_db_idfa


class ClickNotify(unittest.TestCase):
    def setUp(self):
        self.url = "http://k8s-qsj-test-jie.iask.cn/spread/idfa/clickNotify"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("参数正确，点击成功", "1467866510", "auto_test_init05", "10101", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "ok", 200),
        (
        "appid为空", "", "auto_test_init09", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/", "appid错误",
        100002),
        ("idfa为空", "1467866510", "", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/", "idfa错误",
         100002),
        ("channel为空", "1467866510", "auto_test_init09", "", "192.168.130.116", "1562234911895", "https://baidu.com/",
         "channel错误", 100002),
        ("ip为空", "1467866510", "auto_test_init09", "10101", "", "1562234911895", "https://baidu.com/", "不符合IP规则",
         100002),
        ("appid错误", "1467866510tesj发", "auto_test_init09", "10101", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "无效的appid", 100002),
        ("appid传null", "null", "auto_test_init09", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/",
         "appid错误", 100002),
        ("appid小于5", "1234", "auto_test_init09", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/",
         "appid错误", 100002),
        ("appid大于32", "123456789012345678901234567890123", "auto_test_init09", "10101", "192.168.130.116",
         "1562234911895", "https://baidu.com/", "appid错误", 100002),
        ("idfa小于5", "1467866510", "1234", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/", "idfa错误",
         100002),
        ("idfa大于50", "1467866510", "123456789012345678901234567890123456789012345678901", "10101", "192.168.130.116",
         "1562234911895", "https://baidu.com/", "idfa错误", 100002),
        ("channel错误", "1467866510", "auto_test_init09", "10101UUU", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "渠道错误", 100002),
        ("channel小于5", "1467866510", "auto_test_init09", "aaaa", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "channel错误", 100002),
        ("channel大于20", "1467866510", "auto_test_init09", "123456789012345678901", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "channel错误",
         100002),
        ("ip错误", "1467866510", "auto_test_init09", "10101", "192168130116", "1562234911895", "https://baidu.com/",
         "不符合IP规则", 100002),
        ("callback为空", "1467866510", "auto_test_init09", "10101", "192.168.130.1", "1562234911895", "", "ok", 200),

    ])
    def test_clickNotify(self, case, appid, idfa, channel, ip, timestamp, callback, msg, code):
        ''' 点击下载接口测试 '''
        data = {"appid": appid, "idfa": idfa, "channel": channel, "ip": ip, "timestamp": timestamp,
                "callback": callback}
        self.result = requests.post(url=self.url, data=data).json()
        if case == '参数正确，点击成功':
            db_idfa = test_db_idfa.T_DB().t_db2()
            self.assertEqual(idfa, str(db_idfa))
            self.assertEqual(self.result["msg"], msg)
        elif case == 'callback为空':
            self.assertEqual(self.result["msg"], msg)
            self.assertEqual(self.result["code"], code)
        else:
            self.assertEqual(self.result["msg"], msg)


if __name__ == "__main__":
    unittest.main()
