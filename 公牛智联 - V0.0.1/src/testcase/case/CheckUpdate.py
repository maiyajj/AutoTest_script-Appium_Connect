# coding:utf-8
import os,re
command = "adb shell dumpsys window displays"
devices = os.popen(command).read()
tmp = re.findall("init=(.+?) ", devices)[0].split("x")
print tmp
