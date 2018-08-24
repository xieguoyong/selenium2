from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

# 输入框输入内容
driver.find_element(By.ID, "kw").send_keys("Selenium2")
sleep(3)

# 删除输入框中Selenium2中的2
driver.find_element(By.ID, "kw").send_keys(Keys.BACK_SPACE)
sleep(3)

# 输入空格+教程
driver.find_element(By.ID, "kw").send_keys(Keys.SPACE)
driver.find_element(By.ID, "kw").send_keys("教程")
sleep(3)

# 全选输入框内容
driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'a')
sleep(3)

# 剪切输入框内容
driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'x')
sleep(3)

# 粘贴内容
driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'v')
sleep(3)

# 通过回车代替click操作
driver.find_element(By.ID, "su").send_keys(Keys.ENTER)
sleep(3)

driver.quit()