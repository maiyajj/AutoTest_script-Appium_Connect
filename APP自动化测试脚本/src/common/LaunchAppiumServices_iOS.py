# coding=utf-8
import logging
import logging.handlers
import shutil
import traceback
from subprocess import *

import psutil

from src.utils.ShellCommand import *


def launch_appium_error_log(func):
    def wrapper(self):
        # appium服务调用进程链的pid，name等信息，每次运行程序前会清空，而运行时追加，所以写在while True外面.
        # Popen(command, shell=True)语句是非阻塞式，如果appium服务崩溃则会继续往下执行然后回到while True.
        while True:
            try:
                # 主进程崩溃后有残留子进程，关闭当前子进程
                if not psutil.pid_exists(self.main_pid):
                    psutil.Process(self.current_pid).kill()
                func(self)
            except BaseException:
                with open(os.path.join(self.log_path, "appium_error.log"), "a") as appium_error:
                    appium_error.write(traceback.format_exc())
                print(traceback.format_exc())
            finally:
                # 轮询检测端口占用，若端口已关闭则重启Appium服务。
                while True:
                    port = [i for i in self.sc.find_proc_and_pid_by_port(self.port) if "node" in i[0].lower()]
                    wda_port = self.sc.find_proc_and_pid_by_port(self.wda_port)
                    self.debug.info("Check! Port_proc: %s; wda_port_proc: %s" % (port, wda_port))
                    if not port or not wda_port:
                        for i in self.appium_pid:
                            try:
                                psutil.Process(i).kill()
                                self.debug.info("Kill! Pid: %s" % i)
                            except psutil.NoSuchProcess:
                                self.debug.info("Kill Error! NoSuchProcess! Pid: %s" % i)
                            except psutil.AccessDenied:
                                self.debug.info("Kill Error! AccessDenied! Pid: %s" % i)
                        break
                    else:
                        time.sleep(1)

    return wrapper


class LaunchAppiumServicesIos(object):
    """
    Start appium service for android system.
    """

    def __init__(self, device_info):
        self.device_info = device_info
        self.port = device_info["port"]
        self.bp_port = device_info["bp_port"]
        self.wda_port = device_info["wda_port"]
        self.log_name = device_info["log_name"]
        self.udid = device_info["udid"]
        self.model = device_info["model"]
        self.current_pid = os.getpid()
        self.main_pid = psutil.Process(self.current_pid).parent().parent().pid  # 主进程pid

        self.sc = ShellCommand()
        self.log_path = os.path.join(self.sc.set_appium_log_addr(), "%s" % time.strftime("%Y-%m-%d_%H.%M"), "Appium")
        # The appium service log stores the directory.
        # Classify at current minute time.
        if os.path.exists(self.log_path) is False:
            try:
                os.makedirs(self.log_path)
            except OSError:
                pass

        self.appium_port_debug()

        # Screenshot directory in android phone.
        self.folder = "%s{%s}" % (self.model, self.udid)

        self.kill_adb()
        # self.create_adb_folder()

    def kill_adb(self):
        # Before starting the appium service， must kill residue adb services,
        # or there will be conflicts and appium services doesn`t work.
        self.sc.kill_proc_by_proc("adb")

    def pst_pid(self, pid):
        """可用如下lambda表达式代替函数的定义与调用，唯一的缺点就是不能使用异常捕捉函数
        tmp = lambda pid: [self.appium_pid.append(i) or tmp(i.pid) for i in psutil.Process(pid).children()]
        tmp(appium_proc.pid)
        [tmp(int(i[1])) or self.appium_pid.append(psutil.Process(int(i[1]))) for i in port]
        [tmp(int(i[1])) or self.appium_pid.append(psutil.Process(int(i[1]))) for i in wda_port]
        """
        try:
            c_pid = psutil.Process(pid).children()
        except psutil.NoSuchProcess:
            c_pid = []
        for i in c_pid:
            self.appium_pid.append(i.pid)
            self.pst_pid(i.pid)

    @launch_appium_error_log
    def launch_appium(self):
        # appium服务日志存放目录
        log = os.path.join(self.log_path, "%s-[%s].log" % (self.log_name, time.strftime("%Y-%m-%d %H-%M-%S")))
        # 启动appium服务命令
        command = 'appium -a 127.0.0.1 -p %s -bp %s -U %s -g "%s" --no-reset --local-timezone' % (
            self.port, self.bp_port, self.udid, log)
        print(command)

        # 为了后期调试方便，将当前appium启动命令写入文件中，方便使用shell命令调试手机.
        with open("appium command %s.log" % self.log_name, "a") as filess:
            filess.write(time.strftime("%Y-%m-%d %H-%M") + "\n")
            filess.write(command.replace(' -g "%s"' % log, "") + "\n")
            filess.write("from appium import webdriver" + "\n")

        # 启动Appium服务，非阻塞式服务.
        appium_proc = Popen(command, shell=True)
        print(appium_proc.pid)
        self.appium_pid = [appium_proc.pid]  # 保证属性一致，初始<subprocess.Popen object at 0x...>也有pid属性
        # 获取所有Appium调用的进程pid
        # appium_proc是非阻塞式，命令启动后轮询检测指定端口，检测端口已开启则判断Appium服务已开启。
        end_time = time.time() + 30
        while True:
            port = [i for i in self.sc.find_proc_and_pid_by_port(self.port) if "node" in i[0].lower()]
            wda_port = self.sc.find_proc_and_pid_by_port(self.wda_port)
            self.debug.info("Port_proc: %s; wda_port_proc: %s" % (port, wda_port))
            if port and wda_port:
                break
            else:
                time.sleep(1)
                if time.time() > end_time:
                    break

        # 获取appium服务及对应服务的进程pid
        self.pst_pid(appium_proc.pid)
        [self.pst_pid(i[1]) or self.appium_pid.append(i[1]) for i in port if psutil.pid_exists(i[1])]
        [self.pst_pid(i[1]) or self.appium_pid.append(i[1]) for i in wda_port if psutil.pid_exists(i[1])]

        # pid保持顺序去重
        self.appium_pid = reduce(lambda x, y: x if y in x else x + [y], [[], ] + self.appium_pid)

        # 将int(pid)转换成psutil.Process(pid)并记录log
        [self.debug.info("child_proc: %s" % x) for x in map(lambda x: psutil.Process(x), self.appium_pid)]

        # 记录自动化测试工具进程pid和当前appium服务主pid
        self.debug.info("Pid!Main: %s; Current: %s" % (psutil.Process(self.main_pid), psutil.Process(self.current_pid)))

        # 优先关闭子进程，关闭所有子进程后再关闭主进程。
        self.appium_pid = list(reversed(self.appium_pid))  # 将主进程pid换至表尾

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

    def init_log(self, log):
        file_path = os.path.join(self.log_path, "appium_port_%s.log" % self.log_name)
        logging.basicConfig(level=logging.INFO)  # 设置打印级别
        formatter = logging.Formatter("[%(asctime)s]%(message)s", "%Y-%m-%d %X")  # log文件写入内容，此处为正文
        handler = logging.FileHandler(file_path)
        handler.setFormatter(formatter)
        log.addHandler(handler)  # 初始化完毕
        return log

    def appium_port_debug(self):
        file_name = "appium_port_%s" % self.log_name
        self.debug = self.init_log(logging.getLogger(file_name))  # 初始化完毕

        logging.shutdown()
