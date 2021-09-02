from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    """
    注册页PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入注册信息
        点击注册
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, "#corp_name").send_keys("奥特曼学院")
        return True
