from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 设置窗口大小
driver.set_window_size(600, 600)

# 搜索
driver.find_element(By.ID, "kw").send_keys("selenium")
driver.find_element(By.ID, "su").submit()
sleep(3)

# 设置滚动条位置
driver.execute_script("window.scrollTo(100, 450);")
sleep(5)

driver.quit()
