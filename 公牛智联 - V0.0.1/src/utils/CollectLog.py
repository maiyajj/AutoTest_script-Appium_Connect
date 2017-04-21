# coding=utf-8
import logging
import logging.handlers

from GetPhoneInfo import *

try:
    for v in device.values():
        with open(r"./log/%s - [%s].log" % (v["log_name"], v["udid"]), "w") as logger_file:
            pass
except IOError:
    os.makedirs(r"./log/")


def init_log_save_mode(file_name, log):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 初始化完毕
    return log


for k, v in device.items():
    device[k]["logger"] = init_log_save_mode(r"./log/%s - [%s].log" % (v["log_name"], v["udid"]),
                                             logging.getLogger("%s1" % v['deviceName']))
logging.shutdown()
