# coding=utf-8
import os
import re


# 判断adb端口是否被占用
def check_port():
    while True:
        try:
            command = 'netstat -aon|findstr 5037'  # 判断5037端口是否被占用
            data = os.popen(command).read().split("\n")
            data = [i for i in data if re.findall(r".+LIS.+?(\d+)", i) != []]
            port = [re.findall(r".+LIS.+?(\d+)", i)[0] for i in data]
            print port
            for i in port:
                command = 'tasklist|findstr %s' % i
                proc = re.findall(r"(.+?) .+?\d+", os.popen(command).read())
                command = 'taskkill /f /t /pid %s' % i
                os.popen(command)
                print u"关闭%s" % proc
        except IndexError:
            print u"5037端口未占用"
            break


check_port()
