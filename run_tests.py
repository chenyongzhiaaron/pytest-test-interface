import sys, os
import time
import unittest
import logging
from HTMLTestRunner import HTMLTestRunner

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from parameterized import parameterized

sys.path.append('./interface/')
sys.path.append('./db_fixture')
sys.path.append('./Global_bse')
sys.path.append('./report')

# 指定测试用例为当前文件夹下的 interface 目录
# test_dir = 'F:\/auto\qsjInterface\interface\'
test_dir = "F:\/QSJ/interface/"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

if __name__ == "__main__":
    # test_data.init_data()  # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = "F:\/QSJ/report/" + now + '_result.html'
    # filename = "./report/" + now + '_TestReportResult.html'
    filename = "F:\/QSJ/report/" + 'TestReport.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='APP&信息流&路由&导流接口预发布环境接口测试报告',
                            description='Implementation Example with: APP&信息流&路由&导流接口预发布环境接口测试报告')
    logging.info("------------自动化测试 action ---------------")
    runner.run(discover)
    logging.info("------------自动化测试 end ---------------")
    fp.close()
