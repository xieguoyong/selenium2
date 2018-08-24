from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from time import ctime

"""
显示等待和隐式等待的区别：
1、显示等待的代码定义了等待条件，只有该条件触发，才执行后续代码，否则跳出Exception。
2、隐式等待是在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间。默认设置是0秒。
一旦设置了隐式等待时间，它的作用范围就是Webdriver对象实例的整个生命周期。
在使用隐式等待的时候，实际上浏览器会在设定的时间内不断的刷新页面去寻找我们需要的元素
3、显示等待针对指定的元素；隐式等待可以针对整个页面也可以这针对指定元素
"""


def xianshi():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    # 设置显示等待
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kww")))
    element.send_keys("selenium")

    driver.quit()


def yinshi():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 设置隐式等待
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")

    try:
        print(ctime())
        driver.find_element(By.ID, "kww").send_keys("selenium")
    except NoSuchElementException as e:
        print(e)
    finally:
        print(ctime())
        driver.quit()


yinshi()
xianshi()
