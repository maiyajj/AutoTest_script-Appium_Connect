# coding=utf-8
import shutil
from ShellCommand import *

class LaunchAppiumServicesAndroid(object):
    def __init__(self, device_info):
        self.device_info = device_info
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.log_name = self.device_info["log_name"]
        self.udid = self.device_info["udid"]

        self.sc = ShellCommand()

        self.folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])

        self.kill_adb()
        # self.create_adb_folder()

    def kill_adb(self):
        self.sc.kill_proc_by_proc("adb")

    def launch_appium(self):
        log_tmp = os.path.join(self.sc.set_appium_log_addr(), "AutoTestGNApp")
        print log_tmp
        if os.path.exists(log_tmp) is False:
            os.makedirs(log_tmp)
        i = 0
        while True:
            log = os.path.join(log_tmp, "%s_%s.log" % (self.log_name, i))
            command = 'appium -a 127.0.0.1 -p %s -bp %s -U %s -g "%s" --no-reset' % (
                self.port, self.bp_port, self.udid, log)
            print command
            os.system(command)
            i += 1
            for ports in [self.port, self.bp_port]:
                if self.sc.find_proc_and_pid_by_port(ports) == []:  # 判断当前端口是否被占用
                    print "%s端口未占用" % ports


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

