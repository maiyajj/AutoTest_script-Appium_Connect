# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter2(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'单一电价验证'  # 用例名称
        self.zentao_id = 1138  # 禅道ID
    
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
                            attribute.append(self.ac.get_attribute(new_value, "name"))
                            break
                    step += 1
                    break
            elif now_time == str(now_h + 1):
                break
            else:
                time.sleep(60)
                self.driver.tap([(10, 10)])
        
        self.case_over(True)
