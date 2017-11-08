# coding=utf-8
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
