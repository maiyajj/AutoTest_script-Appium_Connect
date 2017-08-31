# coding=utf-8
from src.testcase.case.WaitCase_GN import *
from src.testcase.case.WaitCase_JD import *

class WaitCase(object):
    def __init__(self, device_list, device_name):
        self.app = device_list[device_name]["app"]

        if self.app == "GN":
            WaitCaseGN(device_list, device_name)
        elif self.app == "JD":
            WaitCaseJD(device_list, device_name)
        else:
            raise KeyError("%s:The App not support" % self.app)
