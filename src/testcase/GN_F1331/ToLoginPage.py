# coding=utf-8
import os

from src.common.WidgetCheckUnit import *


class ToLoginPage(object):
    def __init__(self, driver, device_info):
        self.driver = driver
        self.page = device_info["page"]  # 页面元素库
        self.debug = device_info["debug"]  # debug日志
        self.ac = device_info["ac"]  # appium command
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, device_info)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case()

    # 引导页
    def check_splash(self):
        while True:
            try:
                self.wait_widget(self.page["splash_popup"]["title"])
                self.widget_click(self.page["splash_popup"]["skip"])
            except TimeoutException:
                try:
                    self.wait_widget(self.page["splash_popup"]["title"], 1, 0.5)
                except TimeoutException:
                    break

    # 检查APP是否升级，取消
    def check_update(self):
        try:
            self.wait_widget(self.page["update_popup"]["title"])
            self.debug.info(u"[APP_INF] APP有最新版本，可以更新")
            self.widget_click(self.page["update_popup"]["cancel"],
                              log_record=0)
            self.debug.info(u"[APP_INF] 取消更新")
        except TimeoutException:
            pass

    # 关闭广告
    def close_ad(self):
        try:
            self.wait_widget(self.page["close_ad_popup"]["title"])
            self.debug.info(u"[APP_INF] 页面有广告，关闭广告")
            self.widget_click(self.page["close_ad_popup"]["confirm"],
                              self.page["app_home_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    # 退出登录至登录界面
    def device_to_login(self):
        self.wait_widget(self.page["app_home_page"]["title"])
        self.widget_click(self.page["app_home_page"]["account_setting"],
                          self.page["account_setting_page"]["title"],
                          log_record=0)
        try:
            element = self.wait_widget(self.page["account_setting_page"]["username"])
            if self.ac.get_attribute(element, "name") == u'点击登录':
                self.debug.info(u"[APP_INF] 当前APP未登录，直接进入登录页")
                self.widget_click(self.page["account_setting_page"]["username"],
                                  self.page["login_page"]["title"],
                                  log_record=0)
            else:
                self.debug.info(u"[APP_INF] 当前APP已登录，退出进入登录页")
                self.widget_click(self.page["account_setting_page"]["help_setting"],
                                  self.page["help_setting_page"]["title"],
                                  log_record=0)

                self.ac.swipe(0.1, 0.9, 0.1, 0.4, self.driver)
                self.widget_click(self.page["help_setting_page"]["logout"],
                                  self.page["logout_popup"]["title"],
                                  log_record=0)

                self.widget_click(self.page["logout_popup"]["confirm"],
                                  self.page["login_page"]["title"],
                                  log_record=0)
        except TimeoutException:
            self.debug.info(u"[APP_INF] APP进入登录页面失败")
            self.driver.close_app()
            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            raise TimeoutException("ToLoginPage Error!")

    # 用例动作
    def case(self):
        self.check_splash()
        self.check_update()
        self.close_ad()
        self.device_to_login()
        self.wait_widget(self.page["login_page"]["title"])
        self.debug.info(u"[APP_INF] APP当前页面为登录页面")
