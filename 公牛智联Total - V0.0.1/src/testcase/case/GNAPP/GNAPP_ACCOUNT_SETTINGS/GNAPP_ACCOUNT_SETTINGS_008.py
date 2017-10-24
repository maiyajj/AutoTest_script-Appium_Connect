# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppAccountSettings8(LaunchAppGN):
    @case_run_gn(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'昵称修改成功，页面信息检查'  # 用例名称
        self.zentao_id = 1949  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["account_setting"],
                          self.page["account_setting_page"]["title"])

        self.widget_click(self.page["account_setting_page"]["nickname"],
                          self.page["change_nickname_page"]["title"])

        nickname = self.widget_click(self.page["change_nickname_page"]["nickname"],
                                     self.page["change_nickname_page"]["title"])

        # 全选
        nickname.clear()
        self.ac.send_keys(nickname, u"被修改的昵称", self.driver)
        self.logger.info(u'[APP_INPUT] ["昵称"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["change_nickname_page"]["commit"],
                          self.page["account_setting_page"]["title"])

        self.widget_click(self.page["account_setting_page"]["to_return"],
                          self.page["personal_settings_page"]["title"])

        element = self.wait_widget(self.page["personal_settings_page"]["nickname"])
        modified_nickname = self.ac.get_attribute(element, "name")
        if modified_nickname != u"被修改的昵称":
            raise TimeoutException("nickname is different from modified_nickname, current is %s" % modified_nickname)

        self.case_over(True)
