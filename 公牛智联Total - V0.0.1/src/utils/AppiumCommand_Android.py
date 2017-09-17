# coding=utf-8
import time


class AppiumCommandAndroid(object):
    def send_keys(self, element, keys, driver):
        time.sleep(0.1)
        element.send_keys(keys)
        time.sleep(0.1)
        self.hide_keyboard(element, driver)

    def get_attribute(self, element, name):
        if name == "enabled":
            attribute_value = str(element.is_enabled()).lower()
        elif name == "is_displayed":
            attribute_value = str(element.is_displayed()).lower()
        else:
            attribute_value = element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, element, driver):
        driver.hide_keyboard()

    def get_location(self, element):
        location = element.location
        size = element.size
        location = dict(location, **size)
        x = int(location["x"])
        y = int(location["y"])
        height = int(location["height"])
        width = int(location["width"])
        centre = (x + width / 2, y + height / 2)
        location["centre"] = centre
        return location

    def swipe(self, x1, y1, x2, y2, step, driver):
        window_size = driver.get_window_size()
        height = window_size["height"]
        width = window_size["width"]
        driver.swipe(int(width * x1), int(height * y1), int(width * x2), int(height * y2), step)
