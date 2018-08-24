from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://videojs.com/")
sleep(5)

video = driver.find_element(By.XPATH, "//body/section[1]/div/video")

# 返回播放地址
url = driver.execute_script("return arguments[0].currentSrc", video)
print("播放地址：", url)

# 点击播放
print("start..")
driver.find_element(By.XPATH, "//body/section[1]/div/button").click()

# 播放15秒
sleep(15)

# 暂停
print("stop")
driver.execute_script("return arguments[0].pause()", video)
sleep(3)

# 播放
print("again start..")
driver.execute_script("return arguments[0].play()", video)

# 再播放5秒
sleep(5)

driver.execute_script("return arguments[0].pause()", video)
sleep(3)

# 重新加载视频
print("reload video")
driver.execute_script("return arguments[0].load()", video)

sleep(3)
driver.quit()
