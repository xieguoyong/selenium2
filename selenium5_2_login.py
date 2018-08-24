from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://qa-patient.dr-elephant.com/index")

    # 登录
    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        # self.driver.find_element(By.XPATH, "//div[@class='pointer']/i").click()
        self.driver.find_element(By.XPATH, "//input[@class='but']").submit()
        sleep(5)

    # 退出登录
    def logout(self):
        self.driver.find_element(By.XPATH, "//a[@class='powerSupply fr']").click()
        sleep(3)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
