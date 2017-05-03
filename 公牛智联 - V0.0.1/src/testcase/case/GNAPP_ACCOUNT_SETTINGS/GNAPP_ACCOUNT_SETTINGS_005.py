# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppAccountSettings5(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改页面，旧密码输入错误，提示信息检查'  # 用例名称
        self.ZenTao_id = 1970  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_005

        self.launch_app(Login_page=False)  # 启动APP
        self.case()

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
            data = "1234567890"
            old_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["错误旧密码"] input success')
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
            data = conf["login_pwd"].decode('hex')
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

    def output(self):
        self.run()
        return self.result()
