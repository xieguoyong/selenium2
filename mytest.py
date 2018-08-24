from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa-admin.dr-elephant.com/index")

driver.find_element(By.XPATH, "//input[@class='rowinp ng-untouched ng-pristine ng-invalid']").send_keys("superadmin1001")
driver.find_element(By.XPATH, "//input[@class='rowinp ng-untouched ng-pristine ng-invalid']").send_keys("doctor123")
driver.find_element(By.XPATH, "//div[@class='cen cursor']/i").click()
sleep(15)
driver.find_element(By.CLASS_NAME, "but").click()
sleep(2)


driver.get("https://qa-admin.dr-elephant.com/slide/doctorAuthority/doctorList")
driver.find_element(By.CLASS_NAME, "active").click()
contents = driver.find_elements(By.XPATH, "//div[@class='radio iconfont']")
discontents = driver.find_elements(By.XPATH, "//div[@class='radio iconfont radioCheck']")
contents[0].click()
discontents[0].click()


