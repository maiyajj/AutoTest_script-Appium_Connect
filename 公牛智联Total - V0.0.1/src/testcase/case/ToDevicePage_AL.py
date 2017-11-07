# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *
from src.utils.ReadConf import *


class ToDevicePageAL(object):
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

    # 检查APP是否升级，取消
    def check_update(self):
        try:
            self.wait_widget(self.page["update_popup"]["title"])
            self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
            self.widget_click(self.page["update_popup"]["cancel"],
                              self.page["god_page"]["title"],
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

    # 登录至APP主页面
    def login_to_device(self):
        try:
            self.wait_widget(self.page["app_home_page"]["no_device"])
            self.widget_click(self.page["app_home_page"]["my"],
                              self.page["god"]["title"],
                              log_record=0)
            try:
                self.wait_widget(self.page["login_page"]["title"])
                now_page = "wait_login_page"
                wait_action = "1"
            except TimeoutException:
                self.wait_widget(self.page["my_page"]["title"])
                now_page = "app_home_page_no_device"
                wait_action = "2"
        except TimeoutException:
            try:
                self.wait_widget(self.page["login_page"]["title"])
                now_page = "login_page"
                wait_action = "3"
            except TimeoutException:
                self.wait_widget(self.page["app_home_page"]["has_device"])
                now_page = "app_home_page_has_device"
                wait_action = "4"

        try:
            if now_page == "wait_login_page" or now_page == "login_page":
                self.logger.info(u"[APP_INF] 当前APP未登录，开始重新登录")
                self.check_user_pwd()
            else:
                self.logger.info(u"[APP_INF] 当前APP已登录")
                if wait_action == "2":
                    self.widget_click(self.page["app_home_page"]["my_home"],
                                      self.page["app_home_page"]["title"],
                                      log_record=0)
        except TimeoutException:
            self.logger.info(u"[APP_INF] APP进入设备主页失败，退出")
            self.driver.close_app()
            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            raise TimeoutException("ToDevicePage Error!")

    # 显示密码
    def show_pwd(self):
        while True:
            try:
                if self.ac.get_attribute(self.wait_widget(self.page["login_page"]["password"]), "name") != "":
                    break
                else:
                    self.wait_widget(self.page["login_page"]["check_box"]).click()
            except TimeoutException:
                pass

    # 检查账户用户名和密码
    def check_user_pwd(self):
        self.show_pwd()
        user_name = self.widget_click(self.page["login_page"]["username"],
                                      self.page["login_page"]["title"])

        # 发送数据
        data = self.user["user_name"]
        data = str(data).decode('hex').replace(" ", "")
        user_name.clear()
        self.ac.send_keys(user_name, data, self.driver)
        time.sleep(0.5)

        precise_pwd = copy.copy(self.user["precise_pwd"])
        for x in precise_pwd:
            login_pwd = self.widget_click(self.page["login_page"]["password"],
                                          self.page["login_page"]["title"])

            pwd_data = x.decode('hex').replace(" ", "")
            login_pwd.clear()
            self.ac.send_keys(login_pwd, pwd_data, self.driver)
            try:
                self.widget_click(self.page["login_page"]["login_button"],
                                  self.page["app_home_page"]["title"])
                self.user["login_pwd"] = x
                self.user["new_pwd"] = precise_pwd.remove(x)[0]
                break
            except TimeoutException:
                pass

        try:
            self.wait_widget(self.page["app_home_page"]["title"])
            modified_conf(conf)
        except TimeoutException:
            raise TimeoutException("password is wrong")

    # 用例动作
    def case(self):
        self.check_update()
        self.skip_welcome()
        self.login_to_device()
