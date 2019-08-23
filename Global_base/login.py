import requests
from Global_base import global_base
import time


class LoginByPassWord():
    def login_by_password(self, username):
        url = global_base.DefTool.url(self, '/usercenter/sys/loginByPass')
        pa = {"ver": "2.6.0", "password": "8ff15b24341602becdf011679ec383c1",
              "verno": 15, "deviceId": "867910035562539", "deviceType": 1, "productId": 1003,
              "channelId": "sinaif", "deviceToken": "ef70fb3178dccde19df9295a68aca0a3", "mjbname": "qsj",
              "username": username}
        param = global_base.DefTool.payload(self, **pa)
        result = requests.post(url=url, data=param).json()
        time.sleep(1)
        try:
            if result['code'] == 200:
                accountid = result['data']['accountid']
                token = result['token']
                datas = [accountid, token]
        except Exception as e:
            print(e)
        return datas


if __name__ == '__main__':
    a = LoginByPassWord().login_by_password(18999000000)
    print(a)
