from selenium7_1_2_jisuan import Count
import unittest


class Sub(unittest.TestCase):
    def setUp(self):
        print("start test_sub!")

    def test_sub1(self):
        subb = Count(5, 3)
        self.assertEqual(subb.sub(), 2)

    def test_sub2(self):
        subb = Count(11, 10)
        self.assertEqual(subb.sub(), 1, msg="差不为2！")

    def tearDown(self):
        print("end test_sub!")


if __name__ == '__main__':
    unittest.main()
