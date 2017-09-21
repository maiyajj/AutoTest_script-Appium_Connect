# coding=utf-8
# 由IncrementalUpdate.py生成
from ReadAPPElement_AL import *
from ReadAPPElement_GN import *
from ReadAPPElement_JD import *


class PageElement(object):
    def __init__(self, device, phone_os, app):
        self.phone_os = phone_os
        self.device = device
        self.app = app

    def wrapper(self):
        if self.app == "GN":
            return PageElementGN(self.device, self.phone_os, self.app).get_page_element()
        elif self.app == "JD":
            return PageElementJD(self.device, self.phone_os, self.app).get_page_element()
        elif self.app == "AL":
            return PageElementAL(self.device, self.phone_os, self.app).get_page_element()
        else:
            raise KeyError("%s:No such App!" % self.app)
