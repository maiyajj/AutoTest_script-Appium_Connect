# coding=utf-8

class AppiumCommandIos(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, value):
        self.element.set_value(value)

    def get_attribute(self, name):
        if name == "id":
            attribute_value = self.element.get_attribute("id")
        elif name == "name":
            attribute_value = self.element.get_attribute("name")
        elif name == "checked":
            try:
                attribute_value = self.element.get_attribute("wdValue")
                if attribute_value is None:
                    attribute_value = 'false'
                else:
                    raise ValueError()
            except AttributeError:
                attribute_value = 'true'
        else:
            attribute_value = self.element.get_attribute(name)
        return attribute_value
