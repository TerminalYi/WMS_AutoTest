# 用于生成日志对象
import logging
from WMS.Utils.get_path import Info_Logs_DIR, Error_Logs_DIR


class LoggerUtil:
    # 1.声明日志器对象logger,设置其日志记录级别为最低等级DEBUG(---1级---)
    logger = logging.getLogger("WMS接口日志")
    logger.setLevel(level=logging.DEBUG)
    # 2.声明过滤器对象filter,用于规范格式,格式属性为fmt,具体参数参考CSDN
    filter01 = logging.Formatter(
        fmt="%(asctime)s 级别：%(levelname)s 日志名：%(name)s 所在文件名：%(filename)s 函数名称:%(funcName)s 具体行数:%(lineno)d 打印内容：%(message)s")
    # 3.声明一个记录INFO级别(---2级---)日志的文件处理器对象,指明其输出路径为Logs/info_logs.log
    handler_01 = logging.FileHandler(filename=Info_Logs_DIR, mode="a", encoding="utf-8")
    handler_01.setLevel(level=logging.INFO)
    # 4.声明一个记录Error级别(---3级---)日志的文件处理对象,指明其输出路径问Logs/error_logs.log
    handler_02 = logging.FileHandler(filename=Error_Logs_DIR, mode="a", encoding="utf-8")
    handler_02.setLevel(level=logging.ERROR)
    # 5.将过滤器加入到---->两个处理器中,规范输出格式
    handler_01.setFormatter(filter01)
    handler_02.setFormatter(filter01)
    # 6.将处理器加入到日志器中
    logger.addHandler(handler_01)
    logger.addHandler(handler_02)



