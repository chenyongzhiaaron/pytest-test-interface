import unittest
import requests
from Global_base import global_base
from Global_base import login
from parameterized import parameterized


class Attendance(unittest.TestCase):
    "获取消息状态"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/getMsgReadStatus')

    @parameterized.expand([
        ('获取最新口子列表成功', "1", "867910035562539"),
    ])
    def test_attendance(self, case, deviceType, deviceId):
        value = login.LoginByPassWord()
        values = value.login_by_password(18127813601)
        accountId = values[0]
        token = values[1]
        params = {"accountId": accountId, "deviceType": deviceType, "token": token, "deviceId": deviceId}
        params_new = global_base.DefTool.payload(self, **params)
        self.result = requests.post(url=self.url, data=params_new).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
