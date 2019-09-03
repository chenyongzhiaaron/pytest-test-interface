import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class CheckUpdate(unittest.TestCase):
    def setUp(self):
        # self.url = "https://api.sinawallent.com/statistics/static/logs/batchInsertVisitInfoByQsj"
        self.url = "https://jie.iask.cn/mweb/static/logs/batchInsertVisitInfo"

    def tearDown(self):
        print("请求参数:{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求响应:{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @unittest.skip("pass")
    def test_batchInsertVisitInfo(self):
        '''监控埋点'''
        self.params = {"source": "monitor-h5",
                       "ostype": "ios",
                       "json": [{
                           "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/watched.html?token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                           "channel": "error",
                           "mobileSystem": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                           "currentEventCode": "错误信息：[object ErrorEvent] or {\"isTrusted\":true}",
                           "currentEventParams": "", "deviceId": "24C64FCD-F36D-4E5B-B71F-C10F7ED7B445"}]}
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
