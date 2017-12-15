# coding=utf-8
from GetPhoneInfo_Android import *
from GetPhoneInfo_iOS import *


class GetPhoneInfo(ShellCommand):
    def title(self):
        print(u"***************************************************************")
        print(u"***            测试安卓手机可选择Windows或Mac OS            ***")
        print(u"***  测试iPhone暂不支持Windows，请务必在Mac OS上进行测试！  ***")
        print(u"***************************************************************")

    def select_port(self, selected_port):
        while True:
            if not self.find_proc_and_pid_by_port(selected_port):
                break
            else:
                selected_port += 1  # 端口已被占用，端口号+1

        return selected_port

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
        self.title()
        # 获取所有手机型号等信息 #
        self.kill_other_python()

        android_phone = GetPhoneInfoAndroid().get_phone_info()
        ios_phone = GetPhoneInfoIos().get_phone_info()
        device = dict(android_phone, **ios_phone)

        # Appium可使用的端口 #
        selected_port = 4725  # Appium服务初始选择端口
        for k in device.keys():
            need_port = ["port", "bp_port", "wda_port"]
            for ports in need_port:
                selected_port = self.select_port(selected_port)
                device[k][ports] = selected_port
                selected_port += 1
        '''
        device = {'8681-M02-0xa0a151df':
                      {'deviceName': '8681-M02',
                       'log_name': '8681-M02',
                       'bp_port': 4726,
                       'udid': '8681-M02-0xa0a151df',
                       'platformVersion': '5.1',
                       'model': '8681_M02',
                       'platformName': 'Android',
                       'port': 4725,
                       'dpi': {'width': '1080', 'height': '1920'}},
                  '6910ec366b7e396410c2be813bff57ef1c9ccc7e':
                      {'deviceName': 'iPhone6s Plus',
                       'log_name': 'iPhone6s Plus',
                       'wda_Port': 4729,
                       'bp_port': 4728,
                       'udid': '6910ec366b7e396410c2be813bff57ef1c9ccc7e',
                       'platformVersion': '10.3.2',
                       'model': 'iPhone6s Plus',
                       'platformName': 'ios',
                       'port': 4727,
                       'dpi': {'width': 1080, 'height': 1920}}}
        '''
        return device
