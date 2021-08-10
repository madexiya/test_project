import requests
from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util


class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()

    def test_create(self, userid, mobile, name="奥特曼", department=None):
        # access_token = self.get_token()
        if department is None:
            department = [1]
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": [1]}
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #                   json=request_body)
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]}
        }
        return self.send(data)
        # return r.json()

    def test_get(self, userid):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        return r.json()

    def test_update(self, userid, name="奥特曼996"):
        request_body = {
            "userid": userid,
            "name": name,
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
                          json=request_body)
        return r.json()

    def test_delete(self, userid):
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        return r.json()
