# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.GetPhoneInfo import *
from src.utils.ReadConf import *


def app_init():
    device = get_phone_info()
    for k in device.keys():
        device[k]["desired_caps"] = {}
        device[k]["desired_caps"]['driver'] = '%s' % k
        device[k]["desired_caps"]['platformName'] = '%s' % device[k]["platformName"]
        device[k]["desired_caps"]['browserName'] = ''
        device[k]["desired_caps"]["unicodeKeyboard"] = "True"
        device[k]["desired_caps"]["resetKeyboard"] = "True"
        device[k]["desired_caps"]['platformVersion'] = '%s' % device[k]["platformVersion"]
        device[k]["desired_caps"]['deviceName'] = '%s' % device[k]["deviceName"]
        device[k]["desired_caps"]['appPackage'] = '%s' % conf["App"]["GN"][0]
        device[k]["desired_caps"]['appActivity'] = '%s' % conf["App"]["GN"][1]
        device[k]["desired_caps"]['waitActivity'] = '%s' % conf["App"]["GN"][2]

    return device
