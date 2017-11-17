"appium -a 127.0.0.1 -p 4725 -bp 4726 -U 85GABMN9UDD2  --no-reset --local-timezone"
# coding=utf-8
import copy
import re
import time
import traceback

from appium import webdriver
from selenium.common.exceptions import *

driver = webdriver.Remote('http://localhost:4725/wd/hub',
                          {'deviceName': '85GABMN9UDD2', 'wdaLocalPort': '4727', 'unicodeKeyboard': 'True',
                           'waitActivity': 'com.jd.smart.activity.LoadingActivity', 'automationName': 'Appium',
                           'resetKeyboard': 'True', 'driver': '85GABMN9UDD2', 'browserName': '',
                           'newCommandTimeout': '999999', 'platformVersion': '5.1', 'appPackage': 'com.aliyun.alink',
                           'platformName': 'Android', 'appActivity': 'com.aliyun.alink.page.main.MainActivity'})
conf = {"MAC": ['C4:11:E0:00:00:00']}


class MainPageWidgetAndroidAL(object):
    # 欢迎页
    def welcome_page(self):
        d = {}
        # 标题
        d["title"] = ["btn_skip", "id", u"欢迎页"]
        # 跳过
        d["skip"] = ["btn_skip", "id", u"跳过"]
        return d

    # “我的”页面
    def my_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='自动化']", "xpath", u"“我的”页面"]
        # 设置
        d["setting"] = ["com.aliyun.alink:id/layout_container_item_setting", "id", u"设置"]
        return d

    # 账户登录页面
    def login_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='登录密码']", "xpath", u"账户登录页面"]
        # 用户名
        d["username"] = ["com.aliyun.alink:id/accountCompleteTextView", "id", u"用户名输入框"]
        # 密码
        d["password"] = ["com.aliyun.alink:id/content", "id", u"密码输入框"]
        # 显示/关闭密码
        d["check_box"] = [u"//android.widget.TextView[contains(@content-desc, '显示密码')]", "xpath", u"显示/关闭密码"]
        # 其他账户登录
        d["other_user"] = ["com.aliyun.alink:id/switchLogin", "id", u"密码输入框"]
        # 登录
        d["login_button"] = ["com.aliyun.alink:id/loginButton", "id", u"登录按钮"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/aliuser_title_bar_back_button", "id", u"返回"]
        return d

    # 设置页面
    def setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置']", "xpath", u"设置页面"]
        # 帮助与反馈
        d["feedback"] = [u"//android.widget.TextView[text='帮助与反馈']", "xpath", u"帮助与反馈"]
        # 关于阿里智能
        d["about"] = [u"//android.widget.TextView[text='关于阿里智能']", "xpath", u"关于阿里智能"]
        # 返回
        d["to_return"] = ["//android.widget.TextView[@text='']", "xpath", u"返回"]
        # 登出
        d["logout"] = [u"//android.widget.TextView[text='退出当前账号']", "id", u"退出当前账号"]
        return d

    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = ["com.aliyun.alink:id/home_page_topbar_home_name", "id", u"App主页面"]
        # +号
        d["add_device"] = ["com.aliyun.alink:id/homepage_topbar_menu_btn", "id", u"+号"]
        # 没有设备
        d["no_device"] = [u"//android.widget.TextView[@text='添加设备开启智能生活']", "xpath", u"没有设备"]
        # 设备
        device = {}
        device_button = {}
        device_state = {}
        for i in xrange(7):
            device[i] = ("//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]//"
                         "android.widget.TextView" % (i + 1))
            device_button[i] = ("//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]//"
                                "android.widget.RelativeLayout/android.widget.ImageView" % (i + 1))
            device_state[i] = ("//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]/"
                               "android.widget.LinearLayout/android.widget.TextView" % (i + 1))
        d["device"] = [device, "xpath", u"待控设备"]
        # 有设备
        d["has_device"] = ["com.aliyun.alink:id/home3_device_listitem_deviceinfo_devicedesc", "id", u"有设备"]
        # 设备开关
        d["device_button"] = [device_button, "xpath", u"待控设备开关"]
        # 设备状态
        d["device_state"] = [device_state, "xpath", u"设备状态"]
        # “我的”按钮
        d["my"] = [u"//android.widget.FrameLayout[4]//android.widget.TextView[contains(@resource-id, "
                   u"'textview_homebaritem_title')]", "xpath", u"“我的”按钮"]
        # “我的家”按钮
        d["my_home"] = [u"//android.widget.FrameLayout//android.widget.TextView[contains(@resource-id, "
                        u"'textview_homebaritem_title')]", "xpath", u"“我的家”按钮"]
        return d

    # 选择添加方式页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='选择添加方式']", "xpath", u"选择添加方式"]
        # 分类查找
        d["variety"] = ["com.aliyun.alink:id/relativelayout_devicesentry_manual", "id", u"分类查找"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 设备类别页面
    def add_device_class_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设备类别']", "xpath", u"设备类别页面"]
        # 插座排插
        d["outlet"] = [u"//android.widget.TextView[@text='插座排插']", "xpath", u"插座排插"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 插座排插页面
    def add_outlet_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='插座排插']", "xpath", u"插座排插页面"]
        # 公牛WiFi智能插座2代（电量统计版）
        d["y201S"] = [u"//android.widget.TextView[@text='公牛WiFi智能插座2代（电量统计版）']", "xpath",
                      u"公牛WiFi智能插座2代（电量统计版）"]
        # 公牛WiFi智能插座2代
        d["y2010"] = [u"//android.widget.TextView[@text='公牛WiFi智能插座2代']", "xpath", u"公牛WiFi智能插座2代"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 搜索设备页
    def add_specification_page(self):
        d = {}
        # 标题
        d["title"] = ["com.aliyun.alink:id/imageview_deviceopration_stepimg", "xpath", u"搜索设备页"]
        # 下一步
        d["next"] = ["com.aliyun.alink:id/button_deviceopration_next", "id", u"下一步"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/button_deviceopration_back", "id", u"返回"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        d = {}
        # 标题
        d["title"] = ["com.aliyun.alink:id/imageview_devicewificonfig_bg", "id", u"进入输入密码页面"]
        # 确认wifi密码按钮
        d["confirm"] = ["com.aliyun.alink:id/button_devicewificonfig_next", "id", u"确认wifi密码按钮"]
        # wifi密码输入框
        d["password"] = ["com.aliyun.alink:id/edittext_devicewificonfig_pwd", "id", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = ["com.aliyun.alink:id/button_devicewificonfig_pwd_switch", "id", u"密码显示关闭"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/button_devicewificonfig_back", "id", u"返回"]
        return d

    # 搜索设备等待页面
    def search_device_loading_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[text='设备添加中']", "xpath", u"搜索设备等待页面"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/button_deviceconfigprocess_back", "id", u"返回"]
        return d

    # 搜索设备超时
    def search_device_fail_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[text='配网失败']", "xpath", u"搜索设备超时"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        # 重试
        d["retry"] = ["com.aliyun.alink:id/button_deviceconfigfailed_retry", "id", u"重试"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='开关按钮']", "xpath", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_info"] = ["com.aliyun.alink:id/textview_atopbar_right_1", "id", u"设备信息进入按钮"]
        # 设备已启动模式定时
        d["launch_mode"] = ["//android.webkit.WebView/android.view.View[2]", "xpath", u"设备已启动模式定时"]
        # 设备离线标志
        d["offline"] = [u"//android.view.View[@text='content-desc='该设备已断开连接！']", "xpath", u"设备离线标志"]
        # 功率
        d["power"] = ["//android.webkit.WebView/android.view.View[3]", "xpath", u"功率"]
        # 电源开关
        d["power_button"] = [u"//android.view.View[@content-desc='开关按钮']", "xpath", u"电源开关"]
        # 热水器模式
        d["water_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项热水器']", "xpath", u"热水器模式"]
        # 小夜灯模式
        d["night_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项小夜灯']", "xpath", u"小夜灯模式"]
        # 鱼缸模式
        d["fish_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项鱼缸模式']", "xpath", u"鱼缸模式"]
        # 蚊香模式
        d["mosquito_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项蚊香模式']", "xpath", u"蚊香模式"]
        # 充电保护模式
        d["piocc_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项充电保护']", "xpath", u"充电保护模式"]
        # 取暖器模式
        d["warmer_mode_timer"] = [u"//android.view.View[@content-desc='栅格选项取暖器']", "xpath", u"取暖器模式"]
        # 定时任务
        d["normal_timer"] = [u"//android.view.View[contains(@content-desc, '定时任务')]", "xpath", u"定时任务"]
        # 延时任务
        d["delay_timer"] = [u"//android.view.View[contains(@content-desc, '延时任务')]", "xpath", u"延时任务"]
        # 循环任务
        d["cycle_timer"] = [u"//android.view.View[contains(@content-desc, '循环任务')]", "xpath", u"循环任务"]
        # 电价设置
        d["set_elec"] = [u"//android.view.View[contains(@content-desc, '电价设置')]", "xpath", u"电价设置"]
        # 用电数据
        d["elec"] = [u"//android.view.View[contains(@content-desc, '用电数据')]", "xpath", u"用电数据"]
        # 设备记忆模式
        d["memory_mode"] = ["//android.webkit.WebView/android.view.View[6]/android.view.View[2]", "xpath", u"记忆功能"]
        # 指示灯
        d["led"] = ["//android.webkit.WebView/android.view.View[7]/android.view.View[2]", "xpath", u"指示灯"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设备详情']", "xpath", u"设备信息页面"]
        # 删除设备按钮
        d["unbind"] = ["com.aliyun.alink:id/button_device_detail_unbind", "id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["com.aliyun.alink:id/relativeLayout_device_detail", "id", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 修改设备备注页面
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='修改设备名称']", "xpath", u"修改设备备注页面"]
        # 保存
        d["saved"] = ["com.aliyun.alink:id/textview_atopbar_right_1", "id", u"保存"]
        # 备注输入框
        d["nickname"] = ["//android.widget.EditText", "xpath", u"备注输入框"]
        # 返回按钮
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
        return d

    # 热水器模式页面
    def water_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='热水器模式']", "xpath", u"热水器模式页面"]
        # 开启时间
        d["start_time"] = ["//android.widget.ListView/android.view.View", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View[2]", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//android.widget.ListView[2]/android.view.View/android.view.View", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//android.widget.ListView", "xpath", u"时间交换", {"px": [0.05, 0.5]}]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 小夜灯模式页面
    def night_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='小夜灯模式']", "xpath", u"小夜灯模式页面"]
        # 开启时间
        d["start_time"] = ["//android.widget.ListView/android.view.View", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View[2]", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//android.widget.ListView[2]/android.view.View/android.view.View", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//android.widget.ListView", "xpath", u"时间交换", {"px": [0.05, 0.5]}]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 鱼缸模式页面
    def fish_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='鱼缸模式']", "xpath", u"鱼缸模式页面"]
        # 开启时间
        d["start_time"] = ["//android.widget.ListView/android.view.View", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View[2]", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//android.widget.ListView[2]/android.view.View/android.view.View", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//android.widget.ListView", "xpath", u"时间交换", {"px": [0.05, 0.5]}]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 蚊香模式页面
    def mosquito_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='电蚊香模式']", "xpath", u"蚊香模式页面"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View/android.view.View", "xpath", u"关闭时间"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 充电保护模式页面
    def piocc_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='充电保护模式']", "xpath", u"充电保护模式页面"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View/android.view.View", "xpath", u"关闭时间"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 取暖器模式页面
    def warmer_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='取暖器模式']", "xpath", u"取暖器模式页面"]
        # 开启时间
        d["start_time"] = ["//android.widget.ListView/android.view.View", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = ["//android.widget.ListView/android.view.View[2]", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//android.widget.ListView[2]/android.view.View/android.view.View", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"//android.view.View[@content-desc='启动模式']", "xpath", u"启动模式"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='关闭模式']", "xpath", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//android.widget.ListView", "xpath", u"时间交换", {"px": [0.05, 0.5]}]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='预约定时']", "xpath", u"普通定时页面"]
        # 添加定时
        d["add_normal_timer"] = [u"//android.view.View[@content-desc='添加一个']", "xpath", u"添加定时按钮"]
        # 编辑
        d["timer_edit"] = [u"//android.view.View[@content-desc='编辑']", "xpath", u"编辑按钮"]
        # 无设备
        d["no_timer"] = [u"//android.view.View[@content-desc='开关按钮']", "xpath", u"无设备"]
        # 删除定时
        d["delete_timer"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View", "xpath", u"删除定时"]
        # 删除
        d["delete"] = [u"//android.view.View[@content-desc='删除']", "xpath", u"删除"]
        # 完成
        d["saved"] = [u"//android.view.View[@content-desc='完成']", "xpath", u"完成"]
        # 定时循环信息
        timer_loop = {}
        for i in xrange(20):
            timer_loop[i] = "//android.webkit.WebView/android.view.View[4]/android.view.View[%s]" % (i * 3 + 2)
        d["timer_loop"] = [timer_loop, "xpath", u"定时循环信息"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='定时预约']", "xpath", u"新建普通定时页面"]
        # 定时开
        d["power_on"] = [u"//android.view.View[contains(@content-desc, '定时开')]", "xpath", u"定时开"]
        # 定时关
        d["power_off"] = [u"//android.view.View[contains(@content-desc, '定时关')]", "xpath", u"定时关"]
        # 时间滚轮整体控件
        d["roll"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.ListView",
                       "xpath", u"时间滚轮,时", {"px": [0.5, 0.59]}]
        # 时间滚轮,分
        d["roll_m"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.ListView[2]",
                       "xpath", u"时间滚轮,分", {"px": [0.5, 0.508]}]
        # 重复
        d["repeat"] = ["//android.view.View[4]/android.widget.ListView[2]/android.view.View/android.view.View",
                       "xpath", u"重复"]
        # 完成
        d["saved"] = [u"//android.view.View[@content-desc='完成']", "xpath", u"完成"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        return d

    # 新建延时定时页面
    def delay_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='延时任务']", "xpath", u"新建延时定时页面"]
        # 定时开
        d["power_on"] = [u"//android.view.View[contains(@content-desc, '延时开')]", "xpath", u"延时开"]
        # 定时关
        d["power_off"] = [u"//android.view.View[contains(@content-desc, '延时关')]", "xpath", u"延时关"]
        # 时间滚轮整体控件
        d["roll"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.ListView",
                       "xpath", u"时间滚轮,时", {"px": [0.5, 0.59]}]
        # 时间滚轮,分
        d["roll_m"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.ListView[2]",
                       "xpath", u"时间滚轮,分", {"px": [0.5, 0.508]}]
        # 启动
        d["launch"] = [u"//android.view.View[@content-desc='启动']", "xpath", u"启动"]
        # 延时时间
        d["delay_time"] = ["//android.view.View[3]/android.view.View", "xpath", u"延时时间"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 循环任务页面
    def cycle_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='循环任务']", "xpath", u"循环任务页面"]
        # 开启时间
        d["start_time"] = [u"//android.widget.ListView/android.view.View//android.view.View"
                           u"[contains(@content-desc, '分钟')]", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = [u"//android.widget.ListView/android.view.View[2]//android.view.View"
                         u"[contains(@content-desc, '分钟')]", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//android.widget.ListView[2]/android.view.View/android.view.View", "xpath", u"重复"]
        # 启动
        d["launch"] = [u"//android.view.View[@content-desc='启动']", "xpath", u"启动"]
        # 关闭模式
        d["close"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 时间交换
        d["time_exchange"] = ["//android.widget.ListView", "xpath", u"时间交换", {"px": [0.05, 0.5]}]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 定时重复页面
    def timer_repeat_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='完成']", "xpath", u"定时重复页面"]
        # 永不
        d["once"] = [u"//android.view.View[contains(@content-desc, '永不')]", "xpath", u"永不", {"px": [0.09, 0.5]}]
        # 周一
        d["monday"] = [u"//android.view.View[contains(@content-desc, '周一')]", "xpath", u"周一", {"px": [0.09, 0.5]}]
        # 周二
        d["tuesday"] = [u"//android.view.View[contains(@content-desc, '周二')]", "xpath", u"周二", {"px": [0.09, 0.5]}]
        # 周三
        d["wednesday"] = [u"//android.view.View[contains(@content-desc, '周三')]", "xpath", u"周三", {"px": [0.09, 0.5]}]
        # 周四
        d["thursday"] = [u"//android.view.View[contains(@content-desc, '周四')]", "xpath", u"周四", {"px": [0.09, 0.5]}]
        # 周五
        d["friday"] = [u"//android.view.View[contains(@content-desc, '周五')]", "xpath", u"周五", {"px": [0.09, 0.5]}]
        # 周六
        d["saturday"] = [u"//android.view.View[contains(@content-desc, '周六')]", "xpath", u"周六", {"px": [0.09, 0.5]}]
        # 周日
        d["weekday"] = [u"//android.view.View[contains(@content-desc, '周日')]", "xpath", u"周日", {"px": [0.09, 0.5]}]
        # 执行次数
        d["cycle_count"] = ["//android.webkit.WebView/android.view.View[4]/android.view.View", "xpath", u"执行次数",
                            {"px": [0.5, 0.5]}]
        # 完成
        d["saved"] = [u"//android.view.View[@content-desc='完成']", "xpath", u"完成"]
        # 取消
        d["to_return"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        return d

    # 电价设置页面
    def set_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[contains(@content-desc, '单一电价')]", "xpath", u"电价设置页面"]
        # 单一电价设置
        d["single_price"] = [u"//android.view.View[contains(@content-desc, '单一电价')]", "xpath", u"单一电价设置"]
        # 峰谷电价设置
        d["peak_valley_price"] = [u"//android.view.View[contains(@content-desc, '峰谷时间')]", "xpath", u"峰谷电价设置"]
        # 单一电价设置按钮
        d["single_button"] = [u"//android.view.View[contains(@content-desc, '单一电价')]", "xpath",
                              u"单一电价设置按钮", {"px": [0.09, 0.5]}]
        # 峰谷电价设置按钮
        d["peak_valley_button"] = [u"//android.view.View[contains(@content-desc, '峰谷时间')]", "xpath",
                                   u"峰谷电价设置按钮", {"px": [0.09, 0.5]}]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 返回按钮
        d["to_return"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"返回"]
        return d

    # 单一电价设置页面
    def single_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='单一电价设置']", "xpath", u"单一电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//android.widget.EditText", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 峰谷电价设置页面
    def peak_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='峰谷电设置']", "xpath", u"峰谷电价设置页面"]
        # 开启时间
        d["start_time"] = [u"//android.view.View[contains(@content-desc, '峰电开始时间')]", "xpath", u"峰电开始时间"]
        # 关闭时间
        d["end_time"] = [u"//android.view.View[contains(@content-desc, '峰电结束时间')]", "xpath", u"峰电结束时间"]
        # 设置峰电电价
        d["set_peak_price"] = ["//android.widget.ListView/android.view.View[3]/android.view.View", "xpath",
                               u"设置峰电电价"]
        # 设置谷电电价
        d["set_valley_price"] = ["//android.widget.ListView[2]/android.view.View[3]/android.view.View", "xpath",
                                 u"设置谷电电价"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 设置峰电电价
    def set_peak_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='峰电电价设置']", "xpath", u"峰电电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//android.widget.EditText", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 设置谷电电价
    def set_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='谷电电价设置']", "xpath", u"谷电电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//android.widget.EditText", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 用电数据页面
    def elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='用电数据']", "xpath", u"用电数据页面"]
        # 日
        d["day"] = [u"//android.view.View[@content-desc='日']", "xpath", u"日"]
        # 周
        d["week"] = [u"//android.view.View[@content-desc='周']", "xpath", u"周"]
        # 月
        d["month"] = [u"//android.view.View[@content-desc='月']", "xpath", u"月"]
        # 年
        d["year"] = [u"//android.view.View[@content-desc='年']", "xpath", u"年"]
        # 电费电量统计周期
        d["elec_time"] = ["//android.view.View[3]/android.view.View[7]", "xpath", u"电费电量统计周期"]
        # 当前年月
        d["now_year_month"] = ["//android.view.View[11]/android.view.View", "xpath", u"当前年月"]
        # 更多用电历史
        d["more_elec_history"] = [u"//android.view.View[@content-desc='更多']", "xpath", u"更多"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 更多用电历史页面
    def more_elec_history_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[contains(@content-desc, '月用电历史')]", "xpath", u"更多用电历史页面"]
        day_elec = {}
        for i in xrange(31):
            day_elec[i] = "//android.view.View[3]/android.view.View[%s]/android.view.View" % (i + 3)
        # 电量日期
        d["day_elec"] = [day_elec, "xpath", u"电量日期"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d

    # 日用电历史页面
    def day_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[contains(@content-desc, '日用电历史')]", "xpath", u"更多用电历史页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//android.view.View[3]/android.view.View[%s]/android.view.View" % (i + 2)
            price_value[i] = "//android.webkit.WebView/android.widget.ListView[%s]/android.view.View[2]" % (i + 2)
        # 电量时间
        d["elec_time"] = [price_time, "xpath", u"电量时间"]
        # 电量值
        d["elec_value"] = [price_value, "xpath", u"电量值"]
        # 返回按钮
        d["to_return"] = ["//android.webkit.WebView/android.view.View", "xpath", u"返回"]
        return d


class PopupWidgetAndroidAL(object):
    # 升级弹窗
    def update_popup(self):
        d = {}
        # 升级弹窗
        d["title"] = [u"//android.widget.TextView[@text='发现新版本']", "xpath", u"升级弹窗"]
        # 下次再更新
        d["cancel"] = [u"//android.widget.TextView[@text='下次再提醒']", "xpath", u"下次再更新"]
        # 立即更新
        d["confirm"] = [u"//android.widget.Button[@text='立即更新']", "xpath", u"立即更新"]
        return d

    # 添加设备弹窗
    def add_device_popup(self):
        d = {}
        # 添加设备弹窗
        d["title"] = [u"//android.widget.TextView[@text='添加家庭成员']", "xpath", u"添加设备弹窗"]
        # 添加设备
        d["add_device"] = [u"//android.widget.TextView[@text='添加设备']", "xpath", u"添加设备"]
        # 添加场景
        d["add_scene"] = [u"//android.widget.TextView[@text='添加场景']", "xpath", u"添加场景"]
        # 添加家庭成员
        d["add_home_member"] = [u"//android.widget.TextView[@text='添加家庭成员']", "xpath", u"添加家庭成员"]
        # 关闭按钮
        d["close"] = ["com.aliyun.alink:id/homepage_topbar_menu_btn", "id", u"关闭按钮"]
        return d

    # 设备已被绑定
    def bind_device_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[text='该设备已被绑定']", "xpath", u"该设备已被绑定"]
        return d

    # 解绑设备弹窗
    def unbind_device_popup(self):
        d = {}
        # 删除设备弹窗
        d["title"] = [u"//android.widget.TextView[@text='确认解除绑定？']", "xpath", u"删除设备按钮"]
        # 确定
        d["confirm"] = [u"//android.widget.Button[@text='解绑']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.widget.Button[@text='取消']", "xpath", u"取消"]
        return d

    # 模式冲突提示弹窗
    def mode_timer_conflict_popup(self):
        d = {}
        # 模式冲突提示
        d["title"] = [u"//android.view.View[contains(@content-desc, '之前的定时模式将失效')]", "xpath", u"模式冲突提示弹窗"]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        return d

    # 页面加载等待
    def loading_popup(self):
        d = {}
        # 标题
        d["title"] = ["com.aliyun.alink:id/aloadview2_imageview_icon", "id", u"正在加载中loading..."]
        # 设备状态上传
        d["upload"] = [u"//android.view.View[@content-desc='正在同步设备状态，请稍候...']", "xpath", u"设备状态上传"]
        return d

    # 登出弹窗
    def logout_popup(self):
        d = {}
        # 退出登录弹窗
        d["title"] = [u"//android.widget.TextView[@text='退出登录']", "xpath", u"退出登录弹窗"]
        # 确认
        d["confirm"] = [u"//android.widget.TextView[@text='退出登录']", "xpath", u"退出登录"]
        # 取消
        d["cancel"] = [u"//android.widget.TextView[@text='取消']", "xpath", u"取消"]
        return d

    # 时间设置滚轮
    def timer_roll_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='设置时间']", "xpath", u"设置时间"]
        # 时间滚轮整体控件
        d["roll"] = ["//android.webkit.WebView/android.view.View[6]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//android.webkit.WebView/android.view.View[6]/android.widget.ListView", "xpath",
                       u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["//android.webkit.WebView/android.view.View[6]/android.widget.ListView[2]", "xpath",
                       u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 确定
        d["confirm"] = [u"//android.view.View[@content-desc='确定']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.view.View[@content-desc='取消']", "xpath", u"取消"]
        return d


class MainPageWidgetIosAL(object):
    # 欢迎页
    def welcome_page(self):
        d = {}
        # 标题
        d["title"] = ["btn_skip", "accessibility_id", u"欢迎页"]
        # 跳过
        d["skip"] = ["btn_skip", "accessibility_id", u"跳过"]
        return d

    # “我的”页面
    def my_page(self):
        d = {}
        # 标题
        d["title"] = [u"自动化", "accessibility_id", u"“我的家”页面"]
        # 设置
        d["setting"] = [u"设置", "accessibility_id", u"设置"]
        return d

    # 账户登录页面
    def login_page(self):
        d = {}
        # 标题
        d["title"] = [u"账户登录", "accessibility_id", u"账户登录页面"]
        # 用户名
        d["username"] = ["//XCUIElementTypeTextField", "xpath", u"用户名输入框"]
        # 密码
        d["password"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeTextField", "xpath", u"密码输入框"]
        # 显示/关闭密码
        d["check_box"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeButton", "xpath", u"显示/关闭密码"]
        # 登录
        d["login_button"] = [u"登录", "accessibility_id", u"登录按钮"]
        # 返回
        d["to_return"] = [u"返回", "accessibility_id", u"返回"]
        return d

    # 设置页面
    def setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"设置", "accessibility_id", u"设置页面"]
        # 帮助与反馈
        d["feedback"] = [u"  帮助与反馈 ", "accessibility_id", u"帮助与反馈"]
        # 关于阿里智能
        d["about"] = [u"  关于阿里智能 ", "accessibility_id", u"关于阿里智能"]
        # 返回
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        # 登出
        d["logout"] = [u" 退出当前账号", "accessibility_id", u"退出当前账号"]
        return d

    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = [u"我的场景", "accessibility_id", u"App主页面"]
        # +号
        d["add_device"] = [u"〡", "accessibility_id", u"+号"]
        # 没有设备
        d["no_device"] = [u"添加设备开启智能生活", "accessibility_id", u"没有设备"]
        # 设备
        device = {}
        device_button = {}
        device_state = {}
        tmp = "//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView"
        for i in xrange(7):
            device[i] = ("%s/XCUIElementTypeCell[%s]//XCUIElementTypeStaticText" % (tmp, i + 1))
            device_button[i] = ("%s/XCUIElementTypeCell[%s]//XCUIElementTypeButton" % (tmp, i + 1))
            device_state[i] = ("%s/XCUIElementTypeCell[%s]//XCUIElementTypeStaticText[2]" % (tmp, i + 1))
        d["device"] = [device, "xpath", u"待控设备"]
        # 有设备
        d["has_device"] = ["//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView"
                           "/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage", "xpath", u"有设备"]
        # 设备开关
        d["device_button"] = [device_button, "xpath", u"待控设备开关"]
        # 设备状态
        d["device_state"] = [device_state, "xpath", u"设备状态"]
        # “我的”按钮
        d["my"] = [u"我的", "accessibility_id", u"“我的”按钮"]
        # “我的家”按钮
        d["my_home"] = [u"我的家", "accessibility_id", u"“我的家”按钮"]
        return d

    # 选择添加方式页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = [u"选择添加方式", "accessibility_id", u"选择添加方式"]
        # 分类查找
        d["variety"] = ["akp add category add", "accessibility_id", u"分类查找"]
        # 返回
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        return d

    # 设备类别页面
    def add_device_class_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备类别", "accessibility_id", u"设备类别页面"]
        # 插座排插
        d["outlet"] = [u"插座排插", "accessibility_id", u"插座排插"]
        # 返回
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        return d

    # 插座排插页面
    def add_outlet_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"插座排插", "accessibility_id", u"插座排插页面"]
        # 公牛WiFi智能插座2代（电量统计版）
        d["y201S"] = [u"//XCUIElementTypeButton[contains(@name, '公牛WiFi智能插座2代（电量统计版）')]", "xpath",
                      u"公牛WiFi智能插座2代（电量统计版）"]
        # 公牛WiFi智能插座2代
        d["y2010"] = [u"//XCUIElementTypeButton[contains(@name, '公牛WiFi智能插座2代']", "xpath", u"公牛WiFi智能插座2代"]
        # 返回
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        return d

    # 搜索设备页
    def add_specification_page(self):
        d = {}
        # 标题
        d["title"] = [u"//XCUIElementTypeTextView[contains(@name, '插座上电，若指示灯红蓝交替闪烁')]", "xpath", u"搜索设备页"]
        # 下一步
        d["next"] = [u"下一步", "accessibility_id", u"下一步"]
        # 返回
        d["to_return"] = ["bt nav back", "accessibility_id", u"返回"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"确认家庭Wi-Fi", "accessibility_id", u"进入输入密码页面"]
        # wifi
        d["wifi"] = ["//XCUIElementTypeTextField", "xpath", u"wifi名称"]
        # 确认wifi密码按钮
        d["confirm"] = [u"搜索设备", "accessibility_id", u"确认wifi密码按钮"]
        # wifi密码输入框
        d["password"] = ["//XCUIElementTypeTextField", "xpath", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = ["//XCUIElementTypeButton[contains(@name, 'akp pwd reveal')]", "xpath", u"密码显示关闭"]
        # 返回
        d["to_return"] = ["bt nav back", "accessibility_id", u"返回"]
        return d

    # 搜索设备等待页面
    def search_device_loading_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备添加中...", "accessibility_id", u"搜索设备等待页面"]
        # 返回
        d["to_return"] = ["bt nav back", "accessibility_id", u"返回"]
        return d

    # 搜索设备超时
    def search_device_fail_page(self):
        d = {}
        # 标题
        d["title"] = [u"配网失败", "accessibility_id", u"搜索设备超时"]
        # 返回
        d["to_return"] = ["ic back nav", "accessibility_id", u"返回"]
        # 重试
        d["retry"] = [u"重试", "accessibility_id", u"重试"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"实时功率", "accessibility_id", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_info"] = [u"を", "accessibility_id", u"设备信息进入按钮"]
        # 设备已启动模式定时
        d["launch_mode"] = [u"//XCUIElementTypeOther[contains(@name, '设备控制面板')]/XCUIElementTypeOther[2]"
                            u"/XCUIElementTypeStaticText", "xpath", u"设备已启动模式定时"]
        # 功率
        d["power"] = ["/XCUIElementTypeOther[4]/XCUIElementTypeStaticText", "xpath", u"功率"]
        # 电源开关
        d["power_button"] = [u"开关按钮", "accessibility_id", u"电源开关"]
        # 热水器模式
        d["water_mode_timer"] = [u"热水器", "accessibility_id", u"热水器模式"]
        # 小夜灯模式
        d["night_mode_timer"] = [u"小夜灯", "accessibility_id", u"小夜灯模式"]
        # 鱼缸模式
        d["fish_mode_timer"] = [u"鱼缸模式", "accessibility_id", u"鱼缸模式"]
        # 蚊香模式
        d["mosquito_mode_timer"] = [u"蚊香模式", "accessibility_id", u"蚊香模式"]
        # 充电保护模式
        d["piocc_mode_timer"] = [u"充电保护", "accessibility_id", u"充电保护模式"]
        # 取暖器模式
        d["warmer_mode_timer"] = [u"取暖器", "accessibility_id", u"取暖器模式"]
        # 定时任务
        d["normal_timer"] = [u"定时任务", "accessibility_id", u"定时任务"]
        # 延时任务
        d["delay_timer"] = [u"延时任务", "accessibility_id", u"延时任务"]
        # 循环任务
        d["cycle_timer"] = [u"循环任务", "accessibility_id", u"循环任务"]
        # 电价设置
        d["set_elec"] = [u"电价设置", "accessibility_id", u"电价设置"]
        # 用电数据
        d["elec"] = [u"用电数据", "accessibility_id", u"用电数据"]
        # 设备记忆模式
        d["memory_mode"] = ["//XCUIElementTypeOther[10]/XCUIElementTypeOther", "xpath", u"记忆功能"]
        # 指示灯
        d["led"] = ["//XCUIElementTypeOther[11]/XCUIElementTypeOther", "xpath", u"指示灯"]
        # 返回
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备详情", "accessibility_id", u"设备信息页面"]
        # 删除设备按钮
        d["unbind"] = ["com.aliyun.alink:id/button_device_detail_unbind", "accessibility_id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["//XCUIElementTypeCell[3]/XCUIElementTypeStaticText[3]", "xpath", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = [u"返回", "accessibility_id", u"返回"]
        return d

    # 修改设备备注页面
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改设备名称", "accessibility_id", u"修改设备备注页面"]
        # 保存
        d["saved"] = [u"保存", "accessibility_id", u"保存"]
        # 备注输入框
        d["nickname"] = ["//XCUIElementTypeTextField", "xpath", u"备注输入框"]
        # 返回按钮
        d["to_return"] = ["  ", "accessibility_id", u"返回"]
        return d

    # 热水器模式页面
    def water_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"热水器模式", "accessibility_id", u"热水器模式页面"]
        # 开启时间
        d["start_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"开启时间"]
        # 跨日定时
        d["is_date"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther"
                        "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"跨日定时"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeOther"
                         "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//XCUIElementTypeOther[6]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//XCUIElementTypeOther[3]", "xpath", u"时间交换"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 小夜灯模式页面
    def night_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"小夜灯模式", "accessibility_id", u"小夜灯模式页面"]
        # 开启时间
        d["start_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"开启时间"]
        # 跨日定时
        d["is_date"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther"
                        "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"跨日定时"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeOther"
                         "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//XCUIElementTypeOther[6]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//XCUIElementTypeOther[3]", "xpath", u"时间交换"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 鱼缸模式页面
    def fish_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"鱼缸模式", "accessibility_id", u"鱼缸模式页面"]
        # 开启时间
        d["start_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"开启时间"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther"
                         "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//XCUIElementTypeOther[6]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//XCUIElementTypeOther[3]", "xpath", u"时间交换"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 蚊香模式页面
    def mosquito_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"电蚊香模式", "accessibility_id", u"蚊香模式页面"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath",
                         u"关闭时间"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 充电保护模式页面
    def piocc_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"充电保护模式", "accessibility_id", u"充电保护模式页面"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath",
                         u"关闭时间"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 取暖器模式页面
    def warmer_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"取暖器模式", "accessibility_id", u"取暖器模式页面"]
        # 开启时间
        d["start_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"开启时间"]
        # 跨日定时
        d["is_date"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther"
                        "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"跨日定时"]
        # 关闭时间
        d["end_time"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeOther"
                         "/XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"关闭时间"]
        # 重复
        d["repeat"] = ["//XCUIElementTypeOther[6]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 启动模式
        d["launch"] = [u"启动模式", "accessibility_id", u"启动模式"]
        # 关闭模式
        d["close"] = [u"关闭模式", "accessibility_id", u"关闭模式"]
        # 时间交换
        d["time_exchange"] = ["//XCUIElementTypeOther[3]", "xpath", u"时间交换"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"预约定时", "accessibility_id", u"普通定时页面"]
        # 添加定时
        d["add_normal_timer"] = [u"添加一个", "accessibility_id", u"添加定时按钮"]
        # 编辑
        d["timer_edit"] = [u"编辑", "accessibility_id", u"编辑按钮"]
        # 无设备
        d["no_timer"] = [u"开关按钮", "accessibility_id", u"无设备"]
        # 删除定时
        d["delete_timer"] = [u"//XCUIElementTypeStaticText[contains(@name, '')]", "xpath", u"删除定时"]
        # 删除
        d["delete"] = [u"删除", "accessibility_id", u"删除"]
        # 完成
        d["saved"] = [u"完成", "accessibility_id", u"完成"]
        # 定时循环信息
        timer_loop = {}
        for i in xrange(20):
            timer_loop[i] = "//XCUIElementTypeOther[%s]/XCUIElementTypeStaticText" % (i * 3 + 3)
        d["timer_loop"] = [timer_loop, "xpath", u"定时循环信息"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"定时预约", "accessibility_id", u"新建普通定时页面"]
        # 定时开
        d["power_on"] = [u"定时开", "accessibility_id", u"定时开"]
        # 定时关
        d["power_off"] = [u"定时关", "accessibility_id", u"定时关"]
        # 时间滚轮整体控件
        d["roll"] = ["//XCUIElementTypeOther[4]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeOther[2]", "xpath", u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeOther[3]", "xpath", u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 重复
        d["repeat"] = [u"//XCUIElementTypeOther[6]//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 完成
        d["saved"] = [u"完成", "accessibility_id", u"完成"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 新建延时定时页面
    def delay_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"延时任务", "accessibility_id", u"新建延时定时页面"]
        # 定时开
        d["power_on"] = [u"定时开", "accessibility_id", u"定时开"]
        # 定时关
        d["power_off"] = [u"定时关", "accessibility_id", u"定时关"]
        # 时间滚轮整体控件
        d["roll"] = ["//XCUIElementTypeOther[4]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeOther[2]", "xpath", u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["//XCUIElementTypeOther[4]//XCUIElementTypeOther[3]", "xpath", u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 启动
        d["launch"] = [u"启动", "accessibility_id", u"启动"]
        # 延时时间_时
        d["delay_time_h"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeStaticText", "xpath", u"延时时间_时"]
        # 延时时间_分
        d["delay_time_m"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeStaticText[3]", "xpath", u"延时时间_分"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 循环任务页面
    def cycle_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"循环任务", "accessibility_id", u"循环任务页面"]
        # 开启时间_时
        d["start_time_h"] = [u"//android.widget.ListView/android.view.View//android.view.View"
                             u"[contains(@content-desc, '小时')]", "xpath", u"开启时间_时"]
        # 开启时间_分
        d["start_time_m"] = [u"//android.widget.ListView/android.view.View//android.view.View"
                             u"[contains(@content-desc, '分钟')]", "xpath", u"开启时间_分"]
        # 关闭时间_时
        d["end_time_h"] = [u"//android.widget.ListView/android.view.View[2]//android.view.View"
                           u"[contains(@content-desc, '小时')]", "xpath", u"关闭时间_时"]
        # 关闭时间_分
        d["end_time_m"] = [u"//android.widget.ListView/android.view.View[2]//android.view.View"
                           u"[contains(@content-desc, '分钟')]", "xpath", u"关闭时间_分"]
        # 重复
        d["repeat"] = ["//XCUIElementTypeLink[3]/XCUIElementTypeStaticText", "xpath", u"重复"]
        # 启动
        d["launch"] = [u"启动", "accessibility_id", u"启动"]
        # 关闭模式
        d["close"] = [u"取消", "accessibility_id", u"取消"]
        # 时间交换
        d["time_exchange"] = ["//XCUIElementTypeOther[2]", "xpath", u"时间交换"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 定时重复页面
    def timer_repeat_page(self):
        d = {}
        # 标题
        d["title"] = [u"完成", "accessibility_id", u"定时重复页面"]
        # 永不
        d["once"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther"
                     "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"永不"]
        # 周一
        d["monday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[2]"
                       "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周一"]
        # 周二
        d["tuesday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[3]"
                        "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周二"]
        # 周三
        d["wednesday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[4]"
                          "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周三"]
        # 周四
        d["thursday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[5]"
                         "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周四"]
        # 周五
        d["friday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[6]"
                       "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周五"]
        # 周六
        d["saturday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[7]"
                         "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周六"]
        # 周日
        d["weekday"] = ["//XCUIElementTypeOther[3]/XCUIElementTypeOther[8]"
                        "//XCUIElementTypeLink/XCUIElementTypeStaticText", "xpath", u"周日"]
        # 执行次数
        d["cycle_count"] = [u"//XCUIElementTypeOther[contains(@name, '设备控制面板')]/XCUIElementTypeOther[2]",
                            "xpath", u"执行次数"]
        # 完成
        d["saved"] = [u"完成", "accessibility_id", u"完成"]
        # 取消
        d["to_return"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 电价设置页面
    def set_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"单一电价设置", "accessibility_id", u"电价设置页面"]
        # 单一电价设置
        d["single_price"] = [u"单一电价设置", "accessibility_id", u"单一电价设置"]
        # 峰谷电价设置
        d["peak_valley_price"] = [u"峰谷时间段电价", "accessibility_id", u"峰谷电价设置"]
        # 单一电价设置按钮
        d["single_button"] = [u"//XCUIElementTypeLink[contains(@name, '单一')]//XCUIElementTypeStaticText",
                              "xpath", u"单一电价设置按钮"]
        # 峰谷电价设置按钮
        d["peak_valley_button"] = [u"//XCUIElementTypeLink[contains(@name, '峰谷')]//XCUIElementTypeStaticText",
                                   "xpath", u"峰谷电价设置按钮"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 单一电价设置页面
    def single_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"单一电价设置", "accessibility_id", u"单一电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//XCUIElementTypeTextField", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 峰谷电价设置页面
    def peak_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"峰谷电设置", "accessibility_id", u"峰谷电价设置页面"]
        # 开启时间
        d["start_time"] = [u"//XCUIElementTypeLink[contains(@name, '峰电开始时间 ')]", "xpath", u"峰电开始时间"]
        # 关闭时间
        d["end_time"] = [u"//XCUIElementTypeLink[contains(@name, '峰电结束时间 ')]", "xpath", u"峰电结束时间"]
        # 设置峰电电价
        d["set_peak_price"] = [u"//XCUIElementTypeOther[3]/XCUIElementTypeOther[3]//XCUIElementTypeLink"
                               u"//XCUIElementTypeStaticText", "xpath", u"设置峰电电价"]
        # 设置谷电电价
        d["set_valley_price"] = [u"//XCUIElementTypeOther[5]/XCUIElementTypeOther[3]//XCUIElementTypeLink"
                                 u"//XCUIElementTypeStaticText", "xpath", u"设置谷电电价"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 设置峰电电价
    def set_peak_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"峰电电价设置", "accessibility_id", u"峰电电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//XCUIElementTypeTextField", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 设置谷电电价
    def set_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"谷电电价设置", "accessibility_id", u"谷电电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//XCUIElementTypeTextField", "xpath", u"设置电价"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 用电数据页面
    def elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"用电数据", "accessibility_id", u"用电数据页面"]
        # 日
        d["day"] = [u"日", "accessibility_id", u"日"]
        # 周
        d["week"] = [u"周", "accessibility_id", u"周"]
        # 月
        d["month"] = [u"月", "accessibility_id", u"月"]
        # 年
        d["year"] = [u"年", "accessibility_id", u"年"]
        # 电费电量统计周期
        d["elec_time"] = [u"//XCUIElementTypeStaticText[contains(@name, '总电量:')]", "xpath", u"电费电量统计周期"]
        # 当前年月
        d["now_year_month"] = [u"//XCUIElementTypeOther[contains(@name, '设备控制面板')]/XCUIElementTypeOther[8]"
                               u"//XCUIElementTypeStaticText", "xpath", u"当前年月"]
        # 更多用电历史
        d["more_elec_history"] = [u"//XCUIElementTypeOther[8]/XCUIElementTypeOther[4]/XCUIElementTypeStaticText",
                                  "xpath", u"更多"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 更多用电历史页面
    def more_elec_history_page(self):
        d = {}
        # 标题
        d["title"] = [u"//XCUIElementTypeStaticText[contains(@name, '月用电历史')]", "xpath", u"更多用电历史页面"]
        day_elec = {}
        for i in xrange(31):
            day_elec[i] = "//XCUIElementTypeOther[%s]/XCUIElementTypeStaticText" % (i + 4)
        # 电量日期
        d["day_elec"] = [day_elec, "xpath", u"电量日期"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d

    # 日用电历史页面
    def day_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//XCUIElementTypeStaticText[contains(@name, '日用电历史')]", "xpath", u"更多用电历史页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//XCUIElementTypeOther[%s]/XCUIElementTypeStaticText" % (i + 3)
            price_value[i] = "//XCUIElementTypeOther[%s]/XCUIElementTypeOther/XCUIElementTypeStaticText" % (i + 3)
        # 电量时间
        d["elec_time"] = [price_time, "xpath", u"电量时间"]
        # 电量值
        d["elec_value"] = [price_value, "xpath", u"电量值"]
        # 返回按钮
        d["to_return"] = [u"", "accessibility_id", u"返回"]
        return d


class PopupWidgetIosAL(object):
    # 升级弹窗
    def update_popup(self):
        d = {}
        # 升级弹窗
        d["title"] = [u"发现新版本", "accessibility_id", u"升级弹窗"]
        # 下次再更新
        d["cancel"] = [u"下次再提醒", "accessibility_id", u"下次再更新"]
        # 立即更新
        d["confirm"] = [u"立即更新", "accessibility_id", u"立即更新"]
        return d

    # 添加设备弹窗
    def add_device_popup(self):
        d = {}
        # 添加设备弹窗
        d["title"] = [u"添加家庭成员", "accessibility_id", u"添加设备弹窗"]
        # 添加设备
        d["add_device"] = [u"添加设备　　", "accessibility_id", u"添加设备"]
        # 添加场景
        d["add_scene"] = [u"添加场景　　", "accessibility_id", u"添加场景"]
        # 添加家庭成员
        d["add_home_member"] = [u"添加家庭成员", "accessibility_id", u"添加家庭成员"]
        # 关闭按钮
        d["close"] = [u"〡", "accessibility_id", u"关闭按钮"]
        return d

    # 设备已被绑定
    def bind_device_popup(self):
        d = {}
        # 标题
        d["title"] = [u"您的账号还没被授权", "accessibility_id", u"该设备已被绑定"]
        return d

    # 解绑设备弹窗
    def unbind_device_popup(self):
        d = {}
        # 删除设备弹窗
        d["title"] = [u"确认解除绑定？", "accessibility_id", u"删除设备按钮"]
        # 确定
        d["confirm"] = [u"解绑", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 模式冲突提示弹窗
    def mode_timer_conflict_popup(self):
        d = {}
        # 模式冲突提示
        d["title"] = [u"//XCUIElementTypeStaticText[contains(@name, '之前的定时模式将失效')]", "xpath", u"模式冲突提示弹窗"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 页面加载等待
    def loading_popup(self):
        d = {}
        # 标题
        d["title"] = ["AKLoadingView.bundle/loading", "accessibility_id", u"正在加载中loading..."]
        # 正在加载
        d["load"] = [u"//XCUIElementTypeStaticText[contains(@name, '正在加载')]", "xpath", u"正在加载"]
        # 设备状态上传
        d["upload"] = [u"//XCUIElementTypeStaticText[contains(@name, '正在同步设备状态')]", "xpath", u"设备状态上传"]
        return d

    # 登出弹窗
    def logout_popup(self):
        d = {}
        # 退出登录弹窗
        d["title"] = [u"  退出登录]", "accessibility_id", u"退出登录弹窗"]
        # 确认
        d["confirm"] = [u"  退出登录", "accessibility_id", u"退出登录"]
        # 取消
        d["cancel"] = [u"  取消", "accessibility_id", u"取消"]
        return d

    # 时间设置滚轮
    def timer_roll_popup(self):
        d = {}
        # 标题
        d["title"] = [u"设置时间", "accessibility_id", u"设置时间"]
        # 时间滚轮整体控件
        d["roll"] = ["//XCUIElementTypeOther[8]/XCUIElementTypeOther[2]", "xpath", u"时间滚轮整体控件"]
        # 时间滚轮,时
        d["roll_h"] = ["//XCUIElementTypeOther[8]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]", "xpath",
                       u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["//XCUIElementTypeOther[8]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]", "xpath",
                       u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d


class PageElement(object):
    def __init__(self):
        self.mpw = MainPageWidgetAndroidAL()
        self.pw = PopupWidgetAndroidAL()
        # self.mpw = MainPageWidgetIosJD()
        # self.pw = PopupWidgetIosJD()
        self.get_page_element()

    def get_page_element(self):
        self.page = {}
        self.page["add_device_class_page"] = self.mpw.add_device_class_page()
        self.page["add_device_method_page"] = self.mpw.add_device_method_page()
        self.page["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        self.page["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        self.page["add_specification_page"] = self.mpw.add_specification_page()
        self.page["app_home_page"] = self.mpw.app_home_page()
        self.page["change_nickname_page"] = self.mpw.change_nickname_page()
        self.page["control_device_page"] = self.mpw.control_device_page()
        self.page["cycle_timer_page"] = self.mpw.cycle_timer_page()
        self.page["day_elec_page"] = self.mpw.day_elec_page()
        self.page["delay_timer_page"] = self.mpw.delay_timer_page()
        self.page["device_info_page"] = self.mpw.device_info_page()
        self.page["elec_page"] = self.mpw.elec_page()
        self.page["fish_mode_timer_page"] = self.mpw.fish_mode_timer_page()
        self.page["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.page["login_page"] = self.mpw.login_page()
        self.page["more_elec_history_page"] = self.mpw.more_elec_history_page()
        self.page["mosquito_mode_timer_page"] = self.mpw.mosquito_mode_timer_page()
        self.page["my_page"] = self.mpw.my_page()
        self.page["night_mode_timer_page"] = self.mpw.night_mode_timer_page()
        self.page["normal_timer_page"] = self.mpw.normal_timer_page()
        self.page["peak_valley_price_page"] = self.mpw.peak_valley_price_page()
        self.page["piocc_mode_timer_page"] = self.mpw.piocc_mode_timer_page()
        self.page["search_device_fail_page"] = self.mpw.search_device_fail_page()
        self.page["search_device_loading_page"] = self.mpw.search_device_loading_page()
        self.page["set_elec_page"] = self.mpw.set_elec_page()
        self.page["set_peak_price_page"] = self.mpw.set_peak_price_page()
        self.page["set_valley_price_page"] = self.mpw.set_valley_price_page()
        self.page["setting_page"] = self.mpw.setting_page()
        self.page["single_price_page"] = self.mpw.single_price_page()
        self.page["timer_repeat_page"] = self.mpw.timer_repeat_page()
        self.page["warmer_mode_timer_page"] = self.mpw.warmer_mode_timer_page()
        self.page["water_mode_timer_page"] = self.mpw.water_mode_timer_page()
        self.page["welcome_page"] = self.mpw.welcome_page()

        self.page["add_device_popup"] = self.pw.add_device_popup()
        self.page["bind_device_popup"] = self.pw.bind_device_popup()
        self.page["loading_popup"] = self.pw.loading_popup()
        self.page["logout_popup"] = self.pw.logout_popup()
        self.page["mode_timer_conflict_popup"] = self.pw.mode_timer_conflict_popup()
        self.page["timer_roll_popup"] = self.pw.timer_roll_popup()
        self.page["unbind_device_popup"] = self.pw.unbind_device_popup()
        self.page["update_popup"] = self.pw.update_popup()

        return self.page


page = PageElement().page


class WidgetCheckUnit(Exception):
    def __init__(self, driver, page_element):
        self.driver = driver
        self.page = page_element

    def copy(self):
        copy.copy("init for copy")

    # 等待元素出现，同于find_element_*
    def wait_widget(self, main_widget, timeout=3.0, interval=1.0, log_record=1):
        self.px = plural = False  # 元素在屏幕的像素坐标
        if not isinstance(main_widget, list):
            raise TypeError("main_widget must be list! [widget, locate method...]")
        locate = main_widget[1]  # page函数中的元素查找名称，例："//XCUIElementTypeTextField","btn_skip"，etc
        widget = main_widget[0]  # page函数中的元素查找方式，例："xpath","name","id"，etc
        try:
            if isinstance(widget, dict):
                plural = "dict"
            keys = main_widget[3]  # 读取页面元素的附加属性，包含index索引；px参考系为指定元素的坐标；pxw，参考系为屏幕分辨率；
            key = keys.keys()
            if "px" in key:
                self.px = [keys["px"], "px"]  # 待控元素像素对参考元素坐标的比例关系
            elif "pxw" in key:
                self.px = [keys["pxw"], "pxw"]  # 待控元素像素对屏幕分辨率的比例关系
            if "index" in key:
                index = int(keys["index"])  # 采用find_elements后的元素列表索引来定位元素
                plural = True  # 采用find_elements定位
        except IndexError:
            pass
        end_time = time.time() + timeout  # 设定元素查找超时时间
        while True:
            try:
                time.sleep(0.5)
                # 元素定位方式
                if locate == "id":
                    if plural is False:
                        element = self.driver.find_element_by_id(widget)
                    else:
                        element = self.driver.find_elements_by_id(widget)[index]
                elif locate == "accessibility_id":
                    if plural is False:
                        element = self.driver.find_element_by_accessibility_id(widget)
                    else:
                        element = self.driver.find_elements_by_accessibility_id(widget)[index]
                elif locate == "xpath":
                    # 当页面同类型元素很多或者页面元素不确定是否会出现时，单一判断依据已失效，
                    # 使用xpath轮询的方式来查找出所有同类元素，再根据待查找元素的指定特征再进行判断；
                    if plural is False:
                        element = self.driver.find_element_by_xpath(widget)
                    elif plural is True:
                        element = self.driver.find_elements_by_xpath(widget)[index]
                    else:
                        # 返回元素字典
                        # 输入→//XCUIElementTypeTextField[1] 输出→type(driver.WebElement...[1])
                        #      //XCUIElementTypeTextField[2]      type(driver.WebElement...[2])
                        #      ...                                ...
                        # return element:{0:WebElement, 1:WebElement...}
                        element = {}
                        for k, v in widget.items():
                            try:
                                element[k] = self.driver.find_element_by_xpath(v)
                            except NoSuchElementException:
                                element[k] = None
                elif locate == "class":
                    if plural is False:
                        element = self.driver.find_element_by_class_name(widget)
                    else:
                        element = self.driver.find_elements_by_class_name(widget)[index]
                elif locate == "name":
                    if plural is False:
                        element = self.driver.find_element_by_name(widget)
                    else:
                        element = self.driver.find_elements_by_name(widget)[index]
                elif locate == "activity":
                    element = self.driver.wait_activity(widget)
                else:
                    raise KeyError('find_element_by_%s must in ["id", "name", "class", "xpath", "activity", '
                                   '"accessibility_id"' % locate)
                # 根据需要开启log日志记录
                log_tmp = '[APP_INFO] wait_widget ["%s"] success' % main_widget[2]
                if log_record != 0:
                    print(log_tmp)

                return element
            except NoSuchElementException:
                if time.time() > end_time:
                    raise TimeoutException()
                time.sleep(interval)

    # 点击元素，同于element.click()
    def widget_click(self, operate_widget=None, wait_page=None, wait_time1=3, wait_time2=3,
                     times=3, interval=1, log_record=1):
        """
            Using click operation widgets - 使用点击方式操作元素
            widget_click(self, operate_widget=None, wait_page=None, wait_time1=1, wait_time2=1, timeout=6, interval=1,
                         log_record=1, operate_driver="find_element_in_driver", wait_driver="find_element_in_driver")
        Args:
            :param operate_widget: To control operation
                               待操作的元素
            :param wait_page: Check whether the widgets operation is successful
                          检查元素是否操作成功
            :param wait_time1: operate_widget——wait_time
                           operate_widget操作等待时间，超时报错
            :param wait_time2: wait_page——wait_time
                           wait_page操作等待时间，超时报错
            :param times: Operate times
                        元素操作次数
            :param interval: Polling time
                         轮询时间
            :param log_record: The flag of record the log
                        是否记录log
        :return element
        """
        if not isinstance(operate_widget, list):
            raise TypeError("operate_widget must be list! [widget_id, type(widget_id)]")
        elif not (isinstance(wait_page, list) or wait_page is None):
            raise TypeError("wait_page must be list! [widget_id, type(widget_id)]")
        run_times = times  # 操作元素的次数，不使用时间，需要元素操作次数场合使用时间不确定性太大。
        flag = 0  # 元素操作失败步骤标志位
        click_flag = True
        widget = None  # 初始化widget，避免Local variable 'widget' might be referenced before assignment错误；
        while True:
            try:
                # 点击待控元素
                if click_flag is True:
                    flag = 0
                    widget = self.wait_widget(operate_widget, wait_time1, interval, 0)
                    if self.px is False:  # 元素附属属性没有px/pxw，使用正常操作点击元素
                        widget.click()
                    elif self.px[1] == "px":  # 使用px方式点击元素坐标
                        px = self.px[0]
                        lc, sz = widget.location, widget.size
                        pxx, pxy = int(lc["x"] + px[0] * sz["width"]), int(lc["y"] + px[1] * sz["height"])
                        try:
                            self.driver.tap([(pxx, pxy)])
                        except WebDriverException:
                            raise TimeoutException()
                    else:  # 使用pxw方式点击屏幕坐标
                        px = self.px[0]
                        ws = self.driver.get_window_size()
                        pxx, pxy = int(ws["width"] * px[0]), int(ws["height"] * px[1])
                        try:
                            self.driver.tap([(pxx, pxy)])
                        except WebDriverException:
                            raise TimeoutException()

                    # 点击元素后会有页面跳转加载动画，等待页面加载完成
                    while True:
                        try:
                            for k in self.page["loading_popup"].keys():
                                self.wait_widget(self.page["loading_popup"][k], 0.2, 0.1, 0)
                        except TimeoutException:
                            break
                    # 根据需要开启log日志记录
                    log_tmp = '[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2]
                    if log_record != 0:
                        print(log_tmp)
                    time.sleep(0.1)
                # 点击元素后等待页面加载
                # 如果wait_page为None，则跳过此检测
                if wait_page is not None:
                    flag = 1
                    self.wait_widget(wait_page, wait_time2, interval, 0)
                return widget
            except TimeoutException:
                run_times -= 1
                if run_times == 0:
                    if flag == 0:  # 点击操作未完成
                        error_info = "[ERROR]Failed to operate element.UiSelector[RESOURCE_ID=%s]" % [operate_widget[0]]
                        logger_info = '[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2]
                    else:  # 完成点击操作，等待页面加载失败
                        error_info = "[ERROR]Failed to wait element.UiSelector[RESOURCE_ID=%s]" % [wait_page[0]]
                        logger_info = '[APP_CLICK] wait_page ["%s"] error' % wait_page[2]

                    if log_record != 0:
                        print(logger_info)

                    raise TimeoutException(error_info)
                else:  # 第一次元素操作未完成
                    try:  # 若页面仍停留在待点击元素页面
                        self.wait_widget(operate_widget, wait_time1, interval, 0)
                        click_flag = True
                    except TimeoutException:
                        try:  # 页面已跳转
                            self.wait_widget(wait_page, wait_time2, interval, 0)
                            click_flag = False  # 若页面已跳转，则下次操作不会再点击元素
                        except TimeoutException:
                            raise TimeoutException(self.driver.page_source)


class ac(object):
    def send_keys(self, element, keys, driver):
        time.sleep(0.1)
        element.send_keys(keys)
        time.sleep(0.1)
        self.hide_keyboard(element, driver)

    def get_attribute(self, element, name, driver=None):
        import re
        if name == "enabled":
            attribute_value = str(element.is_enabled()).lower()
        elif name == "is_displayed":
            windows_size = driver.get_window_size()
            lc = element.location
            if 0 <= lc["x"] <= windows_size["width"] and 0 <= lc["y"] <= windows_size["height"]:
                attribute_value = "true"
            else:
                attribute_value = "false"
                # attribute_value = str(element.is_displayed()).lower()
        elif name in ["password", "index", "focusable", "focused", "scrollable", "long-clickable", "selected"]:
            if not isinstance(element, list):
                raise KeyError("If attribute is password. The 'element' must be id of elements,is list,not WebElement")
            page_src = driver.page_source
            attribute_value = re.findall(r'.+%s="(.+?)".+?"%s"' % (name, element[0]), page_src)[0]
        else:
            attribute_value = element.get_attribute(name)
        return attribute_value

    def hide_keyboard(self, element, driver):
        driver.hide_keyboard()

    def get_location(self, element):
        """
        Get the centre location of element.
        """
        location = element.location
        size = element.size
        location = dict(location, **size)
        x = int(location["x"])
        y = int(location["y"])
        height = int(location["height"])
        width = int(location["width"])
        centre = (x + width / 2, y + height / 2)
        location["centre"] = centre
        return location

    def swipe(self, x1, y1, x2, y2, driver, step=100):
        window_size = driver.get_window_size()
        height = window_size["height"]
        width = window_size["width"]
        driver.swipe(int(width * x1), int(height * y1), int(width * x2), int(height * y2), step)


class a(object):
    def __init__(self):
        self.driver = driver
        self.ac = ac()
        self.page = page
        widget_check_unit = WidgetCheckUnit(self.driver, self.page)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget

    def choose_home_device(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        # 使用copy函数将列表的值赋予给另一变量，不然修改变量的值会影响到原列表的值造成问题
        new_value = copy.copy(self.page["app_home_page"]["device"])
        # 将元素定位名称字典换乘字符串，{0:"//...",1:"//..."} →对应"//..."
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        # 通过索引控制元素
        while True:
            try:
                self.widget_click(new_value, self.page["control_device_page"]["title"], 3, 10)
                break
            except TimeoutException:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)  # 当元素在屏幕下方未展示时滑动屏幕
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_device timeout!")

    # 获取元素索引
    def get_index(self, device, element1):
        while True:
            elements = self.wait_widget(element1)  # 返回元素字典
            for index, element in elements.items():
                if element is not None and self.ac.get_attribute(element, "name") == device:
                    return index

    # 选择元素
    def get_home_power_element(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        new_value = copy.copy(self.page["app_home_page"]["device_button"])
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        while True:
            # 通过元素坐标判断元素是否显示，未展示时滑动屏幕
            if self.wait_widget(new_value).location["y"] < self.driver.get_window_size()["height"]:
                return new_value
            else:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_power timeout!")

    # 获取电源状态
    def get_power_state(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        new_value = copy.copy(self.page["app_home_page"]["device_state"])
        new_value[0] = new_value[0][index]
        attribute = self.ac.get_attribute(self.wait_widget(new_value), "name")
        return attribute

    # 设置电源状态
    def set_power(self, device, state):
        # 由于阿里智能开关按钮状态不稳定，连续控制多次来判断按钮状态
        index = self.get_index(device, self.page["app_home_page"]["device"])
        device_button = self.get_home_power_element(device, index)
        power_state_start = self.get_power_state(device, index)
        if state == "power_on":
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state == u"开":
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power on timeout!")
        elif state == "power_off":
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state != power_state_start:
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power off 1 timeout!")
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state == u"关":
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power off 2 timeout!")

    # 设置滚轮
    def set_roll(self, elem):
        element = self.wait_widget(elem)
        lc, sz = element.location, element.size
        lcx, lcy, szw, szh = float(lc["x"]), float(lc["y"]), float(sz["width"]), float(sz["height"])
        return lcx, lcy, szw, szh

    # 设置定时滚轮
    def set_timer_roll(self, elem_e, elem_h, elem_m, elem_t, now_time, set_timer, cycle=False, delay_s=120):
        """
        int
        -int
        ["point", "09:00"]
        ["delay", "00:30"]
        :param elem_e: 滚轮控件框架，用来获取y坐标
        :param elem_h: 滚轮控件“时”框架，用来获取“时”x坐标
        :param elem_m: 滚轮控件“分”框架，用来获取“分”x坐标
        :param elem_t: 滚轮当前的时间值，“HH:MM”格式
        :param now_timer: 设置定时的当前时间
        :param set_timer: 设置定时的目标时间
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param delay_s: 定时的设置时间和启动时间延迟
        :return: 定时启动时间，格式为时间戳float型；定时执行时间，格式为时间戳float型
        """
        # 定时的设置时间包含延迟定时和准点定时：
        # 准点定时为设置定时当前时间前/后***分钟执行，数据格式为int型及以时间格式展现的str字符串型；
        # int型包含int型正数/负数（int型/负int型），用于设置当前时间***分钟前/后执行的定时，关键字为“int”，“minus”；
        # 时间格式str字符串型（"09:00"），用于设置固定时间点执行的定时，关键字为“point”
        # 延迟定时为设置时间段区间执行的定时，多用于鱼缸模式或延迟定时模式，数据格式为以时间格式展现的str字符串型；
        # 时间格式str字符串型（"30:00"），用于设置时间段定时，关键字为“delay”
        # ps：delay_s函数关键词用于给设置定时预留时间，设置定时也需要时间，默认延迟2分钟，当前时间8:00，定时开始执行时间为8:02；
        if isinstance(set_timer, int):
            if set_timer >= 0:
                time_seg = "int"
            else:
                time_seg = "minus"
        else:
            if set_timer[0] == "point":
                time_seg = "point"
            elif set_timer[0] == "delay":
                time_seg = "delay"
            else:
                time_seg = None
        if not isinstance(now_time, str):
            raise KeyError("now time must be time.strftime, current: %s" % str(now_time))
        # 滚轮
        lcx_e, lcy_e, szw_e, szh_e = self.set_roll(elem_e)
        # 时滚轮
        lcx_h, lcy_h, szw_h, szh_h = self.set_roll(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        aszh_h = int(szh_e / 5) + 10  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度，个数默认为5
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_e + szh_e / 2)  # “时”滚轮的操作起始点
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        aszh_m = int(szh_e / 5) + 10
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_e + szh_e / 2)  # “分”滚轮的操作起始点

        time_roll = time.strftime("%Y-%m-%d r:00").replace("r", elem_t)  # 滚轮的当前时间
        time_roll = time.mktime(time.strptime(time_roll, "%Y-%m-%d %X"))  # 转换为时间戳

        # 将now_time添加秒数。
        # 若同时设置普通定时和延迟定时，若两定时执行时间点相同，则难以判断定时执行情况
        # 将延迟模式的启动时间从准点往后推30s则可以和普通定时错开，相应的delay_s也要再加上对应的30s，默认120s→150s
        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = int(time.mktime(time_now))
        if cycle is True:  # 若定时为鱼缸模式，第二个定时的开始时间为第一个定时的结束时间，应将定时设置延迟去除
            time_now = time_now - delay_s

        # 获取定时的执行时间点
        if time_seg == "int" or time_seg == "minus":
            time_set = time_now + set_timer * 60 + delay_s
        elif time_seg == "point" or time_seg == "delay":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %X"))
        else:
            time_set = "error"

        # 定时开始执行和设定的时间点
        time_start = time_now + delay_s
        time_set = time_set

        # 滚轮相关操作
        roll_h, roll_m = time.strftime("%H:%M", time.localtime(time_roll)).split(":")
        set_h, set_m = time.strftime("%H:%M", time.localtime(time_set)).split(":")

        time_et_h = int(set_h) - int(roll_h)  # 时间滚轮的“时”时间和待设置时间差值
        time_et_h_a = abs(time_et_h) % 24  # “时”时间滚轮滑动次数
        time_et_m = int(set_m) - int(roll_m)  # 时间滚轮的“分”时间和待设置时间差值
        time_et_m_a = abs(time_et_m) % 60  # “分”时间滚轮滑动次数

        try:  # 若time_et不相等
            # time_et / time_et_a计算结果为1/-1，获取“时”滚轮滑动目的坐标值，用于计算时间滚轮是往上滑还是往下滑
            end_y_h = start_y_h - time_et_h / time_et_h_a * aszh_h
        except ZeroDivisionError:  # 若time_et相等
            end_y_h = start_y_h
        try:
            # 获取“分”滚轮滑动目的坐标值
            end_y_m = start_y_m - time_et_m / time_et_m_a * aszh_m
        except ZeroDivisionError:
            end_y_m = start_y_m

        # 分钟在前，时钟在后，若为00:00，滚轮会自动加一
        while time_et_m_a > 0:
            self.driver.swipe(start_x_m, start_y_m, start_x_m, end_y_m, 0)
            time_et_m_a -= 1
            time.sleep(0.5)
        while time_et_h_a > 0:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, end_y_h, 0)
            time_et_h_a -= 1
            time.sleep(0.5)

        # 将定时时间（时间戳，float型）格式化为时间（字符串型），仅做日志输出
        start_time = time.strftime("%Y-%m-%d %X", time.localtime(time_start))

        # 延时定时的滚轮时间和实际执行时间不一致，需转换一下
        if time_seg == "delay":
            delay_time = set_timer[1]
            add_h, add_m = delay_time.split(":")
            time_delay = int(add_h) * 3600 + int(add_m) * 60
            time_set = time_now + time_delay + delay_s
            set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
            print("[APP_TIMER]Delay: start_time: %s, set_time: %s, delay_time: %s" % (start_time, set_time, delay_time))
            print("[APP_TIMER]Delay: time_start: %s, time_set: %s, time_delay: %s" % (time_start, time_set, time_delay))
        else:
            set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
            print("[APP_TIMER]start_time: %s, set_time: %s" % (start_time, set_time))
            print("[APP_TIMER]time_start: %s, time_set: %s" % (time_start, time_set))

        time.sleep(2)

        return time_start, time_set

    # 设置次数滚轮
    def set_count_roll(self, elem, roll_value, set_value):
        # 滚轮
        lcx, lcy, szw, szh = self.set_roll(elem)
        pxx, pxy = elem[3]["px"]
        aszh = int(szh / 5)
        start_x, start_y = int(lcx + pxx * szw), int(lcy + pxy * szh)  # 获取滚轮滑动开始坐标值

        diff = set_value - roll_value
        diff_a = abs(diff)
        try:
            # 计算滚轮滑动目标坐标值
            end_y = start_y - diff / diff_a * aszh
        except ZeroDivisionError:
            end_y = start_y
        while diff_a > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 0)
            diff_a -= 1

        print("roll_value: %s, set_value: %s" % (roll_value, set_value))

        time.sleep(2)

    # 创建普通定时
    def create_normal_timer(self, now_time, set_timer, power, loop, delay_s=120):
        """
        :param now_time: 当前时间
        :param set_timer: 设定时间
        :param power: 设定定时开/关
        :param loop: 定时循环模式
        :param delay_s: 定时设定与执行时间差
        :return: 定时启动时间，定时执行时间
        """
        # 根据如下操作能创建一条普通定时并返回定时列表页面
        self.widget_click(self.page["normal_timer_page"]["add_normal_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll"],
                                                   self.page["add_normal_timer_page"]["roll_h"],
                                                   self.page["add_normal_timer_page"]["roll_m"],
                                                   "14:30", now_time, set_timer, delay_s=delay_s)

        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])

        self.set_timer_loop("add_normal_timer_page", loop)

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        print(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))

        return start_time, set_time

    # 创建延时定时
    def create_delay_timer(self, now_time, set_timer, power, delay_s=120, cycle=False):
        """
        :param now_time: 当前时间
        :param set_timer: 设定时间
        :param power: 设定定时开/关
        :param delay_s: 定时设定与执行时间差
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :return: 定时启动时间，定时执行时间
        """
        # 根据如下操作能创建一条延迟定时，且定时已启动
        # 用于获取时间滚轮的时间
        self.widget_click(self.page["delay_timer_page"]["launch"],
                          self.page["delay_timer_page"]["cancel"])
        time_roll = self.ac.get_attribute(self.wait_widget(self.page["delay_timer_page"]["delay_time"]), "name")
        print("[APP_INFO]Time roll value: %s" % time_roll)
        self.widget_click(self.page["delay_timer_page"]["cancel"],
                          self.page["delay_timer_page"]["launch"])

        try:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))
        except ValueError:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X"))
        time_now = time.strftime("%X", time.localtime(time_now))

        self.widget_click(self.page["delay_timer_page"][power],
                          self.page["delay_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll"],
                                                   self.page["delay_timer_page"]["roll_h"],
                                                   self.page["delay_timer_page"]["roll_m"],
                                                   time_roll, time_now, set_timer, cycle, delay_s)

        # 等待启动时间点，并启动定时
        end_time = time.time() + 1 * 60 + 30
        while True:
            if int(time.time()) == start_time:
                self.widget_click(self.page["delay_timer_page"]["launch"])
                print(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                self.wait_widget(self.page["delay_timer_page"]["cancel"], log_record=0)
                break
            else:
                if time.time() > end_time:
                    tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                    raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                time.sleep(1)

        return start_time, set_time

    # 创建循环定时
    def create_cycle_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, cycle=False, loops=0):
        """
        :param page: 定时模式，鱼缸模式/循环模式...etc
        :param now_time: 当前时间
        :param set_start_time: 启动时间时长
        :param set_end_time: 关闭时间时长
        :param loop: 循环模式
        :param delay_s: 定时设定与执行时间差
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param loops: 循环为永久循环时需要产出的时间对个数
        :return:
        """
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")

        # 获取启动时间的时间滚轮值
        tmp = re.findall(u"(\d+)小时", start_roll)
        if tmp == []:
            start_roll_h = 0
        else:
            start_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", start_roll)
        if tmp == []:
            start_roll_m = 0
        else:
            start_roll_m = int(tmp[0])
        start_roll = "%02d:%02d" % (start_roll_h, start_roll_m)
        print("[APP_TIMER]Start roll: %s" % start_roll)

        # 获取关闭时间的时间滚轮值
        tmp = re.findall(u"(\d+)小时", end_roll)
        if tmp == []:
            end_roll_h = 0
        else:
            end_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", end_roll)
        if tmp == []:
            end_roll_m = 0
        else:
            end_roll_m = int(tmp[0])
        end_roll = "%02d:%02d" % (end_roll_h, end_roll_m)
        print("[APP_TIMER]End roll: %s" % end_roll)

        try:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))
        except ValueError:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X"))
        time_now = time.strftime("%X", time.localtime(time_now))

        # 设定滚轮时间
        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, cycle, delay_s)
        print("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (start_time, start_set_time))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        time_now_end = time.strftime("%X", time.localtime(start_set_time))
        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, time_now_end, set_end_time, True)
        print("[APP_TIMER]End_time: %s, End_set_time: %s" % (end_time, end_set_time))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        # 设定循环次数
        set_loop = self.set_timer_loop(page, loop)
        print("[APP_TIMER]Set loop: %s" % set_loop)
        if loop == u"永久循环":
            loop_count = loops  # 生成指定数量的时间对个数
        else:
            loop_count = int(re.findall(u"(\d+)次", set_loop)[0])  # 同时设置循环模式
        # 延迟时间段长度，30分钟为1800s，在上一段定时结束后加上1800s就是下一段定时执行时间点
        start_period = start_set_time - start_time
        end_period = end_set_time - end_time

        # [[power_on开启时间，power_on关闭时间，power_off开启时间，power_off关闭时间]...]
        # power_on关闭时间 = power_off开启时间
        loop_list = [[start_time, start_set_time, end_time, end_set_time]]
        # 第一组定时执行完毕时间
        on_start = end_set_time  # 下一组定时的power_on开启时间，等于上一组定时power_off关闭的时间
        for i in xrange(loop_count):
            on_end = on_start + start_period  # power_on关闭时间
            off_start = on_end  # power_off开启时间
            off_end = off_start + end_period  # power_off关闭时间
            loop_list.append([on_start, on_end, off_start, off_end])  # 写入列表
            on_start = off_end  # 下一组power_on开启时间

        # 定时启动时间
        end_time = time.time() + 1 * 60 + 30
        while True:
            if int(time.time()) == start_time:
                self.widget_click(self.page[page]["launch"],
                                  self.page[page]["close"])
                print(u"[APP_TIMER]Start Time: %s; Now Time: %s[%s]" % (start_time, time.strftime("%X"), time.time()))
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Timer Saved Error, time: %s" % start_time)
                time.sleep(1)

        return loop_list

    # 创建热水器类型模式
    def create_point_mode_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, exchange=False):
        """与创建普通定时相同
        return: ([start_time, start_set_time], [end_time, end_set_time])
        """
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")
        print("[APP_TIMER]Start roll: %s" % start_roll)
        print("[APP_TIMER]End roll: %s" % end_roll)

        try:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))
        except ValueError:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X"))
        time_now = time.strftime("%X", time.localtime(time_now))

        if exchange is True:
            self.widget_click(self.page[page]["time_exchange"],
                              self.page[page]["title"])

        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, delay_s=delay_s)
        print("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (start_time, start_set_time))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, time_now, set_end_time, delay_s=delay_s)
        print("[APP_TIMER]End_time: %s, End_set_time: %s" % (end_time, end_set_time))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.set_timer_loop(page, loop)

        self.widget_click(self.page[page]["launch"],
                          self.page[page]["close"])

        return [start_time, start_set_time], [end_time, end_set_time]

    # 创建充电保护类型模式
    def create_delay_mode_timer(self, page, now_time, set_timer, delay_s=120, cycle=False):
        """与创建延迟定时相同
       return: None
       """
        time_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")
        tmp = re.findall(u"(\d+)小时", time_roll)
        if tmp == []:
            time_roll_h = 0
        else:
            time_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", time_roll)
        if tmp == []:
            time_roll_m = 0
        else:
            time_roll_m = int(tmp[0])
        time_roll = "%02d:%02d" % (time_roll_h, time_roll_m)
        print("[APP_TIMER]Start roll: %s" % time_roll)

        try:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))
        except ValueError:
            time_now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X"))
        time_now = time.strftime("%X", time.localtime(time_now))

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         time_roll, time_now, set_timer, cycle, delay_s)
        print("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (start_time, start_set_time))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        # 等待启动时间点，并启动定时
        end_time = time.time() + 1 * 60 + 30
        while True:
            now = int(time.time())
            print("now time: %s" % now)
            if now == start_time:
                self.widget_click(self.page[page]["launch"])
                print(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                self.wait_widget(self.page[page]["close"], log_record=0)
                break
            else:
                if time.time() > end_time:
                    tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                    raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                time.sleep(1)

        return start_time, start_set_time

    # 设置普通/模式定时循环模式
    def set_timer_loop(self, page, loop):
        loop_mode = {u"周一": "monday",
                     u"周二": "tuesday",
                     u"周三": "wednesday",
                     u"周四": "thursday",
                     u"周五": "friday",
                     u"周六": "saturday",
                     u"周日": "weekday"}
        end_time = time.time() + 60
        while True:
            print("""*******""")
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["repeat"], )

            attr = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if u"重复" in attr:  # 去除多余属性
                attribute = attr.replace(u"重复", "").split()[0]
            else:
                attribute = attr.replace(u"永久循环", "tmp").replace(u"循环", "").replace("tmp", u"永久循环").split()[0]
            print("[APP_INFO]Repeat attr: %s" % attribute)
            # 自定义模式显示为：周一、周三、周五...etc
            # loop传参为[u"周一", u"周三", u"周五"]
            if isinstance(loop, list):
                tmp = u"、".join(loop)  # list → str
            else:
                tmp = loop

            print("[APP_INFO]Repeat set attr: %s" % tmp)
            # 若定时已存在循环模式与设定不同则需要重新设置，若相同则不会设置
            if tmp != attribute:
                if u"每天" in attribute:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                elif u"工作日" in attribute:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                elif u"永不" in attribute:
                    attribute = []
                elif u"周" in attribute:
                    attribute = attribute.split(u"、")
                else:
                    pass

                self.widget_click(self.page[page]["repeat"],
                                  self.page["timer_repeat_page"]["title"])

                if loop == u"永不":
                    self.widget_click(self.page["timer_repeat_page"]["once"],
                                      self.page["timer_repeat_page"]["title"])

                    cycle = loop
                elif u"周" in loop or u"每天" in loop or u"工作日" in loop or isinstance(loop, list):
                    if u"每天" in loop:
                        tmp = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                    elif u"工作日" in loop:
                        tmp = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                    elif u"周" in loop:
                        tmp = [loop]
                    else:
                        tmp = loop
                    # 选择星期时，已存在的星期数是已经被勾选的，要取消需要再次点击；
                    # 例：已有周期为周一，周五，需要设置的周期为周三，周五
                    # 则实际操作为点击周一和周三，而周五不需要点击，因为周五已被选中，再点击周五则周五就会被取消选中
                    # 代码通过下述公式计算，输入当前循环周期和需要设定的周期，输出为需要待操作的周期
                    # 输入：当前[u"周一", u"周五"]，设定[u"周三", u"周五"]；
                    # 输出：[u"周一", u"周三"]；
                    cycle = list((set(attribute) | set(tmp)) - (set(attribute) & set(tmp)))
                    for i in cycle:  # 根据计算元素点击
                        self.widget_click(self.page["timer_repeat_page"][loop_mode[i]],
                                          self.page["timer_repeat_page"]["title"])
                else:
                    if u"永久循环" in attribute:  # 已存在模式为u"永久循环"
                        roll = 0
                    else:  # 已存在模式为u"**次"
                        roll = int(re.findall(u"(\d+)次", attribute)[0])

                    if loop == u"永久循环":
                        cycle = u"0次"
                    else:
                        cycle = loop
                    loop_tmp = int(re.findall(u"(\d+)次", cycle)[0])
                    self.set_count_roll(self.page["timer_repeat_page"]["cycle_count"], roll, loop_tmp)  # 从“**次”到“永久循环”

                # 保存
                self.widget_click(self.page["timer_repeat_page"]["saved"],
                                  self.page[page]["title"])
            else:
                cycle = attribute

            # 再次校验
            # 页面设置完成后，元素属性可能未改变，刷新页面更新元素
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["repeat"], )

            attr = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if u"重复" in attr:
                attribute = attr.replace(u"重复", "").split()[0]
            else:
                attribute = attr.replace(u"永久循环", "tmp").replace(u"循环", "").replace("tmp", u"永久循环").split()[0]
            print("[APP_INFO]Repeat now attr: %s" % attribute)
            if tmp == attribute:
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Cycle set error")

        return cycle

    # 设置峰谷电时间
    def set_peak_valley_time(self, elem, now_time, set_timer, peak):
        attribute = self.ac.get_attribute(elem, "name")
        if u"未设置" in attribute:
            if peak is True:  # 峰电/谷电
                time_roll = "08:00"
            else:
                time_roll = "22:00"
        else:
            time_roll = re.findall("(\d+:\d+)", attribute)[0]

        start_time, set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll"],
                                                   self.page["delay_timer_page"]["roll_h"],
                                                   self.page["delay_timer_page"]["roll_m"],
                                                   time_roll, now_time, set_timer, False, 120)

        return start_time, set_time

    # 定时检查模板
    def check_timer(self, device, start_time, set_time, power_state, power_same_prev=False, sec=True):
        # FIXME：定时的日期检测不完善，跨多天执行会有问题
        # 开始时间
        start_h, start_m, start_s = start_time.split(":")
        start_times = int(start_h) * 60 + int(start_m)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", start_time), "%Y-%m-%d %X"))
        print("[APP_TIMER]Now Time: %s. Start Time: %s" % (time.strftime("%X"), now))

        # 设置时间
        set_h, set_m, set_s = set_time.split(":")
        set_times = int(set_h) * 60 + int(set_m)

        if start_times < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        print("[APP_TIMER]Delay Time: %s" % (delay_times + 30))

        index = self.get_index(device, self.page["app_home_page"]["device"])
        element = copy.copy(self.page["app_home_page"]["power_state"])
        element[0] = element[0][index]
        element = self.wait_widget(element)
        end_time = now + delay_times + 30
        flag = False
        while True:
            if sec is True:
                if time.strftime("%X") == set_time:
                    flag = True
            else:
                if time.strftime("%H:%M") == set_time[:5]:
                    flag = True
            if flag is True:
                now = time.time()
                if power_same_prev is True:
                    time.sleep(10)
                while True:
                    if self.ac.get_attribute(element, "name") == power_state:
                        print("[APP_TIMER]End Time: %s[%s]" % (time.strftime("%X"), now))
                        print(u"[APP_INFO]Device Info: %s" % power_state)
                        break
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Device state Error")
                time.sleep(1)

    # 删除普通定时
    def delete_normal_timer(self):
        # 按照手动操作顺序删除定时
        end_time = time.time() + 120
        flag = False  # 定时点击删掉后，定时消失有延迟，同时排除第一次进入页面加载失败造成的误判
        while True:
            try:
                self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                print("It has normal timer.")
                self.widget_click(self.page["normal_timer_page"]["timer_edit"],
                                  self.page["normal_timer_page"]["delete_timer"])

                self.widget_click(self.page["normal_timer_page"]["delete_timer"],
                                  self.page["normal_timer_page"]["delete"])

                self.widget_click(self.page["normal_timer_page"]["delete"],
                                  self.page["normal_timer_page"]["saved"])

                self.widget_click(self.page["normal_timer_page"]["saved"],
                                  self.page["normal_timer_page"]["timer_edit"])
                flag = True
                try:
                    self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                except TimeoutException:
                    print("It has no timer~")
                    break
            except TimeoutException:
                time.sleep(1)
                if time.time() > end_time:
                    raise TimeoutException("delete_normal_timer timeout, time limit: %sS" % end_time)
                elif flag is True:
                    try:
                        self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                    except TimeoutException:
                        print("It has no timer~")
                        break

    # 关闭模式定时
    def close_mode_timer(self):
        timer_loop = {u"热水器模式": ["water_mode_timer", "water_mode_timer_page"],
                      u"小夜灯模式": ["night_mode_timer", "night_mode_timer_page"],
                      u"鱼缸模式": ["fish_mode_timer", "fish_mode_timer_page"],
                      u"电蚊香模式": ["mosquito_mode_timer", "mosquito_mode_timer_page"],
                      u"充电保护模式": ["piocc_mode_timer", "piocc_mode_timer_page"],
                      u"取暖器模式": ["warmer_mode_timer", "warmer_mode_timer_page"]}
        element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"模式" in attribute:
                print("[APP_INFO]Mode timer is run")
                for timer_mode, value in timer_loop.items():
                    if timer_mode in attribute:
                        self.widget_click(self.page["control_device_page"][value[0]],
                                          self.page[value[1]]["title"])

                        self.widget_click(self.page[value[1]]["close"],
                                          self.page[value[1]]["launch"], times=2)

                        self.widget_click(self.page[value[1]]["to_return"],
                                          self.page["control_device_page"]["title"])
            else:
                print("[APP_INFO]Mode timer don't run")
                break

    # 关闭定时任务
    def close_general_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"任务开" in attribute:
                print("[APP_INFO]Normal timer is run")
                if u"定时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["normal_timer"],
                                      self.page["normal_timer_page"]["title"])

                    self.delete_normal_timer()

                    self.widget_click(self.page["normal_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"延时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["delay_timer"],
                                      self.page["delay_timer_page"]["title"])

                    self.widget_click(self.page["delay_timer_page"]["cancel"],
                                      self.page["delay_timer_page"]["launch"])

                    self.widget_click(self.page["delay_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                else:
                    self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                    self.widget_click(self.page["control_device_page"]["cycle_timer"],
                                      self.page["cycle_timer_page"]["title"])

                    self.widget_click(self.page["cycle_timer_page"]["close"],
                                      self.page["cycle_timer_page"]["launch"])

                    self.widget_click(self.page["cycle_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
            else:
                print("[APP_INFO]Normal timer don't run")
                self.ac.swipe(0.6, 0.6, 0.6, 0.9, self.driver)
                break

    # 启动模式定时
    def launch_mode_timer(self, page, start_time=None, start_now=False):
        if not isinstance(start_now, bool):
            raise KeyError("start_now must be bool type")
        if start_now is True:  # 立即启动，例如普通定时等
            self.widget_click(self.page[page]["launch"])
            print(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
            self.wait_widget(self.page[page]["close"], log_record=0)
        else:  # 需要特定时间点启动，例如延时模式等
            if start_time is None:  # 若选择延迟启动，则启动时间点start_time不能为None
                raise KeyError("if start_now is False, start_time can`t be None type")

            end_time = time.time() + 1 * 60 + 30
            while True:
                now = int(time.time())
                print("now time: %s" % now)
                if now == start_time:
                    self.widget_click(self.page[page]["launch"])
                    print(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                    self.wait_widget(self.page[page]["close"], log_record=0)
                    break
                else:
                    if time.time() > end_time:
                        tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                        raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                    time.sleep(1)

    # 统计电量操作缩减
    def get_device_elect_unit(self, check_time):
        while True:
            if int(time.strftime("%H")) == check_time:
                time.sleep(60)
                break
            else:
                try:
                    self.driver.tap([(10, 10)])
                except BaseException:
                    print("tap 10, 10 error")
                time.sleep(60)

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        self.ac.swipe(0.5, 0.7, 0.5, 0.4, self.driver)

        self.widget_click(self.page["elec_page"]["more_elec_history"],
                          self.page["more_elec_history_page"]["title"])

        # 选择当前日期
        today = time.strftime("%m月%d日").decode("utf")  # 格式化日期
        day_list = self.wait_widget(self.page["more_elec_history_page"]["day_elec"])
        new_value = copy.copy(self.page["more_elec_history_page"]["day_elec"])
        for index, element in day_list.items():
            if element is not None and str(self.ac.get_attribute(element, "name")) == today:
                new_value[0] = new_value[0][index]
                while True:
                    try:
                        self.widget_click(new_value, self.page["day_elec_page"]["title"])
                        break
                    except TimeoutException:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                        time.sleep(1)
            break

        # 读取指定时间点前电费数据
        elec_and_bill_e = self.wait_widget(self.page["day_elec_page"]["elec_time"])
        elec_and_bill_v = copy.copy(self.page["day_elec_page"]["elec_value"])
        for index, element in elec_and_bill_e.items():
            if element is not None:
                elec_and_bill_v[0] = self.page["day_elec_page"]["elec_value"][0][index]
                tmp = re.findall(u"(\d+.\d+|\d+)元.+?(\d+.\d+|\d+)W", self.ac.get_attribute(elec_and_bill_v, "name"))
                self.elec[index] = float(tmp[1])
                self.elec_bill[index] = float(tmp[0])
        print("[APP_INFO]%02d:01_elec: %s" % (check_time, str(self.elec)))
        print("[APP_INFO]%02d:01_elec_bill: %s" % (check_time, str(self.elec_bill)))

        self.widget_click(self.page["day_elec_page"]["to_return"],
                          self.page["more_elec_history_page"]["title"])

        self.widget_click(self.page["more_elec_history_page"]["to_return"],
                          self.page["elec_page"]["title"])

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

    # 统计电量
    def get_device_elect(self, check_time, across=False):
        now_h = int(time.strftime("%H"))
        if across is False:
            if now_h + 2 <= 23:  # 电量为下一整点上传，故从当前时间2个小时后才开始统计电量。判断2个小时后是否跨天
                across_day = False
            else:
                across_day = True
        else:
            across_day = True
        self.elec = {}
        self.elec_bill = {}

        if across_day is True:
            # 晚上23点开始读取当前一天的所有电量数据
            self.get_device_elect_unit(23)

        # 到另一天指定时间点结束统计
        self.get_device_elect_unit(check_time)

        return self.elec, self.elec_bill

    # 密码框显示密码
    def show_pwd(self, element, element1=None, param="name", state="false"):
        while True:
            try:
                if self.ac.get_attribute(element, param) == state:
                    break
                else:
                    if element1 is None:
                        element.click()
                    else:
                        element1.click()
            except BaseException:
                print(traceback.format_exc())
