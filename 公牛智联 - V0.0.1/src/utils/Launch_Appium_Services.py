# coding=utf-8
import os
from src.utils.Get_Phone_Info import *
from data.Database import *


class Launch_Appium_Services(object):
    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def sim_cmd(self):
        command = "appium -a 127.0.0.1 -p 4723  -U  %s  --no-reset" % device.values()[0]["udid"]
        os.system(command)

    def main(self):
        self.kill_adb()
        self.sim_cmd()