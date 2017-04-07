# coding:utf-8
import sys

sys.path.append("..")

# from src.utils.Conf import * # 配置文件或者元素库有更新取消此条注释，用完注释
from src.testcase.case.WaitCase import *
from selenium.webdriver.remote.remote_connection import *

if __name__ == '__main__':
    print device
    app_init_launch_appium()
    WaitCase()
