from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

size = driver.find_element(By.ID, "kw").size
print("输入框size: %s" % size)
text = driver.find_element(By.ID, "jgwab").text
print("按钮text: %s" % text)
attribute = driver.find_element(By.ID, "su").get_attribute("type")
print("按钮的属性： %s" % attribute)
result = driver.find_element(By.ID, "kw").is_displayed()
print("输入框结果是否可见： %s" % result)

driver.quit()