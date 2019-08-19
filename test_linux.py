import paramiko
class cmd():
    def sshAgent_exeNcmd(self,ipu,username,password,cmds,port):
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
            for excmd in cmds:
                s = paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                s.connect(hostname=ipu, port=port, username=username, password=password)
                print(u'执行命令：',excmd)
                stdin, stdout, stderr = s.exec_command(excmd,timeout=240)
                stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
                #注意：执行的指令如果是reboot等没有返回输出结果的指令，则不需要读取stdout，执行完直接关闭连接；
                str = stdout.read(65533)
                if str !=None:
                    print(str)
                if stderr.read(65533) != None:
                    print(stderr.read(65533))
                s.close()
                return str
        except Exception as e:
            print(e)


ip = "192.168.1.182"
username = "deploy"
password = "0hXg0LBtcTGMA3jl"
cmds = ['pwd']
port = "22"

cmdss=cmd()
print(cmdss.sshAgent_exeNcmd(ip,username,password,cmds,port))