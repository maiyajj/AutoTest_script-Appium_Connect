# coding=utf-8
from AppPageElement_GN import *
from AppPageElement_JD import *


class MainPageWidget(object):
    def __init__(self, phone_os, app):
        self.phone_os = phone_os
        self.app = app

    def wrapper(self):
        if self.app == "GN":
            return MainPageWidgetGN(self.phone_os)
        elif self.app == "JD":
            return MainPageWidgetJD(self.phone_os)
        else:
            raise KeyError("The app does not support")
