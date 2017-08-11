# coding=utf-8

class AppiumCommandAndroid(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, keys, driver):
        self.element.send_keys(keys)
        self.hide_keyboard(driver)

    def get_attribute(self, name):
        attribute_value = self.element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, driver):
        driver.hide_keyboard()

    def get_location(self):
        location = self.element.location
        size = self.element.size
        location = dict(location, **size)
        self.x = int(location["x"])
        self.y = int(location["y"])
        self.height = int(location["height"])
        self.width = int(location["width"])
        self.centre = (self.x + self.width / 2, self.y + self.height / 2)
        location["centre"] = self.centre
        return location
