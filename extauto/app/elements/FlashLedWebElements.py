from app.defs.FlashLedDefinitions import *
from app.common.AutoActions import *
from app.common.WebElementHandler import *


class FlashLedWebElements(FlashLedDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_flash_led(self):
        return self.weh.get_element(self.flash_led_seq_id)

    def get_flash_led_return_to_normal(self):
        return self.weh.get_element(self.flash_led_return_to_normal_id)

    def get_flash_led_return_normal_ok_button(self):
        return self.weh.get_element(self.flash_led_return_to_normal_confirm)