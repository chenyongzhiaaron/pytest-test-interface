import requests
from natsort import natsorted
import hashlib

# class Utils():
#     #   用于单一操作
#     def token(self):
#         headers1 = {'Accept': 'application/json', "Access-Token": ''}
#         url1 = DefTool.url(self, "api/auth/captcha?mobile=")
#         url2 = DefTool.url(self, 'api/auth/login')
#         re = requests.get(url=url1, headers=headers1).json()
#         number = test_db.T_DB.t_db(self)
#         payload = {"mobile": 17727475174, "verify_code": number}
#         response = requests.post(url=url2, data=payload, headers=headers1).json()
#         t = response['data']['access_token']
#         b = "bearer "
#         access_token = b + t
#         h = {
#             'Accept': 'application/json',
#             'Authorization': access_token,
#             "Access-Token": '17727475174'
#         }
#         print(h)
#         return h


class DefTool():
    def url(self, patch):
        baseUrl = 'https://k8s-qsj-test-jie.iask.cn'
        url = baseUrl + patch
        return url

    def defBaseParmsGetCode(self):
        headers = {
            "type": 2,
            "ver": "2.5.0",
            "verno": 13,
            "deviceId": "A0000087B98608",
            "deviceType": 1,
            "productId": 1003,
            "channelId": "anzhi",
            "deviceToken": "6418235f5d18aae5c7c6f1513f8c3839",
            "sign": "32f563c16c56a30694ff720b8e74a9c2"
        }
        return headers

    def defBaseParmsGetPassword(self):
            headers = {
                "ver": "2.5.0",
                "verno": 13,
                "deviceId": "A0000087B98608",
                "deviceType": 1,
                "productId": 1003,
                "channelId": "anzhi",
                "deviceToken": "6418235f5d18aae5c7c6f1513f8c3839",
                "sign": "32f563c16c56a30694ff720b8e74a9c2"
            }
            return headers

    def defaultHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Authorization": "bearer ",
            "Access-Token": '',
            'Accept-Language': "cn",
            # "Content encoding": 'UTF-8'
        }
        return headers

    def sign(self, **params):
        sortedList = []
        for key in params:
            try:
                sortedParms = str(key) + str(params[key])
                sortedList.append(sortedParms)
            except Exception as e:
                print(e)
        # print(sortedList)
        sort = natsorted(sortedList)
        argument = "a8235488a6aae009ff7e32430fee2f44"
        keysorted = argument + ("".join(sort))
        md = hashlib.md5()
        md.update(keysorted.encode(encoding='utf-8'))
        sign = md.hexdigest()
        # print(sign)
        return sign



