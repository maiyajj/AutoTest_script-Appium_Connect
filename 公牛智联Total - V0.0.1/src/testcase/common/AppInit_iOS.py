# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitIos(object):
    def __init__(self, device, k):
        self.device = device
        self.k = k
        self.app = conf["user_and_pwd"][k]["app"].upper()
        if self.app == "GN":
            self.app = "GN_iOS"
            self.device[k]["app"] = "GN"
        elif self.app == "JD":
            self.app = "JD_iOS"
            self.device[k]["app"] = "JD"
        else:
            raise KeyError("%s:No such App!" % self.app)

    def app_init_ios(self):
        self.device[self.k]["desired_caps"] = {}
        self.device[self.k]["desired_caps"]['driver'] = '%s' % self.k
        self.device[self.k]["desired_caps"]['platformName'] = '%s' % self.device[self.k]["platformName"]
        self.device[self.k]["desired_caps"]['browserName'] = ''
        self.device[self.k]["desired_caps"]['platformVersion'] = '%s' % self.device[self.k]["platformVersion"]
        self.device[self.k]["desired_caps"]['deviceName'] = '%s' % self.device[self.k]["deviceName"]
        self.device[self.k]["desired_caps"]['newCommandTimeout'] = '600'
        self.device[self.k]["desired_caps"]["autoAcceptAlerts"] = "True"
        self.device[self.k]["desired_caps"]['wdaLocalPort'] = '%s' % self.device[self.k]["wda_port"]
        self.device[self.k]["desired_caps"]['bundleId'] = '%s' % conf["App"][self.app]["bundleId"]
        self.device[self.k]["desired_caps"]["xcodeSigningId"] = "iPhone Developer"
        self.device[self.k]["desired_caps"]["xcodeOrgId"] = "VDJXFKSVCH"

        return self.device
