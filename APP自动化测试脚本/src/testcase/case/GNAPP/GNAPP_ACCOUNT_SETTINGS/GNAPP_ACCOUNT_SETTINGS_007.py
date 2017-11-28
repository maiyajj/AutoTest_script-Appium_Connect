# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppAccountSettings7(WidgetOperationGN):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'昵称为空时，功能检查'  # 用例名称
        self.zentao_id = 1948  # 禅道ID

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
        nickname.clear()
        # 全选
        self.logger.info(u'[APP_INPUT] ["昵称"] delete success')
        time.sleep(0.5)

        element = self.wait_widget(self.page["change_nickname_page"]["commit"])
        state = self.ac.get_attribute(element, "enabled")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (state, len(state)))
        if state != "false":
            raise TimeoutException("nickname commit state is not false, current state is %s" % state)

