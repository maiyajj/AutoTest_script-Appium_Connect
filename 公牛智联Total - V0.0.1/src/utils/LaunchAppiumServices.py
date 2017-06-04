# coding=utf-8
from LaunchAppiumServices_Android import *
from LaunchAppiumServices_iOS import *

class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.device_info = device_list[device_name]
        self.launch_appium()

    def launch_appium(self):
        if self.device_info["platformName"] == "Android":
            LaunchAppiumServicesAndroid(self.device_info).launch_appium()
        elif self.device_info["platformName"] == "iOS":
            LaunchAppiumServicesIos(self.device_info).launch_appium()