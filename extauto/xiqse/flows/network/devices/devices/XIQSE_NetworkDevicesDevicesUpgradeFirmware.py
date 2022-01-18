from xiqse.elements.network.devices.devices.NetworkDevicesDevicesUpgradeFirmwareWebElements import NetworkDevicesDevicesUpgradeFirmwareWebElements
from common.Cli import *
from common.Screen import Screen
from common.AutoActions import AutoActions
from common.WebElementHandler import *


class XIQSE_NetworkDevicesDevicesUpgradeFirmware(NetworkDevicesDevicesUpgradeFirmwareWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.web = WebElementHandler()

    def xiqse_open_assign_firmware_image(self):
        """
        - This keyword opens the Assign Firmware Image selector by selecting "Assign Firmware..." from the Upgrade Firmware dialog.
        - It assumes the Upgrade Firmware dialog is already open.
        - Keyword Usage:
         - ``XIQSE Open Assign Firmware Image``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        assign_firmware_image = self.get_assign_firmware_images_button()
        if assign_firmware_image:
            self.utils.print_info("Clicking 'Assign Firmware...' menu")
            self.auto_actions.click(assign_firmware_image)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Assign Firmware...' button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_open_inventory_settings(self):
        """
        - This keyword opens the Inventory Settings dialog by selecting "Inventory Settings" from the Upgrade Firmware dialog.
        - It assumes the Upgrade Firmware dialog is already open.
        - Keyword Usage:
         - ``XIQSE Open Inventory Settings``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        inventory_settings = self.get_inventory_settings_button()
        if inventory_settings:
            self.utils.print_info("Clicking 'Inventory Settings' button")
            self.auto_actions.click(inventory_settings)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Inventory Settings' button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_click_upgrade_firmware_start_button(self):
        """
         - Clicks the Start button on the Upgrade Firmware Dialog to accept choices
         - It assumes the Firmware Selection dialog is already open
         - Keyword Usage
            - ``XIQSE Click Upgrade Firmware Start Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        start_btn = self.get_upgrade_firmware_start_button()
        if start_btn:
            self.utils.print_info("Clicking Upgrade Firmware Start button")
            self.auto_actions.click(start_btn)
        else:
            self.utils.print_info("Could not find Start button in Upgrade Firmware")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_click_upgrade_firmware_close_button(self):
        """
         - Clicks the Cancel button on the Upgrade Firmware Dialog to discard choices
         - It assumes the Upgrade Firmware dialog is already open
         - Keyword Usage
            - ``XIQSE Click Upgrade Firmware Close Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        cancel_btn = self.get_upgrade_firmware_close_button()
        if cancel_btn:
            self.utils.print_info("Clicking Upgrade Firmware Close button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Close button in Upgrade Firmware")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_click_begin_downloading_firmware_yes_button(self):
        """
         - Clicks the Yes button on the Begin Downloading Firmware Dialog to discard choices
         - It assumes the Begin Downloading Firmware dialog is already open
         - Keyword Usage
            - ``XIQSE Click Begin Downloading Firmware Yes Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        yes_btn = self.get_begin_downloading_firmware_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking Yes button to begin downloading firmware")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find Yes button to begin downloading firmware")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_click_begin_downloading_firmware_no_button(self):
        """
         - Clicks the No button on the Begin Downloading Firmware Dialog to discard choices
         - It assumes the Begin Downloading Firmware dialog is already open
         - Keyword Usage
            - ``XIQSE Click Begin Downloading Firmware No Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        no_btn = self.get_begin_downloading_firmware_no_button()
        if no_btn:
            self.utils.print_info("Clicking No button to stop downloading firmware")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find No button to stop downloading firmware")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_wait_for_processed_no_failures_text(self, seconds=900):
        """
         - Institutes a loop waiting for "Processed 1 of 1 devices with 0 failures" text to appear in the Dialog
         - It assumes the dialog is already open
         - Keyword Usage
            - ``XIQSE Wait for Processed No Failures Text``

        :return: 1 if action was successful, else -1
        """

        self.utils.print_info("wait_until_appears")
        while seconds > 0:
            time.sleep(5)
            self.utils.print_info("get element")
            element = self.get_processed_devices_with_no_failures_text()
            if element and element.is_displayed():
                self.utils.print_info("Upgrade completed")
                return 1
            else:
                seconds = seconds - 5

        self.utils.print_info("Upgrade failed")
        self.screen.save_screen_shot()
        return -1
