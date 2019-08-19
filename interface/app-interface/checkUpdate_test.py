import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class CheckUpdate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/checkUpdate')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("IOS更新设备", "E9E6504B-CC17-4FEE-901A-643DDEE5F4BA", "Q001", "cpjz001", "12", 2, "2.5.2", "1003", "1565242903",
         "16c5ffdb6bef1d962c7dd7d6d9e72db0", "sinaifeasy")
    ])
    def test_checkUpdate(self, case, deviceId, source, channelId, verno, deviceType, ver, productId, timestamp,
                         deviceToken, mjbname):
        pa = {"source": source, "channelId": channelId,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "ver": ver, "productId": productId,
              "timestamp": timestamp, "deviceToken": deviceToken, "mjbname": mjbname}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
