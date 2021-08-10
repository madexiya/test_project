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
    @pytest.fixture(scope="session")
    def token(self):
        request_param = {
            "corpid": "ww6eb2aef1942224c8",
            "corpsecret": "dMLDXAViQsenU_1ljnX-YlQ6LNYcCqAEySHfcST9bCs"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_param)
        return r.json()['access_token']

    def get_token(self):
        request_param = {
            "corpid": "ww6eb2aef1942224c8",
            "corpsecret": "dMLDXAViQsenU_1ljnX-YlQ6LNYcCqAEySHfcST9bCs"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_param)
        return r.json()['access_token']

    def test_create(self, token, userid, mobile, name="奥特曼", department=None):
        # access_token = self.get_token()
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]}
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                          json=request_body)
        return r.json()

    def test_get(self, token, userid):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self, token, userid, name="奥特曼996"):
        request_body = {
            "userid": userid,
            "name": name,
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                          json=request_body)
        return r.json()

    def test_delete(self, token, userid):
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

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
