import requests
import unittest
from Global_base import global_base
from parameterized import parameterized


class CheckUpdate(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.sinawallent.com/statistics/static/logs/batchInsertVisitInfoByQsj"

    def tearDown(self):
        print(self.result)
    @unittest.skip("pass")
    def test_batchInsertVisitInfo(self):
        '''监控埋点'''
        params = {"source": "monitor-h5",
                  "ostype": "ios",
                  "json": [{
                               "sourceEventCode": "https://jie.iask.cn/pg/product/qsjEncryp/index.html?num=15&channel=MJBIOS006&appVersion=1.0&deviceId=26F1ED6A-B927-461B-AEB2-203459A3CEFC&source=Q001&mjbname=sinaifeasy2303&timestamp=1565329571",
                               "channel": "show",
                               "mobileSystem": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                               "currentEventCode": "{\"pageTotalTime\":\"1.00\",\"ajaxTime\":\"0.23\",\"cssTime\":\"0.00\",\"jsTime\":\"0.00\"}",
                               "currentEventParams": "[{\"name\":\"https://jie.iask.cn/pg/product/static/js/all.js\",\"type\":\"script\",\"time\":\"0.00\"},{\"name\":\"https://assets.growingio.com/2.1/gio.js\",\"type\":\"script\",\"time\":\"0.00\"},{\"name\":\"https://jie.iask.cn/pg/product/qsjEncryp/static/css/index.302b0896fb545b68ef9392ceabd90018.css\",\"type\":\"link\",\"time\":\"0.00\"},{\"name\":\"https://jie.iask.cn/pg/product/qsjEncryp/static/js/manifest.0f0c5606887c704c47a2.js\",\"type\":\"script\",\"time\":\"0.00\"},{\"name\":\"https://jie.iask.cn/pg/product/qsjEncryp/static/js/vendor.6f82e3b4eece01216375.js\",\"type\":\"script\",\"time\":\"0.00\"},{\"name\":\"https://jie.iask.cn/pg/product/qsjEncryp/static/js/index.d0501bc2723cee0b72a7.js\",\"type\":\"script\",\"time\":\"0.00\"},{\"name\":\"https://jie.iask.cn/apilations/app/loan/getHomeProductListV3.do\",\"type\":\"xmlhttprequest\",\"time\":\"0.23\"},{\"name\":\"https://api.growingio.com/v2/a573d95da4e28930/web/pv?stm=1565329572388\",\"type\":\"xmlhttprequest\",\"time\":\"0.00\"}]",
                               "deviceId": "26F1ED6A-B927-461B-AEB2-203459A3CEFC"}]}
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], 200)



if __name__ == '__main__':
    unittest.main()
