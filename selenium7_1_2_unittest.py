from selenium7_1_2_jisuan import Count
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        print("start test_add!")

    def tearDown(self):
        print("end test_add!")


class Add(MyTest):
    def test_add1(self):
        summ = Count(2, 3)
        self.assertEqual(summ.add(), 5)

    def test_add2(self):
        summ = Count(5.1, 6)
        self.assertEqual(summ.add(), 10, msg="和不为10！")


class Sub(MyTest):
    def test_sub1(self):
        subb = Count(5, 3)
        self.assertEqual(subb.sub(), 2)

    def test_sub2(self):
        subb = Count(11, 10)
        self.assertEqual(subb.sub(), 2, msg="差不为2！")


if __name__ == '__main__':
    # unittest.main()

    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Add("test_add2"))
    suite.addTest(Add("test_add1"))
    suite.addTest(Sub("test_sub1"))
    suite.addTest(Sub("test_sub2"))
    # 运行
    runner = unittest.TextTestRunner()
    runner.run(suite)
