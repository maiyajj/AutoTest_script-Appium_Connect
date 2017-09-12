# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppVersion1(LaunchAppGN):
    @case_run_gn(False)
    def run(self):
        self.case_module = u"版本信息"  # 用例所属模块
        self.case_title = u'当前版本为最新版本，页面信息检查'  # 用例名称
        self.zentao_id = 1992  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["version_info"],
                          self.page["upgrade_page"]["title"])

        element = self.wait_widget(self.page["upgrade_page"]["current_version"])
        current_version = self.ac.get_attribute(element, "name")[-10:]
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (current_version, len(current_version)))

        element = self.wait_widget(self.page["upgrade_page"]["new_version"])
        new_version = self.ac.get_attribute(element, "name")[-10:]
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (new_version, len(new_version)))

        element = self.wait_widget(self.page["upgrade_page"]["upgrade_button"])
        btn_state = self.ac.get_attribute(element, "enabled")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (btn_state, len(btn_state)))

        if current_version == new_version and btn_state != "false":
            raise TimeoutException()

        self.case_over(True)
