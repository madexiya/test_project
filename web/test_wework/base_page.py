from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_fuyong = Options()
            # 和浏览器打开的测试端口进行通信
            # 浏览器复用，例子：命令行输入chrome --remote-debugging-port=8888(端口号随便输)  开启调试模式
            chrome_fuyong.debugger_address = "127.0.0.1:8888"
            self._driver = webdriver.Chrome(options=chrome_fuyong)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
