# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os
import time


# Create report file.
# Record the result of launch case.
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
    report_path = r"./report/log_report/%s" % current_time
    if os.path.exists(report_path) is False:
        # 多进程打印可能存在冲突，忽略即可
        try:
            os.makedirs(report_path)
        except OSError:
            pass

    # 错误截屏
    if os.path.exists(r"./screenshots/") is False:
        try:
            os.makedirs(r"./screenshots/")
        except OSError:
            pass

    logger_name = r"%s/Report_%s - [%s].log" % (report_path, log_name, udid)
    device_list[device_name]["report"] = init_report(logger_name, logging.getLogger("Report_%s" % udid))

    logging.shutdown()
