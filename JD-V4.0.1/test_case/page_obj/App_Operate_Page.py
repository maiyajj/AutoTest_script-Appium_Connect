# coding=utf-8
import sys

sys.path.append("..")
from models.driver import ReadInfo


class MainPageWidget(ReadInfo):
    def class_mainpage_init(self):
        self.get_timeout_time()
        self.app_home_page()
        self.add_device_method_page()
        self.add_device_list_page()
        self.add_history_list_page()
        self.add_outlet_list_page()
        self.add_specification_page()
        self.input_wifi_password_page()
        self.search_device_loading_page()
        self.batch_add_device_page()
        self.search_device_success_page()
        self.search_device_fail_page()
        self.bind_device_success_page()
        self.bind_device_page()
        self.popups_bind_device_fail_page()
        self.control_device_page()
        self.device_info_page()
        self.popups_unbind_device_page()

    def app_home_page(self):
        # APP主页面标志
        self.app_home = u"微联"
        # +号
        self.add_device_plus = "com.jd.smart:id/iv_right"
        # 广告关闭键
        self.ad = "com.jd.smart:id/close_pop_for_top_news"
        # 检查更新
        self.check_update = "com.jd.smart:id/cancel"
    def add_device_method_page(self):
        # 添加设备页面标志
        self.add_device_method = u"添加设备"
        # 通过设备品类添加
        self.add_variety = u"通过设备品类添加"
        # 添加历史
        self.add_history = "com.jd.smart:id/iv_history"
    def add_device_list_page(self):
        # 添加设备页面标志
        self.add_device_list = u"设备品类"
        # 插座列表选项
        self.outlet_option = u"插座"

    # driver.find_elements_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='2']")
    def add_history_list_page(self):
        # 进入设备添加历史页面标志
        self.add_history_list = u"已添加设备"
        # 公牛Wi-Fi智能转换器2代电量计量版
        self.hgn_y201J = u"公牛WiFi智能电量统计版转换器2代"
        # 公牛Wi-Fi智能转换器2代
        self.hgn_y2011 = u"公牛Wi-Fi智能转换器2代"
        # 公牛Wi-Fi智能插座2代加强版
        self.hgn_y2011dl = u"公牛Wi-Fi智能插座2代加强版"

    def add_outlet_list_page(self):
        # 进入插座列表页面标志
        self.add_outlet_list = u"插座"
        # 公牛Wi-Fi智能插座2代
        self.lgn_y2011 = u"公牛Wi-Fi智能插座2代"
    def add_specification_page(self):
        FrameLayout = "/android.widget.FrameLayout"
        LinearLayout = "/android.widget.LinearLayout"
        TextView = "/android.widget.TextView"
        self.xpath = "".join(("/",FrameLayout,FrameLayout,LinearLayout,LinearLayout,TextView))
        TextValue = "[@text='1']"
        self.add_specification = "".join((self.xpath,TextValue))
        # 下一步
        self.add_specification_confirm = "com.jd.smart:id/tv_action"

    def input_wifi_password_page(self):
        TextValue = "[@text='2']"
        # 进入输入密码页面标志
        self.input_wifi_password = "".join((self.xpath,TextValue))
        # 确认wifi密码按钮
        self.confirm_wifi_password = "com.jd.smart:id/tv_action"
        # wifi密码输入框
        self.wifi_password = "com.jd.smart:id/tv_pwd"

    def search_device_loading_page(self):
        TextValue = "[@text='3']"
        # 搜索设备等待页面
        self.search_device_loading = "".join((self.xpath,TextValue))

    def batch_add_device_page(self):
        # 设备等待添加
        self.batch_add_device = u"批量添加"

    def search_device_success_page(self):
        # 搜索到设备MAC
        self.search_device_mac = self.MAC[self.mac_choose_flag]
        ListView = "//android.widget.ListView"
        LinearLayout = "/android.widget.LinearLayout"
        TextView = "/android.widget.TextView"
        TextValue = "[@text='%s']" % self.search_device_mac
        self.search_device_success = {}
        for i in xrange(1, 5):
            LinearLayout1 = "/android.widget.LinearLayout[%s]" % i
            mac = "".join((ListView, LinearLayout1, LinearLayout,
                           LinearLayout, TextView, TextValue))
            text = "".join((ListView, LinearLayout1, LinearLayout, TextView))
            self.search_device_success[mac] = text

    def search_device_fail_page(self):
        TextValue = "[@text='4']"
        # 搜索设备超时
        self.search_device_fail = "".join((self.xpath,TextValue))

    def bind_device_success_page(self):
        # 绑定成功页面标志
        self.bind_device_success = "com.jd.smart:id/btn_config"
        # 确定绑定按钮
        self.confirm_button = "com.jd.smart:id/btn_config"
        # 输入设备备注名
        self.notes = "com.jd.smart:id/edittext_layout"

    def bind_device_page(self):
        # 设备已被绑定
        self.bind_device = u"该设备已被绑定"

    def popups_bind_device_fail_page(self):
        # 绑定失败
        self.bind_device_fail = "com.jd.smart:id/confirm"

    def control_device_page(self):
        # 设备控制页面标志
        self.control_device = "com.jd.smart:id/i_more"
        # 设备信息进入按钮
        self.device_info_button = "com.jd.smart:id/i_more"
        # 设备离线标志
        self.offline = u"设备不在线"
        # 电源开关
        self.power_button = "android.widget.Button"
        # 电源开启
        self.power_on = u"设备已开启"
        # 电源关闭
        self.power_off = u"设备已关闭"
        # 设备记忆模式
        self.device_memory_mode = u"记忆模式"
        # 设备安全模式
        self.device_safe_mode = u"安全模式"

    def device_info_page(self):
        # 设备信息页面标志
        self.device_info = u"设置"
        # 删除设备按钮
        self.unbind_device = "com.jd.smart:id/btn_unbind"

    def popups_unbind_device_page(self):
        # 删除设备弹窗
        self.unbind_device_confirm = "com.jd.smart:id/confirm"


class Memo(object):
    def smart_link(self):
        print u"一键配网函数API"
        print "app_home_page()"
        print "add_device_list_page()"
        print "add_history_list_page()"
        print "add_outlet_list_page()"
        print "input_wifi_password_page()"
        print "search_device_loading_page()"
        print "search_device_success_page()"
        print "search_device_fail_page()"
        print "bind_device_success_page()"
        print "bind_device_page()"
        print "bind_device_fail_page()"
        print "control_device_page()"
        print "device_info_page()"
        print "unbind_device_page()"