# coding:utf-8
import re
import time
from multiprocessing import Process

from src.testcase.suite.DiffImg import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *
from src.utils.OutputReport import *
from src.utils.ReadConf import *

desired_caps = {}
desired_caps['driver'] = '%s' % device.keys()[0]
desired_caps['platformName'] = '%s' % device.values()[0]["platformName"]
desired_caps['browserName'] = ''
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps['platformVersion'] = '%s' % device.values()[0]["platformVersion"]
desired_caps['deviceName'] = '%s' % device.values()[0]["deviceName"]
desired_caps['appPackage'] = '%s' % conf_App["GN"][0]
desired_caps['appActivity'] = '%s' % conf_App["GN"][1]


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def log():
    with open('./log/myapp.log', 'r') as logfile:
        loglines = follow(logfile)
        for line in loglines:
            tmp = re.findall(r".+localhost", line)
            if tmp == []:
                with open('./log/report.log', 'a') as files:
                    files.write(loglines)
            else:
                pass


def app_init_launch_appium():
    Appium = Process(target=LaunchAppiumServices().main)
    create_input_case = Process(target=create_INPUT_CASE)
    scan_case = Process(target=scan_case_name)
    # diff_img = Process(target=DiffImg)

    Appium.start()
    create_input_case.start()
    scan_case.start()
    # diff_img.start()

    scan_case.join()
    create_input_case.join()

    time.sleep(10)
