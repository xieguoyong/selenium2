from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(5)

# 打开贴吧页面
driver.find_element(By.LINK_TEXT, "贴吧").click()
sleep(5)

# 刷新页面
driver.refresh()
sleep(5)

# 关闭浏览器
driver.quit()
