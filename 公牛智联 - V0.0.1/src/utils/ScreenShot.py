# coding=utf-8
import os
from multiprocessing import Process


class ScreenShot(object):
    def __init__(self, folder, adb_screen, screen_shot):
        screen = Process(target=self.run, args=(folder, adb_screen, screen_shot))
        screen.start()
        screen.join()

    def run(self, folder, adb_screen, screen_shot):
        command = "adb pull /sdcard/Appium/%s/%s ./screenshots/" % (folder, adb_screen)
        os.popen(command)

        os.renames("./screenshots/%s" % adb_screen, "./screenshots/%s" % screen_shot)
