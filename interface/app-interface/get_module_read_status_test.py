import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class GetModuleReadStatus(unittest.TestCase):
    '''获取模块状态接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/getHomeProductListV3.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("未登录获取模块状态", "1", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif", "", "qsj"),
    ])
    def test_get_module_read_status(self, case, type, ver, verno, deviceId, deviceType, productId, channelId,
                                    deviceToken, mjbname):
        pa = {"type": type, "ver": ver, "verno": verno, "deviceId": deviceId, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], '200')


if __name__ == '__main__':
    unittest.main()
