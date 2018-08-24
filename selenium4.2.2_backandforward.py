from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(5)

print("打开新闻页面")
driver.find_element(By.NAME, "tj_trnews").click()
time.sleep(5)

print("后退到百度首页")
driver.back()
time.sleep(5)

print("前进到新闻页面")
driver.forward()
time.sleep(5)

driver.quit()