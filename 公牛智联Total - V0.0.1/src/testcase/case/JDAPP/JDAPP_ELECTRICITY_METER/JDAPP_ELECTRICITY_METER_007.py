# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter7(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'设置峰谷电价'  # 用例名称
        self.zentao_id = 1152  # 禅道ID

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
            self.wait_widget(self.page["control_device_page"]["power_on"])
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_on"])

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, 0, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["peak_valley_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["peak_valley_price"],
                          self.page["peak_valley_price_page"]["title"])

        peak_price = self.widget_click(self.page["peak_valley_price_page"]["set_peak_price"],
                                       self.page["peak_valley_price_page"]["title"])

        peak_data = "5"
        peak_price.clear()
        self.ac.send_keys(peak_price, peak_data, self.driver)
        self.logger.info(u'[APP_INPUT] ["峰电价"] input success')
        time.sleep(0.5)

        valley_price = self.widget_click(self.page["peak_valley_price_page"]["set_valley_price"],
                                         self.page["peak_valley_price_page"]["title"])

        valley_data = "2"
        valley_price.clear()
        self.ac.send_keys(valley_price, valley_data, self.driver)
        self.logger.info(u'[APP_INPUT] ["谷电价"] input success')
        time.sleep(0.5)

        self.now = time.strftime("%H:%M")

        delay_time_1 = ["06:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["start_time"],
                          self.page["peak_valley_price_page"]["roll_h"])

        self.set_timer_roll(self.page["peak_valley_price_page"]["roll_h"],
                            self.page["peak_valley_price_page"]["roll_m"],
                            self.page["peak_valley_price_page"]["start_time_text"],
                            delay_time_1, self.now)

        self.widget_click(self.page["peak_valley_price_page"]["start_time"],
                          self.page["peak_valley_price_page"]["title"])

        delay_time_2 = ["22:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["end_time"],
                          self.page["peak_valley_price_page"]["end_h"])

        self.set_timer_roll(self.page["peak_valley_price_page"]["end_h"],
                            self.page["peak_valley_price_page"]["end_m"],
                            self.page["peak_valley_price_page"]["end_time_text"],
                            delay_time_2, self.now)

        self.widget_click(self.page["peak_valley_price_page"]["end_time"],
                          self.page["peak_valley_price_page"]["title"])

        self.widget_click(self.page["peak_valley_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["set_elec"]), "name")
        if u"峰谷时间段电价" not in attribute:
            raise TimeoutException()

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, 0, self.driver)

        now_h = int(time.strftime("%H"))
        elec = {}
        elec_bill = {}

        while True:
            if time.strftime("%H:%M") == "23:01":
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
                # if index >= now_h + 2:
                elec_bill[index] = self.ac.get_attribute(elec_bill_value, "name")
                self.logger.info("[APP_INFO]23:01_elec_bill:%s" % str(elec_bill))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])
        elec_value = copy.copy(self.page["elec_page"]["elec_value"])
        for index, element in elec_elements.items():
            if element is not None:
                elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                # if index >= now_h + 2:
                elec[index] = self.ac.get_attribute(elec_value, "name")
                self.logger.info("[APP_INFO]23:01_elec:%s" % str(elec))

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        while True:
            if int(time.strftime("%H")) == now_h + 1:
                time.sleep(60)
                break
            else:
                self.driver.tap([(10, 10)])
                time.sleep(60)

        self.widget_click(self.page["control_device_page"]["elec_bill"],
                          self.page["elec_bill_page"]["title"])

        for index, element in elec_bill_elements.items():
            if element is not None:
                elec_bill_value[0] = self.page["elec_bill_page"]["price_value"][0][index]
                # if index <= now_h + 1:
                elec_bill[index] = self.ac.get_attribute(elec_bill_value, "name")
                self.logger.info("[APP_INFO]%s:01_elec_bill:%s" % (time.strftime("%H"), str(elec_bill)))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        for index, element in elec_elements.items():
            if element is not None:
                elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                # if index <= now_h + 1:
                elec[index] = self.ac.get_attribute(elec_value, "name")
                self.logger.info("[APP_INFO]%s:01_elec:%s" % (time.strftime("%H"), str(elec)))

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        peak_price = [v for k, v in elec.items() if 6 <= k <= 22]
        valley_price = [v for k, v in elec.items() if k < 6 and k > 22]
        if sum(elec_bill.values()) != sum(peak_price) * int(peak_data) + sum(valley_price) * int(valley_data):
            raise TimeoutException()

        self.case_over(True)

