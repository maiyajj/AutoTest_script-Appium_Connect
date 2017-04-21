# coding=utf-8
import os
import time
from multiprocessing import Process

from src.testcase.case.WaitCase import *

_main_version = ""
_build_version = ""


def devices(device_name):
    # app_init(device)
    appium = Process(target=LaunchAppiumServices, args=(device_name,))
    appium.start()
    time.sleep(10)
    WaitCase(device_name)


if __name__ == '__main__':
    command = "taskkill /f /t /im adb.exe"
    os.system(command)
    print device
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    scan_case.join()
    process = []
    for key in device.keys():
        process.append(Process(target=devices, args=(key,)))

    for i in process:
        i.start()
        # devices("MX5")
        # first.start()
        # app_init_launch_appium()
        # WaitCase()
