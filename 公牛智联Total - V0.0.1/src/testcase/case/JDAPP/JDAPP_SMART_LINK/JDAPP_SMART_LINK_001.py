# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppSmartLink1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"一键配网"  # 用例所属模块
        self.case_title = u'在TP-link品牌的路由器下添加设备检查"'  # 用例名称
        self.zentao_id = 0001  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["app_home_page"]["add_device"],
                          self.page["add_device_method_page"]["title"])

        self.widget_click(self.page["add_device_method_page"]["history"],
                          self.page["add_history_list_page"]["title"])

        self.widget_click(self.page["add_history_list_page"]["y201J"],
                          self.page["add_specification_page"]["title"])

        time.sleep(4)
        self.widget_click(self.page["add_specification_page"]["next"],
                          self.page["input_wifi_password_page"]["title"])

        self.show_pwd(self.wait_widget(self.page["input_wifi_password_page"]["check_box"]), param="checked")
        pwd = self.widget_click(self.page["input_wifi_password_page"]["password"],
                                self.page["input_wifi_password_page"]["title"])

        data = conf["wifi_pwd"]
        data = str(data).decode('hex').replace(" ", "")
        pwd.clear()
        self.ac.send_keys(pwd, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["wifi密码"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["input_wifi_password_page"]["confirm"],
                          self.page["search_device_loading_page"]["title"])

        start_time = time.time()
        end_time = start_time + 60
        while True:
            try:
                self.wait_widget(self.page["search_device_fail_page"]["title"])
                raise TimeoutException()
            except TimeoutException:
                time.sleep(1)
            try:
                self.wait_widget(self.page["bind_device_page"]["title"])
                raise TimeoutException()
            except TimeoutException:
                time.sleep(1)
            try:
                self.wait_widget(self.page["search_device_success_page"]["title"])
                try:
                    while True:
                        elements = self.wait_widget(self.page["search_device_success_page"]["device_box"])
                        new_value = copy.copy(self.page["search_device_success_page"]["confirm"])
                        for index, element in elements.items():
                            if element is not None and str(self.ac.get_attribute(element, "name")) == conf["MAC"][0]:
                                new_value[0] = new_value[0][index]
                                while True:
                                    try:
                                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                                        raise ValueError()
                                    except TimeoutException:
                                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                        time.sleep(1)
                except ValueError:
                    break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException()
                time.sleep(1)

        i = 2
        while i > 0:
            try:
                self.widget_click(self.page["control_device_page"]["power_button"],
                                  self.page["control_device_page"]["title"])
            except TimeoutException:
                pass
            i -= 1

        self.widget_click(self.page["control_device_page"]["device_info"],
                          self.page["device_info_page"]["title"])

        self.widget_click(self.page["device_info_page"]["nickname"],
                          self.page["change_nickname_page"]["title"])

        nickname = self.widget_click(self.page["change_nickname_page"]["nickname"],
                                     self.page["change_nickname_page"]["title"])
        data = conf["MAC"][0]
        nickname.clear()
        self.ac.send_keys(nickname, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["设备备注"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["change_nickname_page"]["saved"],
                          self.page["device_info_page"]["title"])

        self.case_over(True)
