# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.testcase.case.ToDevicePage import *
from src.utils.ScreenShot import *


class GNAppAccountSettings10(object):
    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger

        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改页面，确认密码为空，提示信息检查'  # 用例名称
        self.ZenTao_id = 1968  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_010
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log

        if self.ZenTao_id in database[device_name].keys():
            pass
        else:
            database[device_name][self.ZenTao_id] = {}
            database[device_name][self.ZenTao_id]["test_count"] = 0
            database[device_name][self.ZenTao_id]["test_pass"] = 0
            database[device_name][self.ZenTao_id]["test_fail"] = 0
            database[device_name][self.ZenTao_id]["test_error"] = 0
            database[device_name][self.ZenTao_id]["test_wait"] = 0
            database[device_name][self.ZenTao_id]["ZenTao"] = self.ZenTao_id
            database[device_name][self.ZenTao_id]["case_title"] = self.case_title

        try:
            self.driver = launch_app(self.device_info)  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = 0
            ToDevicePage(self.driver, self.logger)  # 使APP跳转到设备主页面等待

            self.case()
        except WebDriverException:
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["account_setting"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["change_pwd"],
                              change_pwd_page["title"],
                              1, 1, 1, 10, 0.5)

            old_pwd = self.widget_click(change_pwd_page["title"],
                                        change_pwd_page["old_pwd"],
                                        change_pwd_page["title"],
                                        1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = "chenghao1"
            old_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["旧密码"] input success')
            time.sleep(0.5)

            new_pwd = self.widget_click(change_pwd_page["title"],
                                        change_pwd_page["new_pwd"],
                                        change_pwd_page["title"],
                                        1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = conf["login_pwd"].decode('hex')
            new_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            conform_new_pwd = self.widget_click(change_pwd_page["title"],
                                                change_pwd_page["conform_pwd"],
                                                change_pwd_page["title"],
                                                1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = ""
            conform_new_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            widget_px = change_pwd_page["commit"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(loading_popup["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                    # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.ZenTao_id, self.basename, self.logger)

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
        database[self.device_name][self.ZenTao_id]["test_count"] += 1

    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            database[self.device_name][self.ZenTao_id]["test_pass"] += 1
            return "success", self.ZenTao_id, self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_fail"] += 1
            return "failed", self.ZenTao_id, self.case_title, self.start_time
        elif self.success == "unknown":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_error"] += 1
            return "unknown", self.ZenTao_id, self.case_title, self.start_time
