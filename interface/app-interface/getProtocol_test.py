import requests
import unittest
from Global_base import global_base,globa_phone
from Global_base import login
from parameterized import parameterized


class GetProtocol(unittest.TestCase):
    '''关于我们接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/h5/getProtocol')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))
    @parameterized.expand([
        ("关于我们", "1003", "MJBIOS006", "3", "0", "1.0", "26F1ED6A-B927-461B-AEB2-203459A3CEFC", "Q001",
         "sinaifeasy2303", "1565324192")
    ])
    @unittest.skip("pass")
    def test_getProtocol(self, case, productId, channelId, type, auditStatus, appVersion, deviceId, source, mjbname,
                         timestamp):
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        fromUserId = values[0]
        token = values[1]
        pa = {"productId": productId, "channelId": channelId,
              "type": type, "deviceId": deviceId, "deviceType": auditStatus, "auditStatus": appVersion,
              "appVersion": productId,
              "timestamp": timestamp, "source": source, "mjbname": mjbname, "fromUserId": fromUserId, "token": token}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)
        self.assertEqual(self.result['data']['title'], "关于我们")


if __name__ == '__main__':
    unittest.main()
