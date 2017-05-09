# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppMessageClassify2(LaunchApp):
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面，清空活动历时消息功能检查'  # 用例名称
        self.zentao_id = 1926  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_002
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["message_table"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["setting"],
                              message_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(message_setting_page["title"],
                              message_setting_page["clear_device"],
                              clear_device_popup["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(clear_device_popup["title"],
                              clear_device_popup["confirm"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["device"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            state = self.wait_widget(home_message_page["device"], 3, 1).get_attribute("checked")
            if state is True:
                self.wait_widget(home_message_page["no_message"], 3, 1)
            else:
                self.widget_click(home_message_page["title"],
                                  home_message_page["device"],
                                  home_message_page["title"],
                                  1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
