# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppRegister7(WidgetOperationGN):
    @case_run(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-验证码为中文字符时，提示信息检查'  # 用例名称
        self.zentao_id = 1880  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])

        self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
        check_code = self.widget_click(self.page["register_page"]["check_code"],
                                       self.page["register_page"]["title"])

        data = u"测试"
        check_code.clear()
        self.ac.send_keys(check_code, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
        time.sleep(0.5)

        element = self.page["register_page"]["check_code"]
        check_code = self.ac.get_attribute(self.wait_widget(element), "name")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (check_code, len(check_code)))
        check_code = check_code.replace(element[3]["default_text"], "")
        if len(check_code) != 0:
            raise TimeoutException("check code len is not 0, current is %s" % len(check_code))

