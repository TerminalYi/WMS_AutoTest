import allure
import pytest
import requests

from WMS.Utils.get_mysql import DBUtil
from WMS.Utils.get_token import TokenUtil
from WMS.Utils.get_yaml import YamlUtil
from WMS.Utils.get_path import get_yaml_path
from WMS.Utils.get_logger import LoggerUtil

supplierNo = "ximenzi"
supplierName = "西门子"
bankName = "南京银行"
bankAccount = "65432111223344"
address = "南京市"
mobileNo = "13895710050"
telNo = "88848885"
contact = "13946167038"
level = "第二级"
email = "sty1260205627@gmail.com"
remark = "测试数据1"


@allure.feature("WMS仓管系统供应商修改接口")
class TestUpdateCustomer:

    def setup_method(self):
        # 每次执行一条测试用例前打开连接,建立游标
        self.conn = DBUtil.get_conn()
        self.cursor = DBUtil.get_cursor(self.conn)

    def teardown_method(self):
        # 每次执行一条测试用例后关闭连接,关闭游标
        DBUtil.quit_all(self.cursor, self.conn)

    @pytest.mark.parametrize("params", YamlUtil.get_yaml(get_yaml_path("update_supplier_data.yaml")))
    def test_update_customer(self, params):
        resp = requests.put(url="http://192.168.10.128:9632/wms/supplier",
                            json={
                                "id": params["id"],
                                "supplierNo": params["supplierNo"],
                                "supplierName": params["supplierName"],
                                "bankName": params["bankName"],
                                "bankAccount": params["bankAccount"],
                                "address": params["address"],
                                "mobileNo": params["mobileNo"],
                                "telNo": params["telNo"],
                                "contact": params["contact"],
                                "level": params["level"],
                                "email": params["email"],
                                "remark": params["remark"],
                                "delFlag": params["delFlag"]
                            },
                            headers={
                                "Authorization": TokenUtil.get_token()
                            }
                            )
        print(resp.json())
        res = resp.json()
        if isinstance(res, int):
            assert res == params["expect"]
            LoggerUtil.logger.info(f"接口响应符合预期,用例执行成功,查询提交参数是:{params}")
            sql = f"update wms_supplier set supplier_no ='{supplierNo}',supplier_name ='{supplierName}',bank_name='{bankName}',bank_account='{bankAccount}',address='{address}',mobile_no='{mobileNo}',tel_no='{telNo}',contact='{contact}',level='{level}',email='{email}',remark='{remark}' where id={params["id"]}"
            self.cursor.execute(sql)
            self.conn.commit()
        else:
            LoggerUtil.logger.error(f"接口响应不符合预期,用例执行失败!查询提交参数是:{params}")
            raise AssertionError("测试执行失败")
