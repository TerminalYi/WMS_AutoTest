import os

# 此工具类用于存放所有路径，方便调用且不会出错
Base_DIR = os.path.dirname(os.path.dirname(__file__))
# 返回当前文件的目录的父目录 D:\PythonDirector\Yes--ApiAutoFrameWork2\WMS
Util_DIR = os.path.dirname(__file__)
# 返回当前文件的目录 D:\PythonDirector\Yes--ApiAutoFrameWork2\WMS\Utils

# 父目录路径
Logs_DIR = os.path.join(Base_DIR, "Logs")
Yaml_DIR = os.path.join(Base_DIR, "Datas")
Report_DIR = os.path.join(Base_DIR, "Reports")

# 子目录/文件路径
Info_Logs_DIR = os.path.join(Logs_DIR, "info_logs.log")
Error_Logs_DIR = os.path.join(Logs_DIR, "error_logs.log")
Report_JSON = os.path.join(Report_DIR, "allure_json")  # 目录
Report_HTML = os.path.join(Report_DIR, "allure_html")  # 目录


# 获取不同接口数据文件的路径,路径拼接
def get_yaml_path(yaml_path):
    return os.path.join(Yaml_DIR, yaml_path)
