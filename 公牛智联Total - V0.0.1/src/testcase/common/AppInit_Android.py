# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitAndroid(object):
    def __init__(self):
        pass

    def app_init_android(self, device, k):
        device[k]["desired_caps"] = {}
        device[k]["desired_caps"]['automationName'] = "Appium"
        device[k]["desired_caps"]['driver'] = '%s' % k
        device[k]["desired_caps"]['platformName'] = '%s' % device[k]["platformName"]
        device[k]["desired_caps"]['browserName'] = ''
        device[k]["desired_caps"]['platformVersion'] = '%s' % device[k]["platformVersion"]
        device[k]["desired_caps"]['deviceName'] = '%s' % device[k]["deviceName"]
        device[k]["desired_caps"]['newCommandTimeout'] = '600'
        device[k]["desired_caps"]["unicodeKeyboard"] = "True"
        device[k]["desired_caps"]["resetKeyboard"] = "True"
        device[k]["desired_caps"]['wdaLocalPort'] = '%s' % device[k]["wda_port"]
        device[k]["desired_caps"]['appPackage'] = '%s' % conf["App"]["GN_Android"]["appPackage"]
        device[k]["desired_caps"]['appActivity'] = '%s' % conf["App"]["GN_Android"]["appActivity"]
        device[k]["desired_caps"]['waitActivity'] = '%s' % conf["App"]["GN_Android"]["waitActivity"]

        return device
