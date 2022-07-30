from extauto.app.elements.FlashLedWebElements import *
from extauto.app.elements.NewDeviceOnboardWebElements import *
from extauto.common.AutoActions import *
import time


class FlashLed:
    def __init__(self):
        self.mob_login_web_elements = FlashLedWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def flash_led_on(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_flash_led())
        self.utils.print_info("user clicked on device flash led widget")
        time.sleep(10)
        self.auto_actions.click(self.mob_login_web_elements.get_flash_led_return_normal_ok_button())
        self.utils.print_info("user clicked on okay button")

    def flash_led_off(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_flash_led())
        self.utils.print_info("user clicked on device flash led widget")
        time.sleep(10)
        self.auto_actions.click(self.mob_login_web_elements.get_flash_led_return_to_normal())
        self.utils.print_info("user clicked on check box")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_flash_led_return_normal_ok_button())
        self.utils.print_info("user clicked on okay button")

