import requests
import unittest
from Global_base import global_base
from parameterized import parameterized
from Global_base import login


class GetMainLinkBySublink(unittest.TestCase):
    "获取子链接"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/sublink/getMainLinkBySublink.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取子链接成功", "153882238043381760", "1", "", "12345678910QSJ", "", "%E8%81%9A%E9%BE%99%E9%92%B1%E5%8C%85", "35823", "0", "")
    ])
    def test_getMainLinkBySublink(self, case, subLink, mobileSystem, appVersion, deviceId, referUrl, linkName,
                                      random,out, s, ):

        pa = {"subLink": subLink, "mobileSystem": mobileSystem, "appVersion": appVersion, "referUrl": referUrl, "linkName": linkName,
              "deviceId": deviceId, "random": random, "out": out, "s":s}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], '200')
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
