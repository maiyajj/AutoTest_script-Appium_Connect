# coding=utf-8
import time

class AppiumCommandAndroid(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, keys, driver):
        time.sleep(0.1)
        self.element.send_keys(keys)
        time.sleep(0.1)
        self.hide_keyboard(driver)

    def get_attribute(self, name):
        if name == "enabled":
            attribute_value = str(self.element.is_enabled()).lower()
        elif name == "is_displayed":
            attribute_value = str(self.element.is_displayed()).lower()
        else:
            attribute_value = self.element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, driver):
        driver.hide_keyboard()

    def get_location(self):
        location = self.element.location
        size = self.element.size
        location = dict(location, **size)
        x = int(location["x"])
        y = int(location["y"])
        height = int(location["height"])
        width = int(location["width"])
        centre = (x + width / 2, y + height / 2)
        location["centre"] = centre
        return location
