from extauto.app.elements.DeviceHostnameWebElements import *
from extauto.common.AutoActions import *
import time

class DeviceName:
    def __init__(self):
        self.hostname_web_elements = DeviceHostnameWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_hostname(self, hostnames):
        for hostname in hostnames:
            self.auto_actions.click(self.hostname_web_elements.get_device_hostname_edit_icon())
            self.utils.print_info("User clicked on device hostname edit icon")
            time.sleep(3)
            self.auto_actions.send_keys(self.hostname_web_elements.get_device_hostname_text_field(), hostname)
            self.utils.print_info("user entered the hostname in text field")
            time.sleep(3)
            self.auto_actions.click(self.hostname_web_elements.get_device_hostname_save_button())
            self.utils.print_info("user clicked on save button")
            time.sleep(2)
            hostname_value = self.hostname_web_elements.get_device_hostname()
            self.utils.print_info("changed hostname:", hostname_value)
            time.sleep(2)

    def device_hostname_cancel(self):
        self.auto_actions.click(self.hostname_web_elements.get_device_hostname_edit_icon())
        self.utils.print_info("User clicked on device hostname edit icon")
        time.sleep(3)
        self.auto_actions.click(self.hostname_web_elements.get_device_hostname_save_button())
        self.utils.print_info("user clicked on save button")
        time.sleep(2)
        error_msg = self.hostname_web_elements.get_device_hostname_error_message()
        self.utils.print_info("error message:", error_msg)
        time.sleep(2)
        self.auto_actions.click(self.hostname_web_elements.get_device_hostname_cancel_button())
        self.utils.print_info("user clicked on cancel button")
        time.sleep(2)












