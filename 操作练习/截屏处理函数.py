def screen_shot(self):
    folder = "%s[%s]" % (self.device_info["model"], self.device_info["udid"])
    screen_shot = r"%s/%s - %s - %s - [%s]-[%s].png" \
                  % (folder, database["program_loop_time"], database["case_location"],
                     self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))
    adb_screen = "%s/%s[%s].png" % (folder, self.ZenTao_id, time.strftime("%Y-%m-%d.%H_%M_%S"))

    width = int(int(self.device_info["dpi"]["width"]) * change_pwd_page["commit"][3][0])
    height = int(int(self.device_info["dpi"]['height']) * change_pwd_page["commit"][3][1])
    self.driver.tap([(width, height)], )

    while True:
        try:
            self.wait_widget(loading_popup["title"], 0.5, 0.1)
        except TimeoutException:
            break

    command = "adb -s %s shell /system/bin/screencap -p /sdcard/Appium/%s" % (self.device_info["udid"], adb_screen)
    os.system(command)
    command1 = "adb -s %s shell du /sdcard/Appium/%s" % (self.device_info["udid"], adb_screen)

    screen_count = 3
    while screen_count:
        try:
            time.sleep(0.5)
            len_adb_screen_file = int(re.findall(r"(.+?)/sdcard", os.popen(command1).read())[0].split()[0])
            print len_adb_screen_file
            if len_adb_screen_file != 0:
                self.logger.info('[ADB]adb screen shot success!')
                break
            else:
                os.system(command)
        except ValueError:
            os.system(command)
            screen_count -= 1
            self.logger.info('[ADB]adb find screen file failed still %s times!' % screen_count)

    command = "adb -s {0} pull /sdcard/Appium/{1} ./screenshots/{1}".format(self.device_info["udid"], adb_screen)
    pull_file = re.findall(r".+file pulled.+", os.popen(command).read())
    if pull_file is not []:
        self.logger.info('[ADB]adb screen shot put file to PC success!')
    else:
        self.logger.info('[ADB]adb screen shot put file to PC failed!')

    try:
        os.rename("./screenshots/%s" % adb_screen, "./screenshots/%s" % screen_shot)
        self.logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot success')
    except WindowsError:
        self.logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot failed')
