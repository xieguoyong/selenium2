from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

driver.find_element(By.ID, "kw").send_keys("selenium")
driver.find_element(By.ID, "su").submit()
sleep(3)

# 截图并保存
file_path = "E:\PycharmProjects\selenium2\selenium4.17_getscreenshot.png"
driver.get_screenshot_as_file(file_path)

sleep(2)
driver.quit()
