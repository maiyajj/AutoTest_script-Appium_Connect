# coding=utf-8
import os
import re
import time

from data.Database import *


# FIXME：This module is not currently used. This module used for android toast.
class ScreenShot(object):
    def __init__(self, device_info, zentao_id, basename, logger):
        self.device_info = device_info
        self.zentao_id = zentao_id
        self.basename = basename
        self.logger = logger
        # self.run()

    def run(self):
        folder = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])
        screen_shot = (r"%s/%s - %s - %s - [%s]-[%s].png"
                       % (folder, database["program_loop_time"], database["case_location"],
                          self.zentao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S")))
        adb_screen = "%s/%s{%s}.png" % (folder, self.zentao_id, time.strftime("%Y-%m-%d.%H_%M_%S"))
        print screen_shot, adb_screen
        command = "adb -s %s shell /system/bin/screencap -p /sdcard/Appium/%s" % (self.device_info["udid"], adb_screen)
        os.popen(command)
        command1 = "adb -s %s shell du /sdcard/Appium/%s" % (self.device_info["udid"], adb_screen)

        screen_count = 3
        end_time = time.time() + 10
        while screen_count:
            try:
                time.sleep(1)
                len_adb_screen_file = int(re.findall(r"(.+?)/sdcard", os.popen(command1).read())[0].split()[0])
                print len_adb_screen_file
                if len_adb_screen_file != 0:
                    self.logger.info('[ADB]adb screen shot success!')
                    break
                elif time.time() > end_time:
                    self.logger.info('[ADB]adb screen shot failed!')
                    break
            except ValueError:
                screen_count -= 1
                self.logger.info('[ADB]adb find screen file failed still %s times!' % (screen_count + 1))

        command = "adb -s {0} pull /sdcard/Appium/{1} ./screenshots/{1}".format(self.device_info["udid"], adb_screen)
        pull_file = re.findall(r".+file pulled.+", os.popen(command).read())
        if pull_file is not []:
            self.logger.info('[ADB]adb screen shot put file to PC success!')
        else:
            self.logger.info('[ADB]adb screen shot put file to PC failed!')

        try:
            os.rename("./screenshots/%s" % adb_screen, "./screenshots/%s" % screen_shot)
            self.logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot success')
        except WindowsError:
            self.logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot failed')
