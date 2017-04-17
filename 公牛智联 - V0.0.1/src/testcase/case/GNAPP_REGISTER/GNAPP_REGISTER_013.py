# coding=utf-8
from appium import webdriver
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppRegister13(object):
    def __init__(self):
        self.case_module = u"注册"
        self.case_title = u'注册页面-用户名为空，注册验证'
        self.ZenTao_id = 1825
        self.basename = os.path.basename(__file__).split(".")[0]
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                    % (self.basename, self.case_title, self.ZenTao_id, self.case_module))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.success = 0
        ToLoginPage()
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_register"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)

            user_name = self.widget_click(register_page["title"],
                                          register_page["username"],
                                          register_page["title"],
                                          1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = ""
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["空白用户名"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(register_page["title"],
                                    register_page["password"],
                                    register_page["title"],
                                    1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "1234"
            pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["注册密码"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(register_page["title"],
                                           register_page["check_code"],
                                           register_page["title"],
                                           1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "123456"
            check_code.send_keys(data)
            logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            self.widget_click(register_page["title"],
                              register_page["register_button"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)

            # 截屏
            screen_shot_name = r"./screenshots/%s - %s - %s - [%s]-[%s].png" \
                               % (database["program_loop_time"], database["case_location"],
                                  self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))
            database["screen_name"] = screen_shot_name

            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.width = int(width * 0.5)
            self.height = int(height * 0.75)

            self.driver.tap([(self.width, self.height)], )
            self.driver.tap([(self.width, self.height)], )
            self.driver.tap([(self.width, self.height)], )

            self.driver.save_screenshot(screen_shot_name)
            logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot success')

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
