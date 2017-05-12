# coding=utf-8
from multiprocessing import *

from src.testcase.case.WaitCase import *
from src.testcase.common.AppInit import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *

_main_version = ""
_build_version = ""


def run(device_list, device_name, restart):
    appium = Process(target=LaunchAppiumServices, args=(device_list, device_name,))
    appium.start()
    WaitCase(device_list, device_name, restart)


if __name__ == '__main__':
    device_list = app_init()
    print device_list
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    scan_case.join()

    restart = Queue()
    process = [Process(target=run, args=(device_list, device_name, restart,)) for device_name in device_list.keys()]
    for i in process:
        restart.put(False)
        i.start()
