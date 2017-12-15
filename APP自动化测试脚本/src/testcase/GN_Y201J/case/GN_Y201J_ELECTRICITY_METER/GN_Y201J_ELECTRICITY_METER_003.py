# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JElectricityMeter3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'峰谷电价验证'  # 用例名称
        self.zentao_id = 1139  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_on")

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, self.driver)

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

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, self.driver)

        now_h = int(time.strftime("%H"))
        elec, elec_bill = self.get_device_elect(now_h + 2, True)

        peak_price = [v for k, v in elec.items() if 6 <= k <= 22]
        valley_price = [v for k, v in elec.items() if k < 6 and k > 22]

        elec_bill_info = ("current [elec_bill: %s, peak_price: %s, peak_data: %s, valley_price: %s, valley_data: %s]"
                          % (sum(elec_bill.values()), sum(peak_price), peak_data, sum(valley_price), valley_data))
        self.logger.info(elec_bill_info)

        if sum(elec_bill.values()) != sum(peak_price) * int(peak_data) + sum(valley_price) * int(valley_data):
            raise TimeoutException(elec_bill_info)
