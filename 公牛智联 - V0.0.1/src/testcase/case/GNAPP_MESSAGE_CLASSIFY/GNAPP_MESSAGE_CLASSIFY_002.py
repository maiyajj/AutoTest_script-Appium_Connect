# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.testcase.case.ToDevicePage import *


class GNAppMessageClassify2(object):
    def __init__(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面，清空活动历时消息功能检查'  # 用例名称
        self.ZenTao_id = 1926  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_002
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                    % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log
        try:
            self.driver = launch_app()  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        except WebDriverException:
            self.case_over("unknown")
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
        self.success = 0
        ToDevicePage()  # 使APP跳转到设备主页面等待
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["message_table"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["setting"],
                              message_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(message_setting_page["title"],
                              message_setting_page["clear_device"],
                              clear_device_popup["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(clear_device_popup["title"],
                              clear_device_popup["confirm"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["device"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            state = self.wait_widget(home_message_page["device"], 3, 1).get_attribute("checked")
            if state is True:
                self.wait_widget(home_message_page["no_message"], 3, 1)
            else:
                self.widget_click(home_message_page["title"],
                                  home_message_page["device"],
                                  home_message_page["title"],
                                  1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        self.driver.close_app()  # 关闭APP
        self.driver.quit()  # 退出appium服务
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))

    def result(self):
        if self.success is True:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            return "success", self.case_title, self.start_time
        elif self.success is False:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title, self.start_time
        elif self.success == "unknown":
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            return "unknown", self.case_title, self.start_time
