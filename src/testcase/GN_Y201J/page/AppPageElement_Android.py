# coding=utf-8
class MainPageWidgetAndroid(object):
    # 账户设置页
    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/iv_avatar", "id", u"账户设置页"]
        # 帮助与设置
        d["help_setting"] = ["com.jd.smart:id/iv_setting", "id", u"帮助与设置"]
        # 用户名
        d["username"] = ["com.jd.smart:id/tv_username", "id", u"用户名"]
        return d

    # 帮助与设置
    def help_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='帮助与设置']", "xpath", u"帮助与设置"]
        # 帮助与设置
        d["return"] = ["com.jd.smart:id/iv_left", "id", u"返回"]
        # 登出
        d["logout"] = ["com.jd.smart:id/button_exit", "id", u"退出登录"]
        return d

    # 登录页面
    def login_page(self):
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/login_title_icon", "id", u"登录页面"]
        # 用户名
        d["username"] = ["com.jd.smart:id/username", "id", u"用户名输入框"]
        # 密码
        d["password"] = ["com.jd.smart:id/password", "id", u"密码输入框"]
        # 显示/关闭密码
        d["check_box"] = ["com.jd.smart:id/eye", "id", u"显示/关闭密码"]
        # 登录
        d["login_button"] = ["com.jd.smart:id/button_login", "id", u"登录按钮"]
        return d

    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='微联']", "xpath", u"App主页面"]
        # +号
        d["add_device"] = ["com.jd.smart:id/iv_right", "id", u"+号"]
        # 账户管理
        d["account_setting"] = ["com.jd.smart:id/iv_left", "id", u"账户管理"]
        # 没有设备/未登录
        d["no_device"] = ["com.jd.smart:id/layout_no_device", "id", u"没有设备/未登录"]
        # 设备
        device = {}
        for i in xrange(5):
            device[i] = ("//android.widget.ListView/android.view.View[%s]//android.widget.LinearLayout/"
                         "android.widget.TextView" % (i + 1))
        d["device"] = [device, "xpath", u"待控设备"]
        # 有设备
        d["has_device"] = ["com.jd.smart:id/tv_name", "id", u"没有设备/未登录"]
        return d

    # 添加设备页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='添加设备']", "xpath", u"添加设备页面"]
        # 通过设备品类添加
        d["variety"] = [u"//android.widget.TextView[@text='通过设备品类添加']", "xpath", u"通过设备品类添加"]
        # 添加历史
        d["history"] = ["com.jd.smart:id/iv_history", "id", u"添加历史"]
        return d

    # 添加设备品类页面
    def add_device_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设备品类']", "xpath", u"添加设备品类页面"]
        # 插座列表选项
        d["option"] = [u"//android.widget.TextView[@text='插座']", "xpath", u"插座列表选项"]
        return d

    # 进入设备添加历史页面
    # driver.find_elements_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='2']")
    def add_history_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='已添加设备']", "xpath", u"进入设备添加历史页面"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"//android.widget.TextView[@text='公牛WiFi智能电量统计版转换器2代']", "xpath", u"公牛Wi-Fi智能转换器2代电量计量版"]
        # 公牛Wi-Fi智能转换器2代
        d["y2011"] = [u"//android.widget.TextView[@text='公牛Wi-Fi智能转换器2代']", "xpath", u"公牛Wi-Fi智能转换器2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"//android.widget.TextView[@text='公牛Wi-Fi智能插座2代加强版']", "xpath", u"公牛Wi-Fi智能插座2代加强版"]
        return d

    # 进入插座列表页面
    def add_outlet_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='插座']", "xpath", u"插座列表页面"]
        # 公牛Wi-Fi智能插座2代
        d["y2011"] = [u"//android.widget.TextView[@text='公牛Wi-Fi智能插座2代']", "xpath", u"公牛Wi-Fi智能插座2代"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"//android.widget.TextView[@text='公牛WiFi智能电量统计版转换器2代']", "xpath",
                      u"公牛WiFi智能电量统计版转换器2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"//android.widget.TextView[@text='公牛Wi-Fi智能插座2代加强版']", "xpath",
                        u"公牛Wi-Fi智能插座2代加强版"]
        return d

    # 搜索设备页
    def add_specification_page(self):
        FrameLayout = "/android.widget.FrameLayout"
        LinearLayout = "/android.widget.LinearLayout"
        TextView = "/android.widget.TextView"
        self.xpath = "".join(("/", FrameLayout, FrameLayout, LinearLayout, LinearLayout, TextView))
        TextValue = "[@text='1']"
        self.add_specification = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.add_specification, "xpath", u"搜索设备页"]
        # 下一步
        d["next"] = ["com.jd.smart:id/tv_action", "id", u"下一步"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        TextValue = "[@text='2']"
        self.input_wifi_password = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.input_wifi_password, "xpath", u"进入输入密码页面"]
        # 确认wifi密码按钮
        d["confirm"] = ["com.jd.smart:id/tv_action", "id", u"确认wifi密码按钮"]
        # wifi密码输入框
        d["password"] = ["com.jd.smart:id/tv_pwd", "id", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = ["com.jd.smart:id/cb_eye", "id", u"密码显示关闭"]
        return d

    # 搜索设备等待页面
    def search_device_loading_page(self):
        TextValue = "[@text='3']"
        self.search_device_loading = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.search_device_loading, "xpath", u"搜索设备等待页面"]
        return d

    # 搜索到设备
    def search_device_success_page(self):
        # 搜索到设备MAC
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/tv_desc", "id", u"有设备出现"]
        # 设备元素路径
        device_box = {}
        confirm_box = {}
        for i in xrange(4):
            device_box[i] = "//android.widget.ListView/android.widget.LinearLayout[%s]//android.widget.TextView[2]" % (
                i + 1)
            confirm_box[
                i] = "//android.widget.ListView/android.widget.LinearLayout[%s]/android.widget.LinearLayout/android.widget.TextView" % (
                i + 1)
        # 设备路径
        d["device_box"] = [device_box, "xpath", u"设备等待添加"]
        # 使用
        d["confirm"] = [confirm_box, "xpath", u"使用"]
        return d

    # 搜索设备超时
    def search_device_fail_page(self):
        TextValue = "[@text='4']"
        self.search_device_fail = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.search_device_fail, "xpath", u"搜索设备超时"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/i_more", "id", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_info"] = ["com.jd.smart:id/i_more", "id", u"设备信息进入按钮"]
        # 设备离线标志
        d["offline"] = [u"设备不在线", "name", u"设备离线标志"]
        # 电源开关
        d["power_button"] = ["android.widget.Button", "class", u"电源开关"]
        # 电源状态
        d["power_state"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View",
                            "xpath", u"电源状态"]
        # 功率
        d["power"] = ["//android.widget.ListView/android.view.View[2]", "xpath", u"功率"]
        # 电源开启
        d["power_on"] = [u"//android.view.View[@content-desc='设备已开启']", "xpath", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"//android.view.View[@content-desc='设备已关闭']", "xpath", u"电源关闭"]
        # 设备记忆模式
        d["memory_mode"] = [u"//android.widget.Button[@content-desc='记忆模式']", "xpath", u"设备记忆模式"]
        # 设备安全模式
        d["safe_mode"] = [u"//android.widget.Button[@content-desc='安全模式']", "xpath", u"设备安全模式"]
        # 模式定时
        d["mode_timer"] = ["//android.webkit.WebView/android.view.View/android.view.View[3]", "xpath", u"模式定时"]
        # 普通定时
        d["normal_timer"] = ["//android.webkit.WebView/android.view.View/android.view.View[5]", "xpath", u"普通定时",
                             {"px": [0.95, 0.5]}]
        # 指示灯
        d["led"] = ["//android.webkit.WebView/android.view.View/android.view.View[9]/android.widget.Button", "xpath",
                    u"指示灯"]
        # 用电量
        d["elec"] = [u"//android.view.View[@content-desc='用电量']", "xpath", u"用电量"]
        # 电价设置
        d["set_elec"] = [u"//android.view.View[@content-desc='电价设置']", "xpath", u"电价设置"]
        # 电费
        d["elec_bill"] = [u"//android.view.View[@content-desc='电费']", "xpath", u"电费"]
        # 返回
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置']", "xpath", u"设备信息页面"]
        # 删除设备按钮
        d["unbind"] = ["com.jd.smart:id/btn_unbind", "id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["com.jd.smart:id/ads_edit_name", "id", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/iv_left", "id", u"返回"]
        return d

    # 修改设备备注页面
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='修改名称']", "xpath", u"修改设备备注页面"]
        # 保存
        d["saved"] = ["com.jd.smart:id/btn_cancel", "id", u"保存"]
        # 备注输入框
        d["nickname"] = ["com.jd.smart:id/et_device_name", "id", u"备注输入框"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/iv_left", "id", u"返回"]
        return d

    # 模式定时页面
    def mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='自定义模式']", "xpath", u"模式定时页面"]
        # 热水器模式
        d["water_mode"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]", "xpath", u"热水器模式"]
        # 热水器模式开关
        d["water_button"] = [u"//android.view.View[@content-desc='热水器模式 ']", "xpath", u"热水器模式开关",
                             {"px": [0.95, 0.5]}]
        # 鱼缸模式
        d["fish_mode"] = ["//android.webkit.WebView/android.view.View/android.view.View[5]", "xpath", u"鱼缸模式"]
        # 鱼缸模式开关
        d["fish_button"] = [u"//android.view.View[@content-desc='鱼缸模式 ']", "xpath", u"鱼缸模式开关",
                            {"px": [0.95, 0.5]}]
        # 充电保护模式
        d["piocc_mode"] = ["//android.webkit.WebView/android.view.View/android.view.View[8]", "xpath", u"充电保护模式"]
        # 充电保护模式开关
        d["piocc_button"] = [u"//android.view.View[@content-desc='充电保护模式 ']", "xpath", u"充电保护模式开关",
                             {"px": [0.95, 0.5]}]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 热水器模式定时页面
    def water_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='热水器模式']", "xpath", u"热水器模式定时页面"]
        # 开启时间
        d["start_time"] = [u"//android.view.View[@content-desc='插座开启时间']", "xpath", u"插座开启时间控件"]
        # 开启时间
        d["start_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText", "xpath",
                                u"插座开启时间"]
        # 关闭时间
        d["end_time"] = [u"//android.view.View[@content-desc='插座关闭时间']", "xpath", u"插座关闭时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText[2]", "xpath",
                              u"插座关闭时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"//android.widget.ListView[@content-desc='时']", "xpath", u"时间滚轮,时",
                       {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"//android.widget.ListView[@content-desc='分']", "xpath", u"时间滚轮,分",
                       {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//android.webkit.WebView/android.view.View/android.view.View[3]", "xpath", u"重复"]
        # 模式名称
        d["mode_name"] = ["//android.webkit.WebView/android.view.View/android.view.View[4]", "xpath", u"模式名称"]
        # 执行结果
        d["result"] = ["//android.webkit.WebView/android.view.View/android.view.View[5]", "xpath", u"执行结果"]
        # 取消
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"取消"]
        # 启动
        d["launch"] = ["com.jd.smart:id/button4", "id", u"启动"]
        return d

    # 鱼缸模式定时页面
    def fish_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='鱼缸模式']", "xpath", u"鱼缸模式定时页面"]
        # 开启时间
        d["start_time"] = [u"//android.view.View[@content-desc='插座开启时长']", "xpath", u"插座开启时间控件"]
        # 开启时间
        d["start_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText", "xpath",
                                u"插座开启时间"]
        # 关闭时间
        d["end_time"] = [u"//android.view.View[@content-desc='插座关闭时长']", "xpath", u"插座关闭时间控件"]
        # 关闭时间
        d["end_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText[2]", "xpath",
                              u"插座关闭时间"]
        # 时间滚轮,小时
        d["roll_h"] = [u"//android.widget.ListView[@content-desc='小时']", "xpath", u"时间滚轮,小时",
                       {"px": [0.51, 0.5]}]
        # 时间滚轮,分钟
        d["roll_m"] = [u"//android.widget.ListView[@content-desc='分钟']", "xpath", u"时间滚轮,分钟",
                       {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//android.webkit.WebView/android.view.View/android.view.View[3]", "xpath", u"重复"]
        # 模式名称
        d["mode_name"] = ["//android.webkit.WebView/android.view.View/android.view.View[4]", "xpath", u"模式名称"]
        # 取消
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"取消"]
        # 启动
        d["launch"] = ["com.jd.smart:id/button4", "id", u"启动"]
        return d

    # 充电保护模式定时页面
    def piocc_mode_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='充电保护模式']", "xpath", u"充电保护模式定时页面"]
        # 关闭时间
        d["end_time"] = [u"//android.view.View[@content-desc='插座延时关闭时长']", "xpath", u"插座延时关闭时长控件"]
        # 关闭时间
        d["end_time_text"] = ["//android.webkit.WebView/android.view.View/android.widget.EditText", "xpath",
                              u"插座延时关闭时长"]
        # 时间滚轮,小时
        d["roll_h"] = [u"//android.widget.ListView[@content-desc='小时']", "xpath", u"时间滚轮,小时",
                       {"px": [0.51, 0.5]}]
        # 时间滚轮,分钟
        d["roll_m"] = [u"//android.widget.ListView[@content-desc='分钟']", "xpath", u"时间滚轮,分钟",
                       {"px": [0.51, 0.5]}]
        # 模式名称
        d["mode_name"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]", "xpath", u"模式名称"]
        # 执行结果
        d["result"] = ["//android.webkit.WebView/android.view.View/android.view.View[3]", "xpath", u"执行结果"]
        # 取消
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"取消"]
        # 启动
        d["launch"] = ["com.jd.smart:id/button4", "id", u"启动"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='定时设置']", "xpath", u"普通定时页面"]
        # 添加定时
        d["add_timer"] = ["com.jd.smart:id/button4", "id", u"添加定时按钮"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        # 执行记录
        d["timer_log"] = [u"//android.view.View[@content-desc='执行记录 ']", "xpath", u"执行记录"]
        # 编辑定时
        d["timer_edit"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]", "xpath",
                           u"编辑定时", {"px": [0.9975, 0.5]}]
        # 无定时
        d["no_timer"] = [u"//android.view.View[contains(@content-desc, '暂无设置定时')]", "xpath", u"无定时"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='新建定时']", "xpath", u"新建普通定时页面"]
        # 设定时间
        d["set_timer"] = ["//android.view.View/android.widget.EditText", "xpath", u"设定时间"]
        # 时间滚轮,时
        d["roll_h"] = [u"//android.widget.ListView[@content-desc='时']", "xpath", u"时间滚轮,时",
                       {"px": [0.51, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = [u"//android.widget.ListView[@content-desc='分']", "xpath", u"时间滚轮,分",
                       {"px": [0.51, 0.5]}]
        # 重复
        d["repeat"] = ["//android.webkit.WebView/android.view.View/android.view.View[2]", "xpath", u"重复"]
        # 定时开机
        d["power_on"] = [u"//android.widget.Button[@content-desc='定时开机']", "xpath", u"定时开机"]
        # 定时关机
        d["power_off"] = [u"//android.widget.Button[@content-desc='定时关机']", "xpath", u"定时关机"]
        # 定时名称
        d["timer_name"] = ["//android.webkit.WebView/android.view.View/android.view.View[4]", "xpath", u"定时名称"]
        # 执行结果通知
        d["timer_name"] = ["//android.webkit.WebView/android.view.View/android.view.View[5]", "xpath", u"执行结果通知"]
        # 取消按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"取消"]
        # 保存按钮
        d["saved"] = ["com.jd.smart:id/button4", "id", u"保存按钮"]
        return d

    # 定时重复页面
    def timer_repeat_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='重复']", "xpath", u"定时重复页面"]
        # 重复按钮
        d["repeat_button"] = [u"//android.view.View[@content-desc='重复 ']", "xpath", u"重复按钮",
                              {"px": [0.95, 0.5]}]
        # 执行一次
        d["once"] = [u"//android.view.View[@content-desc='执行一次']", "xpath", u"执行一次"]
        # 每天
        d["everyday"] = [u"//android.view.View[@content-desc='每天']", "xpath", u"每天"]
        # 工作日
        d["workday"] = [u"//android.view.View[@content-desc='工作日']", "xpath", u"工作日"]
        # 自定义
        d["define"] = [u"//android.view.View[@content-desc='自定义']", "xpath", u"自定义"]
        # 周一
        d["monday"] = [u"//android.view.View[@content-desc='周一']", "xpath", u"周一"]
        # 周二
        d["tuesday"] = [u"//android.view.View[@content-desc='周二']", "xpath", u"周二"]
        # 周三
        d["wednesday"] = [u"//android.view.View[@content-desc='周三']", "xpath", u"周三"]
        # 周四
        d["thursday"] = [u"//android.view.View[@content-desc='周四']", "xpath", u"周四"]
        # 周五
        d["friday"] = [u"//android.view.View[@content-desc='周五']", "xpath", u"周五"]
        # 周六
        d["saturday"] = [u"//android.view.View[@content-desc='周六']", "xpath", u"周六"]
        # 周日
        d["weekday"] = [u"//android.view.View[@content-desc='周日']", "xpath", u"周日"]
        # 鱼缸模式循环按钮
        d["fish_repeat_button"] = [u"//android.view.View[@content-desc='永久循环 ']", "xpath",
                                   u"鱼缸模式循环按钮", {"px": [0.95, 0.5]}]
        # 永久循环
        d["forever"] = [u"//android.view.View[@content-desc='永久循环 ']", "xpath", u"永久循环"]
        # 执行次数
        d["cycle_count"] = [u"//android.view.View[@content-desc='执行次数设置(次)']", "xpath", u"执行次数"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
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


class PopupWidgetAndroid(object):
    # app升级确认弹窗
    def update_popup(self):
        d = {}
        d["title"] = [u"//android.widget.TextView[@text='更新提示']", "xpath", u"有更新"]
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
        d["title"] = ["com.jd.smart:id/cancel", "id", u"删除设备按钮"]
        # 确认
        d["confirm"] = ["com.jd.smart:id/confirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.jd.smart:id/cancel", "id", u"取消"]
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
        d["title"] = [u"//android.widget.TextView[@text='确定要退出当前账户吗？']", "xpath", u"退出登录弹窗"]
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

    # 模式定时冲突弹窗
    def mode_timer_conflict_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[@content-desc='开启新定时，将会自动关闭其他定时，是否确认开启？']", "xpath", u"模式定时冲突弹窗"]
        # 确定
        d["confirm"] = [u"//android.widget.Button[@content-desc='是']", "xpath", u"确定"]
        # 取消
        d["cancel"] = [u"//android.widget.Button[@content-desc='否']", "xpath", u"取消"]
        return d
