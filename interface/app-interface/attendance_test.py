import unittest
import requests
from Global_base import global_base, globa_phone
from Global_base import login
from parameterized import parameterized
from db_fixture import test_db


class Attendance(unittest.TestCase):
    "签到接口"

    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/profile/attendance.do')
        value = login.LoginByPassWord()
        self.phone = int(globa_phone.phone())
        # self.phone = 18900000000
        values = value.login_by_password(self.phone)
        self.accountId = values[0]
        self.token = values[1]

    @parameterized.expand([
        ('首签成功', "1", "867910035562539", "ok", "200", 1),
        # ('续签成功', "1", "867910035562539", "签到异常", "100102"),
        # ('签到7次后再签返回签到失败', "1", "867910035562539", "签到异常", "100102", ""),
    ])
    @unittest.skip("pass")
    def test_attendance(self, name, deviceType, deviceId, msg, code, continueDay):
        self.params = {"accountId": self.accountId, "deviceType": deviceType, "token": self.token, "deviceId": deviceId}
        sqlDelete = ("DELETE FROM sinaif_easy.t_user_attendance WHERE accountid = {};".format(self.accountId))
        doSQL = test_db.T_DB.t_db_delete(self, sqlDelete)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], msg)
        self.assertEqual(self.result["code"], code)
        self.assertEqual(self.result['data']['attendanceInfo']['continueDay'], continueDay)

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))


if __name__ == '__main__':
    unittest.main()
