import binascii
import json
from pyDes import des, CBC, PAD_PKCS5, ECB


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """

    secret_key = '2019052400183698'
    iv = secret_key
    k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = '2019052400183698'
    iv = secret_key
    k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

data = {"deviceId":"deviceId","thirdId":"thirdId","phone":"phone","mac":"mac","gps":"gps","city":"city","brand":"brand","channelId":"dyy_qeqd","outChannelId":"outChannelId","pkgChannelId":"pkgChannelId","productId":"1009","ver":"ver","verno":"1","deviceType":"1"}
bizdata = json.dumps(data)
str_en = des_encrypt(bizdata)
print(str_en)
str_de = des_descrypt(str_en)
print(str_de)