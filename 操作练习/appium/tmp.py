# coding:utf-8
import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

command = "adb devices -l"
devices = os.popen(command).read()
device_list = re.findall("(.+?)device product.+?model:(.+?) ", devices)
device = {}
for i in device_list:
    i0 = i[0].split()
    i1 = i[1].split()
    device[i1[0]] = {"udid": i0[0]}
for k, v in device.items():
    command = "adb -s %s shell getprop ro.build.fingerprint" % v["udid"]
    platformVersion = re.findall(r":(.+?)/", os.popen(command).read())[0]
    device[k]["platformVersion"] = platformVersion

    command = "adb -s %s shell getprop ro.build.display.id" % v["udid"]
    deviceName = os.popen(command).read().split()[0]
    device[k]["deviceName"] = deviceName

    command = "adb -s %s shell getprop net.bt.name" % v["udid"]
    platformName = os.popen(command).read().split()[0]
    device[k]["platformName"] = platformName

print device
command = "taskkill /f /t /im adb.exe"
os.system(command)
command = "appium -a 127.0.0.1 -p 4723  -U  %s  --no-reset" % device.values()[0]["udid"]
os.system(command)
