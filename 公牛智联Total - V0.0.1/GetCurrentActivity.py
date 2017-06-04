# coding=utf-8
import os
import re

command = 'adb.exe  shell "dumpsys window windows"'
output = os.popen(command).read()
current_activity = re.findall(r"mCurrentFocus=Window.+/(.+)}", output)[0]
print current_activity
