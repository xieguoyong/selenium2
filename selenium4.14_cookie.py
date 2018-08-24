from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获取未登录前cookie
unlogin_cookie = driver.get_cookies()
print(unlogin_cookie)

# 登录百度
driver.find_element(By.LINK_TEXT, "登录").click()
driver.find_element(By.XPATH, "//p[@class='tang-pass-footerBarULogin pass-link']").click()
driver.find_element(By.ID, "TANGRAM__PSP_10__userName").send_keys("xieguoyong404@sina.com")
driver.find_element(By.ID, "TANGRAM__PSP_10__password").send_keys("xgy@@417")
# driver.find_element(By.XPATH, "//input[@class='pass-checkbox-input pass-checkbox-memberPass']").click()
driver.find_element(By.ID, "TANGRAM__PSP_10__submit").click()
sleep(2)

# 写入cookie
driver.add_cookie({"name": 'testname', "value": 'testvalue'})
# 获取登录后cookie
login_cookie = driver.get_cookies()
print(login_cookie)
# 打印出cookie中的name、value
for cookie in login_cookie:
    print("name:", cookie['name'], "->", "value:", cookie['value'])
