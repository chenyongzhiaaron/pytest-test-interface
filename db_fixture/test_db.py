# coding=utf-8

import pymysql.cursors
import os
import configparser as cparser
import pymysql.cursors
from Global_base import login

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


class T_DB:

    #  查询数据
    def t_db_select(self, sql, params):
        connection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          password=password,
                                          db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        sqlCaptcha = sql  # 编写sql
        try:
            cursor.execute(sqlCaptcha)
            # 查询单条数据 并将结果返回给 result
            result = cursor.fetchone()
            # 查询多条数据 并将结果返回给 result
            # result = cursor.fetchall()
            connection.commit()
        except:
            print("Error: unable to fecth data")
        values = result[params]
        # 关闭数据连接
        connection.close()
        return str(values)

    #   删除指定数据
    def t_db_delete(self, sql):
        connection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          password=password,
                                          db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        sqlCaptcha = sql  # 编写sql语句
        try:
            # 执行删除sql语句
            cursor.execute(sqlCaptcha)
            # 提交删除操作
            connection.commit()
        except:
            # 发生错误时回滚
            connection.rollback()
        # 关闭数据连接
        connection.close()
        return print("删除成功")

        #  更新数据
    def t_db_update(self, sql):
        connection = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        sqlCaptcha = sql  # 编写更新sql语句
        try:
            # 执行删除sql语句
            cursor.execute(sqlCaptcha)
            # 提交更新操作
            connection.commit()
        except:
            # 发生错误时回滚
            connection.rollback()
        # 关闭数据连接
        connection.close()
        return print("更新成功")



#
# test = T_DB()
# sql1 = "select idfa from t_spread_general_idfainfo where appid = 1467866510 order by infoid desc limit 1"
# idfa = test.t_db_select(sql1,"idfa")
# # print("api/user/address/" + str(address_id))
# print(idfa)

# value = login.LoginByPassWord()
# phone = 18127813602
# values = value.login_by_password(phone)
# accountId = values[0]
# test = T_DB()
# sqlDelete = ("DELETE FROM sinaif_easy.t_user_attendance WHERE accountid = {};".format(accountId))
# doSQL = test.t_db_delete(sqlDelete)