# coding=utf-8
from ToDevicePage_AL import *
from ToDevicePage_GN import *
from ToDevicePage_HW import *
from ToDevicePage_JD import *


class ToDevicePage(object):
    def __init__(self, driver, device_info):
        self.app = device_info["app"]

        if self.app == "GN":
            ToDevicePageGN(driver, device_info)
        elif self.app == "JD":
            ToDevicePageJD(driver, device_info)
        elif self.app == "AL":
            ToDevicePageAL(driver, device_info)
        elif self.app == "HW":
            ToDevicePageHW(driver, device_info)
        else:
            raise KeyError("%s:No such App!" % self.app)
