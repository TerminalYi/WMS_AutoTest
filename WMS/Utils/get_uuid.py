import requests


# 获取登录页图片验证码uuid
class UUIDUtils:

    @classmethod
    def get_uuid(cls):
        return requests.get(url="http://192.168.10.128:9632/captchaImage").json()["uuid"]
