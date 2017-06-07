# coding=utf-8

class AppiumCommandAndroid(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, keys):
        self.element.send_keys(keys)

    def get_attribute(self, name):
        if name == "id":
            attribute_value = self.element.get_attribute("id")
        elif name == "name":
            attribute_value = self.element.get_attribute("name")
        elif name == "checked":
            attribute_value = self.element.get_attribute("checked")
        else:
            attribute_value = self.element.get_attribute(name)
        return attribute_value
