from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 光标悬停在设置上
shezhi = driver.find_element(By.LINK_TEXT, "设置")
ActionChains(driver).move_to_element(shezhi).perform()
# 打开搜索设置
driver.find_element(By.LINK_TEXT, "搜索设置").click()
time.sleep(3)
# 点击保存设置  (这里一直出现元素找不到，因为元素还未加载出来就去获取了。在上一步加上time.sleep(3）就可以了)
# save = driver.find_element(By.CLASS_NAME, "prefpanelgo")
# ActionChains(driver).click(save).perform()
driver.find_element(By.CLASS_NAME, "prefpanelgo").click()
time.sleep(3)

# 获取提醒信息
# print("提醒信息：", driver.switch_to_alert().text)
# driver.switch_to_alert().accept()
print("提醒信息：", driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.quit()
