# coding=utf-8
import logging
import logging.handlers
import os
import time


# Create debug file.
# Record the wrong information of program.
def init_debug(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=100 * 1024 * 1024)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def check_debug(device_list, device_name):
    log_name = device_list[device_name]["log_name"]
    udid = device_list[device_name]["udid"]
    current_time = time.strftime("%Y-%m-%d_%H.%M")
    if os.path.exists(r"./debug/%s" % current_time) is False:
        # 多进程打印可能存在冲突，忽略即可
        try:
            os.makedirs(r"./debug/%s" % current_time)
        except OSError:
            pass

    logger_name = r"./debug/%s/Debug_%s - [%s].log" % (current_time, log_name, udid)
    device_list[device_name]["debug"] = init_debug(logger_name, logging.getLogger("Debug_%s" % udid))

    logging.shutdown()
