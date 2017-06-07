# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppFeedBack1(LaunchApp):
    def run(self):
        self.case_module = u"意见反馈"  # 用例所属模块
        self.case_title = u'返回按钮功能检查'  # 用例名称
        self.zentao_id = 1976  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_FEED_BACK_001
        self.driver = self.return_driver()
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
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["feedback"],
                              self.page["feedback_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["feedback_page"]["title"],
                              self.page["feedback_page"]["to_return"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
