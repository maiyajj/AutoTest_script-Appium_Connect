# coding=utf-8

class AppiumCommandIos(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, value):
        self.element.set_value(value)

    def get_attribute(self, name):
        '''
        Valid attribute names are: (
        accessibilityContainer,
        accessible,
        enabled,
        frame,
        label,
        name,
        rect,
        type,
        value,
        visible,
        wdAccessibilityContainer,
        wdAccessible,
        wdEnabled,
        wdFrame,
        wdLabel,
        wdName,
        wdRect,
        wdType,
        wdValue,
        wdVisible
        '''
        if name == "checked":
            try:
                attribute_value = self.element.get_attribute("wdValue")
                if attribute_value is None:
                    attribute_value = 'false'
                else:
                    raise ValueError()
            except AttributeError:
                attribute_value = 'true'
        elif name == "name":
            attribute_value = self.element.get_attribute("value")
        else:
            attribute_value = self.element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, driver):
        location = self.element.location
        x = location["x"] - 1
        y = location["y"] - 1
        driver.tap([(x, y)])
        driver.hide_keyboard()
