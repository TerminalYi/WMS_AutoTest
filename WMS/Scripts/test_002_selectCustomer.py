# 登录接口测试
import os
import subprocess

import allure
import pytest
import requests
from WMS.Utils.get_yaml import YamlUtil
from WMS.Utils.get_path import get_yaml_path
from WMS.Utils.get_logger import LoggerUtil
from WMS.Utils.get_token import TokenUtil
from WMS.Utils.get_mysql import DBUtil

# 初始化日志


@allure.feature("WMS仓管系统用户查询接口")
class TestSelectCustomer:
    def setup_method(self):
        # 每次执行一条测试用例前打开连接,建立游标
        self.conn = DBUtil.get_conn()
        self.cursor = DBUtil.get_cursor(self.conn)

    def teardown_method(self):
        # 每次执行一条测试用例后关闭连接,关闭游标
        DBUtil.quit_all(self.cursor, self.conn)

    @allure.description("用户查询接口接口测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize('params', YamlUtil.get_yaml(get_yaml_path("select_customer_data.yaml")))
    def test_select_customer(self, params):
        response2 = requests.post(url="http://192.168.10.128:9632/wms/customer/list?page=0&size=10",
                                  json={
                                      "customerNo": params["customerNo"],
                                      "customerName": params["customerName"],
                                      "address": params["address"],
                                      "mobile": params["mobile"],
                                      "tel": params["tel"],
                                      "customerPerson": params["customerPerson"],
                                      "customerLevel": params["customerLevel"],
                                      "email": params["email"]
                                  },
                                  headers={"Authorization": TokenUtil.get_token()}
                                  )
        # 通过对每一条用例的所有查询结果的content键的值进行循环,可以判断前端给的数据是通过哪种方式查询
        for i in response2.json()["content"]:
            # 如果遍历的每条结果的customerNo都跟前端传入的数据的值一样,那么就证明用户通过customerNo查询
            if i["customerNo"] == params["customerNo"]:
                # 通过查询结果中的id字段<主键>的值去数据库查询只会获得唯一一条数据,看返回数据的编号是不是结果的编号,验证数据准确性
                sql = f"select customer_no from wms_customer where id = {i["id"]}"
                self.cursor.execute(sql)  # 执行sql 这个东西有返回值 返回值是响应行数 逆天!
                # 看接口响应结果的编号和数据库返回的编号是否一致,验证数据准确性
                assert self.cursor.fetchone()[0] == i["customerNo"]
                LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            elif i["customerName"] == params["customerName"]:
                LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            elif i["customerLevel"] == params["customerLevel"]:
                # 通过查询结果中的id字段<主键>的值去数据库查询只会获得唯一一条数据,看返回数据的等级是不是结果的等级,验证数据准确性
                sql = f"select customer_level from wms_customer where id = {i["id"]}"
                self.cursor.execute(sql)  # 执行sql 这个东西有返回值 返回值是响应行数 逆天!
                # 看接口响应结果的编号和数据库返回的编号是否一致,验证数据准确性
                assert self.cursor.fetchone()[0] == i["customerLevel"]
                LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            elif i["customerPerson"] == params["customerPerson"]:
                # 通过查询结果中的id字段<主键>的值去数据库查询只会获得唯一一条数据,看返回数据的联系人是不是结果的联系人,验证数据准确性
                sql = f"select customer_person from wms_customer where id = {i["id"]}"
                self.cursor.execute(sql)  # 执行sql 这个东西有返回值 返回值是响应行数 逆天!
                # 看接口响应结果的编号和数据库返回的编号是否一致,验证数据准确性
                assert self.cursor.fetchone()[0] == i["customerPerson"]
                LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            else:
                LoggerUtil.logger.error(f"接口响应失败!不符合预期,查询提交参数是:{params}")
                raise AssertionError("响应结果不在预期内!")
