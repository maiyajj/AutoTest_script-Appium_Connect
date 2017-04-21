# coding=utf-8
from GetPhoneInfo import *


class LaunchAppiumServices(object):
    def __init__(self, devices):
        command = "appium -a 127.0.0.1 -p %s -bp %s -U  %s  --no-reset" % (
            device[devices]["port"], device[devices]["bp_port"], device[devices]["udid"])
        os.system(command)
