import unittest
import requests
from Global_base import global_base,login
from parameterized import parameterized


class UpdateUserInfo(unittest.TestCase):
    '''更新用户信息接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/updateUserInfo')

    @parameterized.expand([
        ('身份证号信息已存在无法重新提交', "POST", "422201198811260900", "false", "request1565596327350", "赵冰冰",
         "c50e2b0f1b16429da5df10e601790ak3,", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj"),
    ])
    def test_update_user_info(self, case, method, idcard, json, callbackName, username, tags, ver, verno,
                              deviceId, deviceType, productId, channelId, deviceToken, mjbname):
        mobile = 18127813601
        token = login.LoginByPassWord().login_by_password(mobile)[1]
        header = {"token": token}
        params = {"method": method, "idcard": idcard, "mobile": mobile, "json": json, "callbackName": callbackName,
                  "username": username, "tags": tags, "ver": ver, "verno": verno, "deviceId": deviceId,
                  "deviceType": deviceType, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
                  "mjbname": mjbname}
        params_new = global_base.DefTool().payload(**params)
        self.result = requests.post(url=self.url, headers=header,data=params_new).json()
        self.assertEqual(self.result["msg"], "您填写的身份证号已存在，请重新输入")
        self.assertEqual(self.result["code"], 2100001)

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
