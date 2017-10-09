# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter6(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'单一电价设置'  # 用例名称
        self.zentao_id = 1151  # 禅道ID

    # 用例动作
    def case(self):
        elements = self.wait_widget(self.page["app_home_page"]["device"])
        new_value = copy.copy(self.page["app_home_page"]["device"])
        for index, element in elements.items():
            if element is not None and str(self.ac.get_attribute(element, "name")) == conf["MAC"][0]:
                new_value[0] = new_value[0][index]
                while True:
                    try:
                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                        break
                    except TimeoutException:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                        time.sleep(1)
            break

        try:
            self.wait_widget(self.page["control_device_page"]["power_off"])
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, 0, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_price"],
                          self.page["single_price_page"]["title"])

        elec_price = self.widget_click(self.page["single_price_page"]["set_price"],
                                       self.page["single_price_page"]["title"])

        elec_price_data = "5"
        elec_price.clear()
        self.ac.send_keys(elec_price, elec_price_data, self.driver)
        self.logger.info(u'[APP_INPUT] ["单一电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["single_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["set_elec"]), "name")
        if u"单一电价" not in attribute:
            raise TimeoutException()

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, 0, self.driver)


        now_h = int(time.strftime("%H"))
        elec = {}
        elec_bill = {}

        while True:
            if time.strftime("%H:%M") == "%02d:01" % (now_h + 2):
                break
            else:
                self.driver.tap([(10, 10)])
                time.sleep(30)

        self.widget_click(self.page["control_device_page"]["elec_bill"],
                          self.page["elec_bill_page"]["title"])

        elec_bill_elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
        elec_bill_value = copy.copy(self.page["elec_bill_page"]["price_value"])
        for index, element in elec_bill_elements.items():
            if element is not None:
                elec_bill_value[0] = self.page["elec_bill_page"]["price_value"][0][index]
                # if index - 2 >= now_h + 2:
                elec_bill[index - 2] = self.ac.get_attribute(elec_bill_value, "name")
                self.logger.info("[APP_INFO]%02d:01_elec_bill:%s" % (now_h + 2, str(elec_bill)))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])
        elec_value = copy.copy(self.page["elec_page"]["elec_value"])
        for index, element in elec_elements.items():
            if element is not None:
                elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                # if index - 2 >= now_h + 2:
                elec[index - 2] = self.ac.get_attribute(elec_value, "name")
                self.logger.info("[APP_INFO]%02d:01_elec:%s" % (now_h + 2, str(elec)))

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        if sum(elec_bill[now_h + 1]) != sum(elec[now_h + 1]) * int(elec_price_data):
            raise TimeoutException()

        self.case_over(True)
