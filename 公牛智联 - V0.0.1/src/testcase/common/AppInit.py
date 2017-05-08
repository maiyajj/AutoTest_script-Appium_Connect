# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.GetPhoneInfo import *
from src.utils.ReadConf import *


def app_init():
    device = get_phone_info()
    used_name_and_pwd = []
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

        for k1 in conf["user_and_pwd"].keys():
            if k1 not in used_name_and_pwd:
                used_name_and_pwd.append(k1)
                device[k]["user_and_pwd"] = k1
                break

    return device
