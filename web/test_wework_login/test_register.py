from web.test_wework_login.homepage import HomePage


class TestRegister:
    def setup(self):
        self.homepage = HomePage()

    def test_register(self):
        result = self.homepage.goto_register().register()
        assert result == True
