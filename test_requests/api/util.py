import requests


class Util:
    def get_token(self):
        request_param = {
            "corpid": "ww6eb2aef1942224c8",
            "corpsecret": "dMLDXAViQsenU_1ljnX-YlQ6LNYcCqAEySHfcST9bCs"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_param)
        return r.json()['access_token']
