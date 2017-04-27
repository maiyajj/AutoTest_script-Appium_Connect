# coding=utf-8
import logging
import logging.handlers
import os


def init_debug(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


def check_debug(device_list, device_name):
    log_name = device_list[device_name]["log_name"]
    udid = device_list[device_name]["udid"]
    try:
        with open(r"./log/%s - [%s].log" % (log_name, udid), "w") as logger_file:
            del logger_file
            pass
    except IOError:
        os.makedirs(r"./log/")

    device_list[device_name]["logger"] = init_log(r"./log/%s - [%s].log" %
                                                  (log_name, udid), logging.getLogger("Log_%s" % udid))

    logging.shutdown()
