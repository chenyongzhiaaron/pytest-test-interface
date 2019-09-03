import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class UserAction(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/usercenterh5/partner/userAction.do")

    @parameterized.expand([
        ("参数正确企鹅钱袋getInitInfo获取初始化信息成功",
         "gt3iuSbaCRNK+PyxUUH3vp7/jixjuSkj77n/XuJsY4BK/x9sc+RmOHyslCfzYAWSY0EEVvyHND0JYcw6CIFzvCf/ghLUIUQ5iphHl4dli7DZSgR+/PeyQrNzvSsU2tsXHigLG5WaRu4oF5fMXzBFbdUYD3ok+gG11P1oIO/Bqnw9UqGRLZ6HE3rU4XK0DOyDybFgfco2I1j22ZfmSP4NPXVMjRRkwEjlAGVbXpPVheebhSiPSkWRZJW++Nm4DDokrNEXfYvxOcse1GLc+gZ17luopnBfsOXpbEbDQer5MDdcZmyGvhg3SzZeOiPIWcbvxXodG4SLAMpSBGjrJ4EKYeJwV0uAQL+nk0LGtbRp38mHuGGsABokTWaT5k6ABQPLRJnX+2f65OWyWvO6TIF5NBjcD9ws+WOM",
         "EJ2s7FOVhCsUG72dEb8NxmAsW9wExU2EWKGX8qhBKIF/uXGyeraFlfsmqXkvjeK5naAi0+cMcekC1dWOyrRoViVB3JIcVVc7Ju2s2YigHf/8P5DwvO3MWaFLI0hFT8t+p4JzAg9k2eoPxK15wrYIeaoydRKzKqWgA5djzpjj8Hs=",
         "1", "webh5_qeqd", "getInitInfo", "1567166616292"),
        ("参数正确企鹅钱袋postUserInfo成功",
         "80wbmx1d/JkJWvKSvSGTHAfTU7B9j3ZGMTz597sdV1shUxyuz7Z8J6u6HBkBdGvwJYgBJqQo0eYxu5lpQrlbwrujPPE3GRglKdiCn4tn9R01X8+AH9wX7r4ht62P6wAXvbAJWbhXm/02SrCWeLXkf/MVL8O3j8DhYVEyPAgYg/cITC9spwlbYMefMNcvnSwvf2IvSsOXXPDXXLDsSGbsKGkZ1+8iAu7yxmSFjMY+VOsysNKwiCBzrKaFQfgBWEUE7S0/oPrbR36zhSfIjQYLYHbU9+QzBgK+KdiCn4tn9R1IzLoTyoSTsTjL3tUD2Rn5yxN3SjM46Z4baZ3mWDbqGcQH5zJNU/BbHueBu5nacYl1kQJlyE/pYSxY6irLpCtQoU2QpbLP4SHBFzBV6aZNWamELpKN8+k1E0ewUP5/j+Y9GRRci82qL7x4K4p78PTO",
         "t5bTNdhNjgtRxTjWe3J+lPLQLj8DqYWmrnkMCpm9FKZ88A1c8xoJpA06KawRhrssn1V7wOLNQH1tkn3TlMgRL7+svzdghmt+7VzZJwXeYZg19wKcF64PwK38+0+HjHWpOVglMXFBXTqNwsKKiU1ACP1T/fL7zxxa8yjhNkknnCc=",
         "1", "webh5_qeqd", "postUserInfo", "1567392954796"),
        ("参数正确获取微距产品列表成功",
         "p8IvNWG2SN/7AViSuhgSfki8ia2jt+JihfBChesee4sn1Ncighutzy2WATtwurIsCL3qwCE/7E2ILZgTELom5XH7L4pnhKacPFSG6RVC3HhW/6y0QHGh9Ike6k3FguEJ+HytfgkYL97c6m+f6SnIvKhWPDG7TebUnGkShQJxIpAHoSsJspI3WkIbLuUiClyLnGkShQJxIpA2fvenGHIBlEgbUEA5P8A4/6xoKm9ABZVTb7TncWl1sAhKx9LtVhGP/OmpMV9Cj/oL9SWjMhqxmd8rIIpFiHh1QTfmfK0LZ6Q89/tox/vkvvtbO1y/NpHV7YZ+DZswqVtlTHbqq6/lzCUNAV20Dmbkr8rs+Q09vx3zmpEkpQ+NRemjI+0eHi3b1bwmD8P6oSCzUwWFesyno3XMUgoIRh0V",
         "lv7xOW2C0Bh91egsFYGBjKMKaTQGcyOaQyYwp6JSVtTvBdedlhs3m8a9WnGUd8u7DU3SSJLXc5eWD10P+soYtAoWmngxLKtI/JjP63ItPI3dqfMbknpRjbTHmM0iMElVpqc21bekxJ3ohUbavESLnsDaGT/HOUdYKA0OTpbe/aw=",
         "1", "webh5_wj", "getList", "1539073086805")
    ])
    def test_userAction_success(self, name, bizData, bizKey, enVerNo, mchId, reqName, time):
        '''代运营获取初始化信息接口'''
        self.params = {
            "bizData": bizData,
            "bizKey": bizKey,
            "enVerNo": enVerNo, "mchId": mchId, "reqName": reqName, "time": time}
        result = global_base.RunMain("post", self.url, self.params)
        self.result = result.re
        self.assertEqual(self.result['code'], 200)

    def tearDown(self):
        print("请求URL：{}".format(self.url))
        print("请求参数为：{}".format(self.params))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == "__main__":
    unittest.main()
