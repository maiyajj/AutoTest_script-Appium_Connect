# coding=utf-8
import os
import re
import shutil
import time
from Queue import Empty


class LaunchAppiumServices(object):
    def __init__(self, device_list, device_name):
        self.device_info = device_list[device_name]
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.udid = self.device_info["udid"]
        self.restart_count = 0

        self.folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])

    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def launch_appium(self, restart):
        self.kill_adb()
        self.create_adb_folder()
        self.restart_count = 0
        while True:
            while True:
                try:
                    restart_ready = restart.get_nowait()
                    break
                except Empty:
                    print "%s Empty" % self.device_info["deviceName"]
                    time.sleep(1)
            print restart_ready
            if restart_ready is True:
                self.restart_count += 1
                self.restart_appium()
            else:
                log = os.path.join(os.getenv('Temp'), "AutoTestGNApp")
                if os.path.exists(log) is False:
                    os.makedirs(log)
                log = os.path.join(log, "%s.log" % self.udid)
                command = "appium -a 127.0.0.1 -p %s -bp %s -U %s -g %s --command-timeout 86400 --no-reset" % (
                    self.port, self.bp_port, self.udid, log)
                print command
                os.system(command)

    def restart_appium(self):
        try:
            command = "netstat  -aon|findstr %s" % self.port
            port = re.findall(r".+LISTENING.+?(\d+)", os.popen(command).read())[0]
            command = "taskkill /f /pid %s" % port
            print os.popen(command).read()
        except IndexError:
            print "%s端口未占用" % self.port

        try:
            command = "netstat  -aon|findstr %s" % self.bp_port
            bp_port = re.findall(r".+LISTENING.+?(\d+)", os.popen(command).read())[0]
            command = "taskkill /f /pid %s" % bp_port
            print os.popen(command).read()
        except IndexError:
            print "%s端口未占用" % self.bp_port

        log = os.path.join(os.getenv('Temp'), "AutoTestGNApp")
        if os.path.exists(log) is False:
            os.makedirs(log)
        log = os.path.join(log, "Restart_%s_%s.log" % (self.udid, self.restart_count))
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
