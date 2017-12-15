# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPForgetPassword2(WidgetOperation):
    @case_run(True)
    def run(self):
        self.case_module = u"忘记密码"  # 用例所属模块
        self.case_title = u'忘记密码页面-未注册账户检测'  # 用例名称
        self.zentao_id = 1909  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_find_password"],
                          self.page["find_password_page"]["title"])

        user_name = self.widget_click(self.page["find_password_page"]["user_name"],
                                      self.page["find_password_page"]["title"])

        # 发送数据
        data = "13811111111"
        user_name.clear()
        self.ac.send_keys(user_name, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["未注册用户名"] input success')
        time.sleep(0.5)

        check_code = self.widget_click(self.page["find_password_page"]["check_code"],
                                       self.page["find_password_page"]["title"])

        data = "123456"
        check_code.clear()
        self.ac.send_keys(check_code, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["验证码"] input success')
        time.sleep(0.5)

        widget_px = self.ac.get_location(self.wait_widget(self.page["find_password_page"]["to_next"]))
        self.driver.tap([widget_px["centre"]])
        self.logger.info(u'[APP_CLICK] operate_widget success')

        while True:
            try:
                self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
            except TimeoutException:
                break

            # 截屏获取设备toast消息
            ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

        self.case_over("screen")
