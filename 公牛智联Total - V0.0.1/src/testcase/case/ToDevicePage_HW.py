# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *
from src.utils.ReadConf import *


class ToDevicePageHW(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.driver = driver
        self.logger = logger
        self.device_info = device_info
        self.page = page_element
        self.ac = AppiumCommand(self.device_info["platformName"])
        self.debug = self.device_info["debug"]
        self.user = conf["user_and_pwd"][self.device_info["udid"]][self.device_info["app"]]
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, self.page, self.logger, self.debug)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case()

    # 关闭广告
    def close_ad(self):
        try:
            self.wait_widget(self.page["ad_popup"]["title"])
            self.logger.info(u"[APP_INF] APP有广告")
            self.widget_click(self.page["ad_popup"]["skip"],
                              wait_time1=5,
                              log_record=0)
            self.logger.info(u"[APP_INF] 关闭广告")
        except TimeoutException:
            pass

    # 检查APP是否升级，取消
    def check_update(self):
        try:
            self.wait_widget(self.page["update_popup"]["title"])
            self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
            self.widget_click(self.page["update_popup"]["cancel"],
                              log_record=0)
            self.logger.info(u"[APP_INF] 取消更新")
        except TimeoutException:
            pass

    # 登录至APP主页面
    def login_to_device(self):
        # TODO: 华为账号退出登录，由于APP的安全限制暂未定是否要做。
        pass

    # 用例动作
    def case(self):
        self.close_ad()
        self.check_update()
        self.login_to_device()
