import requests
import unittest
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class SaveGps(unittest.TestCase):
    '''保存GPS接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/credit/saveGps')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))

    @parameterized.expand([
        ("保存gps", "1003", "cpjz001", '[{"city":"深圳市","content":"广东省深圳市南山区高新南六道靠近朗科大厦","longitude":"113.952595","areacode":"440305","latitude":"22.535389","locationtime":"2019-08-08 13:50:27","type":"0"}]', "1565243427", "16c5ffdb6bef1d962c7dd7d6d9e72db0", "E9E6504B-CC17-4FEE-901A-643DDEE5F4BA", "Q001",
         "2", "sinaifeasy", "2.5.2", 12)
    ])
    @unittest.skip("pass")
    def test_saveGps(self, name, productId, channelId, strJson, timestamp, deviceToken, deviceId, source, deviceType,
                         mjbname, ver, verno):
        pa = {"productId": productId, "channelId": channelId, "strJson": strJson, "timestamp": timestamp,
              "deviceToken": deviceToken,
              "deviceId": deviceId, "source": source, "deviceType": deviceType, "mjbname": mjbname, "ver": ver, "verno": verno}
        self.params = global_base.DefTool().payload(**pa)
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        token = values[1]
        headers = {"token": token}
        self.result = requests.post(url=self.url, headers=headers, data=self.params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
            self.assertEqual(self.result['data']['title'], "关于我们")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
