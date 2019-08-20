import requests
from natsort import natsorted
import hashlib


class DefTool():
    def url(self, patch):
        baseUrl = 'https://k8s-qsj-test-jie.iask.cn'
        url = baseUrl + patch
        return url

    def payload(self, **params):
        sortedList = []
        for key in params:
            try:
                sortedParms = str(key) + str(params[key])
                sortedList.append(sortedParms)
            except Exception as e:
                print(e)
        sort = natsorted(sortedList)
        argument = "a8235488a6aae009ff7e32430fee2f44"
        keysorted = argument + ("".join(sort))
        md = hashlib.md5()
        md.update(keysorted.encode(encoding='utf-8'))
        sign_old = md.hexdigest()
        sign = {"sign": sign_old}
        payload = dict(params, **sign)
        return payload



