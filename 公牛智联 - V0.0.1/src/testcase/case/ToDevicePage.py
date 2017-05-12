# coding=utf-8
import os

from src.testcase.common.WidgetCheckUnit import *
from src.utils.ReadConf import *


class ToDevicePage(object):
    def __init__(self, driver, logger, device_info):
        self.driver = driver
        self.logger = logger
        self.device_info = device_info
        self.debug = self.device_info["debug"]
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(self.driver, self.logger)
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
                    self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
                    self.widget_click(update_popup["title"],
                                      update_popup["cancel"],
                                      god_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                    self.logger.info(u"[APP_INF] 取消更新")
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(login_popup["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                    self.widget_click(login_popup["title"],
                                      login_popup["confirm"],
                                      login_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                except TimeoutException:
                    pass

            if self.driver.current_activity == login_page["activity"][0]:
                self.logger.info(u"[APP_INF] APP当前页面为登录页面,登录")
                try:
                    self.widget_click(login_page["title"],
                                      login_page["login_button"],
                                      device_page["title"],
                                      1, 1, 1, 10, 0.5, 0)
                except TimeoutException:
                    try:
                        user_name = self.widget_click(login_page["title"],
                                                      login_page["username"],
                                                      login_page["title"],
                                                      1, 1, 1, 10, 0.5)

                        # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
                        self.driver.press_keycode(29, 28672)
                        # KEYCODE_FORWARD_DEL 删除键 112
                        self.driver.press_keycode(112)
                        # 发送数据
                        data = str(conf["user_and_pwd"][self.device_info["user_and_pwd"]][0]).decode('hex')
                        user_name.send_keys(data)
                        self.logger.info(u'[APP_INPUT] ["重新登陆用户名"] input success')
                        time.sleep(0.5)

                        login_pwd = self.widget_click(login_page["title"],
                                                      login_page["password"],
                                                      login_page["title"],
                                                      1, 1, 1, 10, 0.5)

                        self.driver.press_keycode(29, 28672)
                        self.driver.press_keycode(112)
                        data = str(conf["user_and_pwd"][self.device_info["user_and_pwd"]][1]).decode('hex')
                        login_pwd.send_keys(data)
                        self.logger.info(u'[APP_INPUT] ["重新输入登录密码"] input success')

                        self.widget_click(login_page["title"],
                                          login_page["login_button"],
                                          device_page["title"],
                                          1, 1, 1, 10, 0.5, 0)

                    except TimeoutException:
                        self.logger.info(u"[APP_INF] APP进入设备主页失败，退出")
                        self.driver.close_app()
                        self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
                        raise WebDriverException()

            if self.driver.current_activity == device_page["activity"][0]:
                self.logger.info(u"[APP_INF] APP当前页面为主页面")
                break
