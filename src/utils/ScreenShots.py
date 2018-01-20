# coding=utf-8
import os


class ScreenShots(object):
    def __init__(self, device_info):
        self.udid = device_info["udid"]
        self.path = device_info["debug_path"]

    def screenshots(self):
        adb_screen = r"%s/screenshots.png" % self.udid

        os.system("adb shell mkdir /sdcard/Appium")
        os.system("adb shell mkdir /sdcard/Appium/%s" % self.udid)

        command = "adb -s %s shell /system/bin/screencap -p /sdcard/Appium/%s" % (self.udid, adb_screen)
        os.system(command)

        command = "adb -s %s pull /sdcard/Appium/%s %s" % (self.udid, adb_screen, self.path)
        os.system(command)
