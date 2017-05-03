# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os
import time


def init_report(file_name, report1):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    report1.addHandler(handler)  # 初始化完毕
    return report1


def check_report(device_list, device_name):
    log_name = device_list[device_name]["log_name"]
    udid = device_list[device_name]["udid"]
    current_time = time.strftime("%Y-%m-%d_%H.%M")

    log_report = r"./report/log_report/%s" % current_time
    if os.path.exists(log_report) is False:
        os.makedirs(log_report)

    if os.path.exists(r"./screenshots/") is False:
        os.makedirs(r"./screenshots/")

    logger_name = r"%s/Report_%s - [%s].log" % (log_report, log_name, udid)
    device_list[device_name]["report"] = init_report(logger_name, logging.getLogger("Report_%s" % udid))

    logging.shutdown()
