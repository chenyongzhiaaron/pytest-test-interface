# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger="Root"):#logger  为显示类名（默认为Root）
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG) #文件写入DEBUG级别及以上（可自行调整）

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H', time.localtime(time.time()))  #每小时一个文件
        log_path = os.path.dirname(os.getcwd()) + '/testOutput/log/'#保存地址
        log_path1 = './testOutput/log/'
        try:
            log_name = log_path + rq + '.log'
            fh = logging.FileHandler(log_name,encoding='utf-8',mode="a+")
        except:
            log_name = log_path1 + rq + '.log'
            fh = logging.FileHandler(log_name,encoding='utf-8',mode="a+")

        fh.setLevel(logging.INFO)
        fh.close()

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.close()

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        if not self.logger.handlers:
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def getlog(self):
        return self.logger