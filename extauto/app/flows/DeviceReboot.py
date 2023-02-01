from time import sleep

from extauto.app.elements.DeviceRebootWebElements import DeviceRebootWebElements
from extauto.app.elements.NewDeviceOnboardWebElements import NewDeviceOnboardWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils


class DeviceReboot:
    def __init__(self):
        self.mob_login_web_elements = DeviceRebootWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_reboot(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click_reference(self.mob_login_web_elements.get_reboot_device)
        self.utils.print_info("user clicked on reboot device widget")
        sleep(7)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_reboot_device_cancel_button)
        self.utils.print_info("user clicked on  cancel option of reboot device ")
        sleep(3)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_reboot_device)
        self.utils.print_info("user clicked on reboot device widget")
        sleep(6)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_reboot_device_yes_button)
        self.utils.print_info("used click on  Yes to  reboot device ")
        sleep(6)
