from extauto.app.defs.DeviceHostnameDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *


class DeviceHostnameWebElements(DeviceHostnameDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_device_hostname_edit_icon(self):
        return self.weh.get_element(self.hostname_edit_icon_id)

    def get_device_hostname_text_field(self):
        return self.weh.get_element(self.hostname_entry_text_field)

    def get_device_hostname_cancel_button(self):
        return self.weh.get_element(self.hostname_cancel_button_id)

    def get_device_hostname_save_button(self):
        return self.weh.get_element(self.hostname_save_button_id)

    def get_device_hostname_error_message(self):
        error_message = self.weh.get_element(self.hostname_error_msg_id)
        if error_message.is_displayed():
            return error_message.text

    def get_device_hostname(self):
        hostname = self.weh.get_element(self.hostname_id)
        if hostname.is_displayed():
            return hostname.text


