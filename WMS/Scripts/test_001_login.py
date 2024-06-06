# 登录接口测试
import logging

import allure
import pytest
import requests
from WMS.Utils.get_uuid import UUIDUtils
from WMS.Utils.get_yaml import YamlUtil
from WMS.Utils.get_path import get_yaml_path
from WMS.Utils.get_logger import LoggerUtil


@allure.feature("WMS仓管系统登录接口")
class TestLogin:

    @allure.description("登录接口测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize('params', YamlUtil.get_yaml(get_yaml_path("login_data.yaml")))
    def test_login(self, params):
        response2 = requests.post(url="http://192.168.10.128:9632/login",
                                  json={
                                      "username": params["username"],
                                      "password": params["password"],
                                      "code": params["code"],
                                      "uuid": UUIDUtils.get_uuid()
                                  }
                                  )
        if response2.json()["msg"] == params["msg"]:
            LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,参数是:{params}")
        else:
            LoggerUtil.logger.error(f"用例执行失败,结果是:{response2.json()["msg"]}")
            raise AssertionError("响应结果不在预期内!")
