# coding=utf-8
import multiprocessing

from src.utils.GetPhoneInfo import *
from .AppInit_Android import *
from .AppInit_iOS import *


class AppInit(object):
    def __init__(self):
        pass

    def app_init(self):
        sc = ShellCommand()
        replace_appium_js = multiprocessing.Process(target=sc.replace_appium_js)
        replace_appium_js.start()

        device_info = GetPhoneInfo().get_phone_info()
        if not device_info:
            print(u"ERROR! 未检测到设备，请检查手机链接。")
            os._exit(-1)

        process = [multiprocessing.Process(target=sc.push_appium_app, args=(k,)) for k in device_info.keys()]
        for i in process:
            i.start()

        for k, v in device_info.items():
            if v["platformName"] == "Android":
                AppInitAndroid(device_info, k).app_init_android()
            elif v["platformName"] == "iOS":
                AppInitIos(device_info, k).app_init_ios()
            else:
                raise KeyError("The phone os is wrong")

        replace_appium_js.join()
        for i in process:
            i.join()

        return device_info
