# coding:utf-8
import logging
import logging.handlers
from data.Database import *


def init_log_save_mode(file_name, logger):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %H:%M:%S")  # log文件写入内容，此处为正文
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    logger.addHandler(handler)  # 初始化完毕
    return logger


logger = logging.getLogger()
logger = init_log_save_mode(r"../log/" + database["log_name"], logger)
logging.shutdown()
