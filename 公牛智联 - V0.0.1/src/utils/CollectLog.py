# coding:utf-8
import logging
import logging.handlers

from data.Database import *


def init_log_save_mode(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def init_report(file_name, report1):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    report1.addHandler(handler)  # 初始化完毕
    return report1


logger = init_log_save_mode(r"../log/" + database["log_name"], logging.getLogger("1"))
report = init_report(r"../report/Report.log", logging.getLogger("2"))
logging.shutdown()
