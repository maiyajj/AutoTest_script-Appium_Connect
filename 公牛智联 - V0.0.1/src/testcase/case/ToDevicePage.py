# coding=utf-8
from selenium.common.exceptions import *
from src.testcase.common.WidgetCheckUnit import *


class ToDevicePage(object):
    def __init__(self):
        self.driver = database["driver"]
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.driver.find_element_by_class_name("android.widget.FrameLayout").click()
        time.sleep(0.01)
        self.case()

    def case(self):
        # 用例动作
        while True:
            if self.driver.current_activity == login_popup["activity"][0]:
                try:
                    self.wait_widget(update_popup["title"], 3, 1)
                    logger.info(u"[APP_INF] APP有最新版本，可以更新")
                    self.widget_click(update_popup["title"],
                                      update_popup["cancel"],
                                      god_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                    logger.info(u"[APP_INF] 取消更新")
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(login_popup["title"], 3, 1)
                    logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                    self.widget_click(login_popup["title"],
                                      login_popup["confirm"],
                                      login_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                except TimeoutException:
                    pass

            if self.driver.current_activity == login_page["activity"][0]:
                logger.info(u"[APP_INF] APP当前页面为登录页面,登录")
                try:
                    self.widget_click(login_page["title"],
                                      login_page["login_button"],
                                      device_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                except TimeoutException:
                    logger.info(u"[APP_INF] APP进入设备主页失败，退出")
                    self.driver.quit()

            if self.driver.current_activity == device_page["activity"][0]:
                logger.info(u"[APP_INF] APP当前页面为主页面")
                break
