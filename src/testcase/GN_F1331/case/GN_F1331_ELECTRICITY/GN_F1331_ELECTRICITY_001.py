# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Electricity1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"电量统计(#8)"  # 用例所属模块
        self.case_title = u'app显示功率为0，显示效果检查'  # 用例名称
        self.zentao_id = "71"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_on")

        self.input_serial_command("device_info")

        attr = self.wait_widget(self.page["control_device_page"]["power"])
        value = self.ac.get_attribute(attr, "name")

        end_time = time.time() + 180
        while True:
            tmp = self.ac.get_attribute(attr, "name")
            if tmp != value:
                break
            if time.time() > end_time:
                break
        if not value == u"0W":
            raise TimeoutException("device state error, current: %s" % value)

        device_info_state_list = self.check_device_info_state(True)
        time_0 = time.time()
        elect_0 = self.get_last_device_state(device_info_state_list, time_0)
        # [1517399064.0, '1', '1', '1', '1', '1', '0', '0', '0000', '0000']
        print(elect_0)
