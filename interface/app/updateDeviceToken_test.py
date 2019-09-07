import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class UpdateDeviceToken(unittest.TestCase):
    """跟新IOS设备接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/updateDeviceToken')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("IOS更新设备", "Q001", "MJBIOS006", 12, "26F1ED6A-B927-461B-AEB2-203459A3CEFC", 2, "2.5.2", "1003", "1565323649",
         "63edacc63684d3566ec3ebf3e9939732", "qsj")
    ])
    def test_updateDeviceToken(self, name, source, channelId, verno, deviceId, deviceType, ver, productId, timestamp, deviceToken, mjbname):
        """跟新IOS设备接口"""
        pa = {"source": source, "channelId": channelId,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "ver": ver,
              "productId": productId, "timestamp": timestamp, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
