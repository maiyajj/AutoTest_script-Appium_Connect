# coding=utf-8
from AppiumCommand_Android import *
from AppiumCommand_iOS import *


class AppiumCommand(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os

    def send_keys(self, element, keys):
        if self.phone_os == "Android":
            return AppiumCommandAndroid(element).send_keys(keys)
        elif self.phone_os == "iOS":
            return AppiumCommandIos(element).send_keys(keys)
        else:
            raise KeyError("The OS is wrong!")

    def get_attribute(self, element, name):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid(element).get_attribute(name)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos(element).get_attribute(name)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value

    def hide_keyboard(self, element, driver):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid(element).hide_keyboard(driver)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos(element).hide_keyboard(driver)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value
