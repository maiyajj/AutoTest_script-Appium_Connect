# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *


class ToLoginPageJD(object):
    def __init__(self, driver, logger, device_info, page_element):
        self.driver = driver
        self.logger = logger
        self.device_info = device_info
        self.page = page_element
        self.debug = self.device_info["debug"]
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

    def device_to_login(self):
        pass
        # try:
        #     self.wait_widget(self.page["app_home_page"]["title"], 1, 0.5)
        #     self.logger.info(u"[APP_INF] APP当前页面为主页面,等待退出")
        #     try:
        #         self.widget_click(self.page["app_home_page"]["title"],
        #                           self.page["app_home_page"]["account_setting"],
        #                           self.page["account_setting_page"]["title"],
        #                           log_record=0)
        #
        #         self.widget_click(self.page["account_setting_page"]["title"],
        #                           self.page["account_setting_page"]["help_setting"],
        #                           self.page["help_setting_page"]["title"],
        #                           log_record=0)
        #
        #         self.driver.swipe(100, 500, 100, 100, 0)
        #         self.widget_click(self.page["help_setting_page"]["title"],
        #                           self.page["help_setting_page"]["logout"],
        #                           self.page["logout_popup"]["title"],
        #                           log_record=0)
        #
        #         self.widget_click(self.page["logout_popup"]["title"],
        #                           self.page["logout_popup"]["confirm"],
        #                           self.page["login_page"]["title"],
        #                           log_record=0)
        #     except TimeoutException:
        #         self.logger.info(u"[APP_INF] APP进入登录页面失败，正在重新启动")
        #         self.driver.close_app()
        #         self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
        #         raise WebDriverException()
        # except TimeoutException:
        #     pass

    def case(self):
        # 用例动作
        i = 0
        while True:
            self.check_update()
            self.close_ad()
            self.device_to_login()
            try:
                self.wait_widget(self.page["login_page"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP当前页面为登录页面")
                break
            except TimeoutException:
                pass
            i += 1
            if i > 3:
                raise TimeoutException("ToLoginPage Error!")
