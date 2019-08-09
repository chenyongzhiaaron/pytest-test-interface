import json

from natsort import natsorted
import hashlib

a = ['username18127813600', 'password8ff15b24341602becdf011679ec383c1', 'ver2.5.1', 'verno14',
     'deviceId868777047018746',
     'deviceType1', 'productId1003', 'channelIdcpjz002', 'deviceTokenc5967b66d97e626caa0bf8dc32c675ab',
     'mjbnamecjhj']
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