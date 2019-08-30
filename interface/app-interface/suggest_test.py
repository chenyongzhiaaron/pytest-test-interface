import requests
import unittest
from Global_base import global_base,globa_phone
from parameterized import parameterized
from Global_base import login


class GetMainLinkBySublink(unittest.TestCase):
    "我的建议接口"
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/suggest')

    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(self.params))
        print("响应结果为{}".format(self.result))

    @parameterized.expand([
        (
        "建议提交", "A11", "", "867910035562539", "2.6.0", "15", "1003",
        "1", "sinaif", "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    @unittest.skip("pass")
    def test_getMainLinkBySublink(self, case, suggestcontent, contactway, deviceId, ver, verno,
                                  productId, deviceType, channelId, deviceToken, mjbname):
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        token = values[1]
        header = {"token": token}
        pa = {"suggestcontent": suggestcontent, "contactway": contactway, "deviceId": deviceId, "ver": ver,
              "verno": verno, "productId": productId, "channelId": channelId, "deviceToken": deviceToken,
              "mjbname": mjbname, "deviceType": deviceType}
        self.params = global_base.DefTool().payload(**pa)
        self.result = requests.post(url=self.url, headers=header, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
