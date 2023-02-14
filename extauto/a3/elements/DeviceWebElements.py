from a3.defs.DeviceWebElementDefs import DeviceWebElementDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class DeviceWebElements(DeviceWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def select_device_ui(self):
        return self.weh.get_element(self.device_ui)
