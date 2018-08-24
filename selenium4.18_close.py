from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获取百度搜索窗口句柄
searchwindow_handle = driver.current_window_handle

# 点击打开注册页面
driver.find_element(By.LINK_TEXT, "登录").click()
driver.find_element(By.LINK_TEXT, "立即注册").click()

# 获取当前所有打开窗口的句柄
all_handles = driver.window_handles

# 进入注册页面 而后关闭
for handle in all_handles:
    if searchwindow_handle != handle:
        driver.switch_to.window(handle)
        print("now register window~")
        driver.find_element(By.NAME, "userName").send_keys("test")
        driver.find_element(By.NAME, "phone").send_keys("15221739591")
        sleep(3)
        # 关闭该窗口
        driver.close()

for handle in all_handles:
    if searchwindow_handle == handle:
        driver.switch_to.window(handle)
        driver.find_element(By.ID, "kw").send_keys("Selenium2")
        driver.find_element(By.ID, "su").submit()
        sleep(5)

driver.quit()
