# coding=utf-8

class AppiumCommandAndroid(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, keys):
        self.element.send_keys(keys)

    def get_attribute(self, name):
        attribute_value = self.element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, driver):
        driver.hide_keyboard()
