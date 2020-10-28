# 导包
import unittest
import time
import app
from scripts.test01_login import TestLogin
from scripts.test02_login import TestLogin02
from scripts.test03_login import TestLogin03
from tools.HTMLTestRunner import HTMLTestRunner

# 封装测试报告
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestLogin02))
suite.addTest(unittest.makeSuite(TestLogin03))

# 指定测试报告路径  # 按住ctrl键，点击strftime即可查看各个字符对应的意思
report = app.BASE_DIR + '/report/report-{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
# 文件流形式打开文件
with open(report, "wb") as f:
    # 创建HTMLTestRunner的运行器
    runner = HTMLTestRunner(f, title='登录接口测试报告')
    # 执行测试套件
    runner.run(suite)

