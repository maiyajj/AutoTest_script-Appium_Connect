# coding=utf-8
import os
import shutil


class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.device_info = device_list[device_name]
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.udid = self.device_info["udid"]

        self.folder = "%s[%s]" % (self.device_info["model"], self.device_info["udid"])

        self.kill_adb()
        self.create_adb_folder()
        self.launch_appium()

    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def launch_appium(self):
        command = "appium -a 127.0.0.1 -p %s -bp %s -U  %s  --no-reset" % (self.port, self.bp_port, self.udid)
        os.system(command)

    def create_adb_folder(self):
        command = "adb -s %s shell mkdir /sdcard/Appium" % self.udid
        os.popen(command)

        command = "adb -s %s shell mkdir /sdcard/Appium/%s" % (self.udid, self.folder)
        os.popen(command)

        try:
            os.makedirs("./screenshots/%s" % self.folder)
        except WindowsError:
            shutil.rmtree("./screenshots/%s" % self.folder, True)
            os.makedirs("./screenshots/%s" % self.folder)
