from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from time import sleep
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesFirmwareSelectionWebElements import NetworkDevicesDevicesFirmwareSelectionWebElements


class XIQSE_NetworkDevicesDevicesFirmwareSelection(NetworkDevicesDevicesFirmwareSelectionWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.view_el = NetworkDevicesDevicesFirmwareSelectionWebElements()


    def xiqse_click_refresh_images(self):
        """
        - This keyword refreshes the uploaded firmware images by selecting "Refresh Images..." from the Firmware Selection dialog.
        - It assumes the Firmware Selection dialog is already open.
        - Keyword Usage:
        - ``XIQSE Click Refresh Images``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        refresh_images = self.get_refresh_images_button()
        if refresh_images:
            self.utils.print_info("Clicking 'Refresh Images...' button")
            self.auto_actions.click(refresh_images)
            ret_val = self.xiqse_wait_for_refresh_images_to_complete()
        else:
            self.utils.print_info("Unable to find 'Refresh Images...' button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_for_refresh_images_to_complete(self, retry_duration=10, retry_count=30):
        """
        - This keyword waits for the "Refreshing Images" loading mask to complete before continuing
        - Keyword Usage
        - ''XIQSE Wait For Refresh Images to Complete''
        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Image Refresh to complete: loop {count}")
            load_mask = self.view_el.get_refresh_load_mask()
            if load_mask:
                self.utils.print_info(f"Refresh still in progress")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Refresh has completed")
                return 1
            count +=1

        self.utils.print_info("Search did not complete within specified time")
        self.screen.save_screen_shot()

        return -1



    def xiqse_select_firmware_image(self, firmware_image):
        """
         - This keyword selects the specified firmware for the device upgrade.
         - It is assumed the user is already on the Firmware Selection dialog.
         - Keyword Usage
          - ``XIQSE Select Firmware Image``

        :param firmware_image: Firmware Image from the table to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Selecting Firmware Image {firmware_image}")
        rows = self.get_firmware_images_table_rows()
        if rows:
            for row in rows:
                if firmware_image in row.text:
                    self.utils.print_debug(f"Found image {firmware_image} in row {self.xiqse_table.format_table_row(row.text)}")
                    row_selected = row.get_attribute("aria-selected")
                    if row_selected and row_selected == "true":
                        self.utils.print_info(f"Row for firmware image {firmware_image} is already selected")
                    else:
                        self.utils.print_info(f"Selecting firmware image {firmware_image}")
                        self.auto_actions.click(row)
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No rows are present")

        if ret_val == -1:
            self.utils.print_info(f"Unable to select firmware image {firmware_image}")
        return ret_val

    def xiqse_click_firmware_selection_ok_button(self):
        """
         - Clicks the OK button on the Firmware Selection Dialog to accept choices
         - It assumes the Firmware Selection dialog is already open
         - Keyword Usage
            - ``XIQSE Click Firmware Selection OK Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        ok_btn = self.get_firmware_selection_ok_button()
        if ok_btn:
            self.utils.print_info("Clicking Firmware Selection OK button")
            self.auto_actions.click(ok_btn)
        else:
            self.utils.print_info("Could not find OK button in Firmware Selection")
            ret_val = -1

        return ret_val

    def xiqse_click_firmware_selection_cancel_button(self):
        """
         - Clicks the Cancel button on the Firmware Selection Dialog to discard choices
         - It assumes the Firmware Selection dialog is already open
         - Keyword Usage
            - ``XIQSE Click Firmware Selection Cancel Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        cancel_btn = self.get_firmware_selection_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Firmware Selection Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Firmware Selection")
            ret_val = -1

        return ret_val