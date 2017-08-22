# coding=utf-8
import os
import re


class PortBindError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ShellCommandMac(object):
    def __init__(self):
        pass

    def kill_zombie_proc(self):
        os.system("killall -9 idevicesyslog")
        os.system("killall -9 mdworker")


    def kill_other_python(self):
        port = re.findall(r"Python.+?(\d+) .+", os.popen("lsof -c Python").read())
        for i in [i for i in set(port) if str(os.getpid()) != i]:
            os.popen("kill -9 %s" % i)

        self.kill_zombie_proc()

    def find_proc_and_pid_by_port(self, port):
        '''

        :param port:
        :return:(proc, pid)
        '''
        try:
            int(port)
        except ValueError:
            raise KeyError("key must be port! Is int, but real %s!" % type(port))
        except TypeError:
            raise KeyError("key must be port! Is int, but real %s!" % type(port))
        command = 'lsof -i:%s' % port  # 判断端口是否被占用
        find_pid = re.findall(r"(.+?) .+?(\d+).+LISTEN.+?", os.popen(command).read())

        self.kill_zombie_proc()
        return find_pid

    def find_proc_and_pid_by_pid(self, pid):
        '''

        :param pid:
        :return:
        '''
        try:
            int(pid)
        except ValueError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        except TypeError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        command = 'lsof -p %s' % pid
        find_pid = list(set(re.findall(r"(.+?) .+?(\d+).+", os.popen(command).read())))

        self.kill_zombie_proc()
        return find_pid

    def find_proc_and_pid_by_proc(self, proc):
        '''

        :param proc:
        :return:
        '''
        command = 'lsof -c %s' % proc
        find_pid = list(set(re.findall(r"(.+?) .+?(\d+).+", os.popen(command).read())))

        self.kill_zombie_proc()
        return find_pid

    def kill_proc_by_proc(self, proc):
        if not isinstance(proc, str):
            raise KeyError("key must be process name! Is string, but real %s!" % type(proc))

        command = 'killall -9 %s' % proc  # 通过进程名杀死进程
        os.popen(command)
        self.kill_zombie_proc()
        if self.find_proc_and_pid_by_proc(proc) == []:
            print u"终止 %s 进程。" % proc
        else:
            raise PortBindError("kill %s fail." % proc)

    def kill_proc_by_pid(self, pid):
        try:
            int(pid)
        except ValueError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))
        except TypeError:
            raise KeyError("key must be pid! Is int, but real %s!" % type(pid))

        command = 'kill -9 %s' % pid  # 通过pid杀死进程
        os.popen(command)
        self.kill_zombie_proc()
        if self.find_proc_and_pid_by_pid(pid) == []:
            print u"终止 PID %s。" % pid
        else:
            raise PortBindError("kill %s fail." % pid)

    def set_appium_log_addr(self):
        code = ["utf-8", "gbk"]
        addr = None
        for i in code:
            try:
                addr = os.getcwd().decode(i)
                break
            except UnicodeDecodeError:
                pass
        if addr is None:
            raise UnicodeDecodeError("%s codec can't decode bytes in os.getcwd()" % code)
        else:
            return addr
