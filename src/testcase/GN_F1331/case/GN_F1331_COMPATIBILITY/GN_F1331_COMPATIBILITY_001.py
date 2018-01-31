# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Compatibility1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"兼容性检查(#12)"  # 用例所属模块
        self.case_title = u'不同路由器同一手机一键配网兼容性检查'  # 用例名称
        self.zentao_id = "162"  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["app_home_page"]["add_device"],
                          self.page["add_device_method_page"]["title"])

        self.widget_click(self.page["add_device_method_page"]["history"],
                          self.page["add_history_list_page"]["title"])

        self.widget_click(self.page["add_history_list_page"]["gn_f1331"],
                          self.page["add_specification_page"]["title"])

        time.sleep(5)

        self.widget_click(self.page["add_specification_page"]["next"],
                          self.page["input_wifi_password_page"]["title"])

        pwd = self.widget_click(self.page["input_wifi_password_page"]["password"],
                                self.page["input_wifi_password_page"]["title"])

        data = conf["wifi_pwd"]
        data = bytearray.fromhex(str(data)).decode("utf-8").replace(" ", "")
        pwd.clear()
        self.ac.send_keys(pwd, data, self.driver)
        time.sleep(0.5)

        self.widget_click(self.page["input_wifi_password_page"]["confirm"],
                          self.page["search_device_loading_page"]["title"])

        end_time = time.time() + 60
        while True:
            try:
                self.wait_widget(self.page["search_device_fail_page"]["title"])
                raise TimeoutException("current page is search_device_fail_page")
            except TimeoutException:
                time.sleep(1)
            try:
                self.wait_widget(self.page["bind_device_page"]["title"])
                raise TimeoutException("current page is bind_device_page")
            except TimeoutException:
                time.sleep(1)
            try:
                self.wait_widget(self.page["search_device_success_page"]["title"])

                self.choose_device(conf["MAC"]["GN_F1331"]["0"],
                                   self.page["search_device_success_page"]["device_box"],
                                   self.page["search_device_success_page"]["confirm"])

                self.wait_widget(self.page["control_device_page"]["title"])
                break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException("search device timeout!")
                time.sleep(1)

        i = 3
        while i > 0:
            self.widget_click(self.page["control_device_page"]["main_button"])
            i -= 1

        self.widget_click(self.page["control_device_page"]["device_setting"],
                          self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["nickname"],
                          self.page["change_nickname_page"]["title"])

        nickname = self.widget_click(self.page["change_nickname_page"]["nickname"],
                                     self.page["change_nickname_page"]["title"])
        data = conf["MAC"]["GN_F1331"]["0"]
        nickname.clear()
        self.ac.send_keys(nickname, data, self.driver)
        time.sleep(0.5)

        self.widget_click(self.page["change_nickname_page"]["saved"],
                          self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["unbind"],
                          self.page["unbind_device_popup"]["title"])

        self.widget_click(self.page["unbind_device_popup"]["confirm"],
                          self.page["control_device_page"]["title"])

        v = self.get_index(conf["MAC"][self.app][self.device_mac], self.page["app_home_page"]["device"])
        if not v:
            raise TimeoutException()
