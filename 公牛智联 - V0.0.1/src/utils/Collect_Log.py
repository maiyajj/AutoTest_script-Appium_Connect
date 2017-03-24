# coding:utf-8
import logging
import logging.handlers


def init_log_save_mode(file_name, logger):
    logging.basicConfig(level=logging.INFO)  # 设置打印级别
    log_mode = 'midnight'  # 'midnight' #设置每天凌晨0点拆分log文件，可设置任意时间单位秒，分，时，天，周，月，年
    log_interval = 1  # 时间单位的参数，此处为1天
    log_max_files = 0  # 最大保存文件个数，0代表无限制
    formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
    handler = logging.handlers.TimedRotatingFileHandler(file_name, log_mode, log_interval, log_max_files)
    handler.suffix = "-[%Y-%m-%d_%H-%M-%S].log"  # 保存log文件名称格式
    # 此处改了suffix源文件345行
    handler.setFormatter(formatter)
    logger.addHandler(handler)  # 初始化完毕
    return logger


logger = logging.getLogger(r"%s" % "log")
logger = init_log_save_mode(r"log/myapp", logger)
logger.info(data)
