from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Page(object):
    login_url = "https://qa-patient.dr-elephant.com/index"

    def __init__(self, selenium_driver, url=login_url):
        self.driver = selenium_driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def page_element(self, *loc):
        return self.driver.find_element(*loc)


class PageLogin(Page):
    username_doc = (By.NAME, "username")
    password_doc = (By.ID, "pass")
    login_click = (By.XPATH, "//input[@class='but']")

    # 操作
    def element_username(self, username):
        return self.page_element(*self.username_doc).send_keys(username)

    def element_password(self, password):
        return self.page_element(*self.password_doc).send_keys(password)

    def element_login(self):
        return self.page_element(*self.login_click).submit()


# 组合单个的操作
def user_login(driver, username, password):
    page_login = PageLogin(driver)
    page_login.open()
    page_login.element_username(username)
    page_login.element_password(password)
    page_login.element_login()


def main():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        # 输入用户名密码登录
        username = '12200000000'
        password = '123456'
        user_login(driver, username, password)
        sleep(5)
        user = driver.find_element(By.XPATH, "//p[@class='userName']").text
        assert(user == '患者'), "用户名不对，登录失败！"
    finally:
        driver.quit()


if __name__ == '__main__':
    main()



