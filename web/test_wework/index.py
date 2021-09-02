from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.test_wework.add_member import AddMember
from web.test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        进入添加成员页面
        :return:
        """
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        return AddMember(self._driver)

    def import_adress(self):
        """
        导入通讯录
        :return:
        """
        pass
