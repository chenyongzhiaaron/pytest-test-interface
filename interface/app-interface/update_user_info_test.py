import unittest
import requests
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class UpdateUserInfo(unittest.TestCase):
    '''更新用户信息接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/updateUserInfo')

    @parameterized.expand([
        ('参数正确，提交成功', "POST", "422201198811260900", "false", "request1565596327350", "赵冰冰",
         "c50e2b0f1b16429da5df10e601790ak3,", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj", 'ok', 200),
    ])
    @unittest.skip("pass")
    def test_update_user_info(self, case, method, idcard, json, callbackName, username, tags, ver, verno,
                              deviceId, deviceType, productId, channelId, deviceToken, mjbname, msg, code):
        mobile = int(globa_phone.phone())
        token = login.LoginByPassWord().login_by_password(mobile)[1]
        header = {"token": token}
        params = {"method": method, "idcard": idcard, "mobile": mobile, "json": json, "callbackName": callbackName,
                  "username": username, "tags": tags, "ver": ver, "verno": verno, "deviceId": deviceId,
                  "deviceType": deviceType, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
                  "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**params)
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], msg)
        self.assertEqual(self.result["code"], code)

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))


if __name__ == '__main__':
    unittest.main()
