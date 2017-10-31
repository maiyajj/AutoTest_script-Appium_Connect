# coding=utf-8
import shutil
from subprocess import *

import psutil

from ShellCommand import *


class LaunchAppiumServicesIos(object):
    """
    Start appium service for ios system.
    """

    def __init__(self, device_info):
        self.device_info = device_info
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.wda_port = self.device_info["wda_port"]
        self.log_name = self.device_info["log_name"]
        self.udid = self.device_info["udid"]

        self.sc = ShellCommand()

        self.folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])

        self.kill_adb()
        # self.create_adb_folder()

    def kill_adb(self):
        self.sc.kill_proc_by_proc("adb")

    def launch_appium(self):
        log_tmp = os.path.join(self.sc.set_appium_log_addr(), "AutoTestGNApp/%s" % time.strftime("%Y-%m-%d %H-%M"))
        if os.path.exists(log_tmp) is False:
            try:
                os.makedirs(log_tmp)
            except OSError:
                pass
        with open(os.path.join(self.sc.set_appium_log_addr(), "appium_port_%s.txt" % self.log_name), "w") as files:
            while True:
                log = os.path.join(log_tmp, "%s-[%s].log" % (self.log_name, time.strftime("%Y-%m-%d %H-%M-%S")))
                command = 'appium -a 127.0.0.1 -p %s -bp %s -U %s -g "%s" --no-reset --local-timezone' % (
                    self.port, self.bp_port, self.udid, log)
                print command
                with open("appium command %s.txt" % self.device_info["udid"], "a") as filess:
                    filess.write(time.strftime("%Y-%m-%d %H-%M") + "\n")
                    filess.write(command.replace(' -g "%s"' % log, "") + "\n")
                    filess.write("from appium import webdriver" + "\n")

                appium_proc = Popen(command, shell=True)
                appium_pid = [appium_proc.pid]
                while True:
                    port = self.sc.find_proc_and_pid_by_port(self.port)
                    wda_port = self.sc.find_proc_and_pid_by_port(self.wda_port)
                    if port != [] and wda_port != []:
                        for i in appium_pid:
                            child_proc = psutil.Process(i).children()
                            if child_proc != []:
                                for x in child_proc:
                                    appium_pid.append(x.pid)
                                    print x.pid, x.name(), x.parent()
                                    files.write(str(x.pid) + x.name() + str(x.parent()) + "\n")
                        files.write(str(appium_pid) + "\n")
                        break
                    else:
                        time.sleep(3)

                while True:
                    if self.sc.find_proc_and_pid_by_port(self.port) == []:
                        for i in appium_pid[1:]:
                            try:
                                psutil.Process(i).kill()
                            except psutil.NoSuchProcess:
                                pass
                        appium_proc.kill()
                        break
                    else:
                        time.sleep(3)
                        files.write(time.strftime("%Y-%m-%d %H-%M-%S") + ":" + str(self.port) + "," + str(port) + "\n")

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
