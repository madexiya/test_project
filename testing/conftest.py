import pytest
from pythoncode.calc import Calculator


# fixtrue 默认作用域scope=function
# autouse 为true自动在测试用例中使用fixture标记的方法 不用在测试用例中传入
@pytest.fixture()
def login(request):
    print("这是登录方法")
    # param 传入的参数，需要使用固定方式request.param来获取调用
    # print(request.param)
    # yield 暂停并记录上一次运行的位置
    yield ['username', 'password']
    print("teardown")


@pytest.fixture(autouse=True)
def setup():
    cal = Calculator()
    print("【开始计算】")
    yield
    print("【计算结束】")
