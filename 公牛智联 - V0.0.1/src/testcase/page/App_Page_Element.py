# coding=utf-8

class MainPageWidget(object):
    def login_page(self):
        d = {}
        # 用户名输入框
        d["username"] = ["com.iotbull.android.superapp:id/loginUserNameEditText", "id"]
        # 密码输入框
        d["password"] = ["com.iotbull.android.superapp:id/loginPasswordEditText", "id"]
        # 忘记密码
        d["to_find_password"] = ["com.iotbull.android.superapp:id/loginFindPasswordTextView", "id"]
        # 登录按钮
        d["login_button"] = ["com.iotbull.android.superapp:id/loginCommitButton", "id"]
        # 新账号注册
        d["to_register"] = ["com.iotbull.android.superapp:id/loginToRegistTextView", "id"]
        return d

    def find_password_page(self):
        d = {}
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        # 手机号
        d["user_name"] = ["com.iotbull.android.superapp:id/forget_password_user_name_edit_text", "id"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/forget_password_check_code_edit_text", "id"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/forget_password_get_check_code_text_view", "id"]
        # 下一步
        d["to_next"] = ["com.iotbull.android.superapp:id/forget_password_commit_button", "id"]
        return d

    def register_page(self):
        d = {}
        # 用户名
        d["username"] = ["com.iotbull.android.superapp:id/registUserNameEditText", "id"]
        # 密码
        d["password"] = ["com.iotbull.android.superapp:id/registPasswordEditText", "id"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/registCheckCodeEditText", "id"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/registGetCheckCodeTextView", "id"]
        # 立即注册按钮
        d["register_button"] = ["com.iotbull.android.superapp:id/regist_commit_button", "id"]
        # 公牛服务协议
        d["to_protocol"] = ["com.iotbull.android.superapp:id/registToRegistProtocolTextView", "id"]
        # 已有账户登录
        d["to_login"] = ["com.iotbull.android.superapp:id/registToLoginTextView", "id"]
        # 密码可见/不可见
        d["check_box"] = ["com.iotbull.android.superapp:id/checkBox", "id"]
        return d

    def protocol_page(self):
        d = {}
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        return d

    def devices_page(self):
        d = {}
        pass
        return d

    def personal_settings_page(self):
        d = {}
        # 头像
        d["head_image"] = ["com.iotbull.android.superapp:id/home_setting_head_image_view", "id"]
        # 昵称
        d["nickname"] = ["com.iotbull.android.superapp:id/menu_setting_nickname_text_view", "id"]
        # 账号
        d["id"] = ["com.iotbull.android.superapp:id/menu_setting_phone_text_view", "id"]
        # 账户设置
        d["account_setting"] = [u"账户设置", "name"]
        # 使用帮助
        d["using_help"] = [u"使用帮助", "name"]
        # 意见反馈
        d["feedback"] = [u"意见反馈", "name"]
        # 主题风格
        d["theme_style"] = [u"主题风格", "name"]
        # 版本信息
        d["version_info"] = [u"版本信息", "name"]
        # 关于我们
        d["about_us"] = [u"关于我们", "name"]
        return d

    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"账户设置", "name"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        # 昵称
        d["nickname"] = [u"昵称", "name"]
        # 性别
        d["gender"] = [u"性别", "name"]
        # 地址
        d["address"] = [u"地址", "name"]
        # 生日
        d["birthday"] = [u"生日", "name"]
        # 修改密码
        d["change_pwd"] = [u"修改密码", "name"]
        # 退出登录
        d["logout"] = ["com.iotbull.android.superapp:id/user_info_btn_logout", "id"]
        return d

    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改昵称", "name"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        # 输入框
        d["nickname"] = ["com.iotbull.android.superapp:id/user_name_update_nickname_edit_text", "id"]
        # 完成
        d["commit"] = ["com.iotbull.android.superapp:id/user_name_update_commit_button", "id"]
        return d

    # uiautomatorviewer没办法读取滚轮数值，暂不使用
    def gender_page(self):
        d = {}
        # 选择性别
        d["choose_gender"] = [u"选择性别", "name"]
        # 取消
        d["cancel"] = [u"取消", "name"]
        # 确定
        d["submit"] = [u"确定", "name"]
        return d

    def change_pwd_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改密码", "name"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        # 旧密码
        d["old_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_old_password_edit_text", "id"]
        # 新密码
        d["new_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_new_password_edit_text", "id"]
        # 确认新密码
        d["conform_pwd"] = [
            "com.iotbull.android.superapp:id/user_password_update_new_password_commit_password_edit_text",
            "id"]
        # 确定
        d["commit"] = ["com.iotbull.android.superapp:id/user_password_update_commit_button", "id"]
        return d

    def feedback_page(self):
        d = {}
        # 标题
        d["title"] = [u"意见反馈", "name"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class"]
        # 问题类型
        d["problem_types"] = [u"问题类型", "name"]
        # 涉及设备
        d["involve_device"] = [u"涉及设备", "name"]
        # 问题描述
        d["problem_describe"] = ["com.iotbull.android.superapp:id/feedback_content_edit_text", "id"]
        # 联系方式
        d["contact"] = ["com.iotbull.android.superapp:id/feedback_title_edit_text", "id"]
        # 提交
        d["commit"] = ["com.iotbull.android.superapp:id/feedback_add_button", "id"]
        return d

    def device_page(self):
        d = {}
        # 设备table
        d["device_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_device", "id"]
        # 消息table
        d["message_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_message", "id"]
        # 商城table
        d["mall_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_mall", "id"]
        # 添加设备按钮
        d["add_device"] = ["com.iotbull.android.superapp:id/device_iv_add", "id"]
        # 切换九宫格
        d["change_layout"] = ["com.iotbull.android.superapp:id/device_iv_change_layout", "id"]
        return d
