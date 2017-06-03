# coding=utf-8
import os
import re


class GetPhoneInfo(object):
    def __init__(self):
        pass

    def get_system_info(self):
        system = os.name
        if system == "nt":
            return "windows"
        if system == "posix":
            return "mac"

    def check_port(self):
        self.system = self.get_system_info()
        # 判断adb端口是否被占用
        try:
            if self.system == "windows":
                self.commond = "taskkill /f /t /im adb.exe"
                command = 'netstat -aon|findstr 5037'  # 判断5037端口是否被占用
                port = re.findall(r".+LISTENING.+?(\d+)", os.popen(command).read())[0]
                command = 'tasklist|findstr %s' % port
                proc = re.findall(r"(.+?) .+?\d+", os.popen(command).read())[0]
                command = 'taskkill /f /t /pid %s' % port
                os.popen(command)
                print u"关闭%s" % proc
            elif self.system == "mac":
                self.commond = "killall -9 adb"
                command = 'lsof -i:5037'  # 判断5037端口是否被占用
                proc = re.findall(r"(.+?) .+LISTEN.+?", os.popen(command).read())[0]
                command = 'killall -9 %s' % proc
                os.popen(command)
                print u"关闭%s" % proc
        except IndexError:
            print u"5037端口未占用"
        finally:
            # 杀死adb进程
            os.system(self.commond)

    def get_phone_info(self):
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

        self.check_port()
        phone_index = {"iPhone8,2": {"name": "iPhone6s Plus", "dpi": [1920, 1080]},
                       "iPhone6,1": {"name": "iPhone5s", "dpi": [1136, 640]}}
        device = {}  # 初始化字典，包含所需设备信息
        # 获取多个设备的udid #
        command = "idevice_id -l"
        devices = os.popen(command).read()
        device_list = re.findall("(.+)", devices)
        for i in device_list:
            device[i] = {"udid": i}  # {udid:{"udid": udid, "model": model}}

        print device
        # 获取多个设备的信息
        selected_port = 4725  # Appium服务初始选择端口
        for k, v in device.items():
            phone_info = os.popen("ideviceinfo -u %s" % k).read()
            # 系统版本号 #
            device[k]["platformVersion"] = re.findall("ProductVersion: (.+)", phone_info)[0]

            # 设备型号 #
            device_name = re.findall("ProductType: (.+)", phone_info)[0]
            device[k]["model"] = device[k]["deviceName"] = phone_index[device_name]["name"]

            # 系统名称 IOS/ANDROID #
            device[k]["platformName"] = "ios"

            # 设备分辨率 #
            device[k]["dpi"] = {}
            device[k]["dpi"]['height'] = phone_index[device_name]["dpi"][0]
            device[k]["dpi"]['width'] = phone_index[device_name]["dpi"][1]

            # Appium可使用的端口 #
            need_port = ["port", "bp_port", "wda_port"]
            for ports in need_port:
                while True:
                    try:
                        if self.system == "windows":
                            command = 'netstat -aon|findstr %s' % selected_port  # 判断当前端口是否被占用
                        elif self.system == "mac":
                            command = 'lsof -i:%s' % selected_port  # 判断当前端口是否被占用

                        used_port = re.findall(r".+LISTEN.+", os.popen(command).read())[0]
                        selected_port += 1  # 端口已被占用，端口号+1
                        del used_port
                    except IndexError:
                        device[k][ports] = selected_port  # appium与设备通讯端口
                        selected_port += 1
                        break

            # 设备运行log文件名称 #
            device[k]["log_name"] = "%s-%s" % (v["deviceName"], v["udid"][:15])

        '''
        device: {'6910ec366b7e396410c2be813bff57ef1c9ccc7e':
                     {'deviceName': 'iPhone6s Plus',
                      'log_name': 'iPhone6s Plus',
                      'wda_Port': 4727, 
                      'bp_port': 4726, 
                      'udid': '6910ec366b7e396410c2be813bff57ef1c9ccc7e',
                      'platformVersion': '10.3.2',
                      'model': 'iPhone6s Plus',
                      'platformName': 'ios', 
                      'port': 4725, 
                      'dpi': {'width': 1080, 'height': 1920}}}
        '''
        return device
