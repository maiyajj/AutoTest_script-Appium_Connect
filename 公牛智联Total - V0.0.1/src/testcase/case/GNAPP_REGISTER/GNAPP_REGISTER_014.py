# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppRegister14(LaunchApp):
    @case_run(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-用户名为英文字符时，提示信息检查'  # 用例名称
        self.zentao_id = 1824  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            user_name = self.widget_click(self.page["register_page"]["title"],
                                          self.page["register_page"]["username"],
                                          self.page["register_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = "abcdefg"
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["英文用户名"] input success')
            time.sleep(0.5)

            element = self.wait_widget(self.page["register_page"]["username"], 1, 0.5)
            user_name = self.ac.get_attribute(element, "name")
            if len(user_name) != 0:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

