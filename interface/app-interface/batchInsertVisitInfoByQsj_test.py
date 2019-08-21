import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class BatchInsertVisitInfoByQsj(unittest.TestCase):
    '''曝光埋点'''
    def setUp(self):
        self.url = "https://api.sinawallent.com/statistics/static/logs/batchInsertVisitInfoByQsj"

    def tearDown(self):
        print(self.result)
    @unittest.skip("pass")
    def test_batchInsertVisitInfoByQsj(self):
        params = {"productId": "1003",
                  "timeStr": "Mon Aug 12 2019 16:29:45 GMT+0800 (中国标准时间)",
                  "ostype": "2",
                  "accountId": "156335749888185575",
                  "channel": "MJBIOS015",
                  "appVersion": "2.6.0",
                  "mobileSystem": "2",
                  "source": "1003",
                  "sourceEventCode": "https://k8s-qsj-test-jie.iask.cn/pg/qsjEncryp/index.html?num=15&channel=MJBIOS015&appVersion=1.1&deviceId=1ED714DC-8B19-4AD9-9EC7-8507AD23C454&source=Q001&mjbname=yjwy&timestamp=1566201102",
                  "visitStartTime": "1566201257003",
                  "currentEventCode": "url_exposure",
                  "json": [{"productId": "1003", "timeStr": "Mon Aug 19 2019 15:54:17 GMT+0800 (CST)", "ostype": 2,
                            "accountId": "", "channel": "MJBIOS015", "appVersion": "1.1", "mobileSystem": 2,
                            "source": "1003",
                            "sourceEventCode": "https://k8s-qsj-test-jie.iask.cn/pg/qsjEncryp/index.html?num=15&channel=MJBIOS015&appVersion=1.1&deviceId=1ED714DC-8B19-4AD9-9EC7-8507AD23C454&source=Q001&mjbname=yjwy&timestamp=1566201102",
                            "visitStartTime": 1566201257003, "currentEventCode": "url_exposure",
                            "currentEventParams": "[{\"index\":\"4\",\"id\":\"153160989482770432\",\"name\":\"惠普钱袋\",\"openUrl\":\"bMzq7y/EYLL1PeBki5fEwfXZkXeCQSe9gJTlJtg0mE5gYyoaATphYRhSOZebmreQJZhzA2IgooJ/uK21+O3AHw==\"},{\"index\":\"5\",\"id\":\"153558164838637568\",\"name\":\"信客花\",\"openUrl\":\"+oK6dxq1Q4Z0ePgbk9SbULKTrHFKxN3qqH4Vuwbw8Y75rM8HqBahA7d/3GxF55N5qDTid7oFuOrOWOpiZpV5T7VWHG1oEvqhKP2mLrDj1hM=\"}]",
                            "deviceId": "1ED714DC-8B19-4AD9-9EC7-8507AD23C454",
                            "sourceEventParams": "{\"forClient\":\"qsj\",\"cfgId\":\"\",\"batch\":\"\"}"}]}
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                  "Accept":"application/json, text/plain, */*"}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)



if __name__ == '__main__':
    unittest.main()
