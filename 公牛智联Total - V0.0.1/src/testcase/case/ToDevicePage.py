# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *
from src.utils.ReadConf import *


class ToDevicePage(object):
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

    def case(self):
        # 用例动作
        while True:
            try:
                self.wait_widget(self.page["update_popup"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
                self.widget_click(self.page["update_popup"]["title"],
                                  self.page["update_popup"]["cancel"],
                                  self.page["god_page"]["title"],
                                  1, 1, 1, 10, 0.5, 0)
                self.logger.info(u"[APP_INF] 取消更新")
            except TimeoutException:
                pass

            try:
                self.wait_widget(self.page["login_popup"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                self.widget_click(self.page["login_popup"]["title"],
                                  self.page["login_popup"]["confirm"],
                                  self.page["login_page"]["title"],
                                  1, 1, 1, 10, 0.5, 0)
            except TimeoutException:
                pass

            try:
                self.wait_widget(self.page["login_page"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP当前页面为登录页面,登录")
                try:
                    self.widget_click(self.page["login_page"]["title"],
                                      self.page["login_page"]["login_button"],
                                      self.page["device_page"]["title"],
                                      1, 1, 1, 6, 0.5, 0)
                except TimeoutException:
                    try:
                        user_name = self.widget_click(self.page["login_page"]["title"],
                                                      self.page["login_page"]["username"],
                                                      self.page["login_page"]["title"],
                                                      1, 1, 1, 10, 0.5)

                        # 发送数据
                        data = conf["user_and_pwd"][self.device_info["udid"]]["user_name"]
                        data = str(data).decode('hex').replace(" ", "")
                        user_name.clear()
                        self.ac.send_keys(user_name, data)
                        self.logger.info(u'[APP_INPUT] ["重新登陆用户名"] input success')
                        time.sleep(0.5)

                        login_pwd = self.widget_click(self.page["login_page"]["title"],
                                                      self.page["login_page"]["password"],
                                                      self.page["login_page"]["title"],
                                                      1, 1, 1, 10, 0.5)

                        data = conf["user_and_pwd"][self.device_info["udid"]]["login_pwd"]
                        data = str(data).decode('hex').replace(" ", "")
                        
                        self.show_pwd()
                        login_pwd.clear()
                        self.ac.send_keys(login_pwd, data)
                        self.logger.info(u'[APP_INPUT] ["重新输入登录密码"] input success')
                        try:
                            self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["login_button"],
                                              self.page["device_page"]["title"],
                                              1, 1, 1, 10, 0.5, 0)
                        except TimeoutException:
                            i = 1
                            while i <= 33:
                                time.sleep(10)
                                widget_px = self.page["god_page"]["title"][3]["px"]
                                width = int(int(self.device_info["dpi"]["width"]) * widget_px["width"])
                                height = int(int(self.device_info["dpi"]["height"]) * widget_px["height"])
                                self.driver.tap([(width, height)], )
                                print "time sleep %sS" % (i * 10)
                                i += 1
                            self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["login_button"],
                                              self.page["device_page"]["title"],
                                              1, 1, 1, 10, 0.5, 0)
                    except TimeoutException:
                        self.logger.info(u"[APP_INF] APP进入设备主页失败，退出")
                        self.driver.close_app()
                        self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
                        raise WebDriverException()
            except TimeoutException:
                pass

            try:
                self.wait_widget(self.page["device_page"]["title"], 1, 0.5)
                self.logger.info(u"[APP_INF] APP当前页面为主页面")
                break
            except TimeoutException:
                pass

    def show_pwd(self):
        try:
            element = self.wait_widget(self.page["login_page"]["check_box"])
            while True:
                if self.ac.get_attribute(element, "checked") == "true":
                    break
                else:
                    element.click()
        except TimeoutException:
            pass
