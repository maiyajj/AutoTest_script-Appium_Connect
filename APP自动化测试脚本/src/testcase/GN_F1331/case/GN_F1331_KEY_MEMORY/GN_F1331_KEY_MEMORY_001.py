# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"开关操作"  # 用例所属模块
        self.case_title = u'开关操作及记忆功能'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_off")

        self.input_serial_command("power")

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_off"])

        btn_state_list = self.check_serial_button_state()

        btn_state = btn_state_list[0]
        if [1, 1, 1] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[1]
        if [0, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[2]
        if [1, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[3]
        if [1, 1, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[4]
        if [1, 1, 1] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[5]
        if [0, 1, 1] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[6]
        if [0, 0, 1] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)

        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[7]
        if [0, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)
