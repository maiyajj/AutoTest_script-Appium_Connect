# coding:utf-8
import logging
import logging.handlers


def init_report_save_mode(file_name, report1):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    report1.addHandler(handler)  # 初始化完毕
    return report1


report = init_report_save_mode(r"../report/Report.log", logging.getLogger("2"))
logging.shutdown()
