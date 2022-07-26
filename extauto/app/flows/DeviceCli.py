from app.elements.DeviceCliWebElements import *
from app.elements.NewDeviceOnboardWebElements import *
from extauto.common.AutoActions import *
import time


class DeviceCli:
    def __init__(self):
        self.mob_login_web_elements = DeviceCliWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_cli(self,  cli_cmd):
        self.utils.print_info("user is on AP details screen...............")
        self.auto_actions.click(self.mob_login_web_elements.get_device_cli())
        self.utils.print_info("click on device cli widget")
        time.sleep(7)
        for cli in cli_cmd:
            self.auto_actions.send_keys(self.mob_login_web_elements.get_device_cli_search_field(), cli)
            self.utils.print_info("user entered the command in search field")
            time.sleep(2)
            self.auto_actions.click(self.mob_login_web_elements.get_device_cli_apply_button())
            self.utils.print_info("user clicked on apply button")
            time.sleep(5)
            cli = self.mob_login_web_elements.get_device_cli_text()
            self.utils.print_info("cmdline text", cli)
            time.sleep(5)

    def device_cli_exit(self):
        self.auto_actions.click(self.mob_login_web_elements.get_device_cli_exit())
        self.utils.print_info("user clicked on device cli close link")
        self.utils.print_info("click on device cli close link")

