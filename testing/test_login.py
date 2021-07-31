import pytest


# 用例执行前，先执行login方法
def test_case1(login):
    print("测试用例1")


def test_case2():
    print("测试用例2")


# 参数化结合fixture使用
# indirect=True时，可以将fixture装饰的login方法在parametrize中传入
# 使用多个parametrize 参数取笛卡尔积
@pytest.mark.parametrize('login', [
    ('username1', 'password1'),
    ('username2', 'password2')
], indirect=True)
def test_case3(login):
    print("测试用例3")
