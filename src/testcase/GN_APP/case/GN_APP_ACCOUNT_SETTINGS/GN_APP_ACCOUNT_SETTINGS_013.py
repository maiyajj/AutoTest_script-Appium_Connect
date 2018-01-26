# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPAccountSettings13(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'昵称长度16位验证，功能检查'  # 用例名称
        self.zentao_id = "1947"  # 禅道ID

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

        # 发送数据
        data = "12345678901234567"
        nickname.clear()
        self.ac.send_keys(nickname, data, self.driver)
        self.debug.info(u'[APP_INPUT] ["17位用户名"] input success')
        time.sleep(0.5)

        element = self.page["change_nickname_page"]["nickname"]
        nick_name = self.ac.get_attribute(self.wait_widget(element), "name")
        self.debug.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (nick_name, len(nick_name)))
        nick_name = nick_name.replace(element[3]["default_text"], "")
        if len(nick_name) != 16:
            raise TimeoutException("nick name len is not 16, current len is %s" % len(nick_name))
