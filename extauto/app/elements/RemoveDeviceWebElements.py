from extauto.app.defs.RemoveDeviceDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *


class RemoveDeviceWebElements(RemoveDeviceDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_remove_device(self):
        return self.weh.get_element(self.remove_device_id)

    def get_remove_device_confirm(self):
        return self.weh.get_element(self.remove_device_confirm_id)

    def get_remove_device_cancel(self):
        return self.weh.get_element(self.remove_device_cancel_id)
