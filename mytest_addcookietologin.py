from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com")
# 添加Cookie
driver.add_cookie({'name': 'BAIDUID', 'value': '94249FEE3EA2F1A94770D236D424D2F9:SL=0:NR=10:FG=1'})
driver.add_cookie({'name': 'BDUSS', 'value': 'MzSUExTjgwWVBnY2p1a1BTaHhIaTFCbkNvMWNKTkpUY01FOXdaSG9-T25SNU5iQVFBQUFBJCQAAAAAAAAAAAEAAACS9So30PnUr-zh4L3gvQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKe6a1unumtbN0'})
driver.refresh()

# 获取登录用户名并打印
username = driver.find_element(By.CLASS_NAME, "user-name").text
print(username)

driver.quit()
