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
            self.widget_click(self.page["update_popup"]["cancel"],
                              self.page["god_page"]["title"],
                              log_record=0)
            self.logger.info(u"[APP_INF] 取消更新")
        except TimeoutException:
            pass

    def close_ad(self):
        try:
            self.wait_widget(self.page["close_ad_popup"]["title"], 1, 0.5)
            self.logger.info(u"[APP_INF] 页面有广告，关闭广告")
            self.widget_click(self.page["close_ad_popup"]["confirm"],
                              self.page["app_home_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    def login_to_device(self):
        try:
            self.wait_widget(self.page["app_home_page"]["no_device"], 1, 0.5)
            self.widget_click(self.page["app_home_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              log_record=0)
            try:
                element = self.wait_widget(self.page["account_setting_page"]["username"])
                if self.ac.get_attribute(element, "name") == u'点击登录':
                    self.logger.info(u"[APP_INF] 当前APP未登录，开始重新登录")
                    self.widget_click(self.page["account_setting_page"]["username"],
                                      self.page["login_page"]["title"],
                                      log_record=0)
                    user_name = self.widget_click(self.page["login_page"]["username"],
                                                  self.page["login_page"]["title"])

                    # 发送数据
                    data = self.user["user_name"]
                    data = str(data).decode('hex').replace(" ", "")
                    user_name.clear()
                    self.ac.send_keys(user_name, data, self.driver)
                    self.logger.info(u'[APP_INPUT] ["重新登陆用户名"] input success')
                    time.sleep(0.5)

                    self.show_pwd()
                    login_pwd = self.widget_click(self.page["login_page"]["password"],
                                                  self.page["login_page"]["title"])

                    data = self.user["login_pwd"]
                    data = str(data).decode('hex').replace(" ", "")
                    login_pwd.clear()
                    self.ac.send_keys(login_pwd, data, self.driver)
                    self.logger.info(u'[APP_INPUT] ["重新输入登录密码"] input success')
                    try:
                        self.widget_click(self.page["login_page"]["login_button"],
                                          self.page["app_home_page"]["title"])

                    except TimeoutException:
                        i = 1
                        while i <= 31:
                            time.sleep(10)
                            self.driver.tap([(10, 10)])
                            self.logger("time sleep %sS" % (i * 10))
                            i += 1
                        self.widget_click(self.page["login_page"]["login_button"],
                                          self.page["app_home_page"]["title"])
                else:
                    self.widget_click(self.page["app_home_page"]["add_device"],
                                      self.page["app_home_page"]["title"])
                    if self.ac.get_attribute(element, "is_displayed") == False:
                        pass
                    else:
                        raise TimeoutException()
            except TimeoutException:
                self.logger.info(u"[APP_INF] APP进入设备主页失败，退出")
                self.driver.close_app()
                self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
                raise WebDriverException(u"[APP_INF] APP进入设备主页失败，退出")
        except TimeoutException:
            pass

    def show_pwd(self):
        try:
            element = self.wait_widget(self.page["login_page"]["check_box"])
            while True:
                if self.ac.get_attribute(self.wait_widget(self.page["login_page"]["password"]), "name") != "":
                    break
                else:
                    element.click()
        except TimeoutException:
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
