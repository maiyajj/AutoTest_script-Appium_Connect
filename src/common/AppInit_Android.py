# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitAndroid(object):
    def __init__(self, device_info, k):
        self.d = device_info
        self.k = k
        app = conf["phone_name"][k]["app"].upper()
        app_list = {"GN_APP": "GN_Android",
                    "GN_201S": "AL_Android",
                    "GN_201J": "JD_Android",
                    "GN_201H": "HW_Android",
                    "GN_F1331": "JD_Android"}
        try:
            self.app = app_list[app]
            self.d[k]["app"] = app
        except KeyError:
            raise

    def app_init_android(self):
        self.d[self.k]["desired_caps"] = {}
        self.d[self.k]["desired_caps"]['automationName'] = "Appium"
        self.d[self.k]["desired_caps"]['driver'] = '%s' % self.k
        self.d[self.k]["desired_caps"]['platformName'] = '%s' % self.d[self.k]["platformName"]
        self.d[self.k]["desired_caps"]['browserName'] = ''
        self.d[self.k]["desired_caps"]['platformVersion'] = '%s' % self.d[self.k]["platformVersion"]
        self.d[self.k]["desired_caps"]['deviceName'] = '%s' % self.d[self.k]["deviceName"]
        self.d[self.k]["desired_caps"]['newCommandTimeout'] = '999999'
        self.d[self.k]["desired_caps"]["unicodeKeyboard"] = "True"
        self.d[self.k]["desired_caps"]["resetKeyboard"] = "True"
        self.d[self.k]["desired_caps"]['wdaLocalPort'] = '%s' % self.d[self.k]["wda_port"]
        self.d[self.k]["desired_caps"]['appPackage'] = '%s' % conf["App"][self.app]["appPackage"]
        self.d[self.k]["desired_caps"]['appActivity'] = '%s' % conf["App"][self.app]["appActivity"]
        self.d[self.k]["desired_caps"]['waitActivity'] = '%s' % conf["App"][self.app]["waitActivity"]

        return self.d
