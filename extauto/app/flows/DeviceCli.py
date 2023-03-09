from time import sleep

from extauto.app.elements.DeviceCliWebElements import DeviceCliWebElements
from extauto.app.elements.NewDeviceOnboardWebElements import NewDeviceOnboardWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils


class DeviceCli:
    def __init__(self):
        self.mob_login_web_elements = DeviceCliWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_cli(self,  cli_cmd):
        self.utils.print_info("user is on AP details screen...............")
        self.auto_actions.click_reference(self.mob_login_web_elements.get_device_cli)
        self.utils.print_info("click on device cli widget")
        sleep(7)
        for cli in cli_cmd:
            self.auto_actions.send_keys(self.mob_login_web_elements.get_device_cli_search_field(), cli)
            self.utils.print_info("user entered the command in search field")
            sleep(2)
            self.auto_actions.click_reference(self.mob_login_web_elements.get_device_cli_apply_button)
            self.utils.print_info("user clicked on apply button")
            sleep(5)
            cli = self.mob_login_web_elements.get_device_cli_text()
            self.utils.print_info("cmdline text", cli)
            sleep(5)

    def device_cli_exit(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.get_device_cli_exit)
        self.utils.print_info("user clicked on device cli close link")
        self.utils.print_info("click on device cli close link")
