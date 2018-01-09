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

    # app异常修复
    def app_error_fix(self):
        try:
            self.wait_widget(self.page["exit_error"]["title"])
            self.debug.info(u"[APP_INF] APP异常修复")
            self.widget_click(self.page["exit_error"]["skip"],
                              log_record=0)
            self.debug.info(u"[APP_INF] 跳过")
        except TimeoutException:
            pass

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

    # 跳过欢迎界面
    def skip_welcome(self):
        try:
            self.wait_widget(self.page["welcome_page"]["title"])
            self.debug.info(u"[APP_INF] 页面有欢迎页，跳过")
            self.widget_click(self.page["welcome_page"]["skip"],
                              self.page["app_home_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    # 退出登录至登录界面
    def device_to_login(self):
        self.wait_widget(self.page["app_home_page"]["title"])
        self.widget_click(self.page["app_home_page"]["my"],
                          log_record=0)

        try:
            self.wait_widget(self.page["login_page"]["title"])
            now_page = "login_page"
        except TimeoutException:
            self.wait_widget(self.page["my_page"]["title"])
            now_page = "my_page"

        try:
            if now_page == "login_page":
                self.debug.info(u"[APP_INF] 当前APP未登录，直接进入登录页")
            else:
                self.debug.info(u"[APP_INF] 当前APP已登录，退出进入登录页")
                self.widget_click(self.page["my_page"]["setting"],
                                  self.page["setting_page"]["title"],
                                  log_record=0)

                self.widget_click(self.page["setting_page"]["logout"],
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
        self.app_error_fix()
        self.check_update()
        self.skip_welcome()
        self.device_to_login()
        self.wait_widget(self.page["login_page"]["title"])
        self.debug.info(u"[APP_INF] APP当前页面为登录页面")
