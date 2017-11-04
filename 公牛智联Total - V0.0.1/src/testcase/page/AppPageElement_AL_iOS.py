# coding=utf-8
class MainPageWidgetIosAL(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["android.widget.FrameLayout", "class", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

    # “我的”页面
    def my_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='我的家']", "xpath", u"“我的”页面"]
        # 设置
        d["setting"] = ["com.aliyun.alink:id/layout_container_item_setting", "id", u"设置"]
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
        # 设备开关
        d["device_button"] = [device_button, "xpath", u"待控设备开关"]
        # 设备状态
        d["device_state"] = [device_state, "xpath", u"待控设备开关"]
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
        d["y201S"] = [u"//android.widget.TextView[@text='公牛WiFi智能插座2代（电量统计版）']", "xpath", u"公牛WiFi智能插座2代（电量统计版）"]
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
        d["check_box"] = ["com.aliyun.alink:id/button_devicewificonfig_pwd_switch", "id", u"wifi密码输入框"]
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
        d["retry"] = ["com.aliyun.alink:id/button_deviceconfigfailed_retry", "id", u"返回"]
        return d

    # 设备已被绑定
    def bind_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[text='该设备已被绑定']", "xpath", u"该设备已被绑定"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.view.View[contains(@content-desc, '实时功率')]", "xpath", u"设备控制页面"]
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
        d["water_mode_timer"] = [u"//android.view.View[@content-desc='热水器']", "xpath", u"热水器模式"]
        # 小夜灯模式
        d["night_mode_timer"] = [u"//android.view.View[@content-desc='小夜灯']", "xpath", u"小夜灯模式"]
        # 鱼缸模式
        d["fish_mode_timer"] = [u"//android.view.View[@content-desc='鱼缸模式']", "xpath", u"鱼缸模式"]
        # 蚊香模式
        d["mosquito_mode_timer"] = [u"//android.view.View[@content-desc='蚊香模式']", "xpath", u"蚊香模式"]
        # 充电保护模式
        d["piocc_mode_timer"] = [u"//android.view.View[@content-desc='充电保护']", "xpath", u"充电保护模式"]
        # 取暖器模式
        d["warmer_mode_timer"] = [u"//android.view.View[@content-desc='取暖器']", "xpath", u"取暖器模式"]
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
        d["title"] = [u"//android.view.View[@content-desc='重复']", "xpath", u"定时重复页面"]
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


class PopupWidgetIosAL(object):
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
