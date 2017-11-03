# coding=utf-8
class MainPageWidgetAndroidHW(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["android.widget.FrameLayout", "class", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

    # 账户设置页
    # def account_setting_page(self):
    #     d = {}
    #     # 标题
    #     d["title"] = ["com.jd.smart:id/iv_avatar", "id", u"账户设置页"]
    #     # 帮助与设置
    #     d["help_setting"] = ["com.jd.smart:id/iv_setting", "id", u"帮助与设置"]
    #     # 用户名
    #     d["username"] = ["com.jd.smart:id/tv_username", "id", u"用户名"]
    #     return d
    #
    # # 帮助与设置
    # def help_setting_page(self):
    #     d = {}
    #     # 标题
    #     d["title"] = [u"//android.widget.TextView[@text='帮助与设置']", "xpath", u"帮助与设置"]
    #     # 帮助与设置
    #     d["return"] = ["com.jd.smart:id/iv_left", "id", u"返回"]
    #     # 登出
    #     d["logout"] = ["com.jd.smart:id/button_exit", "id", u"退出登录"]
    #     return d
    #
    # # 登录页面
    # def login_page(self):
    #     d = {}
    #     # 标题
    #     d["title"] = ["com.jd.smart:id/login_title_icon", "id", u"登录页面"]
    #     # 用户名
    #     d["username"] = ["com.jd.smart:id/username", "id", u"用户名输入框"]
    #     # 密码
    #     d["password"] = ["com.jd.smart:id/password", "id", u"密码输入框"]
    #     # 显示/关闭密码
    #     d["check_box"] = ["com.jd.smart:id/eye", "id", u"显示/关闭密码"]
    #     # 登录
    #     d["login_button"] = ["com.jd.smart:id/button_login", "id", u"登录按钮"]
    #     return d

    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='智家']", "xpath", u"App主页面"]
        # +号
        d["add_device"] = ["com.huawei.smarthome:id/myhome__tool_bar", "id", u"+号"]
        # 账户管理
        d["account_setting"] = [u"//android.widget.TextView[@text='我的']", "xpath", u"账户管理"]
        # 设备
        device = {}
        for i in xrange(5):
            device[i] = ("//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]//"
                         "android.widget.TextView" % (i + 1))
        d["device"] = [device, "xpath", u"待控设备"]
        return d

    # 添加设备页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/hand_device_btn_come", "id", u"添加设备页面"]
        # 手动添加
        d["add_hand"] = ["com.huawei.smarthome:id/hand_device_btn_come", "id", u"手动添加"]
        # 正在添加
        d["loading"] = [u"//android.widget.TextView[@text='正在扫描…']", "xpath", u"正在添加"]
        # 重新扫描
        d["retry"] = ["com.huawei.smarthome:id/add_device_scan_btn", "id", u"重新扫描"]
        # 未发现设备
        d["no_device"] = [u"//android.widget.TextView[@text='未发现设备']", "xpath", u"未发现设备"]
        # 设备
        d["device"] = ["//android.widget.ListView//android.widget.TextView", "xpath", u"设备"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/common_title_back", "id", u"返回"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='认证']", "xpath", u"进入输入密码页面"]
        # WiFi名称
        d["wifi_name"] = ["com.huawei.smarthome:id/add_device_outh_wifi_name", "id", u"WiFi名称"]
        # 下一步
        d["next"] = ["com.jd.smart:id/tv_action", "id", u"确认wifi密码按钮"]
        # 记住密码
        d["remind_pwd"] = ["com.huawei.smarthome:id/remind_cb", "id", u"记住密码"]
        # wifi密码输入框
        d["password"] = ["com.huawei.smarthome:id/add_device_outh_password", "id", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = ["com.huawei.smarthome:id/add_device_outh_password_switch_img", "id", u"密码显示关闭"]
        return d

    # 设备名称及位置
    def set_name_addr_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置设备名称及位置']", "xpath", u"设备名称及位置"]
        # 备注
        d["nickname"] = ["//android.widget.EditText", "xpath", u"备注"]
        # 摆放位置
        d["addr"] = ["//android.widget.ListView//android.widget.ImageView", "xpath", u"摆放位置客厅"]
        # 下一步
        d["next"] = ["com.huawei.smarthome:id/device_loc_next", "id", u"设备"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/common_ui_new_title_back", "id", u"返回"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/base_device_layout_title_setting", "id", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_info"] = ["com.huawei.smarthome:id/base_device_layout_title_setting", "id", u"设备信息进入按钮"]
        # 设备离线标志
        d["offline"] = [u"设备不在线", "name", u"设备离线标志"]
        # 电源开关
        d["power_button"] = ["com.huawei.smarthome:id/device_control_btn_title", "id", u"电源开关"]
        # 电源状态
        d["power_state"] = ["com.huawei.smarthome:id/device_control_socket_new_state", "id", u"电源状态"]
        # 电源开启
        d["power_on"] = [u"//android.widget.TextView[@text='电源已开启']", "xpath", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"//android.widget.TextView[@text='电源已关闭']", "xpath", u"电源关闭"]
        # 普通定时
        d["normal_timer"] = [u"//android.widget.TextView[@text='定时']", "xpath", u"普通定时"]
        # 延迟定时
        d["delay_timer"] = [u"//android.widget.TextView[@text='倒计时']", "xpath", u"延迟定时"]
        # 指示灯
        d["led"] = [u"//android.widget.TextView[@text='指示灯']", "xpath", u"指示灯"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/hw_otherdevice_title_back", "id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置']", "xpath", u"设备信息页面"]
        # 删除设备按钮
        d["unbind"] = ["com.huawei.smarthome:id/hw_otherdevice_setting_delete_device", "id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["com.huawei.smarthome:id/setting_item_name", "id", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = ["com.huawei.smarthome:id/common_ui_new_title_back", "id", u"返回"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='定时']", "xpath", u"普通定时页面"]
        # 添加定时
        d["add_timer"] = ["com.huawei.smarthome:id/device_time_add", "id", u"添加定时按钮"]
        # 编辑定时
        d["timer_edit"] = ["com.huawei.smarthome:id/time_normal_item_time", "id", u"编辑定时"]
        # 无定时
        d["no_timer"] = [u"//android.widget.TextView[@text='没有定时任务']", "xpath", u"无定时"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/device_time_back", "id", u"返回"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='新增定时']", "xpath", u"新建普通定时页面"]
        # 重复
        d["repeat"] = ["com.huawei.smarthome:id/setting_item_value", "id", u"重复"]
        # 定时开机
        d["timer_on"] = ["com.huawei.smarthome:id/device_control_time_config_open_switch", "id", u"定时开机"]
        # 定时关机
        d["timer_off"] = ["com.huawei.smarthome:id/device_control_time_config_close_switch", "id", u"定时关机"]
        # 开启时间
        d["time_on"] = ["//android.widget.RelativeLayout[3]//android.widget.TextView[2]", "xpath", u"开启时间"]
        # 关闭时间
        d["time_off"] = ["//android.widget.RelativeLayout[5]//android.widget.TextView[2]", "xpath", u"关闭时间"]
        # 取消按钮
        d["cancel"] = ["com.huawei.smarthome:id/device_time_config_cancle", "id", u"取消"]
        # 保存按钮
        d["confirm"] = ["com.huawei.smarthome:id/device_time_config_ok", "id", u"保存按钮"]
        # 删除
        d["delete"] = [u"//android.widget.Button[@text='删除']", "xpath", u"删除"]
        return d

    # 定时执行记录页面
    def timer_log_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='执行记录']", "xpath", u"定时执行记录页面"]
        # 清空定时记录
        d["clear"] = [u"//android.widget.TextView[@text='清空']", "xpath", u"清空定时记录"]
        # 有执行记录
        d["has_log"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]", "xpath", u"有执行记录"]
        # 无执行记录
        d["no_log"] = [u"//android.view.View[@content-desc='暂无执行纪录！']", "xpath", u"无执行记录"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 设置电价页面
    def set_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='电价设置']", "xpath", u"电价设置页面"]
        # 单一电价设置
        d["single_price"] = [u"//android.view.View[@content-desc='单一电价 ']", "xpath", u"单一电价设置"]
        # 峰谷电价设置
        d["peak_valley_price"] = [u"//android.view.View[@content-desc='峰谷时间段电价 ']",
                                  "xpath", u"峰谷电价设置"]
        # 单一电价设置按钮
        d["single_button"] = [u"//android.view.View[@content-desc='单一电价 ']", "xpath",
                              u"单一电价设置按钮", {"px": [0.07, 0.5]}]
        # 峰谷电价设置按钮
        d["peak_valley_button"] = [u"//android.view.View[@content-desc='峰谷时间段电价 ']", "xpath",
                                   u"峰谷电价设置按钮", {"px": [0.07, 0.5]}]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 单一电价设置页面
    def single_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='单一电价设置']", "xpath", u"单一电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//android.widget.EditText", "xpath", u"设置电价"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 峰谷电价设置页面
    def peak_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='峰谷电设置']", "xpath", u"峰谷电价设置页面"]
        # 开启时间
        d["start_time"] = [u"//android.view.View[@content-desc='峰电开始时间']", "xpath", u"峰电开始时间控件"]
        # 开启时间
        d["start_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText", "xpath",
                                u"峰电开始时间"]
        # 关闭时间
        d["end_time"] = [u"//android.view.View[@content-desc='峰电结束时间']", "xpath", u"峰电结束时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText[2]", "xpath",
                              u"峰电结束时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"//android.widget.ListView[@content-desc='时']", "xpath", u" 时间滚轮,时",
                       {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"//android.widget.ListView[@content-desc='分']", "xpath", u"时间滚轮,分",
                       {"px": [0.51, 0.5]}]
        # 设置峰电电价
        d["set_peak_price"] = ["//android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[2]/"
                               "android.widget.EditText", "xpath", u"设置电价"]
        # 设置谷电电价
        d["set_valley_price"] = ["//android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View[2]/"
                                 "android.widget.EditText", "xpath", u"设置电价"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 用电量页面
    def elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='用电量']", "xpath", u"电价设置页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//android.webkit.WebView/android.widget.ListView[%s]/android.view.View" % (i + 2)
            price_value[i] = "//android.webkit.WebView/android.widget.ListView[%s]/android.view.View[2]" % (i + 2)
        # 电量时间
        d["elec_time"] = [price_time, "xpath", u"电量时间"]
        # 电量值
        d["elec_value"] = [price_value, "xpath", u"电量值"]
        # 日
        d["day"] = [u"//android.view.View[@content-desc='日']", "xpath", u"日"]
        # 周
        d["week"] = [u"//android.view.View[@content-desc='周']", "xpath", u"周"]
        # 月
        d["month"] = [u"//android.view.View[@content-desc='月']", "xpath", u"月"]
        # 年
        d["year"] = [u"//android.view.View[@content-desc='年']", "xpath", u"年"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 电费页面
    def elec_bill_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='电费']", "xpath", u"电费页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//android.webkit.WebView/android.widget.ListView[%s]/android.view.View" % (i + 2)
            price_value[i] = "//android.webkit.WebView/android.widget.ListView[%s]/android.view.View[2]" % (i + 2)
        # 电费时间
        d["price_time"] = [price_time, "xpath", u"电费时间"]
        # 电费值
        d["price_value"] = [price_value, "xpath", u"电费值"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d


class PopupWidgetAndroidHW(object):
    # app升级确认弹窗
    def update_popup(self):
        d = {}
        d["title"] = ["com.jd.smart:id/title", "id", u"有更新", {"text": u"更新提示"}]
        # 更新
        d["confirm"] = ["com.jd.smart:id/confirm", "id", u"更新"]
        # 检查更新
        d["cancel"] = ["com.jd.smart:id/cancel", "id", u"稍后提醒"]
        return d

    def close_ad_popup(self):
        d = {}
        # 广告关闭键
        # d["title"] = [u"操作失败，账号在其他手机登录，请确认是否本人使用。", "name", u"提示 - 重新登录"]
        d["title"] = ["com.jd.smart:id/close_pop_for_top_news", "id", u"发现广告"]
        # 确认
        d["confirm"] = ["com.jd.smart:id/close_pop_for_top_news", "id", u"确认"]
        return d

    def unbind_device_popup(self):
        d = {}
        # 删除设备弹窗
        d["title"] = [u"//android.widget.TextView[contains(@text, '此操作会清除手机')]", "xpath", u"删除设备弹窗"]
        # 确认
        d["confirm"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_comfirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_cancle", "id", u"取消"]
        return d

    def loading_popup(self):
        d = {}
        # com.huawei.smarthome:id/load_dialog_msg 正在删除…
        # com.huawei.smarthome:id/load_dialog_msg 正在创建…
        # com.huawei.smarthome:id/title_loading
        # 正在配网
        d["title"] = [u"//android.widget.TextView[@text='正在发送网络配置信息']", "xpath", u"正在配网"]
        # 设备注册中
        d["register"] = [u"//android.widget.TextView[@text='设备注册中']", "xpath", u"设备注册中"]
        # 设备正在控制中
        d["control"] = [u"//android.widget.TextView[@text='设备正在控制中...']", "xpath", u"设备正在控制中"]
        # 正在加载
        d["loading"] = [u"//android.widget.TextView[@text='正在加载…']", "xpath", u"正在加载"]
        # 删除定时
        d["delete_timer"] = [u"//android.widget.TextView[@text='正在删除…']", "xpath", u"正在删除"]
        return d

    def logout_popup(self):
        d = {}
        # 退出登录弹窗
        d["title"] = ["com.jd.smart:id/title", "id", u"退出登录弹窗", {"text": u"确定要退出当前账户吗？"}]
        # 确认
        d["confirm"] = ["com.jd.smart:id/confirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.jd.smart:id/cancel", "id", u"取消"]
        return d

    # 定时执行记录清除弹窗
    def timer_log_clear_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='是否清空记录']", "xpath", u"是否清空记录"]
        # 确认
        d["confirm"] = [u"//android.widget.Button[@content-desc='是']", "xpath", u"确认"]
        # 取消
        d["cancel"] = [u"//android.widget.Button[@content-desc='否']", "xpath", u"取消"]
        return d

    # 过期定时删除弹窗
    def timer_edit_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.Button[@content-desc='编辑']", "xpath", u"编辑"]
        # 编辑
        d["edit"] = [u"//android.widget.Button[@content-desc='编辑']", "xpath", u"编辑", {"pxw": [0.5, 0.79]}]
        # 删除
        d["delete"] = [u"//android.widget.Button[@content-desc='删除']", "xpath", u"删除", {"pxw": [0.5, 0.87]}]
        # 取消
        d["cancel"] = [u"//android.widget.Button[@content-desc='取消']", "xpath", u"取消", {"pxw": [0.5, 0.95]}]
        return d

    # 修改设备备注弹窗
    def change_nickname_popup(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/common_ui_name_edittext", "id", u"修改设备备注弹窗"]
        # 备注输入框
        d["nickname"] = ["com.huawei.smarthome:id/common_ui_name_edittext", "id", u"备注输入框"]
        # 确认
        d["confirm"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_comfirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_cancle", "id", u"取消"]
        return d

    # 定时重复页面
    def timer_repeat_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='重复']", "xpath", u"定时重复页面"]
        # 执行一次
        d["once"] = [u"//android.widget.TextView[@text='执行一次']", "xpath", u"执行一次"]
        # 每天
        d["everyday"] = [u"//android.widget.TextView[@text='每天']", "xpath", u"每天"]
        # 工作日
        d["workday"] = [u"//android.widget.TextView[contains(@text, '工作日'])", "xpath", u"工作日"]
        # 周末
        d["weekend"] = [u"//android.widget.TextView[@text='周末']", "xpath", u"周末"]
        # 自定义
        d["define"] = [u"//android.widget.TextView[@text='自定义']", "xpath", u"自定义"]
        # 周一
        d["monday"] = [u"//android.widget.TextView[@text='周一']", "xpath", u"周一"]
        # 周二
        d["tuesday"] = [u"//android.widget.TextView[@text='周二']", "xpath", u"周二"]
        # 周三
        d["wednesday"] = [u"//android.widget.TextView[@text='周三']", "xpath", u"周三"]
        # 周四
        d["thursday"] = [u"//android.widget.TextView[@text='周四']", "xpath", u"周四"]
        # 周五
        d["friday"] = [u"//android.widget.TextView[@text='周五']", "xpath", u"周五"]
        # 周六
        d["saturday"] = [u"//android.widget.TextView[@text='周六']", "xpath", u"周六"]
        # 周日
        d["weekday"] = [u"//android.widget.TextView[@text='周日']", "xpath", u"周日"]
        # 完成
        d["confirm"] = [u"//android.widget.Button[@content-desc='完成']", "xpath", u"完成"]
        # 取消
        d["cancel"] = [u"//android.widget.Button[@content-desc='取消']", "xpath", u"取消"]
        return d
