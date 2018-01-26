# coding=utf-8
from .ShellCommand import *


class GetPhoneInfoIos(ShellCommand):
    def check_port(self):
        self.os = self.get_os()
        # 判断***端口是否被占用
        pass

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
        device_list = self.get_phone_udid_for_ios()
        for i in device_list:
            device[i] = {"udid": i}  # {udid:{"udid": udid}}

        # 获取多个设备的信息
        phone_index = {"iPhone7,2": {"name": "iPhone6", "dpi": [1334, 750]},
                       "iPhone8,1": {"name": "iPhone6s", "dpi": [1334, 750]},
                       "iPhone8,2": {"name": "iPhone6sPlus", "dpi": [1920, 1080]},
                       "iPhone6,1": {"name": "iPhone5s", "dpi": [1136, 640]}}
        for k, v in device.items():
            phone_info = os.popen("ideviceinfo -u %s" % k).read()
            # 系统版本号 #
            device[k]["platformVersion"] = re.findall("ProductVersion: (.+)", phone_info)[0]

            # 设备型号 #
            device_name = re.findall("ProductType: (.+)", phone_info)[0]
            device[k]["model"] = device[k]["deviceName"] = phone_index[device_name]["name"]

            # 系统名称 IOS/ANDROID #
            device[k]["platformName"] = "iOS"

            # 设备分辨率 #
            device[k]["dpi"] = {}
            device[k]["dpi"]['height'] = phone_index[device_name]["dpi"][0]
            device[k]["dpi"]['width'] = phone_index[device_name]["dpi"][1]

            # 设备运行log文件名称 #
            device[k]["log_name"] = "%s-%s" % (v["deviceName"], v["udid"][:15])

            # PC OS
            device[k]["os"] = self.os
        '''
        device = {'6910ec366b7e396410c2be813bff57ef1c9ccc7e':
                      {'deviceName': 'iPhone6s Plus',
                       'log_name': 'iPhone6s Plus',
                       'udid': '6910ec366b7e396410c2be813bff57ef1c9ccc7e',
                       'platformVersion': '10.3.2',
                       'model': 'iPhone6s Plus',
                       'platformName': 'iOS',
                       'os': 'windows',
                       'dpi': {'width': 1080, 'height': 1920}}}
        '''
        return device
