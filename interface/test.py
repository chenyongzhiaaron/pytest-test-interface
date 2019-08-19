import json
from Global_base import global_base
from natsort import natsorted
import hashlib
from db_fixture import test_db
import paramiko

'''
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
'''


def sshAgent_execmd_multi(ip, username, password, cmds, port):
    '''
    :param ip: 目标主机的ip
    :param username: 目标主机登录用户名
    :param password: 用户名对应的密码
    :param cmds: 指令列表，list类型
    :param port: ssh连接端口
    :return: 返回获取的指令执行结果
    '''
    paramiko.util.log_to_file("paramiko.log")
    try:
        # 将列表cmds中的指令用';'连接成一个分号分隔的字符串
        excmd = ';'.join(cmds)
        # 建立ssh连接
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=ip, port=port, username=username, password=password)
        print(u'执行命令：', excmd)
        stdin, stdout, stderr = s.exec_command(excmd, timeout=24000)
        # stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        # 注意：执行的指令如果是reboot等没有返回输出结果的指令，则不需要读取stdout，执行完直接关闭连接；
        str = stdout.read(65533)
        strerror = stderr.read()
        if str != None:
            print(str)
            print(strerror)
        if stderr.read(65533) != None:
            print(stderr.read(65533))
            print(strerror)
        s.close()
        return str
    except Exception as e:
        print(e)

a = "cd home/deploy/logs/", ' grep "自动化排序出错" sinaif-easy-app.log'
ip = "192.168.1.182"
username = "deploy"
password = "0hXg0LBtcTGMA3jl"
cmds = ['pwd']
port = "22"
sshAgent_execmd_multi(ip, username, password, cmds, port)
