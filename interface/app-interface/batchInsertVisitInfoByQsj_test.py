import requests
import unittest
import json
from Global_base import global_base
from parameterized import parameterized


class BatchInsertVisitInfoByQsj(unittest.TestCase):
    '''曝光埋点'''

    def setUp(self):
        self.url = "https://jie.iask.cn/mweb/static/logs/batchInsertVisitInfoByQsj"

    def tearDown(self):
        print("请求URL： {}".format(self.url))
        print("请求的参数:{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))

    @unittest.skip("pass")
    def test_batchInsertVisitInfoByQsj_url_exposure(self):
        ''' 精准曝光埋点'''
        self.params = {"productId": "1003",
                       "timeStr": "Tue Sep 03 2019 11:40:47 GMT+0800 (CST)",
                       "ostype": "2",
                       "accountId": "151635537517645909",
                       "channel": "MJBIOS008",
                       "appVersion": "1.1",
                       "mobileSystem": "2",
                       "source": "1003",
                       "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/query.html?cfgId=16&hsinaifNeedFullWin=2&token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                       "visitStartTime": "1567482047611",
                       "currentEventCode": "url_exposure",
                       "json": [{"productId": "1003", "timeStr": "Tue Sep 03 2019 11:40:47 GMT+0800 (CST)", "ostype": 2,
                                 "accountId": "151635537517645909", "channel": "MJBIOS008", "appVersion": "1.1",
                                 "mobileSystem": 2, "source": "1003",
                                 "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/query.html?cfgId=16&hsinaifNeedFullWin=2&token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                                 "visitStartTime": 1567482047611, "currentEventCode": "url_exposure",
                                 "currentEventParams": "[{\"index\":\"11\",\"id\":\"5814\",\"name\":\"有钱花\",\"openUrl\":\"F1HzUHqnfCiGrDcCJPr86yhEwZpdNneSD4nnchyTcBGKSDBlnO6GASessqSVlKA1diVDFgdWttaIV1ZZ5DL3ttEWVKbJyG6pjgm6dnbfsKk=\"},{\"index\":\"12\",\"id\":\"6134\",\"name\":\"钱伴\",\"openUrl\":\"GjSEh/5j4PENTxVkL2oKXZRXkxNBh85UNo9Ai9AIMtLuM52j5VXjlvMUeEVi/okTjnCgJ6A9u9Ow1c6/AGxpiKj/8YB2jYB400XkEeqwL/k=\"},{\"index\":\"13\",\"id\":\"5484\",\"name\":\"易美付\",\"openUrl\":\"wOAynDHA5wg3m9TVesRtIawQL224hFBntw1fW4j9YXKnhL8LtdcZCVO8xLV0fnmynz/DQwtXp5vg+WKj+YnHFzxvMlAENi/DjD2eckNCHqY=\"},{\"index\":\"14\",\"id\":\"6191\",\"name\":\"功夫贷\",\"openUrl\":\"k9hXA1HZYLM9mz5dHdHKIp958267uANans4JGu2GgM8Ee7N/GBhib+4UdTaJTEVuBpByFA/bIhBxzK2YDfHfMjZRsxEiYHSvZptiL6fN/AE=\"},{\"index\":\"15\",\"id\":\"6171\",\"name\":\"及贷\",\"openUrl\":\"UJCewwwVedZKqsulkvBWICfUK056oryPIsGb+PjNtoqY+CU//0Vk9b3THFXYiAVjJ2QRS1/mW6nxc23xDjagKqPG5x/E/SJS/KwNxTcerWs=\"},{\"index\":\"16\",\"id\":\"5651\",\"name\":\"瑞贷\",\"openUrl\":\"FzjgtMjZw/RPYjtVxbrBHYmyULOlHbW/KZ499w0dt/+94nYb4vQPpvtj3dkbQemIDukzIBfw7i7wA1mkOAyWCRJSsgf7l6KFqZfgkvbYZnI=\"},{\"index\":\"17\",\"id\":\"5924\",\"name\":\"玖富万卡\",\"openUrl\":\"SOrTNXfgN47iEfWYRFqpQyg0zgP+QClEdRIXDbcTzSSBHXrBNhyMGFWG7dNYkcLiQYEC0cT08I+GFYyS5wydANROPfzDALMJK/QTYPxtgPE=\"},{\"index\":\"18\",\"id\":\"6199\",\"name\":\"51人品贷\",\"openUrl\":\"fG8ut8XuBBf7yWUuiSP2q3SyWn1C1b1xd/GjDy8mDlwJKOJvebHjOpLOmpASZKgBUg1B/rtuEJOZwEmzYLcvPoH5u39ctrRn3QA9kEDfmXI=\"},{\"index\":\"19\",\"id\":\"6215\",\"name\":\"优智借\",\"openUrl\":\"iOnO4iMRaUKAh4Lo0B1vxT7PMa8qHutVmlXiA55C5nlOcMy+dHygQsvClsVWCAw6hBuQaaqTQHxqjFaR+oDXRTgb6foHRJKh6rizaFyhe/Y=\"},{\"index\":\"20\",\"id\":\"5838\",\"name\":\"猎豹贷款\",\"openUrl\":\"0+5gSRQklI52fTvH9OWkOSqgKL/WocokMIgv57K21/5j1D80dBNStUevjNO9aW57/LAf56bY/1y4kk/UJCqgEJWBN49flN5zzKrV/kDzLBI=\"}]",
                                 "deviceId": "24C64FCD-F36D-4E5B-B71F-C10F7ED7B445",
                                 "sourceEventParams": "{\"forClient\":\"qsj\",\"cfgId\":\"16\",\"batch\":\"\"}"}]}
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                  "Accept": "application/json, text/plain, */*"}
        self.result = requests.post(url=self.url, headers=header, params=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)
    @unittest.skip("pass")
    def test_batchInsertVisitInfoByQsj_ad(self):
        '''点击埋点'''
        self.params = {"productId": "1003",
                       "timeStr": "Tue Sep 03 2019 11:46:09 GMT+0800 (CST)",
                       "ostype": "2",
                       "accountId": "151635537517645909",
                       "channel": "MJBIOS008",
                       "appVersion": "1.1",
                       "mobileSystem": "2",
                       "source": "1003",
                       "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/query.html?cfgId=16&hsinaifNeedFullWin=2&token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                       "visitStartTime": "1567482369539",
                       "currentEventCode": "ad_小蓝卡",
                       "json": [{"productId": "1003", "timeStr": "Tue Sep 03 2019 11:46:09 GMT+0800 (CST)", "ostype": 2,
                                 "accountId": "151635537517645909", "channel": "MJBIOS008", "appVersion": "1.1",
                                 "mobileSystem": 2, "source": "1003",
                                 "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/query.html?cfgId=16&hsinaifNeedFullWin=2&token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                                 "visitStartTime": 1567482369539, "currentEventCode": "ad_小蓝卡",
                                 "currentEventParams": "{\"index\":\"30\",\"id\":\"6213\",\"openUrl\":\"lMT/0sMVkBOcal5OClUVPfY11PHWgziI3GOEsrdiUmYWz9rwBzmWXjQEbQ8JQtXRxlDjRTze+d0HFt+SOuCWzJ59vaPEFeOvaC77+B+Dt1M=\"}",
                                 "deviceId": "24C64FCD-F36D-4E5B-B71F-C10F7ED7B445",
                                 "sourceEventParams": "{\"forClient\":\"qsj\",\"cfgId\":\"16\",\"batch\":\"\"}"}]}
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                  "Accept": "application/json, text/plain, */*",
                  "Referer": "https: // jie.iask.cn / pg / product / qsjwebapp / index.html"}
        self.result = requests.post(url=self.url, headers=header, params=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)
    @unittest.skip("pass")
    def test_batchInsertVisitInfoByQsj_ym(self):
        '''页面曝光埋点'''
        self.params = {"productId": "1003",
                       "timeStr": "Tue Sep 03 2019 11:46:09 GMT+0800 (CST)",
                       "ostype": "2",
                       "accountId": "151635537517645909",
                       "channel": "MJBIOS008",
                       "appVersion": "1.1",
                       "mobileSystem": "2",
                       "source": "1003",
                       "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/watched.html?token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                       "visitStartTime": "1567482369539",
                       "currentEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/watched.html?token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                       "json": [{"productId": "1003", "timeStr": "Tue Sep 03 2019 11:55:23 GMT+0800 (CST)", "ostype": 2,
                                 "accountId": "151635537517645909", "channel": "MJBIOS008", "appVersion": "1.1",
                                 "mobileSystem": 2, "source": "1003",
                                 "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/watched.html?token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                                 "visitStartTime": 1567482923642,
                                 "currentEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/watched.html?token=947f5a82e812dc4cd1f4e2b1707f6322&channel=MJBIOS008&channelId=MJBIOS008&appVersion=1.1&deviceId=24C64FCD-F36D-4E5B-B71F-C10F7ED7B445&source=Q001&mjbname=dakalai&fromUserId=151635537517645909",
                                 "currentEventParams": "{\"starttime\":\"2019/9/3 11:55:23\",\"endtime\":\"2019/9/3 11:55:23\",\"times\":250}",
                                 "deviceId": "24C64FCD-F36D-4E5B-B71F-C10F7ED7B445",
                                 "sourceEventParams": "{\"forClient\":\"qsj\",\"cfgId\":\"\",\"batch\":\"\"}",
                                 "templateUrl": None}]}
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                  "Accept": "application/json, text/plain, */*"}
        self.result = requests.post(url=self.url, headers=header, params=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)


if __name__ == '__main__':
    unittest.main()
