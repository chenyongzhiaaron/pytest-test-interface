import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class SendPhoneCode(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/userrecord/record/add.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("找回密码成功", "867910035562539", "1003", "1", "154907325559300096", "sinaif",
         "1", "2.6.0", "15", "1234")
    ])
    def test_send_phone_code(self, case, deviceId, productId, deviceType, targetId, channelId, actType,
                             versionName, versionNo, actSource):

        accountId = "18888888888"
        token = "token"
        code = "1234512dd"
        pa = {"targetId": targetId, "code": code, "accountId": accountId, "deviceId": deviceId, "actType": actType, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "versionName": versionName, "versionNo": versionNo, "actSource": actSource, "token": token}
        value = global_base.DefTool.sign(self, **pa)
        sign = {"sign": value}
        params = dict(pa, **sign)
        self.result = requests.post(url=self.url, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except AssertionError as  e:
            print(e)


if __name__ == '__main__':
    unittest.main()
