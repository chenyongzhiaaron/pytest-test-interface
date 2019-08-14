import json
from Global_base import global_base
from natsort import natsorted
import hashlib
from db_fixture import test_db

a = ["productId1003",
"channelIdcpjz001",
'strJson[{"city":"深圳市","content":"广东省深圳市南山区高新南六道靠近朗科大厦","longitude":"113.952595","areacode":"440305","latitude":"22.535389","locationtime":"2019-08-08 13:50:27","type":"0"}]',
"timestamp1565243427",
"deviceToken16c5ffdb6bef1d962c7dd7d6d9e72db0",
"deviceIdE9E6504B-CC17-4FEE-901A-643DDEE5F4BA",
"sourceQ001",
"deviceType2",
"mjbnamesinaifeasy",
"ver2.5.2",
"verno12"]

b = natsorted(a)
print(b)
print("".join(b))
sign = "a8235488a6aae009ff7e32430fee2f44"

print(sign + "".join(b))
sign_sort = sign + "".join(b)
md = hashlib.md5()
md.update(sign_sort.encode(encoding='utf-8'))
sign_new = md.hexdigest()
print('MD5加密前：' + sign_sort)
print('MD5加密后：' + sign_new)

params = {"phone": "18888888888",
"type": "2",
"verno": "15",
"deviceId": "867910035562539",
"ver": "2.6.0",
"deviceType": "1",
"productId": "1003",
"channelId": "sinaif",
"deviceToken": "ef70fb3178dccde19df9295a68aca0a3",
"mjbname": "qsj"}

si = global_base.DefTool.sign(params)
print(si)


sql = "select smscode from sinaif_easy.t_app_smsinfo where mobile = 18888888888 order by sendtime desc limit 1"
smscode = "smscode"
smscode_new = test_db.T_DB.t_db2( sql, smscode)
print(smscode_new)