# coding=utf-8
class MainPageWidgetAndroidAL(object):
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
        for i in xrange(7):
            device[
                i] = "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]//android.widget.TextView" % (
            i + 1)
        d["device"] = [device, "xpath", u"待控设备"]
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
    def add_history_list_page(self):
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
        '''
        webview！！！！！！！！！！！
        :return:
        '''
        d = {}
        # 标题
        d["title"] = ["//android.webkit.WebView[@content-desc='设备控制面板']", "xpath", u"设备控制页面", ]
        # 设备信息进入按钮
        d["device_info"] = ["com.aliyun.alink:id/textview_atopbar_right_1", "id", u"设备信息进入按钮"]
        # 设备离线标志
        d["offline"] = [u"//android.view.View[@text='content-desc='该设备已断开连接！']", "xpath", u"设备离线标志"]
        # 电源开关
        d["power_button"] = [u"//android.view.View[@content-desc='开关按钮']", "xpath", u"电源开关"]
        # 电源开启
        d["power_on"] = [u"//android.widget.TextView[@text='设备已开启']", "xpath", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"//android.widget.TextView[@text='设备已关闭']", "xpath", u"电源关闭"]
        # 设备记忆模式
        d["memory_mode"] = [u"记忆模式", "name", u"设备记忆模式"]
        # 设备安全模式
        d["safe_mode"] = [u"安全模式", "name", u"设备安全模式"]
        # 模式定时
        d["mode_timer"] = [u"自定义模式", "name", u"模式定时"]
        # 模式定时
        d["normal_timer"] = [u"定时设置", "name", u"普通定时"]
        # 返回
        d["to_return"] = ["com.aliyun.alink:id/textview_atopbar_left_1", "id", u"返回"]
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
        d["title"] = [u"自定义模式", "name", u"模式定时页面"]
        # 热水器模式开关
        d["water_button"] = ["com.jd.smart:id/btn_unbind", "id", u"热水器模式开关"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"定时设置", "name", u"普通定时页面"]
        # 添加定时
        d["add_timer"] = ["com.jd.smart:id/button4", "id", u"添加定时按钮"]
        # 返回按钮
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        # 执行记录
        d["timer_log"] = [u"执行记录", "name", u"执行记录"]
        return d

    # 定时执行记录页面
    def timer_log_page(self):
        d = {}
        # 标题
        d["title"] = [u"执行记录", "name", u"定时执行记录页面"]
        # 清空定时记录
        d["clear"] = [u"清空", "name", u"清空定时记录"]
        # 返回
        d["to_return"] = ["com.jd.smart:id/button1", "id", u"返回"]
        # 有执行记录
        d["has_log"] = [u"定时开机删除", "name", u"返回"]
        # 无执行记录
        d["no_log"] = [u"暂无执行纪录！", "name", u"返回"]
        return d


class PopupWidgetAndroidAL(object):
    # 设备升级确认弹窗
    # def update_popup(self):
    #     d = {}
    #     d["title"] = ["com.jd.smart:id/title", "id", u"有更新", {"text": u"更新提示"}]
    #     # 更新
    #     d["confirm"] = ["com.jd.smart:id/confirm", "id", u"更新"]
    #     # 检查更新
    #     d["cancel"] = ["com.jd.smart:id/cancel", "id", u"稍后提醒"]
    #     return d
    #
    # def close_ad_popup(self):
    #     d = {}
    #     # 广告关闭键
    #     # d["title"] = [u"操作失败，账号在其他手机登录，请确认是否本人使用。", "name", u"提示 - 重新登录"]
    #     d["title"] = ["com.jd.smart:id/close_pop_for_top_news", "id", u"发现广告"]
    #     # 确认
    #     d["confirm"] = ["com.jd.smart:id/close_pop_for_top_news", "id", u"确认"]
    #     return d
    #
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

    #
    # def unbind_device_popup(self):
    #     d = {}
    #     # 删除设备弹窗
    #     d["title"] = ["com.jd.smart:id/cancel", "id", u"删除设备按钮"]
    #     # 确认
    #     d["confirm"] = ["com.jd.smart:id/confirm", "id", u"确认"]
    #     # 取消
    #     d["cancel"] = ["com.jd.smart:id/cancel", "id", u"取消"]
    #     return d
    #
    # def bind_device_fail_popup(self):
    #     d = {}
    #     # 绑定失败
    #     d["title"] = ["com.jd.smart:id/confirm", "id", u"绑定失败"]
    #     # 确认
    #     d["confirm"] = ["com.jd.smart:id/confirm", "id", u"确认"]
    #     # 取消
    #     d["cancel"] = ["com.jd.smart:id/cancel", "id", u"取消"]
    #     return d
    #
    # def loading_popup(self):
    #     d = {}
    #     # 标题
    #     # d["title"] = ["loading...", "name", u"正在加载中loading..."]
    #     d["title"] = ["android:id/message", "id", u"正在加载中loading..."]
    #     return d
    #
    def logout_popup(self):
        d = {}
        # 退出登录弹窗
        d["title"] = [u"//android.widget.TextView[@text='退出后不会删除历史纪录，下次登录仍可以使用本账号']", "xpath",
                      u"退出登录弹窗"]
        # 确认
        d["confirm"] = [u"//android.widget.TextView[@text='退出登录']", "xpath", u"退出登录"]
        # 取消
        d["cancel"] = [u"//android.widget.TextView[@text='取消']", "xpath", u"取消"]
        return d
        #
        # # 定时执行记录清除弹窗
        # def timer_log_clear_popup(self):
        #     d = {}
        #     # 标题
        #     d["title"] = [u"是否清空记录", "name", u"是否清空记录"]
        #     # 确认
        #     d["confirm"] = [u"是", "name", u"确认"]
        #     # 取消
        #     d["cancel"] = [u"否", "name", u"取消"]
        #     return d
