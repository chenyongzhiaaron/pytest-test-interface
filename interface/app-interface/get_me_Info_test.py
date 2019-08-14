import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class GetMeInfo(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/profile/getMeInfo.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("我的页面请求成功", "1", "5", "POST", "1", "false", "request1565592555859", "867910035562539", "2.6.0", "15",
         "1003", "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_getMeInfo(self, case, deviceType, recommendSize, method, pageIndex, json, callbackName,
                       deviceId, ver, verno, productId, channelId, deviceToken, mjbname):
        pa = {"deviceType": deviceType, "recommendSize": recommendSize, "method": method,
              "pageIndex": pageIndex, "json": json, "callbackName": callbackName, "deviceId": deviceId, "ver": ver,
              "verno": verno, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        value = global_base.DefTool.sign(pa)
        sign = {"sign": value}
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result['msg'], 'ok')
            self.assertEqual(self.result["code"], '200')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
