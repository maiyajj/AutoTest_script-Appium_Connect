# coding=utf-8
import time

from lxml import etree


class AppiumCommandAndroid(object):
    """
    Re encapsulate the android appium command.
    """

    def send_keys(self, element, keys, driver):
        time.sleep(0.1)
        element.send_keys(keys)
        time.sleep(0.1)
        self.hide_keyboard(element, driver)

    def get_attribute(self, element, name, driver=None, elem=None):
        if name == "enabled":
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
        driver.hide_keyboard()

    def get_location(self, element):
        """
        Get the centre location of element.
        """
        location = element.location
        size = element.size
        px = element.px_attr["px"]
        location = dict(location, **size)
        x = int(location["x"])
        y = int(location["y"])
        height = int(location["height"])
        width = int(location["width"])
        if px:
            x, y, width, height = int(x + width * px[0]), int(y + height * px[1]), 20, 20
        centre = (int(x + width / 2), int(y + height / 2))
        return x, y, width, height, centre

    def swipe(self, x1, y1, x2, y2, driver, step, percent):
        if percent:
            window_size = driver.get_window_size()
            height = window_size["height"]
            width = window_size["width"]
            driver.swipe(int(width * x1), int(height * y1), int(width * x2), int(height * y2), step)
        else:
            driver.swipe(x1, y1, x2, y2, step)
