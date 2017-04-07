# coding:utf-8
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppMessageClassify1(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case_title = u'消息分类页面信息检查'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToDevicePage()
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["message_table"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(message_classify_page["title"],
                              message_classify_page["all_device"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["all_device"][1],
                                      message_classify_page["all_device"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["experience_data"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["experience_data"][1],
                                      message_classify_page["experience_data"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A2"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A2"][1],
                                      message_classify_page["A2"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A3"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A3"][1],
                                      message_classify_page["A3"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A4"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A4"][1],
                                      message_classify_page["A4"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A5"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A5"][1],
                                      message_classify_page["A5"][0],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()
            self.case_over(1)
        except TimeoutException:
            self.case_over(0)

    def case_over(self, success):
        if success == 1:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        elif success == 0:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
