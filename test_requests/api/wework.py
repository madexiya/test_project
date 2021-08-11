import requests
from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util
import yaml


class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token

    def test_create(self, userid, mobile, name="奥特曼", department=None):
        # access_token = self.get_token()
        if department is None:
            department = "1"
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": [1]}
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #                   json=request_body)
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department}
        # }
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        with open("../api/wework.yaml", encoding="utf-8") as f:
            data = yaml.load(f)
        return self.send(data["create"])
        # return r.json()

    def test_get(self, userid):
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        }
        return self.send(data)
        # return r.json()

    def test_update(self, userid, name="奥特曼996"):
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                   json=request_body)
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json": {
                "userid": userid,
                "name": name,
            }
        }
        return self.send(data)

    def test_delete(self, userid):
        # r = requests.get(
        #     f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        }
        return self.send(data)
