# coding=utf-8
import logging
import logging.handlers
import os
import time


def init_log(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def check_log(device_list, device_name):
    log_name = device_list[device_name]["log_name"]
    udid = device_list[device_name]["udid"]
    current_time = time.strftime("%Y-%m-%d_%H.%M")

    if os.path.exists(r"./log/%s" % current_time) is False:
        try:
            os.makedirs(r"./log/%s" % current_time)
        except OSError:
            import traceback
            print traceback.format_exc()

    logger_name = r"./log/%s/Log_%s - [%s].log" % (current_time, log_name, udid)
    device_list[device_name]["logger"] = init_log(logger_name, logging.getLogger("Log_%s" % udid))

    logging.shutdown()
