# coding=utf-8
import os
import re


def get_phone_info():
    """
    获取手机信息：
    udid,
    系统版本号
    系统名称 IOS/ANDROID
    设备型号
    设备分辨率
    Appium可使用的端口
    :return: dict: device{}
    """

    device = {}  # 初始化字典，包含所需设备信息

    # 判断adb端口是否被占用
    try:
        command = 'netstat -aon|findstr 5037'  # 判断5037端口是否被占用
        port = re.findall(r".+LISTENING.+?(\d+)", os.popen(command).read())[0]
        command = 'taskkill /f /t /pid %s' % port
        os.popen(command)
        print u"关闭%s" % port
    except IndexError:
        print u"5037端口未占用"

    # 杀死adb进程
    command = "taskkill /f /t /im adb.exe"
    os.system(command)

    # 获取多个设备的udid #
    command = "adb devices -l"
    devices = os.popen(command).read()
    device_list = re.findall("(.+?)device product.+?model:(.+?) ", devices)
    for i in device_list:
        i0 = i[0].split()
        i1 = i[1].split()
        device[i0[0]] = {"udid": i0[0], "model": i1[0]}  # {udid:{"udid": udid, "model": model}}

    # 获取多个设备的信息
    selected_port = 4725  # Appium服务初始选择端口
    for k, v in device.items():

        # 系统版本号 #
        command = "adb -s %s shell getprop ro.build.version.release" % v["udid"]
        device[k]["platformVersion"] = os.popen(command).read().split()[0]

        # 设备型号 #
        command = "adb -s %s shell getprop ro.product.model" % v["udid"]
        device[k]["deviceName"] = os.popen(command).read().split()[0]

        # 系统名称 IOS/ANDROID #
        command = "adb -s %s shell getprop net.bt.name" % v["udid"]
        device[k]["platformName"] = os.popen(command).read().split()[0]

        # 设备分辨率 #
        device[k]["dpi"] = {}
        command = "adb -s %s shell dumpsys window displays" % v["udid"]
        dpi = re.findall("init=(.+?) ", os.popen(command).read())[0].split("x")
        device[k]["dpi"]['width'] = dpi[0]
        device[k]["dpi"]['height'] = dpi[1]

        # Appium可使用的端口 #
        for i in xrange(selected_port, selected_port + 25):  # 提供25个可选端口
            try:
                command = 'netstat -aon|findstr %s' % i  # 判断当前端口是否被占用
                used_port = re.findall(r".+LISTENING.+", os.popen(command).read())[0]
                selected_port += 1  # 端口已被占用，端口号+1
                del used_port
            except IndexError:
                device[k]["port"] = i  # appium与设备通讯端口
                selected_port += 1
                try:
                    command = 'netstat -aon|findstr %s' % (i + 1)  # 判断当前端口是否被占用
                    used_port = re.findall(r".+LISTENING.+", os.popen(command).read())[0]
                    selected_port += 1  # 端口已被占用，端口号+1
                    del used_port
                except IndexError:
                    device[k]["bp_port"] = i + 1  # appium的bp端口
                    selected_port += 1
                    break

        # 设备运行log文件名称 #
        device[k]["log_name"] = v["deviceName"]

    '''
    device: {udid:{'deviceName': '8681-M02', 
                   'log_name': '8681-M02', 
                   'bp_port': 4726, 
                   'udid': '8681-M02-0xa0a151df',
                   'platformVersion': '5.1', 
                   'model': '8681_M02', 
                   'platformName': 'Android', 
                   'port': 4725, 
                   'dpi': {'width': '1080', 'height': '1920'}}}
    '''
    return device
