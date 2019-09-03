# -*- coding: utf-8 -*-
# Author Mr.xu
from ftplib import FTP
import datetime
import paramiko

hostip = '192.168.18.111'
user = 'root'
passwd = 'root'


def run():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostip, 22, user, passwd)
        stdin, stdout, stderr = ssh.exec_command('df -h')
        result = stdout.readlines()
        for i in result:
            print(i)
        ssh.close()
    except Exception as e:
        print("\tError %s\n" % e)


run()
