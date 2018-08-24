from selenium7_1_2_jisuan import Count
import unittest


class Add(unittest.TestCase):
    def setUp(self):
        print("start test_add!")

    def test_add1(self):
        summ = Count(2, 3)
        self.assertEqual(summ.add(), 5)

    @unittest.skip("跳过")
    def test_add2(self):
        summ = Count(5.1, 6)
        self.assertEqual(summ.add(), 11, msg="和不为10！")

    def tearDown(self):
        print("end test_add!")


if __name__ == '__main__':
    unittest.main()
