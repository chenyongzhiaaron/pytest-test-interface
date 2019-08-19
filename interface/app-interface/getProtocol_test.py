import requests
import unittest
from Global_base import global_base
from Global_base import login
from parameterized import parameterized


class GetProtocol(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/sys/h5/getProtocol')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("关于我们", "1003", "MJBIOS006", "3", "0", "1.0", "26F1ED6A-B927-461B-AEB2-203459A3CEFC", "Q001",
         "sinaifeasy2303", "1565324192")
    ])
    def test_getProtocol(self, case, productId, channelId, type, auditStatus, appVersion, deviceId, source, mjbname,
                         timestamp):
        values = login.LoginByPassWord().login_by_password(18127813601)
        fromUserId = values[0]
        token = values[1]
        pa = {"productId": productId, "channelId": channelId,
              "type": type, "deviceId": deviceId, "deviceType": auditStatus, "auditStatus": appVersion,
              "appVersion": productId,
              "timestamp": timestamp, "source": source, "mjbname": mjbname, "fromUserId": fromUserId, "token": token}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
            self.assertEqual(self.result['data']['title'], "关于我们")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
