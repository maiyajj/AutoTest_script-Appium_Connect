# coding=utf-8
from ReadAPPElement import *


class b(a):
    def case(self):
        try:
            while True:
                element = self.wait_widget(self.page["app_home_page"]["device"], 1, 0.5, True)
                for i in element:
                    if self.ac.get_attribute(i, "name") == conf["MAC"][0]:
                        self.widget_click(self.page["app_home_page"]["device"],
                                          self.page["control_device_page"]["title"],
                                          operate_driver=i.parent)
                        raise ValueError()
                    else:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.4, 0, self.driver)
                        time.sleep(1)
        except ValueError:
            pass

        try:
            self.wait_widget(self.page["control_device_page"]["power_on"], 1, 0.5)
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])
        except TimeoutException:
            pass

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, 0, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_price"],
                          self.page["single_price_page"]["title"])

        elec = self.widget_click(self.page["single_price_page"]["set_price"],
                                 self.page["single_price_page"]["title"])

        data = "5"
        elec.clear()
        self.ac.send_keys(elec, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["单一电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["single_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, 0, self.driver)

        now_h = int(time.strftime("%H"))
        while True:
            if time.strftime("%H") == str(now_h + 2):
                self.widget_click(self.page["control_device_page"]["elec_bill"],
                                  self.page["elec_bill_page"]["title"])
                break
            else:
                time.sleep(60)
        attribute = []
        step = 0
        while True:
            start_h = str((now_h + 2 + step) % 24)
            now_time = time.strftime("%H")
            if now_time == start_h:
                while True:
                    elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
                    new_value = copy.copy(self.page["elec_bill_page"]["price_value"])
                    for index, element in elements.items():
                        if element is not None and str(self.ac.get_attribute(element, "name")) == "%s:00" % (now_h + 1):
                            new_value[0] = new_value[0][index]
                            value = float(self.ac.get_attribute(self.wait_widget(new_value), "name")[:-1])
                            attribute.append(value)
                            break
                    step += 1
                    break
            elif now_time == str(now_h + 1):
                break
            else:
                time.sleep(60)
                self.driver.tap([(10, 10)])
    

b().case()


class c(a):
    def case(self):
        now_h = 20
        attribute = []
        step = 1
        now = 22
        while True:
            start_h = str((now_h + 2 + step) % 24)
            now_time = str(now % 24)
            print now_time, start_h
            if now_time == str(now_h + 1):
                print now_time
                break
            elif now_time == start_h:
                while True:
                    elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
                    new_value = copy.copy(self.page["elec_bill_page"]["price_value"])
                    for index, element in elements.items():
                        print "%02d:00" % int(now_time)
                        if element is not None and str(self.ac.get_attribute(element, "name")) == "%02d:00" % int(
                                now_time):
                            new_value[0] = new_value[0][index]
                            value = float(self.ac.get_attribute(self.wait_widget(new_value), "name")[:-1])
                            attribute.append(value)
                            break
                    step += 1
                    break
            now += 1
            print attribute
            time.sleep(1)

c().case()
