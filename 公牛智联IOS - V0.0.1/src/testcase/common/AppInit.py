# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.GetPhoneInfoIos import *
from src.utils.ReadConf import *


def app_init():
    device = GetPhoneInfo().get_phone_info()
    for k in device.keys():
        device[k]["desired_caps"] = {}
        device[k]["desired_caps"]['driver'] = '%s' % k
        device[k]["desired_caps"]['platformName'] = '%s' % device[k]["platformName"]
        device[k]["desired_caps"]['browserName'] = ''
        device[k]["desired_caps"]["autoAcceptAlerts"] = "True"
        device[k]["desired_caps"]['platformVersion'] = '%s' % device[k]["platformVersion"]
        device[k]["desired_caps"]['deviceName'] = '%s' % device[k]["deviceName"]
        device[k]["desired_caps"]['wdaLocalPort'] = '%s' % device[k]["wda_port"]
        device[k]["desired_caps"]['bundleId'] = '%s' % conf["App"]["GN_ios"]["bundleId"]
        device[k]["desired_caps"]['newCommandTimeout'] = '999999'

    return device
