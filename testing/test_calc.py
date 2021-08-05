import pytest
# 测试文件
from pythoncode.calc import Calculator


class Test_calc:
    cal = Calculator()
    # 类级别，每个类里面前后分别执行setup_class和teardown_class
    # def setup_class(self):
    #     self.cal = Calculator()
    #     print("类级别的setup")
    #
    # def teardown_class(self):
    #     print("类级别的teardown")

    # 方法级别， 每条类里的测试用例前后分别执行setup和teardown
    # def setup(self):
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,result", [
        (1, 2, 3),
        (4, 5, 9),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2)
    ], ids=["int1", "int2", "bigint", "float", "fushu"])
    def test_add(self, a, b, result):
        # 通过self.cal调用类属性
        assert result == self.cal.add(a, b)

    # @pytest.mark.add
    # def test_add1(self):
    #     assert 5 == self.cal.add(2, 3)

    def test_sub(self, a, b, result):
        assert result == self.cal.sub(a, b)

    def test_mul(self, a, b, result):
        assert result == self.cal.mul(a, b)

    @pytest.mark.div
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)
