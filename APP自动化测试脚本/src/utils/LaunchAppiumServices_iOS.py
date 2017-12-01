# coding=utf-8
import shutil
import traceback
from subprocess import *

import psutil

from ShellCommand import *


def launch_appium_error_log(func):
    def wrapper(self):
        try:
            func(self)
        except BaseException:
            with open(os.path.join(self.sc.set_appium_log_addr(), "appium_launch_error.log"), "a") as appium_error:
                appium_error.write(traceback.format_exc())

    return wrapper


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

        # Screenshot directory in android phone.
        self.folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])

        self.kill_adb()
        # self.create_adb_folder()

    def kill_adb(self):
        # Before starting the appium service， must kill residue adb services,
        # or there will be conflicts and appium services doesn`t work.
        self.sc.kill_proc_by_proc("adb")

    @launch_appium_error_log
    def launch_appium(self):
        # The appium service log stores the directory.
        # Classify at current minute time.
        log_tmp = os.path.join(self.sc.set_appium_log_addr(), "AutoTestGNApp/%s" % time.strftime("%Y-%m-%d %H-%M"))
        if os.path.exists(log_tmp) is False:
            try:
                os.makedirs(log_tmp)
            except OSError:
                pass

        # appium服务调用进程链的pid，name等信息，每次运行程序前会清空，而运行时追加，所以写在while True外面.
        with open(os.path.join(self.sc.set_appium_log_addr(), "appium_port_%s.txt" % self.log_name), "w") as files:
            # Popen(command, shell=True)语句是非阻塞式，如果appium服务崩溃则会继续往下执行然后回到while True.
            while True:
                # appium服务日志存放目录
                log = os.path.join(log_tmp, "%s-[%s].log" % (self.log_name, time.strftime("%Y-%m-%d %H-%M-%S")))
                # 启动appium服务命令
                command = 'appium -a 127.0.0.1 -p %s -bp %s -U %s -g "%s" --no-reset --local-timezone' % (
                    self.port, self.bp_port, self.udid, log)
                print(command)

                # 为了后期调试方便，将当前appium启动命令写入文件中，方便使用shell命令调试手机.
                with open("appium_command_%s.txt" % self.log_name, "a") as filess:
                    filess.write(time.strftime("%Y-%m-%d %H-%M") + "\n")
                    filess.write(command.replace(' -g "%s"' % log, "") + "\n")
                    filess.write("from appium import webdriver" + "\n")

                # 启动Appium服务，非阻塞式服务.
                appium_proc = Popen(command, shell=True)
                appium_pid = [appium_proc.pid]
                # 获取所有Appium调用的进程pid
                # appium_proc是非阻塞式，命令启动后轮询检测指定端口，检测端口已开启则判断Appium服务已开启。
                while True:
                    port = self.sc.find_proc_and_pid_by_port(self.port)
                    wda_port = self.sc.find_proc_and_pid_by_port(self.wda_port)
                    files.write("Port: %s; Wda_port: %s\n" % (port, wda_port))
                    if port != [] and wda_port != []:
                        for i in appium_pid:
                            child_proc = psutil.Process(i).children()
                            if child_proc != []:
                                for x in child_proc:
                                    appium_pid.append(x.pid)
                                    files.write("pid: %s; name: %s parent: %s\n" % (x.pid, x.name(), x.parent()))
                        files.write("%s\n" % appium_pid)
                        break
                    else:
                        time.sleep(3)

                # 轮询检测端口占用，若端口已关闭则重启Appium服务。
                # 优先关闭子进程，关闭所有子进程后再关闭主进程。
                appium_pid = list(reversed(appium_pid))  # 将主进程pid换至表尾
                while True:
                    port = self.sc.find_proc_and_pid_by_port(self.port)
                    wda_port = self.sc.find_proc_and_pid_by_port(self.wda_port)
                    files.write("Check! Port: %s; Wda_port: %s\n" % (port, wda_port))
                    if port == [] or wda_port == []:
                        for i in appium_pid:
                            self.sc.kill_proc_by_pid(i)
                        break
                    else:
                        time.sleep(3)
                        files.write("%s: %s, %s\n" % (time.strftime("%Y-%m-%d %H-%M-%S"), self.port, port))

    def create_adb_folder(self):
        """
        Create screenshot folder in phone.
        """
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
