# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppSmartLink1(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"配网功能(#245)"  # 用例所属模块
        self.case_title = u'设备首次配网操作检查'  # 用例名称
        self.zentao_id = 2048  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["app_home_page"]["add_device"],
                          self.page["add_device_page"]["title"])

        end_time = time.time() + 60
        while True:
            try:
                self.wait_widget(self.page["add_device_page"]["no_device"])
                raise TimeoutException("no devices found")
            except TimeoutException:
                time.sleep(1)
            try:

                self.wait_widget(self.page["add_device_page"]["device"])
                self.widget_click(self.page["add_device_page"]["device"],
                                  self.page["input_wifi_password_page"]["title"])
                break
            except TimeoutException:
                if time.time() > end_time:
                    raise TimeoutException("search device timeout!")
                time.sleep(1)

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
                          self.page["set_name_addr_page"]["title"])

        nickname = self.widget_click(self.page["set_name_addr_page"]["nickname"],
                                     self.page["set_name_addr_page"]["title"])

        data = "test_device"
        nickname.clear()
        self.ac.send_keys(nickname, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["设备备注"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["set_name_addr_page"]["next"],
                          self.page["app_home_page"]["title"])

        self.choose_home_device(data)

        i = 3
        while i > 0:
            self.set_power("power_off")
            self.set_power("power_on")
            i -= 1

        self.widget_click(self.page["control_device_page"]["device_setting"],
                          self.page["device_setting_page"]["title"])

        # XXX: 设置设备备注名，需要用的时候取消注释
        # self.widget_click(self.page["device_setting_page"]["device_info"],
        #                   self.page["device_info_page"]["title"])
        #
        # nickname_value = self.ac.get_attribute(self.wait_widget(self.page["device_info_page"]["mac"]), "name")
        #
        # self.widget_click(self.page["device_info_page"]["to_return"],
        #                   self.page["device_setting_page"]["title"])
        #
        # self.widget_click(self.page["device_setting_page"]["nickname"],
        #                   self.page["change_nickname_popup"]["title"])
        #
        # nickname = self.widget_click(self.page["change_nickname_popup"]["nickname"],
        #                              self.page["change_nickname_popup"]["title"])
        # data = nickname_value
        # nickname.clear()
        # self.ac.send_keys(nickname, data, self.driver)
        # self.logger.info(u'[APP_INPUT] ["设备备注"] input success')
        # time.sleep(0.5)
        #
        # self.widget_click(self.page["change_nickname_popup"]["confirm"],
        #                   self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["unbind"],
                          self.page["unbind_device_popup"]["title"])

        self.widget_click(self.page["unbind_device_popup"]["confirm"],
                          self.page["app_home_page"]["title"])

