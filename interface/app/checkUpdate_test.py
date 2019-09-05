import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class CheckUpdate(unittest.TestCase):
    '''检查更新版本'''

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/checkUpdate')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("IOS更新设备", "E9E6504B-CC17-4FEE-901A-643DDEE5F4BA", "Q001", "cpjz001", "12", 2, "2.5.2", "1003", "1565242903",
         "16c5ffdb6bef1d962c7dd7d6d9e72db0", "sinaifeasy")
    ])
    def test_checkUpdate(self, name, deviceId, source, channelId, verno, deviceType, ver, productId, timestamp,
                         deviceToken, mjbname):
        """{}""".format(name)
        pa = {"source": source, "channelId": channelId,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "ver": ver, "productId": productId,
              "timestamp": timestamp, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "当前已是最新版本")
        self.assertEqual(self.result['code'], 1000013)


if __name__ == '__main__':
    unittest.main()
