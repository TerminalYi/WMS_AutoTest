import requests

from WMS.Utils.get_uuid import UUIDUtils


# 固定测试账号admin的token 有问题，可能账号还有个特定的yaml文件存储用户名密码，参数化拉取
class TokenUtil:

    @classmethod
    def get_token(cls):
        response = requests.post(url="http://192.168.10.128:9632/login",
                                 json={
                                     "username": "admin",
                                     "password": "e10adc3949ba59abbe56e057f20f883e",
                                     "code": "2",
                                     "uuid": UUIDUtils.get_uuid()
                                 }
                                 )
        return "Bearer " + response.json()["token"]

