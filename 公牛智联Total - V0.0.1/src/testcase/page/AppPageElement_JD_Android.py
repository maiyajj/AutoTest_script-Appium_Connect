# coding=utf-8
class MainPageWidgetAndroidJD(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["android.widget.FrameLayout", "class", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

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
        d["title"] = [u"帮助与设置", "name", u"帮助与设置"]
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
        d["title"] = [u"微联", "name", u"App主页面"]
        # +号
        d["add_device"] = ["com.jd.smart:id/iv_right", "id", u"+号"]
        # 账户管理
        d["account_setting"] = ["com.jd.smart:id/iv_left", "id", u"账户管理"]
        # 没有设备/未登录
        d["no_device"] = ["com.jd.smart:id/layout_no_device", "id", u"没有设备/未登录"]
        # 设备
        d["device"] = ["com.jd.smart:id/tv_name", "id", u"没有设备/未登录"]
        return d

    # 添加设备页面
    def add_device_method_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加设备", "name", u"添加设备页面"]
        # 通过设备品类添加
        d["variety"] = [u"通过设备品类添加", "name", u"通过设备品类添加"]
        # 添加历史
        d["history"] = ["com.jd.smart:id/iv_history", "id", u"添加历史"]
        return d

    # 添加设备页面
    def add_device_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备品类", "name", u"添加设备页面"]
        # 插座列表选项
        d["option"] = [u"插座", "name", u"插座列表选项"]
        return d

    # 进入设备添加历史页面
    # driver.find_elements_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='2']")
    def add_history_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"已添加设备", "name", u"进入设备添加历史页面"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"公牛WiFi智能电量统计版转换器2代", "name", u"公牛Wi-Fi智能转换器2代电量计量版"]
        # 公牛Wi-Fi智能转换器2代
        d["y2011"] = [u"公牛Wi-Fi智能转换器2代", "name", u"公牛Wi-Fi智能转换器2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"公牛Wi-Fi智能插座2代加强版", "name", u"公牛Wi-Fi智能插座2代加强版"]
        return d

    # 进入插座列表页面
    def add_outlet_list_page(self):
        d = {}
        # 标题
        d["title"] = [u"插座", "name", u"插座列表页面"]
        # 公牛Wi-Fi智能插座2代
        d["y2011"] = [u"公牛Wi-Fi智能插座2代", "name", u"公牛Wi-Fi智能插座2代"]
        # 公牛Wi-Fi智能转换器2代电量计量版
        d["y201J"] = [u"公牛WiFi智能电量统计版转换器2代", "name", u"公牛WiFi智能电量统计版转换器2代"]
        # 公牛Wi-Fi智能插座2代加强版
        d["y2011dl"] = [u"公牛Wi-Fi智能插座2代加强版", "name", u"公牛Wi-Fi智能插座2代加强版"]
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
        d["check_box"] = ["com.jd.smart:id/cb_eye", "id", u"wifi密码输入框"]
        return d

    # 搜索设备等待页面
    def search_device_loading_page(self):
        TextValue = "[@text='3']"
        self.search_device_loading = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.search_device_loading, "xpath", u"搜索设备等待页面"]
        return d

    # 设备等待添加
    def batch_add_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"批量添加", "name", u"设备等待添加"]
        return d

    def search_device_success_page(self):
        # 搜索到设备MAC
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/tv_desc", "id", u"有设备出现"]
        # 确认
        d["confirm"] = [u"使用", "name", u"确定"]
        return d

    # 搜索设备超时
    def search_device_fail_page(self):
        TextValue = "[@text='4']"
        self.search_device_fail = "".join((self.xpath, TextValue))
        d = {}
        # 标题
        d["title"] = [self.search_device_fail, "xpath", u"搜索设备超时"]
        return d

    # 绑定成功页面
    def bind_device_success_page(self):
        d = {}
        # 标题
        d["title"] = ["com.jd.smart:id/btn_config", "id", u"绑定成功页面"]
        # 确定绑定按钮
        d["confirm"] = ["com.jd.smart:id/btn_config", "id", u"确定"]
        # 输入设备备注名
        d["notes"] = ["com.jd.smart:id/edittext_layout", "id", u"绑定成功页面标志"]
        return d

    # 设备已被绑定
    def bind_device_page(self):
        d = {}
        # 标题
        d["title"] = [u"该设备已被绑定", "name", u"该设备已被绑定"]
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
        # 电源开启
        d["power_on"] = [u"设备已开启", "name", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"设备已关闭", "name", u"电源关闭"]
        # 设备记忆模式
        d["memory_mode"] = [u"记忆模式", "name", u"设备记忆模式"]
        # 设备安全模式
        d["safe_mode"] = [u"安全模式", "name", u"设备安全模式"]
        # 模式定时
        d["mode_timer"] = [u"自定义模式", "name", u"模式定时"]
        # 模式定时
        d["normal_timer"] = [u"定时设置", "name", u"普通定时"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"设置", "name", u"设备信息页面"]
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
        d["title"] = [u"修改名称", "name", u"修改设备备注页面"]
        # 保存
        d["saved"] = [u"保存", "name", u"保存"]
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


class PopupWidgetAndroidJD(object):
    # 设备升级确认弹窗
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
        d["title"] = [u"是否清空记录", "name", u"是否清空记录"]
        # 确认
        d["confirm"] = [u"是", "name", u"确认"]
        # 取消
        d["cancel"] = [u"否", "name", u"取消"]
        return d
