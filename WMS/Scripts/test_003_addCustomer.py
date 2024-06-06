import allure
import pytest
import requests

from WMS.Utils.get_mysql import DBUtil
from WMS.Utils.get_token import TokenUtil
from WMS.Utils.get_yaml import YamlUtil
from WMS.Utils.get_path import get_yaml_path
from WMS.Utils.get_logger import LoggerUtil


@allure.feature("WMS仓管系统用户新增接口")
class TestAddCustomer:
    def setup_method(self):
        # 每次执行一条测试用例前打开连接,建立游标
        self.conn = DBUtil.get_conn()
        self.cursor = DBUtil.get_cursor(self.conn)

    def teardown_method(self):
        # 每次执行一条测试用例后关闭连接,关闭游标
        DBUtil.quit_all(self.cursor, self.conn)

    @allure.description("用户新增接口测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize("params", YamlUtil.get_yaml(get_yaml_path("add_customer_data.yaml")))
    def test_add_customer(self, params):
        resp = requests.post(url="http://192.168.10.128:9632/wms/customer",
                             json={
                                 "customerNo": params["customerNo"],
                                 "customerName": params["customerName"],
                                 "address": params["address"],
                                 "mobile": params["mobile"],
                                 "tel": params["tel"],
                                 "customerPerson": params["customerPerson"],
                                 "customerLevel": params["customerLevel"],
                                 "email": params["email"],
                                 "remark": params["remark"],
                                 "bankAccount": params["bankAccount"],
                                 "bankName": params["bankName"]
                             },
                             headers={"Authorization": TokenUtil.get_token()})
        res = resp.json()
        # 插入成功 返回1/符合预期
        if isinstance(res, int):
            if res == params["expect"]:
                sql_01 = f"select * from wms_customer where customer_no = '{params['customerNo']}'"
                self.cursor.execute(sql_01)
                if self.cursor.rowcount != 0:
                    LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
                    sql_02 = f"delete from wms_customer where customer_no = '{params["customerNo"]}'"
                    self.cursor.execute(sql_02)
                    self.conn.commit()
                    # 删除成功代表测试成功
                    assert self.cursor.rowcount != 0
        # 插入成功 bug 返回1不符合预期情况
            elif res != params["expect"]:
                sql_03 = f"select * from wms_customer where customer_no = '{params['customerNo']}'"
                self.cursor.execute(sql_03)
                # 如果能查到数据代表有问题
                if self.cursor.rowcount != 0:
                    LoggerUtil.logger.error(f"接口响应不符合预期,用例执行失败!查询提交参数是:{params}")
                    sql_04 = f"delete from wms_customer where customer_no = '{params["customerNo"]}'"
                    self.cursor.execute(sql_04)
                    self.conn.commit()
                    raise AssertionError("插入数据接口出现BUG!")
        # 插入失败的情况 返回字典类型,且code键为500 / 符合预期
        elif isinstance(res, dict):
            if res["code"] == params["expect"]:
                LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            else:
                pass
        else:
            pass

