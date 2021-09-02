from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.test_wework_login.registerpage import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan_login(self):
        """
        扫码登录
        :return:
        """
        pass

    def goto_register(self):
        """
        点击企业注册
        进入注册页po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)
