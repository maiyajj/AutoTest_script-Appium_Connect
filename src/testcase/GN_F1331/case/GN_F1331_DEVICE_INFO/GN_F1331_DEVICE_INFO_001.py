# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331DeviceInfo1(WidgetOperation):
    @case_run("")
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'设置记忆模式'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("device_info")
        device_info_state_list = self.check_device_info_state(True)
        time_0 = time.time()
        safe_memory_0 = self.get_last_device_info_state(device_info_state_list, time_0)[1]

        self.input_serial_command("power", "device_info")

        self.ac.swipe(0.5, 0.9, 0.5, 0.6, self.driver)

        if safe_memory_0 == "1":
            self.widget_click(self.page["control_device_page"]["memory_mode"])
            time_1 = time.time()

            self.widget_click(self.page["control_device_page"]["safe_mode"])
            time_2 = time.time()
        else:
            self.widget_click(self.page["control_device_page"]["safe_mode"])
            time_1 = time.time()

            self.widget_click(self.page["control_device_page"]["memory_mode"])
            time_2 = time.time()

        device_info_state_list = self.check_device_info_state()
        device_info_state_1_list = self.get_last_device_info_state(device_info_state_list, time_1)
        device_info_state_2_list = self.get_last_device_info_state(device_info_state_list, time_2)
        self.debug.info(u"[APP_INFO]device state: \n"
                        u"device_info_state_list: %s;\n"
                        u"device_info_state_1_list: %s;\n"
                        u"device_info_state_2_list: %s;"
                        % (device_info_state_list, device_info_state_1_list, device_info_state_2_list))

        if safe_memory_0 == "1":
            # 记忆模式
            safe_memory_1 = device_info_state_1_list[1]
            result = [safe_memory_1 == "0"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_1, result))

            # 安全模式
            safe_memory_2 = device_info_state_2_list[1]
            result = [safe_memory_2 == "1"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_2, result))
        else:
            # 安全模式
            safe_memory_1 = device_info_state_1_list[1]
            result = [safe_memory_1 == "1"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_1, result))

            # 记忆模式
            safe_memory_2 = device_info_state_2_list[1]
            result = [safe_memory_2 == "0"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_2, result))
