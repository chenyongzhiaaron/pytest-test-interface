import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class UserAction(unittest.TestCase):
    """代运营获取列表产品信息接口(微聚)'"""
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/apph5/partner/loan/userAction.do")

    @parameterized.expand([
        ("参数正确获取微距产品列表成功",
         "p8IvNWG2SN/7AViSuhgSfki8ia2jt+JihfBChesee4sn1Ncighutzy2WATtwurIsCL3qwCE/7E2ILZgTELom5XH7L4pnhKacPFSG6RVC3HhW/6y0QHGh9Ike6k3FguEJ+HytfgkYL97c6m+f6SnIvKhWPDG7TebUnGkShQJxIpAHoSsJspI3WkIbLuUiClyLnGkShQJxIpA2fvenGHIBlEgbUEA5P8A4/6xoKm9ABZVTb7TncWl1sAhKx9LtVhGP/OmpMV9Cj/oL9SWjMhqxmd8rIIpFiHh1QTfmfK0LZ6Q89/tox/vkvvtbO1y/NpHV7YZ+DZswqVtlTHbqq6/lzCUNAV20Dmbkr8rs+Q09vx3zmpEkpQ+NRemjI+0eHi3b1bwmD8P6oSCzUwWFesyno3XMUgoIRh0V",
         "lv7xOW2C0Bh91egsFYGBjKMKaTQGcyOaQyYwp6JSVtTvBdedlhs3m8a9WnGUd8u7DU3SSJLXc5eWD10P+soYtAoWmngxLKtI/JjP63ItPI3dqfMbknpRjbTHmM0iMElVpqc21bekxJ3ohUbavESLnsDaGT/HOUdYKA0OTpbe/aw=",
         "1", "webh5_wj", "getList", "1539073086805")
    ])
    def test_userAction_success(self, name, bizData, bizKey, enVerNo, mchId, reqName, time):
        """代运营获取列表产品信息接口(微聚)'"""
        self.params = {
            "bizData": bizData,
            "bizKey": bizKey,
            "enVerNo": enVerNo, "mchId": mchId, "reqName": reqName, "time": time}
        result = global_base.RunMain("post", self.url, None, None, self.params)
        self.result = result.re
        self.assertEqual(self.result['code'], "200")

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == "__main__":
    unittest.main()
