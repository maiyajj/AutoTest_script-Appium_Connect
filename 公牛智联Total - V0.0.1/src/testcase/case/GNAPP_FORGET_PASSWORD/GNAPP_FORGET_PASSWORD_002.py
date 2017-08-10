# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppForgetPassword2(LaunchApp):
    @case_run(True)
    def run(self):
        self.case_module = u"忘记密码"  # 用例所属模块
        self.case_title = u'忘记密码页面-未注册账户检测'  # 用例名称
        self.zentao_id = 1909  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_find_password"],
                              self.page["find_password_page"]["title"],
                              1, 1, 1, 10, 0.5)

            user_name = self.widget_click(self.page["find_password_page"]["title"],
                                          self.page["find_password_page"]["user_name"],
                                          self.page["find_password_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = "13811111111"
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["未注册用户名"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(self.page["find_password_page"]["title"],
                                           self.page["find_password_page"]["check_code"],
                                           self.page["find_password_page"]["title"],
                                           1, 1, 1, 10, 0.5)

            data = "123456"
            check_code.clear()
            self.ac.send_keys(check_code, data)
            self.logger.info(u'[APP_INPUT] ["验证码"] input success')
            time.sleep(0.5)

            widget_px = self.page["find_password_page"]["to_next"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

