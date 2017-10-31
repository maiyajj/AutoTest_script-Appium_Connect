# coding=utf-8
from AppiumCommand_Android import *
from AppiumCommand_iOS import *


class AppiumCommand(object):
    """
    API.
    Re encapsulate the android & ios appium command.
    """
    def __init__(self, phone_os):
        self.phone_os = phone_os

    def send_keys(self, element, keys, driver):
        if self.phone_os == "Android":
            return AppiumCommandAndroid().send_keys(element, keys, driver)
        elif self.phone_os == "iOS":
            return AppiumCommandIos().send_keys(element, keys, driver)
        else:
            raise KeyError("The OS is wrong!")

    def get_attribute(self, element, name):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid().get_attribute(element, name)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos().get_attribute(element, name)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value

    def hide_keyboard(self, element, driver):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid().hide_keyboard(element, driver)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos().hide_keyboard(element, driver)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value

    def get_location(self, element):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid().get_location(element)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos().get_location(element)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value

    def swipe(self, x1, y1, x2, y2, step, driver):
        if self.phone_os == "Android":
            attribute_value = AppiumCommandAndroid().swipe(x1, y1, x2, y2, step, driver)
        elif self.phone_os == "iOS":
            attribute_value = AppiumCommandIos().swipe(x1, y1, x2, y2, step, driver)
        else:
            raise KeyError("The OS is wrong!")
        return attribute_value
