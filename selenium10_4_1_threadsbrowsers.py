from selenium import webdriver
from time import ctime, sleep
import threading
from selenium.webdriver.common.by import By


def browers_search(browername, keyword):
    print("启动时间：%s" % ctime())
    print("浏览器驱动：%s, 搜索关键词：%s" % (browername, keyword))
    if browername == 'Chrome':
        driver = webdriver.Chrome()
    elif browername == 'FireFox':
        driver = webdriver.Firefox()
    elif browername == 'IE':
        driver = webdriver.Ie()
    else:
        print("驱动有误，仅支持Chrome,FireFox,IE")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys(keyword)
    driver.find_element(By.ID, "su").click()
    sleep(3)
    driver.quit()


if __name__ == '__main__':
    dicts = {'Chrome': 'selenium', 'FireFox': 'unittest', 'IE': 'python'}
    threads = []
    for browername, keyword in dicts.items():
        t = threading.Thread(target=browers_search, args=(browername, keyword))
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()

    print("结束时间：%s" % ctime())
