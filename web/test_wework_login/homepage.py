from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.test_wework_login.loginpage import LoginPage
from web.test_wework_login.registerpage import RegisterPage


class HomePage:
    def __init__(self):
        option = Options()
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        点击立即注册
        进入注册页po
        :return:
        """
        self.driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a').click()
        return RegisterPage(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入企业登录po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return LoginPage(self.driver)
