import requests
import unittest
from Global_base import global_base
from Global_base import phone_create
from parameterized import parameterized
from db_fixture import test_db
'''

class SendPhoneCode():

    def test_send_phone_code(self, phone):
        phone_new = phone
        pa = {"phone": str(phone_new), "type": "2", "verno": 15, "deviceId": "867910035562539", "ver": "2.6.0", "deviceType": "1",
              "productId": "1003", "channelId": "sinaif", "deviceToken": "ef70fb3178dccde19df9295a68aca0a3", "mjbname": "qsj"}
        value = global_base.DefTool.sign(self, **pa)
        sign = {"sign": value}
        params = dict(pa, **sign)
        result = requests.post(url=self.url, data=params).json()
        sql = "select smscode from sinaif_easy.t_app_smsinfo where mobile = 18888888888 order by sendtime desc limit 1"
        smscode = "smscode"
        smscode_new = test_db.T_DB.t_db2(sql, smscode)
        print(smscode_new)
        return smscode_new

if __name__ =="__main__":
    SendPhoneCode().test_send_phone_code(18888888888)



'''
