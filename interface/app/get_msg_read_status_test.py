import unittest
import requests
import json
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class MsgReadStatus(unittest.TestCase):
    """获取消息状态"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/getMsgReadStatus')

    @parameterized.expand([
        ('参数正确获取消息状态成功',"POST", "false", "request1565595977988", "2.6.0", "15", "867910035562539", "1", "1003", "sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj"),
    ])
    # @unittest.skip("pass")
    def test_getMsgReadStatus(self, name, method, json, callbackName, ver, verno, deviceId, deviceType, productId,
                                  channelId, deviceToken, mjbname):
        """获取消息状态"""
        params = {"method": method, "json": json, "callbackName": callbackName, "ver": ver, "verno": verno,
                  "deviceId": deviceId, "deviceType": deviceType, "productId": productId, "channelId": channelId,
                  "deviceToken": deviceToken, "mjbname": mjbname}
        self.params = global_base.DefTool().payload(**params)
        phone = int(globa_phone.phone())
        value = login.LoginByPassWord().login_by_password(phone)
        token = value[1]
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == '__main__':
    unittest.main()
