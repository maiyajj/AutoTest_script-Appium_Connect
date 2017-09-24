# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


def case():
    try:
        while True:
            elements = wait_widget(page["app_home_page"]["device"])
            new_value = copy.copy(page["app_home_page"]["device"])
            for index, element in elements.items():
                if element is not None and str(ac.get_attribute(element, "name")) == conf["MAC"][0]:
                    new_value[0] = new_value[0][index]
                    while True:
                        try:
                            widget_click(new_value, page["control_device_page"]["title"])
                            raise ValueError()
                        except TimeoutException:
                            ac.swipe(0.6, 0.9, 0.6, 0.6, 0, driver)
            time.sleep(1)
    except ValueError:
        pass

    try:
        wait_widget(page["control_device_page"]["power_off"])
    except TimeoutException:
        widget_click(page["control_device_page"]["power_button"],
                     page["control_device_page"]["power_off"])

    widget_click(page["control_device_page"]["mode_timer"],
                 page["mode_timer_page"]["title"])

    widget_click(page["mode_timer_page"]["water_mode"],
                 page["water_mode_timer_page"]["title"])

    delay_time = 1
    widget_click(page["water_mode_timer_page"]["start_time"],
                 page["water_mode_timer_page"]["start_h"])

    set_timer_roll(page["water_mode_timer_page"]["start_h"],
                   page["water_mode_timer_page"]["start_m"],
                   page["water_mode_timer_page"]["start_time_text"], delay_time)

    widget_click(page["water_mode_timer_page"]["start_time"],
                 page["water_mode_timer_page"]["title"])

    delay_time = -2
    widget_click(page["water_mode_timer_page"]["end_time"],
                 page["water_mode_timer_page"]["end_h"])

    set_timer_roll(page["water_mode_timer_page"]["end_h"],
                   page["water_mode_timer_page"]["end_m"],
                   page["water_mode_timer_page"]["end_time_text"], delay_time)

    widget_click(page["water_mode_timer_page"]["end_time"],
                 page["water_mode_timer_page"]["title"])

    widget_click(page["water_mode_timer_page"]["repeat"],
                 page["timer_repeat_page"]["title"])

    try:
        wait_widget(page["timer_repeat_page"]["once"])
    except TimeoutException:
        widget_click(page["timer_repeat_page"]["repeat_button"],
                     page["timer_repeat_page"]["once"])

    widget_click(page["timer_repeat_page"]["to_return"],
                 page["water_mode_timer_page"]["title"])

    widget_click(page["water_mode_timer_page"]["launch"],
                 page["mode_timer_page"]["title"])

    widget_click(page["mode_timer_page"]["to_return"],
                 page["control_device_page"]["title"])

    wait_widget(page["control_device_page"]["power_off"])

    end_time = time.time() + (abs(delay_time) + 1) * 60
    while True:
        element = wait_widget(page["control_device_page"]["power_state"])
        if ac.get_attribute(element, "name") == u"设备已开启":

            break
        else:
            if time.time() < end_time:
                time.sleep(1)
            else:
                raise TimeoutException(u"定时未执行")

    case_over(True)
