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
    def t_db2(self, sql,params):
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
        sqlCaptcha = sql  # 获取最新一条用户sql语句
        cursor.execute(sqlCaptcha)
        # 查询单条数据 并将结果返回给 result
        result = cursor.fetchone()
        # 查询多条数据 并将结果返回给 result
        # result = cursor.fetchall()
        # idfa = result[0]['idfa']
        value = result[params]
        # 关闭数据连接
        connection.close()
        return str(value)

test = T_DB()
sql1 = "select idfa from t_spread_general_idfainfo where appid = 1467866510 order by infoid desc limit 1"
idfa = test.t_db2(sql1,"idfa")
# print("api/user/address/" + str(address_id))
print(idfa)
