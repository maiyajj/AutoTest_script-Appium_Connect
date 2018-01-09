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

    # 关闭广告
    def close_ad(self):
        try:
            self.wait_widget(self.page["ad_popup"]["title"])
            self.debug.info(u"[APP_INF] APP有广告")
            self.widget_click(self.page["ad_popup"]["skip"],
                              wait_time1=5,
                              log_record=0)
            self.debug.info(u"[APP_INF] 关闭广告")
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

    # 退出登录至登录界面
    def device_to_login(self):
        # TODO: 华为账号退出登录，由于APP的安全限制暂未定是否要做。
        pass

    # 用例动作
    def case(self):
        self.close_ad()
        self.check_update()
        self.device_to_login()
        self.wait_widget(self.page["login_page"]["title"])
        self.debug.info(u"[APP_INF] APP当前页面为登录页面")
