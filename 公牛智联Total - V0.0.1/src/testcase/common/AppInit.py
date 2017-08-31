# coding=utf-8
# from src.testcase.suite.DiffImg import *
from AppInit_Android import *
from AppInit_iOS import *
from src.utils.GetPhoneInfo import *


class AppInit(object):
    def __init__(self):
        pass

    def app_init(self):
        device = GetPhoneInfo().get_phone_info()
        for k, v in device.items():
            if v["platformName"] == "Android":
                AppInitAndroid(device, k).app_init_android()
            elif v["platformName"] == "iOS":
                AppInitIos(device, k).app_init_ios()
            else:
                raise KeyError("The phone os is wrong")

        return device
