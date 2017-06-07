# coding=utf-8
# from src.testcase.suite.DiffImg import *

from src.utils.ReadConf import *


class AppInitIos(object):
    def __init__(self):
        pass

    def app_init_ios(self, device, k):
        device[k]["desired_caps"] = {}
        device[k]["desired_caps"]['driver'] = '%s' % k
        device[k]["desired_caps"]['platformName'] = '%s' % device[k]["platformName"]
        device[k]["desired_caps"]['browserName'] = ''
        device[k]["desired_caps"]['platformVersion'] = '%s' % device[k]["platformVersion"]
        device[k]["desired_caps"]['deviceName'] = '%s' % device[k]["deviceName"]
        device[k]["desired_caps"]['newCommandTimeout'] = '999999'
        device[k]["desired_caps"]["autoAcceptAlerts"] = "True"
        device[k]["desired_caps"]['wdaLocalPort'] = '%s' % device[k]["wda_port"]
        device[k]["desired_caps"]['bundleId'] = '%s' % conf["App"]["GN_iOS"]["bundleId"]

        return device
