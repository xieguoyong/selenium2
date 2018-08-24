import unittest
from selenium7_1_2_testadd import Add
from selenium7_1_2_testsub import Sub
import os

# 构建测试集
# suite = unittest.TestSuite()
# suite.addTest(Add("test_add2"))
# suite.addTest(Add("test_add1"))
# suite.addTest(Sub("test_sub1"))
# suite.addTest(Sub("test_sub2"))
# 定义测试目录为当前目录
test_dir = os.path.dirname(__file__)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='selenium7_1_2_test*.py')
print(discover)

if __name__ == '__main__':
    # 运行
    runner = unittest.TextTestRunner()
    runner.run(discover)
