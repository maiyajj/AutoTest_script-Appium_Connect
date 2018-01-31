# coding=utf-8
from .ShellCommand import *


class GetPhoneInfoAndroid(ShellCommand):
    def check_port(self):
        self.os = self.get_os()
        # 判断adb端口是否被占用
        try:
            for i in self.find_proc_and_pid_by_port(5037):  # 查找占用5037端口进程
                self.kill_proc_by_pid(i[1])  # 杀死占用5037端口进程
                print(u"进程 %s" % i[0])
        except IndexError:
            print(u"5037端口未占用")

    def get_phone_info(self):
        """
        获取手机信息：
        udid,
        系统版本号
        系统名称 IOS/ANDROID
        设备型号
        设备分辨率
        :return: dict: device{}
        """
        self.check_port()

        device = {}  # 初始化字典，包含所需设备信息

        # 获取多个设备的udid #
        device_list = self.get_phone_udid_for_android()
        for i in device_list:
            device[i] = {"udid": i}  # {udid:{"udid": udid}}

        # 获取多个设备的信息
        for k, v in device.items():
            command = "adb -s %s shell getprop" % v["udid"]
            value = subprocess.check_output(command).decode("utf-8")

            # 系统版本号 #
            device[k]["platformVersion"] = re.findall("\[ro.build.version.release]: \[(.+?)]", value)[0]

            # 设备型号 #
            device[k]["deviceName"] = re.findall("\[ro.product.model]: \[(.+?)]", value)[0]
            device[k]["model"] = device[k]["deviceName"]

            # 系统名称 IOS/ANDROID #
            device[k]["platformName"] = re.findall("\[net.bt.name]: \[(.+?)]", value)[0]

            # 设备分辨率 #
            device[k]["dpi"] = {}
            command = "adb -s %s shell dumpsys window displays" % v["udid"]
            dpi = re.findall("init=(.+?) ", subprocess.check_output(command).decode("utf-8"))[0].split("x")
            device[k]["dpi"]['width'] = dpi[0]
            device[k]["dpi"]['height'] = dpi[1]

            # 设备运行log文件名称 #
            device[k]["log_name"] = v["deviceName"]

            # PC OS
            device[k]["os"] = self.os
        '''
        device = {'8681-M02':
                     {'deviceName': '8681-M02',
                      'log_name': '8681-M02',
                      'udid': '8681-M02-0xa0a151df',
                      'platformVersion': '5.1',
                      'model': '8681_M02',
                      'platformName': 'Android',
                      'dpi': {'width': '1080', 'height': '1920'}}}
        '''
        return device
