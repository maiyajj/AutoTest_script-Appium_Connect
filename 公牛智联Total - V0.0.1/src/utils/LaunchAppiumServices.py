# coding=utf-8
from LaunchAppiumServices_Android import *
from LaunchAppiumServices_iOS import *

class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.device_info = device_list[device_name]
        self.phone_os = self.device_info["platformName"]
        self.launch_appium()

    def launch_appium(self):
        if self.phone_os == "Android":
            LaunchAppiumServicesAndroid(self.device_info).launch_appium()
        elif self.phone_os == "iOS":
            LaunchAppiumServicesIos(self.device_info).launch_appium()
        else:
            raise KeyError("The OS is wrong!")
