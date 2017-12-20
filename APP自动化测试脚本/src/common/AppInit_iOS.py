# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitIos(object):
    def __init__(self, device_info, k):
        self.d = device_info
        self.k = k
        app = conf["phone_name"][k]["app"].upper()
        app_list = {"GN_APP": "GN_iOS",
                    "GN_201S": "AL_iOS",
                    "GN_201J": "JD_iOS",
                    "GN_201H": "HW_iOS",
                    "GN_F1331": "JD_iOS"}
        try:
            self.app = app_list[app]
            self.d[k]["app"] = app
        except KeyError:
            raise

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
