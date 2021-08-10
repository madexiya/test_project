import random
import re
import pytest
import requests


def test_create_data():
    """
    生成测试数据 userid name mobile
    :return:
    """
    data = [("aoteman" + str(x),
             "奥特曼",
             "138%08d" % x) for x in range(10)]
    return data


class TestWework:

    @pytest.mark.parametrize("userid,name,mobile", test_create_data())
    def test_wework(self, token, userid, name, mobile):
        # 整体测试
        # userid = "aoteman"
        # name = "奥特曼"
        # mobile = "17603060001"
        try:
            assert "created" == self.test_create(token, userid, mobile, name)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                # 正则获取存在的userid
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                self.test_create(token, userid, mobile, name)
        assert name == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid)["errmsg"]
        assert "奥特曼996" == self.test_get(token, userid)["name"]
        assert "deleted" == self.test_delete(token, userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]
