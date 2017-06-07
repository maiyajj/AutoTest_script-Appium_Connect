# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppVersion1(LaunchApp):
    def run(self):
        self.case_module = u"版本信息"  # 用例所属模块
        self.case_title = u'当前版本为最新版本，页面信息检查'  # 用例名称
        self.zentao_id = 1992  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_VERSION_001
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
                              self.page["personal_settings_page"]["version_info"],
                              self.page["upgrade_page"]["title"],
                              1, 1, 1, 10, 0.5)

            current_version = self.wait_widget(self.page["upgrade_page"]["current_version"], 3, 1).get_attribute(
                "name")[-10:]

            new_version = self.wait_widget(self.page["upgrade_page"]["new_version"], 3, 1).get_attribute("name")[-10:]

            btn_state = self.wait_widget(self.page["upgrade_page"]["upgrade_button"], 3, 1).get_attribute("enabled")

            if current_version == new_version and btn_state != "false":
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
