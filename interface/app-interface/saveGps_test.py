import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class GetProtocol(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/credit/saveGps')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("关于我们", "1003", "cpjz001", [{"city":"深圳市","content":"广东省深圳市南山区高新南六道靠近朗科大厦","longitude":"113.952595","areacode":"440305","latitude":"22.535389","locationtime":"2019-08-08 13:50:27","type":"0"}], "1565243427", "16c5ffdb6bef1d962c7dd7d6d9e72db0", "E9E6504B-CC17-4FEE-901A-643DDEE5F4BA", "Q001",
         "2", "sinaifeasy", "2.5.2", 12, )
    ])
    def test_getProtocol(self, case, productId, channelId, strJson, timestamp, deviceToken, deviceId, source, deviceType,
                         mjbname, ver, verno):
        pa = {"productId": productId, "channelId": channelId,
              "type": type, "deviceId": deviceId, "deviceType": strJson, "strJson": deviceToken,
              "deviceToken": productId,
              "timestamp": timestamp, "source": source, "mjbname": mjbname, "deviceType": deviceType}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        headers = {"headers":"deviceType"}
        self.result = requests.post(url=self.url, headers=headers, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
            self.assertEqual(self.result['data']['title'], "关于我们")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
