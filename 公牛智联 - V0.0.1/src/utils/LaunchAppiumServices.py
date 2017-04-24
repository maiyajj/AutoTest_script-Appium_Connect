# coding=utf-8
import os


class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.port = device_list[device_name]["port"]
        self.bp_port = device_list[device_name]["bp_port"]
        self.udid = device_list[device_name]["udid"]

        self.kill_adb()
        self.create_adb_folder(device_list, device_name)
        self.launch_appium()

    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def launch_appium(self):
        command = "appium -a 127.0.0.1 -p %s -bp %s -U  %s  --no-reset" % (self.port, self.bp_port, self.udid)
        os.system(command)

    def create_adb_folder(self, device_list, device_name):
        command = "adb shell mkdir /sdcard/Appium"
        os.popen(command)

        command = "adb shell mkdir /sdcard/Appium/%s" % device_list[device_name]["udid"]
        os.popen(command)
