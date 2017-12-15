# coding=utf-8
import os
import re

import time


class ShellCommandWindows(object):
    """
    API
    The shell command of Windows.
    """

    def __init__(self):
        pass

    def kill_zombie_proc(self):
        """
        Kill zombie process.
        Avoid system resource crashes.
        nothing now.
        """
        pass

    def kill_other_python(self):
        """
        kill other python before launch this auto test tool.
        maybe some conflict
        """
        port = re.findall(r"python.exe.+?(\d+).+", os.popen("tasklist|findstr python").read())
        for i in [i for i in set(port) if str(os.getpid()) != i]:
            os.system("taskkill /f /t /pid %s" % i)

    def find_proc_and_pid_by_port(self, port):
        """
        find process and pid by process port for Windows.
        int -> list
        :return:[(proc1, pid1), (proc2, pid2)] [str, int]
        """
        try:
            int(port)
        except ValueError:
            raise KeyError("key must be port! Is int, but real %s!" % type(port))
        except TypeError:
            raise KeyError("key must be port! Is int, but real %s!" % type(port))
        command = 'netstat -aon|findstr %s' % port  # 判断端口是否被占用
        bind_pid = set(re.findall(r".+LISTEN.+?(\d+)", os.popen(command).read()))
        find_pid = []
        for i in bind_pid:
            command = 'tasklist|findstr %s' % i
            find_pid.append(re.findall(r"(.+?) .+?(\d+).+", os.popen(command).read()))
        find_pid = sum(find_pid, [])  # 递归列表[[(),()],[()]] → [(),(),()]
        find_pid = map(lambda x: (x[0], int(x[1])), find_pid)

        return find_pid

    def find_proc_and_pid_by_pid(self, pid):
        """
        find process and pid by process pid for Windows.
        int -> list
        :return:[(proc1, pid1), (proc2, pid2)] [str, int]
        """
        try:
            int(pid)
        except ValueError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        except TypeError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        command = 'tasklist|findstr %s' % pid
        find_pid = list(set(re.findall(r"(.+?) .+?(\d+).+", os.popen(command).read())))
        find_pid = map(lambda x: (x[0], int(x[1])), find_pid)

        return find_pid

    def find_proc_and_pid_by_proc(self, proc):
        """
        find process and pid by process name for Windows.
        str -> list
        :return:[(proc1, pid1), (proc2, pid2)] [str, int]
        """
        if not isinstance(proc, str):
            raise KeyError("key must be process name! Is string, but real %s!" % type(proc))
        command = 'tasklist|findstr %s' % proc
        find_pid = list(set(re.findall(r"(.+?) .+?(\d+).+", os.popen(command).read())))
        find_pid = map(lambda x: (x[0], int(x[1])), find_pid)

        return find_pid

    def kill_proc_by_proc(self, proc):
        """
        kill process by process name for Windows.
        """
        if not isinstance(proc, str):
            raise KeyError("key must be process name! Is string, but real %s!" % type(proc))
        if ".exe" in proc:
            command = 'taskkill /f /t /im %s' % proc  # 通过进程名杀死进程
        else:
            command = 'taskkill /f /t /im %s.exe' % proc  # 通过进程名杀死进程
        os.system(command)
        time.sleep(1)
        if self.find_proc_and_pid_by_proc(proc):
            raise AssertionError("kill %s fail." % proc)
        else:
            print(u"终止 %s 进程。" % proc)

    def kill_proc_by_pid(self, pid):
        """
        kill process by process pid for Windows.
        """
        try:
            int(pid)
        except ValueError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        except TypeError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))

        command = 'taskkill /f /t /pid %s' % pid  # 通过pid杀死进程
        os.system(command)
        time.sleep(1)
        if self.find_proc_and_pid_by_pid(pid):
            raise AssertionError("kill %s fail." % pid)
        else:
            print(u"终止 PID %s。" % pid)

    def set_appium_log_addr(self):
        """
        set appium server log repository path for Windows.
        """
        # addr = os.getenv("Temp")
        addr = os.getcwd()
        addr = os.path.join(addr, "debug")
        return addr
