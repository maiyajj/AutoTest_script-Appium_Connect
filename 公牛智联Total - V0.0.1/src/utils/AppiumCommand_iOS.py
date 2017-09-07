# coding=utf-8

class AppiumCommandIos(object):
    def __init__(self, element):
        self.element = element

    def send_keys(self, value, driver):
        self.element.set_value(value)
        self.hide_keyboard(driver)

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
            attribute_value = self.element.get_attribute("wdValue")
            if attribute_value is None:
                attribute_value = 'false'
            else:
                attribute_value = 'true'
        elif name == "name":
            attribute_value = self.element.get_attribute("value")
        elif name == "enabled":
            attribute_value = str(self.element.is_enabled()).lower()
        elif name == "is_displayed":
            attribute_value = str(self.element.is_displayed()).lower()
        else:
            attribute_value = self.element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, driver):
        location = self.element.location
        x = location["x"] - 1
        y = location["y"] - 1
        driver.tap([(x, y)])
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
