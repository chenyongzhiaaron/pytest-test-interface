import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class Init(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/init')

    @parameterized.expand([
        ('初始成功', "000000", "", "7f8af6d4b932a77e", "90:2B:D2:C6:2C:8F", "HONOR", "5860656", "56910413824",
         "38484373504",
         "2.5.1", "14", "868777047018746", "1", "1003", "cpjz002", "", "cjhj"),
    ])
    def test_init(self, caase, imsi, serialnumber, androidid, mac, brand, memory, totalspace, availablespace, ver,
                  verno,
                  deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        pa = {"imsi": imsi, "serialnumber": serialnumber, "androidid": androidid, "mac": mac, "brand": brand,
              "memory": memory, "totalspace": totalspace, "availablespace": availablespace, "ver": ver,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        values = global_base.DefTool.sign(self, **pa)
        sign = {"sign": values}
        params = dict(pa, **sign)
        # print(params)
        try:
            self.result = requests.post(url=self.url, data=params).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result["code"], 200)
        except Exception as e:
            print(e)

    def tearDown(self):
        print(self.result)
        # print(self.url)


if __name__ == '__main__':
    unittest.main()
