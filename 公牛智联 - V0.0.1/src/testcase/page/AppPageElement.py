# coding=utf-8
god_page = {}
god_page["title"] = ["android.widget.FrameLayout", "class", u"万能控件"]


class MainPageWidget(object):
    def view_pager_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/indicator", "id", u"引导页"]
        return d

    def login_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/loginCommitButton", "id", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.LoginActivity", "activity", u"页面activity"]
        # 用户名输入框
        d["username"] = ["com.iotbull.android.superapp:id/loginUserNameEditText", "id", u"用户名输入框"]
        # 密码输入框
        d["password"] = ["com.iotbull.android.superapp:id/loginPasswordEditText", "id", u"密码输入框"]
        # 忘记密码
        d["to_find_password"] = ["com.iotbull.android.superapp:id/loginFindPasswordTextView", "id", u"忘记密码"]
        # 登录按钮
        d["login_button"] = ["com.iotbull.android.superapp:id/loginCommitButton", "id", u"登录按钮"]
        # 新账号注册
        d["to_register"] = ["com.iotbull.android.superapp:id/loginToRegistTextView", "id", u"新账号注册"]
        return d

    def find_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"忘记密码", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 手机号
        d["user_name"] = ["com.iotbull.android.superapp:id/forget_password_user_name_edit_text", "id", u"手机号"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/forget_password_check_code_edit_text", "id", u"验证码"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/forget_password_get_check_code_text_view", "id",
                               u"获取验证码"]
        # 下一步
        d["to_next"] = ["com.iotbull.android.superapp:id/forget_password_commit_button", "id", u"下一步"]
        return d

    def new_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"新密码设置", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 新密码
        d["new_pwd"] = ["com.iotbull.android.superapp:id/forget_password_new_password_password_edit_text", "id", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = ["com.iotbull.android.superapp:id/forget_password_new_password_commit_password_edit_text",
                            "id", u"确认新密码"]
        # 完成
        d["commit"] = ["com.iotbull.android.superapp:id/forget_password_new_password_commit_button", "id", u"完成"]
        return d

    def register_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/regist_commit_button", "id", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.RegistActivity", "activity", u"页面activity"]
        # 用户名
        d["username"] = ["com.iotbull.android.superapp:id/registUserNameEditText", "id", u"用户名"]
        # 密码
        d["password"] = ["com.iotbull.android.superapp:id/registPasswordEditText", "id", u"密码"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/registCheckCodeEditText", "id", u"验证码"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/registGetCheckCodeTextView", "id", u"获取验证码"]
        # 立即注册按钮
        d["register_button"] = ["com.iotbull.android.superapp:id/regist_commit_button", "id", u"立即注册按钮"]
        # 公牛服务协议
        d["to_protocol"] = ["com.iotbull.android.superapp:id/registToRegistProtocolTextView", "id", u"公牛服务协议"]
        # 已有账户登录
        d["to_login"] = ["com.iotbull.android.superapp:id/registToLoginTextView", "id", u"已有账户登录"]
        # 密码可见/不可见
        d["check_box"] = ["com.iotbull.android.superapp:id/checkBox", "id", u"密码可见/不可见"]
        return d

    def protocol_page(self):
        d = {}
        # 标题
        d["title"] = [u"用户注册协议", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.RegistProtocolActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        return d

    def devices_page(self):
        d = {}
        pass
        return d

    def personal_settings_page(self):
        d = {}
        # 标题
        d["title"] = [u"账户设置", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 头像
        d["head_image"] = ["com.iotbull.android.superapp:id/home_setting_head_image_view", "id", u"头像"]
        # 昵称
        d["nickname"] = ["com.iotbull.android.superapp:id/menu_setting_nickname_text_view", "id", u"昵称"]
        # 账号
        d["id"] = ["com.iotbull.android.superapp:id/menu_setting_phone_text_view", "id", u"账号"]
        # 账户设置
        d["account_setting"] = [u"账户设置", "name", u"账户设置"]
        # 使用帮助
        d["using_help"] = [u"使用帮助", "name", u"使用帮助"]
        # 意见反馈
        d["feedback"] = [u"意见反馈", "name", u"意见反馈"]
        # 主题风格
        d["theme_style"] = [u"主题风格", "name", u"主题风格"]
        # 版本信息
        d["version_info"] = [u"版本信息", "name", u"版本信息"]
        # 关于我们
        d["about_us"] = [u"关于我们", "name", u"关于我们"]
        return d

    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"账户设置", "name", u"关于我们"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.userinfo_setting.UserInfoSettingActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 昵称
        d["nickname"] = [u"昵称", "name", u"昵称"]
        # 性别
        d["gender"] = [u"性别", "name", u"性别"]
        # 地址
        d["address"] = [u"地址", "name", u"地址"]
        # 生日
        d["birthday"] = [u"生日", "name", u"生日"]
        # 修改密码
        d["change_pwd"] = [u"修改密码", "name", u"修改密码"]
        # 退出登录
        d["logout"] = ["com.iotbull.android.superapp:id/user_info_btn_logout", "id", u"退出登录"]
        return d

    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改昵称", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.userinfo_setting.UserNameUpdateActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 输入框
        d["nickname"] = ["com.iotbull.android.superapp:id/user_name_update_nickname_edit_text", "id", u"输入框"]
        # 完成
        d["commit"] = ["com.iotbull.android.superapp:id/user_name_update_commit_button", "id", u"完成"]
        return d

    # uiautomatorviewer没办法读取滚轮数值，暂不使用
    def gender_page(self):
        d = {}
        # 选择性别
        d["choose_gender"] = [u"选择性别", "name", u"选择性别"]
        # 取消
        d["cancel"] = [u"取消", "name", u"取消"]
        # 确定
        d["submit"] = [u"确定", "name", u"确定"]
        return d

    def change_pwd_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改密码", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.password_update.UserPasswordUpdateActivity", "activity",
                         u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 旧密码
        d["old_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_old_password_edit_text", "id", u"旧密码"]
        # 新密码
        d["new_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_new_password_edit_text", "id", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = [
            "com.iotbull.android.superapp:id/user_password_update_new_password_commit_password_edit_text",
            "id", u"确认新密码"]
        # 确定
        d["commit"] = ["com.iotbull.android.superapp:id/user_password_update_commit_button", "id", u"确定"]
        return d

    def app_help_page(self):
        d = {}
        # 标题
        d["title"] = [u"使用帮助", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.AppHelpActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        return d

    # .activitys.main_setting.AppUpgradeActivity 版本信息
    # .activitys.main_setting.AppAboutActivity 关于我们
    def feedback_page(self):
        d = {}
        # 标题
        d["title"] = [u"意见反馈", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.feedback.FeedbackActivity", "activity",
                         u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 问题类型
        d["problem_types"] = [u"问题类型", "name", u"问题类型"]
        # 涉及设备
        d["involve_device"] = [u"涉及设备", "name", u"涉及设备"]
        # 问题描述
        d["problem_describe"] = ["com.iotbull.android.superapp:id/feedback_content_edit_text", "id", u"问题描述"]
        # 联系方式
        d["contact"] = ["com.iotbull.android.superapp:id/feedback_title_edit_text", "id", u"联系方式"]
        # 提交
        d["commit"] = ["com.iotbull.android.superapp:id/feedback_add_button", "id", u"提交"]
        return d

    def device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/device_user_image_view", "id", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 用户头像
        d["user_image"] = ["com.iotbull.android.superapp:id/device_user_image_view", "id", u"主页面头像"]
        # 设备table
        d["device_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_device", "id", u"设备table"]
        # 消息table
        d["message_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_message", "id", u"消息table"]
        # 商城table
        d["mall_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_mall", "id", u"商城table"]
        # 添加设备按钮
        d["add_device"] = ["com.iotbull.android.superapp:id/device_iv_add", "id", u"添加设备按钮"]
        # 切换九宫格
        d["change_layout"] = ["com.iotbull.android.superapp:id/device_iv_change_layout", "id", u"切换九宫格"]
        return d

    def home_message_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/message_tab_btn_activity", "id", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 活动
        d["message_activity"] = ["com.iotbull.android.superapp:id/message_tab_btn_activity", "id", u"活动"]
        # 设备
        d["device"] = ["com.iotbull.android.superapp:id/message_tab_btn_alert", "id", u"设备"]
        # 消息分类
        d["classify"] = ["android.widget.ImageButton", "class", u"消息分类"]
        # 设置
        d["setting"] = ["//android.support.v7.widget.LinearLayoutCompat/android.widget.TextView", "xpath", u"设置"]
        return d

    # 消息分类
    def message_classify_page(self):
        d = {}
        # 标题
        d["title"] = [u"消息分类", "name", u"标题"]
        # 页面activity
        d["activity"] = [".activitys.message_mall.message_classify.MessageClassifyActivity", "activity", u"页面activity"]
        # 全部设备
        d["all_device"] = ["//android.widget.LinearLayout[1]//android.widget.RadioButton", "xpath", u"全部设备"]
        # 展示体验数据
        d["experience_data"] = ["//android.widget.LinearLayout[2]//android.widget.RadioButton", "xpath", u"展示体验数据"]
        # A2 管理者
        d["A2"] = ["//android.widget.LinearLayout[3]//android.widget.RadioButton", "xpath", u"A2 管理者"]
        # A3 体验
        d["A3"] = ["//android.widget.LinearLayout[4]//android.widget.RadioButton", "xpath", u"A3 体验"]
        # A4 分享者
        d["A4"] = ["//android.widget.LinearLayout[5]//android.widget.RadioButton", "xpath", u"A4 分享者"]
        # A5 体验
        d["A5"] = ["//android.widget.LinearLayout[6]//android.widget.RadioButton", "xpath", u"A5 体验"]
        return d

        # 消息设置.activitys.message_mall.message_setting.MessageSettingActivity
        # 选择产品类型 .activitys.device_scene.SelectProductActivity
        # 扫描二维码 com.google.zxing.activity.CaptureActivity
        # 公牛智能网关-硬件 .activitys.device_scene.device_add.PrepareSetNetworkActivity
        # 配置网络 .activitys.device_scene.device_add.SetNetworkActivity
        # 添加设备 .activitys.device_scene.device_add.ScanWithSubscribeActivity
        # 添加失败 .activitys.device_scene.device_add.AddFailedActivity


class PopupWidget(object):
    def update_popup(self):
        d = {}
        # 标题
        d["title"] = [u"新版提示", "name", u"标题"]
        # 立即体验
        d["confirm"] = ["android:id/button1", "id", u"立即体验"]
        # 稍后更新
        d["cancel"] = ["android:id/button2", "id", u"稍后更新"]
        # 安装
        d["install"] = ["com.android.packageinstaller:id/ok_button", "id", u"安装"]
        # 取消
        d["install_cancel"] = ["com.android.packageinstaller:id/cancel_button", "id", u"稍后更新"]
        # 完成
        d["install"] = ["com.android.packageinstaller:id/done_button", "id", u"完成"]
        # 打开
        d["install_cancel"] = ["com.android.packageinstaller:id/launch_button", "id", u"打开"]
        return d

    def login_popup(self):
        d = {}
        # 标题
        d["title"] = [u"操作失败，账号超时未操作或异地登录，请重新登录。", "name", u"提示 - 重新登录"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.SplashActivity", "activity", u"页面activity"]
        # 登录
        d["confirm"] = ["android:id/button1", "id", u"登录"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d

    def logout_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否确认退出登录？", "name", u"退出确认"]
        # 确认
        d["confirm"] = ["android:id/button1", "id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d
