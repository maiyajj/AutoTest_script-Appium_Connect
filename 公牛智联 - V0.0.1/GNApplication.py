# coding=utf-8
from multiprocessing import Process

from src.testcase.case.WaitCase import *
from src.testcase.common.AppInit import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *

_main_version = ""
_build_version = ""


def run(device_list, device_name):
    appium = Process(target=LaunchAppiumServices, args=(device_list, device_name))
    appium.start()
    time.sleep(10)
    WaitCase(device_list, device_name)


if __name__ == '__main__':
    device_list = app_init()
    print device_list
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    scan_case.join()

    process = [Process(target=run, args=(device_list, device_name)) for device_name in device_list.keys()]
    for i in process:
        i.start()
