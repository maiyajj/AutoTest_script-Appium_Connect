# coding=utf-8
import inspect
import logging
import re

__author__ = "maiyajj"


class ReadInfo(object):
    # 获取设置超时时间函数
    def get_timeout_time(self):
        with open(r"data/info.txt", "r") as timeout_time:
            func_name1 = inspect.stack()[1][3]
            time_temp = timeout_time.read()
            # 打开APP超时时间
            self.open_app_timeout = float(re.findall(r"open_app_timeout:(.+?)s", time_temp)[0])
            # 搜索设备超时时间
            self.search_device_timeout = float(re.findall(r"search_device_timeout:(.+?)s", time_temp)[0])
            # 操作响应超时
            self.request_timeout = float(re.findall(r"request_timeout:(.+?)s", time_temp)[0])
            # 离线不恢复超时时间
            self.offline_recovery_timeout = float(re.findall(r"offline_recovery_timeout:(.+?)s", time_temp)[0])
            # 程序操作等待时间
            self.operate_wait_time = float(re.findall(r"operate_wait_time:(.+?)s", time_temp)[0])
            # 需要测试的设备Mac地址列表
            # self.MAC = map(lambda x: x + '*name', re.findall(r"MAC:'(.+?)'", time_temp)[0].split(";"))
            self.MAC = re.findall(r"MAC:'(.+?)'", time_temp)[0].split(";")
            # Mac地址列表选取标志位
            self.mac_choose_flag = int(re.findall(r"mac_choose_flag:(.+?)", time_temp)[0])

    # log输出处理函数
    def log_text(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='[%Y-%m-%d %H:%M:%S]',
                            filename=r'report/myapp.log',
                            filemode='w')