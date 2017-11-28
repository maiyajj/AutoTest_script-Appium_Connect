# coding=utf-8
from ToLoginPage_AL import *
from ToLoginPage_GN import *
from ToLoginPage_HW import *
from ToLoginPage_JD import *


class ToLoginPage(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.app = device_info["app"]

        if self.app == "GN":
            ToLoginPageGN(driver, logger, device_info, page_element)
        elif self.app == "JD":
            ToLoginPageJD(driver, logger, device_info, page_element)
        elif self.app == "AL":
            ToLoginPageAL(driver, logger, device_info, page_element)
        elif self.app == "HW":
            ToLoginPageHW(driver, logger, device_info, page_element)
        else:
            raise KeyError("%s:No such App!" % self.app)
