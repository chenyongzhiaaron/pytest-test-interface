import pymongo as pm
"""
mongo里面表名备注
visitedInfoBean 轻松借
AdvanceVisitedInfoRecord 大王
easy_statistic+dt(线上库) statistics_dt(mongo正式库)

"""
class MongoDb:
    def __init__(self):
        pass

    def Mongo(self, tablename, dt):
        # Mongo从库配置
        # 获取连接
        client = pm.MongoClient(host="", port="")
        # 连接数据库(statistics为数据库名)
        db = client["easy_statistics"]
        # 获取集合对象表的名称（visitedInfoBean+日期（分区格式））
        my_table = db[tablename + dt]
        return my_table
