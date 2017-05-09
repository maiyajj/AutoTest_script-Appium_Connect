# coding=utf-8
import os
import shutil


class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.device_info = device_list[device_name]
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.udid = self.device_info["udid"]

        self.folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])

        self.kill_adb()
        self.create_adb_folder()
        self.launch_appium()

    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def launch_appium(self):
        log = os.path.join(os.getenv('Temp'), "AutoTestGNApp")
        if os.path.exists(log) is False:
            os.makedirs(log)
        log = os.path.join(log, "%s.log" % self.udid)
        command = "appium -a 127.0.0.1 -p %s -bp %s -U %s -g %s --command-timeout 86400 --no-reset" % (
        self.port, self.bp_port, self.udid, log)
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
            if os.path.isdir("./screenshots/%s" % self.folder) is False:
                os.makedirs("./screenshots/%s" % self.folder)
