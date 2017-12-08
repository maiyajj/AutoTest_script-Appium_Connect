# coding=utf-8
from ToLoginPage_AL import *
from ToLoginPage_GN import *
from ToLoginPage_HW import *
from ToLoginPage_JD import *


class ToLoginPage(object):
    def __init__(self, driver, device_info):
        self.app = device_info["app"]

        if self.app == "GN":
            ToLoginPageGN(driver, device_info)
        elif self.app == "JD":
            ToLoginPageJD(driver, device_info)
        elif self.app == "AL":
            ToLoginPageAL(driver, device_info)
        elif self.app == "HW":
            ToLoginPageHW(driver, device_info)
        else:
            raise KeyError("%s:No such App!" % self.app)
