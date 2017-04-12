# coding:utf-8
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppDevicePage1(object):
    def __init__(self):
        self.case_title = u'默认页面信息检查'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        ToDevicePage()
        self.success = 0
        self.case()

    # 用例动作
    def case(self):
        try:
            self.wait_widget(device_page["user_image"], 3, 1)

            now_time = self.wait_widget(device_page["welcome"], 3, 1).get_attribute("name")
            if 0 < int(time.strftime("%H")) < 12:
                if now_time != u"上午好":
                    raise TimeoutException()
            else:
                if now_time != u"下午好":
                    raise TimeoutException()

            if self.wait_widget(device_page["welcome"], 3, 1).get_attribute("name") != u"上海市":
                raise TimeoutException()

            self.wait_widget(device_page["weather"], 3, 1)

            self.case_over(1)
        except TimeoutException:
            self.case_over(0)

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        self.driver.close_app()
        self.driver.quit()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))

    def result(self):
        if self.success == 1:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
            return "success", self.case_title
        elif self.success == 0:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title
