# coding=utf-8
import os

from src.common.WidgetCheckUnit import *
from src.utils.AppiumCommand import *
from src.utils.ReadConf import *


class ToDevicePage(object):
    def __init__(self, driver, device_info):
        self.driver = driver
        self.page = device_info["page"]  # 页面元素库
        self.logger = device_info["logger"]  # log日志
        self.debug = device_info["debug"]  # debug日志
        self.ac = device_info["ac"]  # appium command
        self.user = conf["user_and_pwd"][device_info["udid"]][device_info["app"]]
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, device_info)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
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

    # 账户异地登录弹窗，确定跳过
    def login_abnormal(self):
        try:
            self.wait_widget(self.page["login_popup"]["title"])
            self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
            self.widget_click(self.page["login_popup"]["confirm"],
                              self.page["login_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    # 登录至APP主页面
    def login_to_device(self):
        try:
            self.wait_widget(self.page["login_page"]["title"])
            now_page = "login_page"
        except TimeoutException:
            self.wait_widget(self.page["app_home_page"]["has_device"])
            now_page = "app_home_page"

        self.wait_widget(self.page["login_page"]["title"])
        try:
            if now_page == "login_page":
                self.logger.info(u"[APP_INF] 当前APP未登录，开始重新登录")
                self.check_user_pwd()
            else:
                self.logger.info(u"[APP_INF] 当前APP已登录")
        except TimeoutException:
            self.logger.info(u"[APP_INF] APP进入设备主页失败，退出")
            self.driver.close_app()
            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            raise TimeoutException("ToDevicePage Error!")

    # 显示密码
    def show_pwd(self):
        while True:
            try:
                element = self.wait_widget(self.page["login_page"]["check_box"])
                if self.ac.get_attribute(element, "checked") == "true":
                    break
                else:
                    element.click()
            except TimeoutException:
                pass

    # 等待密码超时恢复
    def wait_pwd_timeout(self):
        i = 1
        while i <= 31:
            time.sleep(10)
            print("time sleep %sS" % (i * 10))
            self.logger.info("time sleep %sS" % (i * 10))
            i += 1

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

        count = 2
        while count > 0:
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
            except TimeoutException:
                count -= 1
                if count == 0:
                    break
                else:
                    self.wait_pwd_timeout()

        try:
            self.wait_widget(self.page["app_home_page"]["title"])
            modified_conf(conf)
        except TimeoutException:
            raise TimeoutException("password is wrong")

    # 用例动作
    def case(self):
        self.check_update()
        self.login_abnormal()
        self.login_to_device()
        self.wait_widget(self.page["app_home_page"]["title"])
        self.logger.info(u"[APP_INF] APP当前页面为app主页面")
