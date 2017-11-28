# coding=utf-8
import os

command = "adb shell /system/bin/screencap -p /sdcard/screenshot.png"
os.popen(command)

command = "adb pull /sdcard/screenshot.png F:/BaiduYunDownload"
os.popen(command)
