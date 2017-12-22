# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'开关操作及记忆功能'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_off")

        now = time.time()
        result_thread, result_queue = self.launch_serial_button_state(now)

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [1, 1, 1]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: main button on: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [0, 0, 0]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: main button off: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_on"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [1, 0, 0]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: up button on: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_on"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [1, 1, 0]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: mid button on: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_on"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [1, 1, 1]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: down button on: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_off"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [0, 1, 1]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: up button off: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_off"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [0, 0, 1]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: mid button off: %s" % [up_btn, middle_btn, down_btn])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_off"])

        up_btn, middle_btn, down_btn = self.check_serial_button_state(result_queue)
        if [up_btn, middle_btn, down_btn] != [0, 0, 0]:
            raise TimeoutException("device main button state error, current: %s" % [up_btn, middle_btn, down_btn])
        else:
            self.logger.info(u"[APP_INFO]Device info: down button off: %s" % [up_btn, middle_btn, down_btn])
