from selenium import webdriver
import time

driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()

driver.get("https://www.baidu.com/")

# 通过id定位
# driver.find_element_by_id('kw').send_keys('Selenium2')
# 通过xpath定位
# //表示当前页面某个目录下
# driver.find_element_by_xpath("//input[@name='wd']").send_keys('Selenium2')
# 如果没有唯一标识的属性，可以通过上下级来定位
# driver.find_element_by_xpath("//span[@class='bg s_ipt_wr iptfocus quickdelete-wrap']/input").send_keys('Selenium2')
# 通过and连接多个属性来定位
driver.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('Selenium2')
# driver.find_element_by_id('su').submit()
driver.find_element_by_id('su').click()
time.sleep(5)
driver.quit()
