from app.elements.DeviceRebootWebElements import *
from app.elements.NewDeviceOnboardWebElements import *
from app.common.AutoActions import *
import time


class DeviceReboot:
    def __init__(self):
        self.mob_login_web_elements = DeviceRebootWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_reboot(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_reboot_device())
        self.utils.print_info("user clicked on reboot device widget")
        time.sleep(7)
        self.auto_actions.click(self.mob_login_web_elements.get_reboot_device_cancel_button())
        self.utils.print_info("user clicked on  cancel option of reboot device ")
        time.sleep(3)
        self.auto_actions.click(self.mob_login_web_elements.get_reboot_device())
        self.utils.print_info("user clicked on reboot device widget")
        time.sleep(6)
        self.auto_actions.click(self.mob_login_web_elements.get_reboot_device_yes_button())
        self.utils.print_info("used click on  Yes to  reboot device ")
        time.sleep(6)
