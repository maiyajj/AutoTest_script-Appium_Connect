# coding=utf-8
from appium import webdriver
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppLogin10(object):
    def __init__(self):
        self.case_module = u"登录"
        self.case_title = u'登录页面—位数错误的数字账号，登录提示信息检查'
        self.ZenTao_id = 1895
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
            user_name = self.widget_click(login_page["title"],
                                          login_page["username"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = "1"
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["位数错误用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf_login_pwd.decode('hex')
            login_pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["登录密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              god_page["title"],
                              1, 1, 1, 10, 0.5)

            while True:
                try:
                    self.wait_widget(loading_popup["title"], 1, 0.5)
                except TimeoutException:
                    break

            # 截屏
            screen_shot_name = r"./screenshots/%s - %s - %s - [%s]-[%s].png" \
                               % (database["program_loop_time"], database["case_location"],
                                  self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))
            database["screen_name"] = screen_shot_name

            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.width = int(width * 0.5)
            self.height = int(height * 0.66)

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
