import requests
import unittest
import json
from Global_base import global_base, login, globa_phone
from parameterized import parameterized


class Logout(unittest.TestCase):
    """退出登陆接口"""

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/logout')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("退出登录", "868777047018746", "2.6.0", "15", "1003", "1", "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    # @unittest.skip("pass")
    def test_logout(self, name, deviceId, ver, verno, productId, deviceType, channelId, deviceToken, mjbname):
        """{}""".format(name)
        pa = {"verno": verno, "deviceId": deviceId, "ver": ver, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**pa)
        token = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))[1]
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
