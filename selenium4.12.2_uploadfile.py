from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qa-admin.dr-elephant.com/index")

# 登录
driver.find_element(By.XPATH, "//input[@class='rowinp ng-untouched ng-pristine ng-invalid']").send_keys("testadmin")
driver.find_element(By.XPATH, "//input[@class='rowinp ng-untouched ng-pristine ng-invalid']").send_keys("123456")
driver.find_element(By.XPATH, "//div[@class='cen cursor']/i").click()
sleep(15)
driver.find_element(By.CLASS_NAME, "but").click()
sleep(2)

# 打开商品发布页面
driver.get("https://qa-admin.dr-elephant.com/slide/productRelease")
sleep(5)

# 点击批量导出
driver.find_element(By.XPATH, "//div[@class='navcate']/button[3]").click()
sleep(2)

# 点击浏览，打开系统的文件选择窗口
driver.find_element(By.XPATH, "//div[@class='uploadzzimg2']").click()
sleep(2)
# 调用selenium4.12.2_uploadfile.exe上传文件
os.system("E:\PycharmProjects\selenium2\selenium4.12.2_uploadfile.exe")
sleep(3)
# 上传完文件后点击上传按钮完成上传
driver.find_element(By.XPATH, "//div[@class='button-search checked']").click()
sleep(5)

driver.quit()
