# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *


class ToLoginPageAL(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.driver = driver
        self.logger = logger
        self.device_info = device_info
        self.page = page_element
        self.ac = AppiumCommand(self.device_info["platformName"])
        self.debug = self.device_info["debug"]
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, self.page, self.logger)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        # 唤醒设备
        self.driver.tap([(10, 10)])
        time.sleep(0.01)
        self.case()

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

    # 跳过欢迎界面
    def skip_welcome(self):
        try:
            self.wait_widget(self.page["welcome_page"]["title"])
            self.logger.info(u"[APP_INF] 页面有欢迎页，跳过")
            self.widget_click(self.page["welcome_page"]["skip"],
                              self.page["app_home_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    # 退出登录至登录界面
    def device_to_login(self):
        self.wait_widget(self.page["app_home_page"]["title"])
        self.widget_click(self.page["app_home_page"]["my"],
                          self.page["god"]["title"],
                          log_record=0)

        try:
            self.wait_widget(self.page["login_page"]["title"])
            now_page = "login_page"
        except TimeoutException:
            self.wait_widget(self.page["my_page"]["title"])
            now_page = "my_page"

        try:
            if now_page == "login_page":
                self.logger.info(u"[APP_INF] 当前APP未登录，直接进入登录页")
            else:
                self.logger.info(u"[APP_INF] 当前APP已登录，退出进入登录页")
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
            self.logger.info(u"[APP_INF] APP进入登录页面失败")
            self.driver.close_app()
            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            raise TimeoutException("ToLoginPage Error!")

    # 用例动作
    def case(self):
        self.check_update()
        self.skip_welcome()
        self.device_to_login()
        self.wait_widget(self.page["login_page"]["title"])
        self.logger.info(u"[APP_INF] APP当前页面为登录页面")
