import unittest
import requests
import json
from Global_base import global_base
from parameterized import parameterized


class Init(unittest.TestCase):
    """初始化接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/init')

    @parameterized.expand([
        ('参数正确，初始化成功', "000000", "", "7f8af6d4b932a77e", "90:2B:D2:C6:2C:8F", "HONOR", "5860656", "56910413824",
         "38484373504",
         "2.5.1", "14", "868777047018746", "1", "1003", "cpjz002", "", "cjhj"),
    ])
    def test_init(self, name, imsi, serialnumber, androidid, mac, brand, memory, totalspace, availablespace, ver,
                  verno, deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        """{}""".format(name)
        pa = {"imsi": imsi, "serialnumber": serialnumber, "androidid": androidid, "mac": mac, "brand": brand,
              "memory": memory, "totalspace": totalspace, "availablespace": availablespace, "ver": ver,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == '__main__':
    unittest.main()
