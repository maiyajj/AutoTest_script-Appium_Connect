# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitAndroid(object):
    def __init__(self, device_info, k):
        self.d = device_info
        self.k = k
        self.app = conf["phone_name"][k]["app"].upper()
        if self.app == "GN":
            self.app = "GN_Android"
            self.d[k]["app"] = "GN"
        elif self.app == "JD":
            self.app = "JD_Android"
            self.d[k]["app"] = "JD"
        elif self.app == "AL":
            self.app = "AL_Android"
            self.d[k]["app"] = "AL"
        elif self.app == "HW":
            self.app = "HW_Android"
            self.d[k]["app"] = "HW"
        else:
            raise KeyError("%s:No such App!" % self.app)

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
