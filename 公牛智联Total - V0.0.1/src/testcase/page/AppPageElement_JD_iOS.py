# coding=utf-8
class MainPageWidgetIosJD(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["//XCUIElementTypeStatusBar", "xpath", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

    # 账户设置页
    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = ["//XCUIElementTypeTable/XCUIElementTypeImage", "xpath", u"账户设置页"]
        # 帮助与设置
        d["help_setting"] = [u"帮助与设置", "accessibility_id", u"帮助与设置"]
        # 用户名
        d["username"] = ["//XCUIElementTypeTable/XCUIElementTypeStaticText", "xpath", u"用户名"]
        return d

        # 帮助与设置

    def help_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"帮助与设置", "accessibility_id", u"帮助与设置"]
        # 帮助与设置
        d["return"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton", "xpath", u"返回"]
        # 登出
        d["logout"] = [u"退出登录", "accessibility_id", u"退出登录"]
        return d

    # 登录页面
    def login_page(self):
        d = {}
        # 标题
        d["title"] = ["image_login", "accessibility_id", u"登录页面"]
        # 用户名
        d["username"] = ["//XCUIElementTypeOther[3]//XCUIElementTypeTextField", "xpath", u"用户名输入框"]
        # 密码
        d["password"] = ["//XCUIElementTypeOther[3]//XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField",
                         "xpath", u"密码输入框"]
        # 显示/关闭密码
        d["check_box"] = ["//XCUIElementTypeOther[3]//XCUIElementTypeButton", "xpath", u"显示/关闭密码"]
        # 登录
        d["login_button"] = ["//XCUIElementTypeOther[3]//XCUIElementTypeScrollView/"
                             "XCUIElementTypeOther/XCUIElementTypeButton", "xpath", u"登录按钮"]
        return d

    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = [u"微联", "accessibility_id", u"App主页面"]
        # +号
        d["add_device"] = ["newAdd", "accessibility_id", u"+号"]
        # 账户管理
        d["account_setting"] = ["newMenu", "accessibility_id", u"账户管理"]
        # 没有设备/未登录
        d["no_device"] = [u"认识微联", "accessibility_id", u"没有设备/未登录"]
        # 设备
        device = {}
        for i in xrange(5):
            device[
                i] = "//XCUIElementTypeOther[2]//XCUIElementTypeCell[%s]/XCUIElementTypeStaticText" % (i + 1)
        d["device"] = [device, "xpath", u"待控设备"]
        return d

    # 添加设备页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加设备", "accessibility_id", u"添加设备页面"]
        # 通过设备品类添加
        d["variety"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton[4]", "xpath", u"通过设备品类添加"]
        # 添加历史
        d["history"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton[2]", "xpath", u"添加历史"]
        return d

    # 添加设备品类页面
    def add_device_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备品类", "accessibility_id", u"添加设备品类页面"]
        # 插座列表选项
        d["option"] = [u"插座", "accessibility_id", u"插座列表选项"]
        return d

    # 进入设备添加历史页面
    # driver.find_elements_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='2']")
    def add_history_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"已添加设备", "accessibility_id", u"进入设备添加历史页面"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"公牛WiFi智能电量统计版转换器2代", "accessibility_id", u"公牛Wi-Fi智能转换器2代电量计量版"]
        # 公牛Wi-Fi智能转换器2代
        d["y2011"] = [u"公牛Wi-Fi智能插座2代", "accessibility_id", u"公牛Wi-Fi智能插座2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"公牛Wi-Fi智能插座2代加强版", "accessibility_id", u"公牛Wi-Fi智能插座2代加强版"]
        return d

    # 进入插座列表页面
    def add_outlet_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"插座", "accessibility_id", u"插座列表页面"]
        # 公牛Wi-Fi智能插座2代
        d["y2011"] = [u"公牛Wi-Fi智能插座2代", "accessibility_id", u"公牛Wi-Fi智能插座2代"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"公牛WiFi智能电量统计版转换器2代", "accessibility_id", u"公牛WiFi智能电量统计版转换器2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"公牛Wi-Fi智能插座2代加强版", "accessibility_id", u"公牛Wi-Fi智能插座2代加强版"]
        return d

    # 搜索设备页
    def add_specification_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加公牛WiFi智能电量统计版转换器2代", "accessibility_id", u"搜索设备页"]
        # 下一步
        d["next"] = [u"下一步", "accessibility_id", u"下一步"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加公牛WiFi智能电量统计版转换器2代", "accessibility_id", u"搜索设备页"]
        # 确认wifi密码按钮
        d["confirm"] = [u"没有该元素", "accessibility_id", u"确认wifi密码按钮"]
        # wifi密码输入框
        d["password"] = [u"没有该元素", "accessibility_id", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = [u"没有该元素", "accessibility_id", u"wifi密码输入框"]
        # 下一步
        d["next"] = [u"下一步", "accessibility_id", u"下一步"]
        return d

    # 搜索设备等待页面
    def search_device_loading_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加中", "accessibility_id", u"搜索设备等待页面"]
        return d

    # 搜索到设备
    def search_device_success_page(self):
        # 搜索到设备MAC
        d = {}
        # 标题
        d["title"] = [u"添加公牛WiFi智能电量统计版转换器2代", "accessibility_id", u"有设备出现"]
        # 设备路径
        d["device_box"] = [u"没有该元素", "accessibility_id", u"设备等待添加"]
        # 使用
        d["confirm"] = [u"完成", "accessibility_id", u"使用"]
        return d

    # 搜索设备超时
    def search_device_fail_page(self):
        d = {}
        # 标题
        d["title"] = [u"重试", "accessibility_id", u"搜索设备超时"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = ["setting", "accessibility_id", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_info"] = ["setting", "accessibility_id", u"设备信息进入按钮"]
        # 设备离线标志
        d["offline"] = [u"设备不在线", "accessibility_id", u"设备离线标志"]
        # 电源开关
        d["power_button"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton", "xpath", u"电源开关"]
        # 电源状态
        d["power_state"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]"
                            "/XCUIElementTypeStaticText", "xpath", u"电源状态"]
        # 功率
        d["power"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther/XCUIElementTypeOther[2]/"
                      "XCUIElementTypeStaticText", "xpath", u"功率"]
        # 电源开启
        d["power_on"] = [u"设备已开启", "accessibility_id", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"设备已关闭", "accessibility_id", u"电源关闭"]
        # 设备记忆模式
        d["memory_mode"] = [u"记忆模式", "accessibility_id", u"设备记忆模式"]
        # 设备安全模式
        d["safe_mode"] = [u"安全模式", "accessibility_id", u"设备安全模式"]
        # 模式定时
        d["mode_timer"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]",
                           "xpath", u"模式定时"]
        # 普通定时
        d["normal_timer"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[5]//XCUIElementTypeOther[2]", "xpath",
                             u"普通定时"]
        # 指示灯
        d["led"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[10]/XCUIElementTypeButton", "xpath", u"指示灯"]
        # 用电量
        d["elec"] = [u"用电量", "accessibility_id", u"用电量"]
        # 电价设置
        d["set_elec"] = [u"电价设置", "accessibility_id", u"电价设置"]
        # 电费
        d["elec_bill"] = [u"电费", "accessibility_id", u"电费"]
        # 返回
        d["to_return"] = ["clos_bar", "accessibility_id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"设置", "accessibility_id", u"设备信息页面"]
        # 删除设备按钮
        d["unbind"] = [u"删除设备", "accessibility_id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeButton", "xpath", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = ["gray back", "accessibility_id", u"返回"]
        return d

    # 修改设备备注页面
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改名称", "accessibility_id", u"修改设备备注页面"]
        # 保存
        d["saved"] = [u"保存", "accessibility_id", u"保存"]
        # 备注输入框
        d["nickname"] = ["//XCUIElementTypeTextField", "accessibility_id", u"备注输入框"]
        # 返回按钮
        d["to_return"] = ["gray back", "accessibility_id", u"返回"]
        return d

    # 模式定时页面
    def mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"自定义模式", "accessibility_id", u"模式定时页面"]
        # 热水器模式
        d["water_mode"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[4]", "xpath", u"热水器模式"]
        # 热水器模式开关
        d["water_button"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                             "XCUIElementTypeOther", "xpath", u"热水器模式开关"]
        # 鱼缸模式
        d["fish_mode"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[8]", "xpath", u"鱼缸模式"]
        # 鱼缸模式开关
        d["fish_button"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[5]/XCUIElementTypeOther", "xpath",
                            u"鱼缸模式开关"]
        # 充电保护模式
        d["piocc_mode"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[12]", "xpath", u"充电保护模式"]
        # 充电保护模式开关
        d["piocc_button"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[9]/XCUIElementTypeOther", "xpath",
                             u"充电保护模式开关"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 热水器模式定时页面
    def water_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"热水器模式", "accessibility_id", u"热水器模式定时页面"]
        # 开启时间
        d["start_time"] = [u"插座开启时间", "accessibility_id", u"插座开启时间控件"]
        # 开启时间
        d["start_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField", "xpath", u"插座开启时间"]
        # 关闭时间
        d["end_time"] = [u"插座关闭时间", "accessibility_id", u"插座关闭时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField[2]", "xpath", u"插座关闭时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"//XCUIElementTypeOther[@name='时']", "xpath", u"时间滚轮,时", {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"//XCUIElementTypeOther[@name='分']", "xpath", u"时间滚轮,分", {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[3]", "xpath", u"重复"]
        # 模式名称
        d["mode_name"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[4]", "xpath", u"模式名称"]
        # 执行结果
        d["result"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[5]", "xpath", u"执行结果"]
        # 取消
        d["to_return"] = [u"取消", "accessibility_id", u"取消"]
        # 启动
        d["launch"] = [u"启动", "accessibility_id", u"启动"]
        return d

    # 鱼缸模式定时页面
    def fish_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"鱼缸模式", "accessibility_id", u"鱼缸模式定时页面"]
        # 开启时间
        d["start_time"] = [u"插座开启时长", "accessibility_id", u"插座开启时间控件"]
        # 开启时间
        d["start_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField", "xpath", u"插座开启时间"]
        # 关闭时间
        d["end_time"] = [u"插座关闭时长", "accessibility_id", u"插座关闭时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField[2]", "xpath", u"插座关闭时间"]
        # 时间滚轮,小时
        d["roll_h"] = [u"//XCUIElementTypeOther[@name='小时']", "xpath", u"时间滚轮,小时", {"px": [0.51, 0.5]}]
        # 时间滚轮,分钟
        d["roll_m"] = [u"//XCUIElementTypeOther[@name='分钟']", "xpath", u"时间滚轮,分钟", {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[3]", "xpath", u"重复"]
        # 模式名称
        d["mode_name"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[4]", "xpath", u"模式名称"]
        # 取消
        d["to_return"] = [u"取消", "accessibility_id", u"取消"]
        # 启动
        d["launch"] = [u"启动", "accessibility_id", u"启动"]
        return d

    # 充电保护模式定时页面
    def piocc_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"充电保护模式", "accessibility_id", u"充电保护模式定时页面"]
        # 关闭时间
        d["end_time"] = [u"插座延时关闭时长", "accessibility_id", u"插座延时关闭时长控件"]
        # 关闭时间
        d["end_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField", "xpath", u"插座延时关闭时长"]
        # 时间滚轮,小时
        d["roll_h"] = [u"//XCUIElementTypeOther[@name='小时']", "xpath", u"时间滚轮,小时", {"px": [0.51, 0.5]}]
        # 时间滚轮,分钟
        d["roll_m"] = [u"//XCUIElementTypeOther[@name='分钟']", "xpath", u"时间滚轮,分钟", {"px": [0.51, 0.5]}]
        # 模式名称
        d["mode_name"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[2]", "xpath", u"模式名称"]
        # 执行结果
        d["result"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[3]", "xpath", u"执行结果"]
        # 取消
        d["to_return"] = [u"取消", "accessibility_id", u"取消"]
        # 启动
        d["launch"] = [u"启动", "accessibility_id", u"启动"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"定时设置", "accessibility_id", u"普通定时页面"]
        # 添加定时
        d["add_timer"] = ["newAdd", "accessibility_id", u"添加定时按钮"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        # 执行记录
        d["timer_log"] = [u"执行记录", "accessibility_id", u"执行记录"]
        # 编辑定时
        d["timer_edit"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[2]", "xpath", u"编辑定时", {"px": [0.95, 0.5]}]
        # 无定时
        d["no_timer"] = [u"暂无设置定时", "accessibility_id", u"无定时"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"新建定时", "accessibility_id", u"新建普通定时页面"]
        # 设定时间
        d["set_timer"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField", "xpath", u"设定时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"XCUIElementTypeOther[@name='时']", "xpath", u"时间滚轮,时", {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"XCUIElementTypeOther[@name='分']", "xpath", u"时间滚轮,分", {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[2]", "xpath", u"重复"]
        # 定时开机
        d["power_on"] = [u"定时开机", "accessibility_id", u"定时开机"]
        # 定时关机
        d["power_off"] = [u"定时关机", "accessibility_id", u"定时关机"]
        # 定时名称
        d["timer_name"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]",
                           "xpath", u"定时名称"]
        # 执行结果通知
        d["timer_name"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]",
                           "xpath", u"执行结果通知"]
        # 取消按钮
        d["to_return"] = [u"取消", "accessibility_id", u"取消"]
        # 保存按钮
        d["saved"] = [u"保存", "accessibility_id", u"保存"]
        return d

    # 定时重复页面
    def timer_repeat_page(self):
        d = {}
        # 标题
        d["title"] = [u"重复", "accessibility_id", u"定时重复页面"]
        # 重复按钮
        d["repeat_button"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                              "XCUIElementTypeOther", "xpath", u"重复按钮"]
        # 执行一次
        d["once"] = [u"执行一次", "accessibility_id", u"执行一次"]
        # 每天
        d["everyday"] = [u"每天", "accessibility_id", u"每天"]
        # 工作日
        d["workday"] = [u"工作日", "accessibility_id", u"工作日"]
        # 自定义
        d["define"] = [u"自定义", "accessibility_id", u"自定义"]
        # 周一
        d["monday"] = [u"周一", "accessibility_id", u"周一"]
        # 周二
        d["tuesday"] = [u"周二", "accessibility_id", u"周二"]
        # 周三
        d["wednesday"] = [u"周三", "accessibility_id", u"周三"]
        # 周四
        d["thursday"] = [u"周四", "accessibility_id", u"周四"]
        # 周五
        d["friday"] = [u"周五", "accessibility_id", u"周五"]
        # 周六
        d["saturday"] = [u"周六", "accessibility_id", u"周六"]
        # 周日
        d["weekday"] = [u"周日", "accessibility_id", u"周日"]
        # 鱼缸模式循环按钮
        d["fish_repeat_button"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/"
                                   "XCUIElementTypeOther/XCUIElementTypeOther", "xpath", u"鱼缸模式循环按钮"]
        # 永久循环
        d["forever"] = [u"永久循环", "accessibility_id", u"永久循环"]
        # 执行次数
        d["cycle_index"] = [u"执行次数设置(次)", "accessibility_id", u"执行次数"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 定时执行记录页面
    def timer_log_page(self):
        d = {}
        # 标题
        d["title"] = [u"执行记录", "accessibility_id", u"定时执行记录页面"]
        # 清空定时记录
        d["clear"] = [u"清空", "accessibility_id", u"清空定时记录"]
        # 有执行记录
        d["has_log"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther",
                        "xpath", u"有执行记录"]
        # 无执行记录
        d["no_log"] = [u"暂无执行纪录！", "accessibility_id", u"无执行记录"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 设置电价页面
    def set_elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"电价设置", "accessibility_id", u"电价设置页面"]
        # 单一电价设置
        d["single_price"] = [u"单一电价 ", "accessibility_id", u"单一电价设置"]
        # 峰谷电价设置
        d["peak_valley_price"] = [u"峰谷时间段电价", "accessibility_id", u"峰谷电价设置"]
        # 单一电价设置按钮
        d["single_button"] = ["//XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                              "XCUIElementTypeOther/XCUIElementTypeOther", "xpath", u"单一电价设置按钮"]
        # 峰谷电价设置按钮
        d["peak_valley_button"] = ["XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOth"
                                   "er/XCUIElementTypeOther[2]/XCUIElementTypeOther", "xpath", u"峰谷电价设置按钮"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 单一电价设置页面
    def single_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"单一电价设置", "accessibility_id", u"单一电价设置页面"]
        # 设置电价
        d["set_price"] = [u"//XCUIElementTypeTextField", "xpath", u"设置电价"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 峰谷电价设置页面
    def peak_valley_price_page(self):
        d = {}
        # 标题
        d["title"] = [u"峰谷电设置", "accessibility_id", u"峰谷电价设置页面"]
        # 开启时间
        d["start_time"] = [u"峰电开始时间", "accessibility_id", u"峰电开始时间控件"]
        # 开启时间
        d["start_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField", "xpath", u"峰电开始时间"]
        # 关闭时间
        d["end_time"] = [u"峰电结束时间", "accessibility_id", u"峰电结束时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//XCUIElementTypeWebView//XCUIElementTypeTextField[2]", "xpath", u"峰电结束时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"//XCUIElementTypeOther[@name='时']", "xpath", u" 时间滚轮,时", {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"//XCUIElementTypeOther[@name='分']", "xpath", u"时间滚轮,分", {"px": [0.51, 0.5]}]
        # 设置峰电电价
        d["set_peak_price"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[4]//XCUIElementTypeTextField",
                               "xpath", u"设置电价"]
        # 设置谷电电价
        d["set_valley_price"] = ["//XCUIElementTypeWebView//XCUIElementTypeOther[8]//XCUIElementTypeTextField",
                                 "xpath", u"设置电价"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 用电量页面
    def elec_page(self):
        d = {}
        # 标题
        d["title"] = [u"用电量", "accessibility_id", u"电价设置页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//XCUIElementTypeWebView//XCUIElementTypeOther[%s]/XCUIElementTypeOther/" \
                            "XCUIElementTypeStaticText" % (i + 4)
            price_value[i] = "//XCUIElementTypeWebView//XCUIElementTypeOther[%s]/XCUIElementTypeOther[2]/" \
                             "XCUIElementTypeStaticText" % (i + 4)
        # 电量时间
        d["elec_time"] = [price_time, "xpath", u"电量时间"]
        # 电量值
        d["elec_value"] = [price_value, "xpath", u"电量值"]
        # 日
        d["day"] = [u"日", "accessibility_id", u"日"]
        # 周
        d["week"] = [u"周", "accessibility_id", u"周"]
        # 月
        d["month"] = [u"月", "accessibility_id", u"月"]
        # 年
        d["year"] = [u"年", "accessibility_id", u"年"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d

    # 电费页面
    def elec_bill_page(self):
        d = {}
        # 标题
        d["title"] = [u"电费", "accessibility_id", u"电费页面"]
        price_time = {}
        price_value = {}
        for i in xrange(24):
            price_time[i] = "//XCUIElementTypeWebView//XCUIElementTypeOther[%s]/XCUIElementTypeOther/" \
                            "XCUIElementTypeStaticText" % (i + 4)
            price_value[i] = "//XCUIElementTypeWebView//XCUIElementTypeOther[%s]/XCUIElementTypeOther[2]/" \
                             "XCUIElementTypeStaticText" % (i + 4)
        # 电费时间
        d["price_time"] = [price_time, "xpath", u"电费时间"]
        # 电费值
        d["price_value"] = [price_value, "xpath", u"电费值"]
        # 返回按钮
        d["to_return"] = ["gray_back", "accessibility_id", u"返回"]
        return d


class PopupWidgetIosJD(object):
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
        d["title"] = [u"您的设备尚有定时任务，建议清除定时任务后再删除设备", "accessibility_id", u"删除设备按钮"]
        # 确认
        d["confirm"] = [u"取消", "accessibility_id", u"确认"]
        # 取消
        d["cancel"] = [u"仍然删除", "u", u"取消"]
        return d

    def bind_device_fail_popup(self):
        d = {}
        # 绑定失败
        d["title"] = ["com.jd.smart:id/confirm", "id", u"绑定失败"]
        # 确认
        d["confirm"] = ["com.jd.smart:id/confirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.jd.smart:id/cancel", "id", u"取消"]
        return d

    def loading_popup(self):
        d = {}
        # 标题
        # d["title"] = ["loading...", "name", u"正在加载中loading..."]
        d["title"] = ["android:id/message", "id", u"正在加载中loading..."]
        return d

    def logout_popup(self):
        d = {}
        # 退出登录弹窗
        d["title"] = [u"确定要退出当前账户？", "accessibility_id", u"退出登录弹窗"]
        # 确定
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 定时执行记录清除弹窗
    def timer_log_clear_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否清空记录", "accessibility_id", u"是否清空记录"]
        # 确认
        d["confirm"] = [u"是", "accessibility_id", u"确认"]
        # 取消
        d["cancel"] = [u"否", "accessibility_id", u"取消"]
        return d

    # 过期定时删除弹窗
    def timer_edit_popup(self):
        d = {}
        # 标题
        d["title"] = [u"编辑", "accessibility_id", u"编辑"]
        # 编辑
        d["edit"] = [u"编辑", "accessibility_id", u"编辑"]
        # 删除
        d["delete"] = [u"删除", "accessibility_id", u"删除"]
        # 取消
        d["cancel"] = [u"取消']", "accessibility_id", u"取消"]
        return d

    # 模式定时冲突弹窗
    def mode_timer_conflict_popup(self):
        d = {}
        # 标题
        d["title"] = [u"开启新定时，将会自动关闭其他定时，是否确认开启？", "accessibility_id", u"模式定时冲突弹窗"]
        # 确定
        d["confirm"] = [u"是", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"否", "accessibility_id", u"取消"]
        return d
