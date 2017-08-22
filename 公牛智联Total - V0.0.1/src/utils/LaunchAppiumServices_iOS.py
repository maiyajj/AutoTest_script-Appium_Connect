# coding=utf-8
import shutil

from ShellCommand import *


class LaunchAppiumServicesIos(object):
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
                import traceback
                print traceback.format_exc()
        while True:
            log = os.path.join(log_tmp, "%s-[%s].log" % (self.log_name, time.strftime("%Y-%m-%d %H-%M-%S")))
            command = 'appium -a 127.0.0.1 -p %s -bp %s -U %s -g "%s" --no-reset --local-timezone' % (
                self.port, self.bp_port, self.udid, log)
            print command
            os.system(command)
            for ports in [self.port, self.bp_port, self.wda_port]:
                proc_pid = self.sc.find_proc_and_pid_by_port(ports)
                if proc_pid == []:  # 判断当前端口是否被占用
                    print "COM %s unused" % ports
                else:
                    for i in proc_pid:
                        self.sc.kill_proc_by_pid(i[1])
                        print "Kill %s" % i[0]


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

