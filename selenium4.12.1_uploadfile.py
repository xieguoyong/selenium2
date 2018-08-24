from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
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

# 输入文件url 并提交
file_path = r'C:\Users\xie.guoyong\Desktop\111.xls'
driver.find_element(By.XPATH, "//input[@class='ipt ng-untouched ng-pristine ng-valid']").send_keys(file_path)
sleep(5)
# 此处直接输入文件url后上传按钮置灰的无法实现上传，必须选择文件按钮才能点击
driver.find_element(By.XPATH, "//div[@class='button-search']").click()
sleep(5)

driver.quit()
