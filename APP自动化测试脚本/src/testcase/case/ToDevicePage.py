# coding=utf-8
from ToDevicePage_AL import *
from ToDevicePage_GN import *
from ToDevicePage_HW import *
from ToDevicePage_JD import *


class ToDevicePage(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.app = device_info["app"]

        if self.app == "GN":
            ToDevicePageGN(driver, logger, device_info, page_element)
        elif self.app == "JD":
            ToDevicePageJD(driver, logger, device_info, page_element)
        elif self.app == "AL":
            ToDevicePageAL(driver, logger, device_info, page_element)
        elif self.app == "HW":
            ToDevicePageHW(driver, logger, device_info, page_element)
        else:
            raise KeyError("%s:No such App!" % self.app)
