# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitAndroid(object):
    def __init__(self, device, k):
        self.device = device
        self.k = k
        self.app = conf["user_and_pwd"][k]["app"].upper()
        if self.app == "GN":
            self.app = "GN_Android"
            self.device[k]["app"] = "GN"
        elif self.app == "JD":
            self.app = "JD_Android"
            self.device[k]["app"] = "JD"
        elif self.app == "AL":
            self.app = "AL_Android"
            self.device[k]["app"] = "AL"
        else:
            raise KeyError("%s:No such App!" % self.app)

    def app_init_android(self):
        self.device[self.k]["desired_caps"] = {}
        self.device[self.k]["desired_caps"]['automationName'] = "Appium"
        self.device[self.k]["desired_caps"]['driver'] = '%s' % self.k
        self.device[self.k]["desired_caps"]['platformName'] = '%s' % self.device[self.k]["platformName"]
        self.device[self.k]["desired_caps"]['browserName'] = ''
        self.device[self.k]["desired_caps"]['platformVersion'] = '%s' % self.device[self.k]["platformVersion"]
        self.device[self.k]["desired_caps"]['deviceName'] = '%s' % self.device[self.k]["deviceName"]
        self.device[self.k]["desired_caps"]['newCommandTimeout'] = '999999'
        self.device[self.k]["desired_caps"]["unicodeKeyboard"] = "True"
        self.device[self.k]["desired_caps"]["resetKeyboard"] = "True"
        self.device[self.k]["desired_caps"]['wdaLocalPort'] = '%s' % self.device[self.k]["wda_port"]
        self.device[self.k]["desired_caps"]['appPackage'] = '%s' % conf["App"][self.app]["appPackage"]
        self.device[self.k]["desired_caps"]['appActivity'] = '%s' % conf["App"][self.app]["appActivity"]
        self.device[self.k]["desired_caps"]['waitActivity'] = '%s' % conf["App"][self.app]["waitActivity"]

        return self.device
