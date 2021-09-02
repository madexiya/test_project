from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.test_wework.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        """
        填写页面各种信息
        :return:
        """
        self.find(By.CSS_SELECTOR, "#username").send_keys("奥特曼打怪兽")
        self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("aoteman123")
        self.find(By.ID, "memberAdd_phone").send_keys("17699990000")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
