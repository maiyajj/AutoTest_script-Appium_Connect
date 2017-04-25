# coding=utf-8
import inspect
import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_phone_info():
    command = "adb devices -l"
    devices = os.popen(command).read()
    device_list = re.findall("(.+?)device product.+?model:(.+?) ", devices)
    device = {}
    for i in device_list:
        i0 = i[0].split()
        i1 = i[1].split()
        device[i0[0]] = {"udid": i0[0], "model": i1[0]}
    selected_port = 4725
    for k, v in device.items():
        command = "adb -s %s shell getprop ro.build.version.release" % v["udid"]
        platformVersion = os.popen(command).read().split()[0]
        device[k]["platformVersion"] = platformVersion

        command = "adb -s %s shell getprop ro.product.model" % v["udid"]
        deviceName = os.popen(command).read().split()[0]
        device[k]["deviceName"] = deviceName

        command = "adb -s %s shell getprop net.bt.name" % v["udid"]
        platformName = os.popen(command).read().split()[0]
        device[k]["platformName"] = platformName

        command = "adb -s %s shell dumpsys window displays" % v["udid"]
        try:
            device[k]["dpi"] = {}
            DPI = os.popen(command).read()
            tmp = re.findall("init=(.+?) ", DPI)[0].split("x")
            device[k]["dpi"]['width'] = tmp[0]
            device[k]["dpi"]['height'] = tmp[1]
        except WindowsError:
            pass
        for i in xrange(selected_port, 4750):
            command = 'netstat -aon|findstr %s' % i
            used_port = re.findall(r".+LISTENING.+", os.popen(command).read())
            if used_port == []:
                device[k]["port"] = i
                selected_port += 1
                device[k]["bp_port"] = i + 1
                selected_port += 1
                break
            else:
                selected_port += 1
        device[k]["log_name"] = v["deviceName"]
    print inspect.stack()
    return device
