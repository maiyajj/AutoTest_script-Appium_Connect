# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppSmartLink1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"一键配网"  # 用例所属模块
        self.case_title = u'配网成功率统计"'  # 用例名称
        self.zentao_id = 1965  # 禅道ID

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["app_home_page"]["title"],
                              self.page["app_home_page"]["add_device"],
                              self.page["add_device_method_page"]["title"])

            self.widget_click(self.page["add_device_method_page"]["title"],
                              self.page["add_device_method_page"]["history"],
                              self.page["add_history_list_page"]["title"])

            self.widget_click(self.page["add_history_list_page"]["title"],
                              self.page["add_history_list_page"]["y201J"],
                              self.page["add_specification_page"]["title"])

            self.widget_click(self.page["add_specification_page"]["title"],
                              self.page["add_specification_page"]["next"],
                              self.page["input_wifi_password_page"]["title"])

            self.show_pwd(self.wait_widget(self.page["input_wifi_password_page"]["check_box"]))
            pwd = self.widget_click(self.page["input_wifi_password_page"]["title"],
                                    self.page["input_wifi_password_page"]["password"],
                                    self.page["input_wifi_password_page"]["title"])

            data = conf["wifi_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            pwd.clear()
            self.ac.send_keys(pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["wifi密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["add_specification_page"]["title"],
                              self.page["add_specification_page"]["confirm"],
                              self.page["search_device_loading_page"]["title"])

            while True:
                try:
                    self.wait_widget(self.page["search_device_fail_page"], 1, 0.5)
                    raise TimeoutException()
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(self.page["bind_device_page"], 1, 0.5)
                    raise TimeoutException()
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(self.page["search_device_success_page"], 1, 0.5)
                    break
                except TimeoutException:
                    pass

            self.widget_click(self.page["search_device_success_page"]["title"],
                              self.page["search_device_success_page"]["confirm"],
                              self.page["control_device_page"]["title"])

            i = 5
            while i < 0:
                try:
                    self.wait_widget(self.page["control_device_page"]["power_on"], 1, 0.5)
                    self.widget_click(self.page["control_device_page"]["title"],
                                      self.page["control_device_page"]["power_button"],
                                      self.page["control_device_page"]["power_off"])
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(self.page["control_device_page"]["power_off"], 1, 0.5)
                    self.widget_click(self.page["control_device_page"]["title"],
                                      self.page["control_device_page"]["power_button"],
                                      self.page["control_device_page"]["power_on"])
                except TimeoutException:
                    pass
                i -= 1

            self.widget_click(self.page["control_device_page"]["title"],
                              self.page["control_device_page"]["device_info"],
                              self.page["device_info_page"]["title"])

            self.widget_click(self.page["device_info_page"]["title"],
                              self.page["device_info_page"]["unbind"],
                              self.page["unbind_device_popup"]["title"])

            self.widget_click(self.page["unbind_device_popup"]["title"],
                              self.page["unbind_device_popup"]["confirm"],
                              self.page["app_home_page"]["title"])

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
