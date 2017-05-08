# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppMessageClassify5(LaunchApp):
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息分类页面，选择多个设备后的消息内容检查'  # 用例名称
        self.zentao_id = 1924  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_005
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            pass  # Message: ***
        except BaseException, e:
            self.debug.error("%s:%s" % (self.basename, e))

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

            self.wait_widget(message_setting_page["title"], 3, 1)

            self.wait_widget(message_setting_page["to_return"], 3, 1)

            self.wait_widget(message_setting_page["clear_activity"], 3, 1)

            self.wait_widget(message_setting_page["clear_device"], 3, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
