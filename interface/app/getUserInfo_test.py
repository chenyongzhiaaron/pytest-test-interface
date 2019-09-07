import unittest
import requests
import json
from Global_base import global_base, login,globa_phone
from parameterized import parameterized


class GetUserInfo(unittest.TestCase):
    """获取用户信息接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/getUserInfo')

    @parameterized.expand([
        ('获取用户信息成功', "2.6.0", "15", "867910035562539", "1", "1003", "sinaif", "ef70fb3178dccde19df9295a68aca0a3",
         "qsj"),
    ])
    # @unittest.skip("pass")
    def test_getUserInfo(self, name, ver, verno, deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        """获取用户信息接口"""
        params = {"ver": ver, "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
                  "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        token = login.LoginByPassWord.login_by_password(self, int(globa_phone.phone()))[1]
        header = {"token": token}
        self.params = global_base.DefTool().payload(**params)
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == '__main__':
    unittest.main()
