# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPDevicePage1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'默认页面信息检查'  # 用例名称
        self.zentao_id = "1773"  # 禅道ID

    # 用例动作
    def case(self):
        self.wait_widget(self.page["device_page"]["user_image"])

        element = self.wait_widget(self.page["device_page"]["welcome"])
        now_time = self.ac.get_attribute(element, "name")
        self.debug.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (now_time, len(now_time)))
        if 0 < int(time.strftime("%H")) < 12:
            if now_time != u"上午好":
                raise TimeoutException("now time is not a.m. and now time is %s" % [now_time])
        else:
            if now_time != u"下午好":
                raise TimeoutException("now time is not p.m. and now time is %s" % [now_time])

        element = self.wait_widget(self.page["device_page"]["city"])
        city = self.ac.get_attribute(element, "name")
        self.debug.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (city, len(city)))
        if city != u"上海市":
            raise TimeoutException("city is not ShangHai and current city is %s" % [city])

        self.wait_widget(self.page["device_page"]["weather"])
