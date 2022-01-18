from app.elements.RemoveDeviceWebElements import *
from app.elements.NewDeviceOnboardWebElements import *
from app.common.AutoActions import *
import time


class RemoveDevice:
    def __init__(self):
        self.mob_login_web_elements = RemoveDeviceWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def remove_device_complete(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device())
        self.utils.print_info("user clicked on remove device widget")
        time.sleep(6)
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device_cancel())
        self.utils.print_info("user clicked on cancel option of remove device ")
        time.sleep(4)
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device())
        self.utils.print_info("user clicked on remove device widget")
        time.sleep(6)
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device_confirm())
        self.utils.print_info("user clicked on confirm option of remove device ")
        time.sleep(6)

    def remove_device(self):
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device())
        self.utils.print_info("user clicked on remove device widget")
        time.sleep(6)
        self.auto_actions.click(self.mob_login_web_elements.get_remove_device_confirm())
        self.utils.print_info("user clicked on confirm option of remove device ")
        time.sleep(6)