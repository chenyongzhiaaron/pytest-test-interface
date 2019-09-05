# coding=utf-8
import unittest
import requests
import json
from parameterized import parameterized
from db_fixture import test_db
from  Global_base import global_base


class ClickNotify(unittest.TestCase):
    """对接信息流点击下载接口测试"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/spread/idfa/clickNotify")

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("参数正确，点击成功", "1467866510", "test_in", "10101", "192.168.130.116", "1562234911895",
         "https://baidu.com/", "ok", 200),
        (
        "appid为空", "", "auto_test_init09", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/", "appid错误",
        100002),
        ("idfa为空", "1467866510", "", "10101", "192.168.130.116", "1562234911895", "https://baidu.com/", "idfa错误",
         100002),
        ("channel为空", "1467866510", "auto_test_init09", "", "192.168.130.116", "1562234911895", "https://baidu.com/",
         "channel错误", 100002),
        ("ip为空", "1467866510", "auto_test_init09", "10101", "", "1562234911895", "https://baidu.com/", "ip错误",
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
        ("callback为空", "1467866510", "test_in", "10101", "192.168.130.1", "1562234911895", "", "ok", 200),

    ])
    @unittest.skip("pass")
    def test_clickNotify(self, name, appid, idfa, channel, ip, timestamp, callback, msg, code):
        """{}""".format(name)
        self.params = {"appid": appid, "idfa": idfa, "channel": channel, "ip": ip, "timestamp": timestamp,
                "callback": callback}
        self.result = requests.post(url=self.url, data=self.params).json()
        if name == '参数正确，点击成功':
            sqlSelect = ("select '{}' from t_spread_general_idfainfo where appid = 1467866510 order by infoid desc limit 0,1;".format(str(idfa)))
            db_idfa = test_db.T_DB.t_db_select(self, sqlSelect, idfa)
            self.assertEqual(idfa, str(db_idfa))
            self.assertEqual(self.result["msg"], msg)
        elif name == 'callback为空':
            self.assertEqual(self.result["msg"], msg)
            self.assertEqual(self.result["code"], code)
        else:
            self.assertEqual(self.result["msg"], msg)


if __name__ == "__main__":
    unittest.main()
