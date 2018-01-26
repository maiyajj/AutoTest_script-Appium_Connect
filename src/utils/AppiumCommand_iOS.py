# coding=utf-8
import time

from lxml import etree


class AppiumCommandIos(object):
    """
    Re encapsulate the ios appium command.
    """

    def send_keys(self, element, value, driver):
        element.set_value(value)
        time.sleep(0.1)
        self.hide_keyboard(element, driver)

    def get_attribute(self, element, name, driver=None, elem=None):
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
            attribute_value = element.get_attribute("name")
            if attribute_value == "" or None:
                attribute_value = element.get_attribute("value")
        elif name == "enabled":
            attribute_value = str(element.is_enabled()).lower()
        elif name == "is_displayed":
            windows_size = driver.get_window_size()
            lc = element.location
            if 0 <= lc["x"] <= windows_size["width"] and 0 <= lc["y"] <= windows_size["height"]:
                attribute_value = "true"
            else:
                attribute_value = "false"
                # attribute_value = str(element.is_displayed()).lower()
        else:
            try:
                attribute_value = element.get_attribute(name)
            except BaseException:
                tree = etree.HTML(driver.page_source.encode("utf-8"))
                attribute_value = tree.xpath(elem[0].lower())[0].get(name.lower())
        return attribute_value

    def hide_keyboard(self, element, driver):
        """
        hide_keyboard doesn`t work in ios.
        So click on the top left corner of the keyboard.
        """
        location = element.location
        x = location["x"] - 1
        y = location["y"] - 1
        driver.tap([(x, y)])
        driver.hide_keyboard()

    def get_location(self, element):
        """
        Get the centre location of element.
        """
        location = element.location
        size = element.size
        location = dict(location, **size)
        x = int(location["x"])
        y = int(location["y"])
        height = int(location["height"])
        width = int(location["width"])
        centre = (x + width / 2, y + height / 2)
        return x, y, width, height, centre

    def swipe(self, x1, y1, x2, y2, driver, step, percent):
        if percent:
            window_size = driver.get_window_size()
            height = window_size["height"]
            width = window_size["width"]
            driver.swipe(int(width * x1), int(height * y1), int(width * (x2 - x1)), int(height * (y2 - y1)), step)
        else:
            driver.swipe(x1, y1, (x2 - x1), (y2 - y1), step)
