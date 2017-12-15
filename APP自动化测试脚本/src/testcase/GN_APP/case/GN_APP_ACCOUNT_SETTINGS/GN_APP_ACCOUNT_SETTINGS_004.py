# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPAccountSettings4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'退出当前账号后，确定按钮功能检查'  # 用例名称
        self.zentao_id = 1974  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["account_setting"],
                          self.page["account_setting_page"]["title"])

        self.widget_click(self.page["account_setting_page"]["logout"],
                          self.page["logout_popup"]["title"])

        self.widget_click(self.page["logout_popup"]["confirm"],
                          self.page["login_page"]["title"])

        self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
        element = self.page["login_page"]["password"]
        pwd = self.ac.get_attribute(self.wait_widget(element), "name")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (pwd, len(pwd)))
        pwd = pwd.replace(element[3]["default_text"], "")
        if len(pwd) != 0:
            raise TimeoutException("pwd len is wrong, current len is %s" % len(pwd))
