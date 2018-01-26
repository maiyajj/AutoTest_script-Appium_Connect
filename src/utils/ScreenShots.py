# coding=utf-8
import os


class ScreenShots(object):
    def __init__(self, device_info):
        self.udid = device_info["udid"]
        self.path = device_info["debug_path"]

    def screenshots(self):
        adb_screen = "screenshots.png"

        os.system("adb -s %s shell mkdir /sdcard/Appium" % self.udid)

        command = "adb -s %s shell /system/bin/screencap -p /sdcard/Appium/%s" % (self.udid, adb_screen)
        os.system(command)

        command = "adb -s %s pull /sdcard/Appium/%s %s" % (self.udid, adb_screen, self.path)
        os.system(command)
