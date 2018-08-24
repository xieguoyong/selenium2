from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from test_project.tools.log import Log


class YouDao(unittest.TestCase):
    """有道翻译测试"""
    def setUp(self):
        t1 = time.time()
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.driver = webdriver.Chrome()
        self.logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format('success', 'Chrome', time.time() - t1))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = 'https://www.youdao.com/'

    def test_translate(self):
        """翻译关键词：自动化"""
        self.driver.get(self.url)
        self.driver.find_element(By.NAME, "q").clear()
        self.driver.find_element(By.NAME, "q").send_keys("自动化")
        self.driver.find_element(By.XPATH, "//form[@id='form']/button").click()
        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title, "【自动化】英语怎么说_在线翻译_有道词典")

    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
