import requests
import unittest
import json
from Global_base import global_base,globa_phone
from parameterized import parameterized
from Global_base import login


class RecordAdd(unittest.TestCase):
    """排重接口"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/userrecord/record/add.do')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @parameterized.expand([
        ("浏览记录上报", "867910035562539", "1003", "1", "154907325559300096", "sinaif",
         "1", "2.6.0", "15", "1234")
    ])
    # @unittest.skip("pass")
    def test_record_add(self, name, deviceId, productId, deviceType, targetId, channelId, actType,
                             versionName, versionNo, actSource):
        """排重接口"""
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        token = values[1]
        accountId = values[0]
        code = "1234512dd"
        pa = {"targetId": targetId, "code": code, "accountId": accountId, "deviceId": deviceId, "actType": actType, "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "versionName": versionName, "versionNo": versionNo, "actSource": actSource, "token": token}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
