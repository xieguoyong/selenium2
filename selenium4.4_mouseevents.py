from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

# 定位要右键操作的元素，然后执行右键操作
right_click = driver.find_element(By.NAME, "tj_trnews")
ActionChains(driver).context_click(right_click).perform()
sleep(5)

# 点击空白处
driver.find_element(By.CLASS_NAME, "s_form").click()
sleep(5)

# 定位要鼠标悬停的元素，然后执行鼠标悬停操作
above = driver.find_element(By.NAME, "tj_briicon")
ActionChains(driver).move_to_element(above).perform()
sleep(5)

# 定位要双击的元素，然后执行双击操作
double_click = driver.find_element(By.ID, "su")
ActionChains(driver).double_click(double_click).perform()
sleep(5)

# 定位要拖动的元素，然后执行拖动操作
# 源元素
element = driver.find_element(By.NAME, "tj_trtieba")
# 目标元素
target = driver.find_element(By.ID, "kw")
ActionChains(driver).drag_and_drop(element, target).perform()
sleep(5)
driver.find_element(By.ID, "su").click()
sleep(5)

driver.quit()
