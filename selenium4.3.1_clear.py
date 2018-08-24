from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

driver.find_element(By.ID, "kw").send_keys("Selenium2")
driver.find_element(By.ID, "su").click()
sleep(5)

# 清空输入框
driver.find_element(By.ID, "kw").clear()
sleep(3)
# 重新输入并搜索
driver.find_element(By.ID, "kw").send_keys("Python")
driver.find_element(By.ID, "su").click()
sleep(5)

# 关闭浏览器
driver.quit()