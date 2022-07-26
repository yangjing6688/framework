from app.defs.DeviceRebootDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *


class DeviceRebootWebElements(DeviceRebootDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_reboot_device(self):
        return self.weh.get_element(self.reboot_device_id)

    def get_reboot_device_yes_button(self):
        return self.weh.get_element(self.reboot_device_confirm_id)

    def get_reboot_device_cancel_button(self):
        return self.weh.get_element(self.reboot_device_cancel_id)