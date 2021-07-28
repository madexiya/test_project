import pytest
# 测试文件
from pythoncode.calc import Calculator


class Test_calc:
    def setup_class(self):
        self.cal = Calculator()
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    @pytest.mark.add
    def test_add(self):
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.add
    def test_add1(self):
        assert 7 == self.cal.add(3, 4)

    @pytest.mark.div
    def test_div(self):
        assert 1 == self.cal.div(1, 1)
