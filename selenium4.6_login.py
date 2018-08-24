from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa-doctor.dr-elephant.com/index")
sleep(3)

# 获取登录前的页面title、url
title = driver.title
print("登录前title:", title)
url = driver.current_url
print("登录前url:", url)

# 登录
driver.find_element(By.NAME, "username").send_keys('13916725407')
driver.find_element(By.ID, "pass").send_keys('725407')
driver.find_element(By.CLASS_NAME, "but").click()
sleep(10)

# 获取登录后的页面title、url
title_now = driver.title
print("登录后title:", title_now)
url_now = driver.current_url
print("登录后url:", url_now)

# 检测页面中userName元素是否存在文本“谢医生”。
# 这里设置了1秒检测时间，由于1秒内页面信息可能还没有返回“谢医生”，这里可能出现超时报错
# user = WebDriverWait(driver, 1, 0.5).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "userName"), "谢医生"))

user = driver.find_element(By.CLASS_NAME, "userName").text
print("登录的用户名：", user)

driver.quit()
