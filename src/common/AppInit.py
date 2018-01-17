# coding=utf-8
# from src.testcase.suite.DiffImg import *
from AppInit_Android import *
from AppInit_iOS import *
from src.utils.GetPhoneInfo import *


class AppInit(object):
    def __init__(self):
        pass

    def app_init(self):
        device_info = GetPhoneInfo().get_phone_info()
        if not device_info:
            print(u"ERROR! 未检测到设备，请检查手机链接。")
            exit(-1)
        for k, v in device_info.items():
            if v["platformName"] == "Android":
                AppInitAndroid(device_info, k).app_init_android()
            elif v["platformName"] == "iOS":
                AppInitIos(device_info, k).app_init_ios()
            else:
                raise KeyError("The phone os is wrong")

        return device_info
