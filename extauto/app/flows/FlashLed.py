from time import sleep

from extauto.app.elements.FlashLedWebElements import FlashLedWebElements
from extauto.app.elements.NewDeviceOnboardWebElements import NewDeviceOnboardWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils


class FlashLed:
    def __init__(self):
        self.mob_login_web_elements = FlashLedWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def flash_led_on(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click_reference(self.mob_login_web_elements.get_flash_led)
        self.utils.print_info("user clicked on device flash led widget")
        sleep(10)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_flash_led_return_normal_ok_button)
        self.utils.print_info("user clicked on okay button")

    def flash_led_off(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click_reference(self.mob_login_web_elements.get_flash_led)
        self.utils.print_info("user clicked on device flash led widget")
        sleep(10)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_flash_led_return_to_normal)
        self.utils.print_info("user clicked on check box")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_flash_led_return_normal_ok_button)
        self.utils.print_info("user clicked on okay button")
