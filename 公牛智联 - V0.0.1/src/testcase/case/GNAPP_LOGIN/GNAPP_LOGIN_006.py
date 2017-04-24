# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.testcase.case.ToLoginPage import *
from src.utils.ScreenShot import *


class GNAppLogin6(object):
    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger

        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—错误密码输入次数超过5次后，账号锁定1分钟验证'  # 用例名称
        self.ZenTao_id = 1899  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_006
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log

        try:
            self.driver = launch_app(self.device_info)  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = 0
            ToLoginPage(self.driver, self.logger)  # 使APP跳转到登录页面等待

            self.case()
        except WebDriverException:
            self.case_over("unknown")

    # 用例动作
    def case(self):
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
            data = conf["user_name"].decode('hex')
            user_name.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            count = 5
            while count > 0:
                login_pwd = self.widget_click(login_page["title"],
                                              login_page["password"],
                                              login_page["title"],
                                              1, 1, 1, 10, 0.5)

                self.driver.press_keycode(29, 28672)
                self.driver.press_keycode(112)
                data = conf["err_pwd"].decode('hex')
                login_pwd.send_keys(data)
                self.logger.info(u'[APP_INPUT] ["错误密码"] input success')
                time.sleep(0.5)

                self.widget_click(login_page["title"],
                                  login_page["login_button"],
                                  god_page["title"],
                                  1, 1, 1, 10, 0.5)

                while True:
                    try:
                        self.wait_widget(loading_popup["title"], 1, 0.5)
                    except TimeoutException:
                        break

                count -= 1

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf["login_pwd"].decode('hex')
            login_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              god_page["title"],
                              1, 1, 1, 10, 0.5)
            # 截屏
            screen_shot_name = r"./screenshots/%s - %s - %s - [%s]-[%s].png" \
                               % (database["program_loop_time"], database["case_location"],
                                  self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))

            self.driver.save_screenshot(screen_shot_name)
            self.logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot success')

            time.sleep(1 * 30)
            self.wait_widget(login_page["title"], 3, 1)
            time.sleep(1 * 30)

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf["login_pwd"].decode('hex')
            login_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              device_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        try:
            self.driver.close_app()  # 关闭APP
            self.driver.quit()  # 退出appium服务
        except WebDriverException:
            pass
        self.logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))

    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            return "success", self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title, self.start_time
        elif self.success == "unknown":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            return "unknown", self.case_title, self.start_time
