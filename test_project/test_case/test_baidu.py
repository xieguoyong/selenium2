from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from test_project.tools.log import Log


class BaiDu(unittest.TestCase):
    """百度搜索测试"""
    def setUp(self):
        t1 = time.time()
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.driver = webdriver.Chrome()
        self.logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format('success', 'Chrome', time.time() - t1))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = 'https://www.baidu.com'

    def test_search(self):
        """搜索关键词：unittest"""
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "kw").clear()
        self.driver.find_element(By.ID, "kw").send_keys("unittest")
        self.driver.find_element(By.ID, "su").submit()
        time.sleep(5)
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
