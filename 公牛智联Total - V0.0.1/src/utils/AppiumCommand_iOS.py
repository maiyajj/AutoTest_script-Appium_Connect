# coding=utf-8

class AppiumCommandIos(object):
    def send_keys(self, element, value, driver):
        element.set_value(value)
        self.hide_keyboard(element, driver)

    def get_attribute(self, element, name):
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
            attribute_value = element.get_attribute("wdValue")
            if attribute_value is None:
                attribute_value = 'false'
            else:
                attribute_value = 'true'
        elif name == "name":
            attribute_value = element.get_attribute("value")
        elif name == "enabled":
            attribute_value = str(element.is_enabled()).lower()
        elif name == "is_displayed":
            attribute_value = str(element.is_displayed()).lower()
        else:
            attribute_value = element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, element, driver):
        location = element.location
        x = location["x"] - 1
        y = location["y"] - 1
        driver.tap([(x, y)])
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
