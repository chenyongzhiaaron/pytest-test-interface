# coding=utf-8

import pymysql.cursors
import os
import configparser as cparser
import pymysql.cursors

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


class T_DB():

    def t_db2(self):
        # 连接MySQL数据库
        connection = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句，并执行
        sqlCaptcha = "select idfa from t_spread_general_idfainfo where appid = 1467866510 order by infoid desc limit 1"  # 获取最新一条用户验证码
        cursor.execute(sqlCaptcha)
        # 查询单条数据 并将结果返回给 result
        result = cursor.fetchone()
        # 查询多条数据 并将结果返回给 result
        # result = cursor.fetchall()
        idfa = result['idfa']
        # 关闭数据连接
        connection.close()
        return str(idfa)

test = T_DB()
print(test.t_db2())
idfa = test.t_db2()
# print("api/user/address/" + str(address_id))
print(idfa)