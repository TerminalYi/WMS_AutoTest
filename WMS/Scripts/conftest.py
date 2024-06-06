import os

from WMS.Utils.get_path import Report_JSON, Report_HTML


def pytest_sessionfinish(session, exitstatus):
    # 清除旧的报告，并生成新的报告
    os.system(f"allure generate {Report_JSON} -o {Report_HTML} --clean")
