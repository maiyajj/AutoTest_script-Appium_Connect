# coding=utf-8
from ShellCommand_Mac import *
from ShellCommand_Windows import *


class PidTerminalError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ShellCommand(object):
    """
    API, shell command
    Compatible with Mac and Windows
    """

    def __init__(self):
        self.scw = ShellCommandWindows()
        self.scm = ShellCommandMac()
        self.os = self.get_os()

    def get_os(self):
        """
        get current system type
        """
        system = os.name
        if system == "nt":
            return "windows"
        if system == "posix":
            return "mac"

    def kill_zombie_proc(self):
        """
        Kill zombie process.
        Avoid system resource crashes.
        """
        if self.os == "windows":
            self.scw.kill_zombie_proc()
        elif self.os == "mac":
            self.scm.kill_zombie_proc()
        else:
            raise KeyError("The OS is wrong!")

    def kill_other_python(self):
        """
        kill other python before launch this auto test tool.
        maybe some conflict
        """
        if self.os == "windows":
            self.scw.kill_other_python()
        elif self.os == "mac":
            self.scm.kill_other_python()
        else:
            raise KeyError("The OS is wrong!")

    def get_phone_udid(self):
        """
        Auto get phone udid
        :return:  [udid] -> list
        """
        a = self.get_phone_udid_for_android()
        b = self.get_phone_udid_for_ios()
        a[0:0] = b
        udid = a

        return udid

    def get_phone_udid_for_android(self):
        """
        Get android phone udid
        :return: [udid], -> list
        """
        command = "adb devices -l"
        udid = re.findall("(.+?) {2,}.+?", os.popen(command).read())

        return udid

    def get_phone_udid_for_ios(self):
        """
        Get iphone udid
        :return: [udid] -> list
        """
        command = "idevice_id -l"
        udid = re.findall("(.+)", os.popen(command).read())

        return udid

    def find_proc_and_pid_by_port(self, port):
        """
        find process and pid by process port.
        int -> list
        :return:[(proc1, pid1), (proc2, pid2)]
        """
        if self.os == "windows":
            find_by_port = self.scw.find_proc_and_pid_by_port(port)
        elif self.os == "mac":
            find_by_port = self.scm.find_proc_and_pid_by_port(port)
        else:
            raise KeyError("The OS is wrong!")
        return find_by_port

    def find_proc_and_pid_by_pid(self, pid):
        """
        find process and pid by process pid.
        int -> list
        :return:[(proc1, pid1), (proc2, pid2)]
        """
        if self.os == "windows":
            find_by_pid = self.scw.find_proc_and_pid_by_pid(pid)
        elif self.os == "mac":
            find_by_pid = self.scm.find_proc_and_pid_by_pid(pid)
        else:
            raise KeyError("The OS is wrong!")

        return find_by_pid

    def find_proc_and_pid_by_proc(self, proc):
        """
        find process and pid by process name.
        str -> list
        :return:[(proc1, pid1), (proc2, pid2)]
        """
        if self.os == "windows":
            find_by_proc = self.scw.find_proc_and_pid_by_proc(proc)
        elif self.os == "mac":
            find_by_proc = self.scm.find_proc_and_pid_by_proc(proc)
        else:
            raise KeyError("The OS is wrong!")

        return find_by_proc

    def kill_proc_by_proc(self, proc):
        """
        kill process by process name.
        """
        try:
            if self.os == "windows":
                self.scw.kill_proc_by_proc(proc)
            elif self.os == "mac":
                self.scm.kill_proc_by_proc(proc)
            else:
                raise KeyError("The OS is wrong!")
        except AssertionError, e:
            raise PidTerminalError(e)

    def kill_proc_by_pid(self, pid):
        """
        kill process by process pid.
        """
        try:
            if self.os == "windows":
                self.scw.kill_proc_by_pid(pid)
            elif self.os == "mac":
                self.scm.kill_proc_by_pid(pid)
            else:
                raise KeyError("The OS is wrong!")
        except AssertionError, e:
            raise PidTerminalError(e)

    def set_appium_log_addr(self):
        """
        set appium server log repository path.
        """
        if self.os == "windows":
            addr = self.scw.set_appium_log_addr()
        elif self.os == "mac":
            addr = self.scm.set_appium_log_addr()
        else:
            raise KeyError("The OS is wrong!")

        return addr
