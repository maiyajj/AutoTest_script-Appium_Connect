# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppAccountSettings10(WidgetOperationGN):
    @case_run_gn(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改页面，确认密码为空，提示信息检查'  # 用例名称
        self.zentao_id = 1968  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["account_setting"],
                          self.page["account_setting_page"]["title"])

        self.widget_click(self.page["account_setting_page"]["change_pwd"],
                          self.page["change_pwd_page"]["title"])

        old_pwd = self.widget_click(self.page["change_pwd_page"]["old_pwd"],
                                    self.page["change_pwd_page"]["title"])

        # 发送数据
        data = "chenghao1"
        old_pwd.clear()
        self.ac.send_keys(old_pwd, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["旧密码"] input success')
        time.sleep(0.5)

        new_pwd = self.widget_click(self.page["change_pwd_page"]["new_pwd"],
                                    self.page["change_pwd_page"]["title"])

        # 发送数据
        data = self.user["login_pwd"]
        data = str(data).decode('hex').replace(" ", "")
        new_pwd.clear()
        self.ac.send_keys(new_pwd, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["新密码"] input success')
        time.sleep(0.5)

        conform_new_pwd = self.widget_click(self.page["change_pwd_page"]["conform_pwd"],
                                            self.page["change_pwd_page"]["title"])

        # 发送数据
        data = ""
        conform_new_pwd.clear()
        self.ac.send_keys(conform_new_pwd, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["新密码"] input success')
        time.sleep(0.5)

        widget_px = self.ac.get_location(self.wait_widget(self.page["change_pwd_page"]["commit"]))
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
