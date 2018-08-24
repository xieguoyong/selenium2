import unittest
import os
from test_project.tools.HTMLTestRunner import HTMLTestRunner
from test_project.tools.send_email import SendMail
import time

case_url = os.path.join(os.path.dirname(__file__), 'test_case')
discover = unittest.defaultTestLoader.discover(case_url, pattern="test_*.py")

if __name__ == '__main__':
    report_dir = os.path.join(os.path.dirname(__file__), 'report')
    report_name = os.path.join('result' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.html')
    report_path = os.path.join(report_dir, report_name)
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title="自动化测试用例", description="用例执行情况")
    runner.run(discover)
    fp.close()
    # 发邮件
    send = SendMail()
    send.send_mail(report_path)
