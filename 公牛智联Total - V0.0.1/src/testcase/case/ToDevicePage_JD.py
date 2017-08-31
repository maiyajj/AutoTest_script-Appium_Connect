# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *
from src.utils.ReadConf import *


class ToDevicePageJD(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.driver = driver
        self.logger = logger
        self.device_info = device_info
        self.page = page_element
        self.ac = AppiumCommand(self.device_info["platformName"])
        self.debug = self.device_info["debug"]
        self.user = conf["user_and_pwd"][self.device_info["udid"]][self.device_info["app"]]
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, self.page, self.logger)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        # 唤醒设备
        self.driver.tap([(10, 10)])
        time.sleep(0.01)
        self.case()

    def check_update(self):
        try:
            self.wait_widget(self.page["update_popup"]["title"], 1, 0.5)
            self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
            self.widget_click(self.page["update_popup"]["title"],
                              self.page["update_popup"]["cancel"],
                              self.page["god_page"]["title"],
                              log_record=0)
            self.logger.info(u"[APP_INF] 取消更新")
        except TimeoutException:
            pass

    def close_ad(self):
        try:
            self.wait_widget(self.page["close_ad_popup"]["title"], 1, 0.5)
            self.logger.info(u"[APP_INF] 页面有广告，关闭广告")
            self.widget_click(self.page["close_ad_popup"]["title"],
                              self.page["close_ad_popup"]["confirm"],
                              self.page["app_home_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    def login_to_device(self):
        try:
            pass
        except TimeoutException:
            pass

    def show_pwd(self):
        pass

    def case(self):
        # 用例动作
        i = 0
        while True:
            self.check_update()
            self.close_ad()
            self.login_to_device()
            try:
                self.wait_widget(self.page["app_home_page"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP当前页面为主页面")
                break
            except TimeoutException:
                pass
            i += 1
            if i > 3:
                raise TimeoutException("ToDevicePage Error!")
