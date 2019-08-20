import requests
from Global_base import global_base, login
from db_fixture import test_db
import time


class SendPhoneCode():
    '''未登录发送短信验证码'''

    def send_phone_code(self, phone):
        url = global_base.DefTool.url(self, '/usercenter/sys/sendPhoneCode')
        pa = {"type": "2", "verno": 15, "deviceId": "867910035562539", "ver": "2.6.0", "deviceType": "1",
              "productId": "1003", "channelId": "sinaif", "deviceToken": "ef70fb3178dccde19df9295a68aca0a3",
              "mjbname": "qsj", "phone": phone}
        params = global_base.DefTool().payload(**pa)
        # time.sleep(5)
        result = requests.post(url=url, data=params).json()
        sql = 'SELECT mobile, smscode FROM sinaif_easy.t_app_smsinfo WHERE mobile= {} ORDER BY sendtime DESC LIMIT 0,1;'.format(
            phone)
        code = test_db.T_DB().t_db2(sql, "smscode")
        return code

    def send_phone_code_token(self, phone):
        url = global_base.DefTool.url(self, '/usercenter/sys/sendPhoneCode')
        pa_new = {"phone": phone, "type": "4", "verno": 15, "deviceId": "867910035562539", "ver": "2.6.0",
                  "deviceType": "1",
                  "productId": "1003", "channelId": "sinaif", "deviceToken": "ef70fb3178dccde19df9295a68aca0a3",
                  "mjbname": "qsj"}
        params = global_base.DefTool().payload(**pa_new)
        time.sleep(5)
        values = login.LoginByPassWord().login_by_password(phone)
        token = values[1]
        headers = {"token": token}
        time.sleep(5)
        send_code = requests.post(url=url, headers=headers, data=params).json()
        sql = 'SELECT mobile, smscode FROM sinaif_easy.t_app_smsinfo WHERE mobile= {} ORDER BY sendtime DESC LIMIT 0,1;'.format(
            phone)
        time.sleep(5)
        code = test_db.T_DB().t_db2(sql, "smscode")
        params = []
        params.append(token)
        params.append(code)
        return params

#
# if __name__ == "__main__":
#     # SendPhoneCode().send_phone_code(18888888888)
#     SendPhoneCode().send_phone_code_token(18999000000)
