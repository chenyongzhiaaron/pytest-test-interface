# coding = utf-8
import requests
from natsort import natsorted
import hashlib
import os
import logging
import json
import configparser as cparser

from log import logger


# ======== Reading db_config.ini setting ===========


class DefTool:
    def url(self, patch):
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + "/url.ini"
        cf = cparser.ConfigParser()
        cf.read(file_path)
        # baseUrl = cf.get("urlTestconf", "url_test")
        # baseUrl = cf.get("urlPreconf", "url_pre")
        baseUrl = cf.get("urlProconf", "url_pro")
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

    def headers(self, token):
        header = {"token": token}
        return header


class RunMain:
    """"封装各类请求：get,post,put,deleter,options,head"""
    def __init__(self, method, url, params=None, header=None,  params_json=None):
        self.re = self.http_request(method, url, params, header, params_json)
    def http_request(self, method, url, params=None, header=None, params_json=None):
        result = None
        if method == "get":
            try:
                result = requests.get(url=url, params=params, headers=header, json=params_json)
                logging.info("action get")
            except Exception as e:
                logging.error("请求失败，→url→{}→参数→{}→header→{}".format(url, params, header))
        else:
            try:
                result = requests.post(url=url, data=params, headers=header, json=params_json)
                logging.info("action post")
            except Exception as e:
                logging.error("请求失败，→url→{}→参数→{}→header→{}".format(url, params, header))
        # return json.dumps(result.json(), indent=2, sort_keys=False, ensure_ascii=False)
        return result


if __name__ == "__main__":
    new_url = DefTool()
    url = new_url.url('/app/loan/getHomeProductListV3.do')
    print(url)
    test = RunMain("get", url)
    print(test.re)
