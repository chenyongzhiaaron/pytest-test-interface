import unittest
import requests
from Global_base import global_base,login
from parameterized import parameterized


class UpdateUserInfo(unittest.TestCase):
    "获取消息状态"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/updateUserInfo')

    @parameterized.expand([
        ('获取最新口子列表成功', "POST", "422201198811260900", "false", "request1565596327350", "赵冰冰",
         "c50e2b0f1b16429da5df10e601790ak3,", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj"),
    ])
    def test_update_user_info(self, case, method, idcard, json, callbackName, username, tags, ver, verno,
                              deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        mobile = 18127813601
        token = login.LoginByPassWord().login_by_password(mobile)[1]
        header = {"token":token}
        params = {"method": method, "idcard": idcard, "mobile": mobile, "json": json, "callbackName": callbackName,
                  "username": username, "tags": tags, "ver": ver, "verno": verno, "deviceId": deviceId,
                  "deviceType": deviceType, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
                  "mjbname": mjbname}
        sign = global_base.DefTool.sign(self, **params)
        params_new = dict(params, **sign)
        try:
            self.result = requests.post(url=self.url, headers=header,data=params_new).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result["code"], 200)
        except Exception as e:
            print(e)

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
