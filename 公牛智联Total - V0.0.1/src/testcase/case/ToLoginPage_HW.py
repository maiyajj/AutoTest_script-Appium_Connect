# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *


class ToLoginPageHW(object):
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

    # 退出登录至登录界面
    def device_to_login(self):
        # TODO: 华为账号退出登录，由于APP的安全限制暂未定是否要做。
        pass

    # 用例动作
    def case(self):
        self.check_update()
        self.device_to_login()
        # self.wait_widget(self.page["login_page"]["title"])
        self.logger.info(u"[APP_INF] APP当前页面为登录页面")
