# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppElectricityMeter8(WidgetOperationJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'电价设置验证'  # 用例名称
        self.zentao_id = 1155  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_on")

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, 0, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_price"],
                          self.page["single_price_page"]["title"])

        signal_price = self.widget_click(self.page["single_price_page"]["set_price"],
                                         self.page["single_price_page"]["title"])

        signal_price_data = "5"
        signal_price.clear()
        self.ac.send_keys(signal_price, signal_price_data, self.driver)
        self.logger.info(u'[APP_INPUT] ["单一电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["single_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["set_elec"]), "name")
        if u"单一电价" not in attribute:
            raise TimeoutException("set signal price is wrong, current mode is %s" % [attribute])

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
                self.logger.info("[APP_INFO]23:01_elec_bill:%s" % elec_bill)

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
                self.logger.info("[APP_INFO]23:01_elec:%s" % elec)

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
                self.logger.info("[APP_INFO]%s:01_elec_bill:%s" % (time.strftime("%H"), elec_bill))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        for index, element in elec_elements.items():
            if element is not None:
                elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                # if index <= now_h + 1:
                elec[index] = self.ac.get_attribute(elec_value, "name")
                self.logger.info("[APP_INFO]%s:01_elec:%s" % (time.strftime("%H"), elec))

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        elec_bill_info = ("elec bill is wrong, current [elec_bill:%s, elec:%s, elec_price:%s]"
                          % (sum(elec_bill.values()), sum(elec.values()), signal_price_data))
        self.logger.info(elec_bill_info)

        if sum(elec_bill.values()) != sum(elec.values()) * int(signal_price_data):
            raise TimeoutException(elec_bill_info)

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

        now = time.strftime("%H:%M")

        delay_time_1 = ["06:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["start_time"],
                          self.page["peak_valley_price_page"]["roll_h"])

        self.set_timer_roll(self.page["peak_valley_price_page"]["roll_h"],
                            self.page["peak_valley_price_page"]["roll_m"],
                            self.page["peak_valley_price_page"]["start_time_text"],
                            delay_time_1, now)

        self.widget_click(self.page["peak_valley_price_page"]["start_time"],
                          self.page["peak_valley_price_page"]["title"])

        delay_time_2 = ["22:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["end_time"],
                          self.page["peak_valley_price_page"]["end_h"])

        self.set_timer_roll(self.page["peak_valley_price_page"]["end_h"],
                            self.page["peak_valley_price_page"]["end_m"],
                            self.page["peak_valley_price_page"]["end_time_text"],
                            delay_time_2, now)

        self.widget_click(self.page["peak_valley_price_page"]["end_time"],
                          self.page["peak_valley_price_page"]["title"])

        self.widget_click(self.page["peak_valley_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["set_elec"]), "name")
        if u"峰谷时间段电价" not in attribute:
            raise TimeoutException("set peak valley price is wrong, current mode is %s" % [attribute])

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, 0, self.driver)

        now_h = int(time.strftime("%H"))
        elec, elec_bill = self.get_device_elect(now_h + 2, True)

        peak_price = [v for k, v in elec.items() if 6 <= k <= 22]
        valley_price = [v for k, v in elec.items() if k < 6 and k > 22]

        elec_bill_info = ("current [elec_bill:%s, peak_price:%s, peak_data:%s, valley_price:%s, valley_data:%s]"
                          % (sum(elec_bill.values()), sum(peak_price), peak_data, sum(valley_price), valley_data))
        self.logger.info(elec_bill_info)

        if sum(elec_bill.values()) != sum(peak_price) * int(peak_data) + sum(valley_price) * int(valley_data):
            raise TimeoutException(elec_bill_info)

        self.case_over(True)
