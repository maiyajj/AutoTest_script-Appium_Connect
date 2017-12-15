# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SSmartLink1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_SMTLNK_一键配网(#52)"  # 用例所属模块
        self.case_title = u'FUT_SMTLNK_app能正常添加设备_按分类查找'  # 用例名称
        self.zentao_id = 498  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["app_home_page"]["add_device"],
                          self.page["add_device_popup"]["title"])

        self.widget_click(self.page["add_device_popup"]["add_device"],
                          self.page["add_device_method_page"]["title"])

        self.widget_click(self.page["add_device_method_page"]["variety"],
                          self.page["add_device_class_page"]["title"])

        end_time = time.time() + 30
        while True:
            try:
                self.widget_click(self.page["add_device_class_page"]["outlet"],
                                  self.page["add_outlet_list_page"]["title"])
                break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException()
                self.ac.swipe(0.5, 0.6, 0.5, 0.5, self.driver)

        end_time = time.time() + 30
        while True:
            try:
                self.widget_click(self.page["add_outlet_list_page"]["y201S"],
                                  self.page["add_specification_page"]["title"])
                break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException()
                self.ac.swipe(0.5, 0.6, 0.5, 0.5, self.driver)

        self.widget_click(self.page["add_specification_page"]["next"],
                          self.page["input_wifi_password_page"]["title"])

        self.show_pwd(self.wait_widget(self.page["input_wifi_password_page"]["password"]),
                      self.wait_widget(self.page["input_wifi_password_page"]["check_box"]),
                      "password")

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
                self.wait_widget(self.page["control_device_page"]["title"])
                break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException("search device timeout!")
                time.sleep(1)
