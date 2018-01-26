# coding=utf-8
import logging
import logging.handlers
import os
import time


# Create debug file.
# Record the wrong information of program.
def init_debug(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(message)s", "%Y-%m-%d %X")  # log文件写入内容，此处为正文
    # encoding，Python3无此log会乱码
    handler = logging.handlers.RotatingFileHandler(file_name, encoding="utf-8", maxBytes=100 * 1024 * 1024)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def check_debug(device_info):
    log_name = device_info["log_name"]
    udid = device_info["udid"]
    current_time = time.strftime("%Y-%m-%d_%H.%M")
    debug_path = r"./debug/%s" % current_time
    device_info["debug_path"] = debug_path
    if os.path.exists(debug_path) is False:
        # 多进程打印可能存在冲突，忽略即可
        try:
            os.makedirs(debug_path)
        except OSError:
            pass

    logger_name = r"%s/Debug_%s - [%s].log" % (debug_path, log_name, udid)
    debug = init_debug(logger_name, logging.getLogger("Debug_%s" % udid))

    logging.shutdown()

    return debug
