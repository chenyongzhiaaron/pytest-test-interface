import requests
import unittest
from Global_base import global_base,globa_phone
from Global_base import login
from parameterized import parameterized


class GetMsgList(unittest.TestCase):
    '''消息接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/getMsgList.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("消息", "requestData1565595880131", "867910035562539", "2.6.0", "15", "1003", "1","sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_getMsgList(self, case, callbackName, deviceId, ver, verno, productId, deviceType, channelId, deviceToken,
                             mjbname):
        pa = {"callbackName": callbackName, "type": type, "verno": verno, "deviceId": deviceId, "ver": ver,
              "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        params = global_base.DefTool().payload(**pa)
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        token = values[1]
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
