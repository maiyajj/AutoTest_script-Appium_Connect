# coding=utf-8
from ShellCommand_Mac import *
from ShellCommand_Windows import *


class PortBindError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ShellCommand(object):
    def __init__(self):
        self.scw = ShellCommandWindows()
        self.scm = ShellCommandMac()
        self.os = self.get_os()

    def get_os(self):
        system = os.name
        if system == "nt":
            return "windows"
        if system == "posix":
            return "mac"

    def kill_other_python(self):
        if self.os == "windows":
            self.scw.kill_other_python()
        elif self.os == "mac":
            self.scm.kill_other_python()
        else:
            raise KeyError("The OS is wrong!")

    def get_phone_udid_for_android(self):
        '''

        :return: [udid]
        '''
        command = "adb devices -l"
        udid = re.findall("(.+?) {2,}.+?", os.popen(command).read())

        return udid

    def get_phone_udid_for_ios(self):
        '''

        :return: [udid]
        '''
        command = "idevice_id -l"
        udid = re.findall("(.+)", os.popen(command).read())
        return udid

    def find_proc_and_pid_by_port(self, port):
        '''

        :param port:
        :return:(proc, pid)
        '''
        if self.os == "windows":
            find_by_port = self.scw.find_proc_and_pid_by_port(port)
        elif self.os == "mac":
            find_by_port = self.scm.find_proc_and_pid_by_port(port)
        else:
            raise KeyError("The OS is wrong!")
        return find_by_port

    def find_proc_and_pid_by_pid(self, pid):
        '''

        :param pid:
        :return:
        '''
        if self.os == "windows":
            find_by_pid = self.scw.find_proc_and_pid_by_pid(pid)
        elif self.os == "mac":
            find_by_pid = self.scm.find_proc_and_pid_by_pid(pid)
        else:
            raise KeyError("The OS is wrong!")

        return find_by_pid

    def find_proc_and_pid_by_proc(self, proc):
        '''

        :param proc:
        :return:
        '''
        if self.os == "windows":
            find_by_proc = self.scw.find_proc_and_pid_by_proc(proc)
        elif self.os == "mac":
            find_by_proc = self.scm.find_proc_and_pid_by_proc(proc)
        else:
            raise KeyError("The OS is wrong!")

        return find_by_proc

    def kill_proc_by_proc(self, proc):
        '''

        :param self.os:
        :param proc:
        :return:
        '''
        if self.os == "windows":
            self.scw.kill_proc_by_proc(proc)
        elif self.os == "mac":
            self.scm.kill_proc_by_proc(proc)
        else:
            raise KeyError("The OS is wrong!")

    def kill_proc_by_pid(self, pid):
        '''

        :param self.os:
        :param pid:
        :return:
        '''
        if self.os == "windows":
            self.scw.kill_proc_by_pid(pid)
        elif self.os == "mac":
            self.scm.kill_proc_by_pid(pid)
        else:
            raise KeyError("The OS is wrong!")

    def set_appium_log_addr(self):
        if self.os == "windows":
            addr = self.scw.set_appium_log_addr()
        elif self.os == "mac":
            addr = self.scm.set_appium_log_addr()
        else:
            raise KeyError("The OS is wrong!")

        return addr
