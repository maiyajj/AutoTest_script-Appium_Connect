# coding=utf-8
import logging
import logging.handlers
import os
import time


# Create log file.
# Record the operation information of widget control, widget name or type.
def init_log(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %X")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def check_log(device_info):
    log_name = device_info["log_name"]
    udid = device_info["udid"]
    current_time = time.strftime("%Y-%m-%d_%H.%M")
    log_path = r"./log/%s" % current_time
    if os.path.exists(log_path) is False:
        # 多进程打印可能存在冲突，忽略即可
        try:
            os.makedirs(log_path)
        except OSError:
            pass

    logger_name = r"%s/Log_%s - [%s].log" % (log_path, log_name, udid)
    logger = init_log(logger_name, logging.getLogger("Log_%s" % udid))

    logging.shutdown()

    return logger
