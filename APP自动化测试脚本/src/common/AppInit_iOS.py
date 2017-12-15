# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitIos(object):
    def __init__(self, device_info, k):
        self.d = device_info
        self.k = k
        self.app = conf["phone_name"][k]["app"].upper()
        if self.app == "GN":
            self.app = "GN_iOS"
            self.d[k]["app"] = "GN"
        elif self.app == "JD":
            self.app = "JD_iOS"
            self.d[k]["app"] = "JD"
        elif self.app == "AL":
            self.app = "AL_iOS"
            self.d[k]["app"] = "AL"
        elif self.app == "HW":
            self.app = "HW_iOS"
            self.d[k]["app"] = "HW"
        else:
            raise KeyError("%s:No such App!" % self.app)

    def app_init_ios(self):
        self.d[self.k]["desired_caps"] = {}
        self.d[self.k]["desired_caps"]['driver'] = '%s' % self.k
        self.d[self.k]["desired_caps"]['platformName'] = '%s' % self.d[self.k]["platformName"]
        self.d[self.k]["desired_caps"]['browserName'] = ''
        self.d[self.k]["desired_caps"]['platformVersion'] = '%s' % self.d[self.k]["platformVersion"]
        self.d[self.k]["desired_caps"]['deviceName'] = '%s' % self.d[self.k]["deviceName"]
        self.d[self.k]["desired_caps"]['newCommandTimeout'] = '999999'
        self.d[self.k]["desired_caps"]["autoAcceptAlerts"] = "True"
        self.d[self.k]["desired_caps"]['wdaLocalPort'] = '%s' % self.d[self.k]["wda_port"]
        self.d[self.k]["desired_caps"]['bundleId'] = '%s' % conf["App"][self.app]["bundleId"]
        self.d[self.k]["desired_caps"]["xcodeSigningId"] = "iPhone Developer"
        self.d[self.k]["desired_caps"]["xcodeOrgId"] = "VDJXFKSVCH"

        return self.d
