from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.firmware.NetworkFirmwareWebElements import NetworkFirmwareWebElements
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_NetworkFirmware(NetworkFirmwareWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = NetworkFirmwareWebElements()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_firmware_open_search(self):
        """
        - This keyword opens the search box on the Network > Firmware Tab
        - Keyword Usage
        - ``XIQSE Firmware Open Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_open_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "true":
                self.utils.print_info(f"Clicking Search button")
                self.auto_actions.click(search_btn)
                sleep(2)
            else:
                self.utils.print_info(f"Search field already open")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Search button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_firmware_enter_search_text(self, value):
        """
        - This keyword enters text into the search field on the Network > Firmware Tab
        - Keyword Usage
        - ``XIQSE Firmware Enter Search Text    My Firmware To Find``

        :param value: string to enter in the search box
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_text = self.get_search_text_field()
        if search_text:
            if search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Entering {value} into search box")
                self.auto_actions.send_keys(search_text, value)
                ret_val = 1
            else:
                self.utils.print_info("Search text field is currently hidden")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search text field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_firmware_trigger_search(self):
        """
        - This keyword clicks the search button in the search box on the Network > Firmware Tab to perform the search
        - Keyword Usage
        - ``XIQSE Firmware Trigger Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_trigger_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Search button to perform the search")
                self.auto_actions.click(search_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search button to perform the search")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_firmware_clear_search(self):
        """
        - This keyword clicks the clear button in the search box on the Network > Firmware Tab to perform the search
        - Keyword Usage
        - ``XIQSE Firmware Clear Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        clear_btn = self.get_search_clear_button()
        search_text = self.get_search_text_field()
        if clear_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Clear button")
                self.auto_actions.click(clear_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Clear button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_firmware_wait_for_search_to_complete(self, retry_duration=10, retry_count=30):
        """
        - This keyword waits for the search to complete on the Network > Firmware Tab
        - Keyword Usage
        - ``XIQSE Firmware Wait For Search To Complete``

        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for search to complete: loop {count}")
            load_mask = self.view_el.get_firmware_refresh_load_mask()
            if load_mask:
                self.utils.print_info(f"Search still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Search has completed")
                return 1
            count += 1

        self.utils.print_info("Search did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_firmware_perform_search(self, value, retry_duration=10, retry_count=30):
        """
        - This keyword performs a search on the Network > Firmware Tab
        - Keyword Usage
        - ``XIQSE Firmware Perform Search   My Search String``
        - ``XIQSE Firmware Perform Search   My Search String  retry_duration=5  retry_count=10``

        :param value:          string to search for
        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_firmware_open_search() == 1:
            if self.xiqse_firmware_enter_search_text(value) == 1:
                if self.xiqse_firmware_trigger_search() == 1:
                    if self.xiqse_firmware_wait_for_search_to_complete(retry_duration, retry_count) == 1:
                        ret_val = 1
                        self.utils.print_info(f"Completed search for {value}")

        if ret_val == -1:
            self.utils.print_info(f"Unable to perform search for {value}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_firmware_with_text(self, value):
        """
        - Searches for firmware containing the specified value

        :param value: Value to search for in the firmware row
        :return: return 1 if firmware with specified value is found, else -1
        """
        ret_val = -1

        sleep(5)
        rows = self.get_table_rows()
        if rows:
            for row in rows:
                self.utils.print_info(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if value in row.text:
                    self.utils.print_info(f"Found firmware with value '{value}'")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find firmware with value '{value}'")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not obtain rows from Firmware table")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_firmware_image_filename(self, firmware_image_filename):
        """
        - This keyword selects the specified firmware image.
        - It is assumed the user is already on the Network > Firmware tab.
        - Keyword Usage
        - ``XIQSE Select Firmware Image  My_Firmware_Image_Name``

        :param firmware_image_filename: firmware image to select
        :return: 1 if action was successful, else -1
        """

        ret_val = -1
        self.utils.print_info(f"Selecting Firmware with Firmware Image Name {firmware_image_filename}")

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_table_rows()
                if rows:
                    for row in rows:
                        if firmware_image_filename in row.text:
                            self.utils.print_debug(
                                f"Found firmware image {firmware_image_filename} in row {self.xiqse_table.format_table_row(row.text)}")
                            row_selected = row.get_attribute("aria-selected")
                            if row_selected and row_selected == "true":
                                self.utils.print_info(f"Row for firmware image {firmware_image_filename} is already selected")
                            else:
                                self.utils.print_info(f"Selecting firmware image {firmware_image_filename}")
                                self.auto_actions.click(row)
                            ret_val = 1
                            break
                    break
                else:
                    self.utils.print_info("Did not find any rows in table")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to select firmware image {firmware_image_filename}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_click_firmware_refresh_button(self):
        """
        - This keyword refreshes the uploaded firmware images by selecting "Refresh Images..." from the Firmware Page.
        - It assumes the Network > Firmware tab is already open.
        - Keyword Usage:
        - ``XIQSE Click Refresh Images``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        refresh_images = self.get_firmware_refresh_button()
        if refresh_images:
            self.utils.print_info("Clicking 'Refresh Images...' button")
            self.auto_actions.click(refresh_images)
            ret_val = self.xiqse_wait_for_firmware_refresh_to_complete()
        else:
            self.utils.print_info("Unable to find 'Refresh Images...' button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_for_firmware_refresh_to_complete(self, retry_duration=10, retry_count=30):
        """
        - This keyword waits for the "Firmware Refresh" loading mask to complete before continuing
        - Keyword Usage
        - ''XIQSE Wait For Firmware Refresh to Complete''
        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Image Refresh to complete: loop {count}")
            stale_retry = 1
            while stale_retry <= 10:
                try:
                    load_mask = self.view_el.get_firmware_refresh_load_mask()
                    if load_mask:
                        self.utils.print_info(f"Refresh still in progress")
                        sleep(retry_duration)
                    else:
                        self.utils.print_info(f"Refresh has completed")
                        return 1
                    # Break out of stale element loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1
            count += 1

        self.utils.print_info("Refresh did not complete within specified time")
        self.screen.save_screen_shot()

        return -1

    def xiqse_assign_firmware(self):
        """
        - This keyword selects the Assign Firmware menu item of the selected firmware's context menu
        - It assumes the Firmware Image has already been selected
        - Keyword Usage:
        - 'XIQSE Assign Firmware'
        :return: 1 if action is successful, else -1
        """

        ret_val = -1

        assign_firmware = self.get_assign_firmware_menu_item()
        if assign_firmware:
            self.utils.print_info("Clicking 'Assign Firmware' menu item")
            self.auto_actions.click(assign_firmware)
        else:
            self.utils.print_info("Unable to find 'Assign Firmware' menu item")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_remove_firmware_from_group(self):
        """
        - This keyword selects the Remove Firmware from Group menu item of the selected firmware's context menu
        - It assumes the Firmware Image has already been selected
        - Keyword Usage:
        - 'XIQSE Remove Firmware From Group'
        :return: 1 if action is successful, else -1
        """

        ret_val = -1

        remove_firmware = self.get_remove_firmware_from_group_menu_item()
        if remove_firmware:
            self.utils.print_info("Clicking 'Remove Firmware from Group' menu item")
            self.auto_actions.click(remove_firmware)
        else:
            self.utils.print_info("Unable to find 'Remove Firmware from Group' menu item")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_as_reference_image(self):
        """
        - This keyword selects the Set As Reference Image menu item of the selected firmware's context menu
        - It assumes the Firmware Image has already been selected
        - Keyword Usage:
        - 'XIQSE Set As Reference Image'
        :return: 1 if action is successful, else -1
        """

        ret_val = -1

        set_reference = self.get_set_as_reference_image_menu_item()
        if set_reference:
            self.utils.print_info("Clicking 'Set As Reference Image' menu item")
            self.auto_actions.click(set_reference)
        else:
            self.utils.print_info("Unable to find 'Set As Reference Image' menu item")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_unset_as_reference_image(self):
        """
        - This keyword selects the Unset As Reference Image menu item of the selected firmware's context menu
        - It assumes the Firmware Image has already been selected
        - Keyword Usage:
        - 'XIQSE Unset As Reference Image'
        :return: 1 if action is successful, else -1
        """

        ret_val = -1

        unset_reference = self.get_unset_as_reference_image_menu_item()
        if unset_reference:
            self.utils.print_info("Clicking 'Unset As Reference Image' menu item")
            self.auto_actions.click(unset_reference)
        else:
            self.utils.print_info("Unable to find 'Unset As Reference Image' menu item")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_image(self):
        """
        - This keyword selects the Delete Image menu item of the selected firmware's context menu
        - It assumes the Firmware Image has already been selected
        - Keyword Usage:
        - 'XIQSE Delete Image'
        :return: 1 if action is successful, else -1
        """

        ret_val = -1

        delete_image = self.get_delete_image_menu_item()
        if delete_image:
            self.utils.print_info("Clicking 'Delete Image' menu item")
            self.auto_actions.click(delete_image)
        else:
            self.utils.print_info("Unable to find 'Delete Image' menu item")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_open_firmware_context_menu(self, firmware_image_filename):
        """
        - This keyword right-clicks the specified firmware image.
        - It is assumed the user is already on the Network > Firmware tab.
        - Keyword Usage
        - ``XIQSE Right-Click Firmware Image  My_Firmware_Image_Name``

        :param firmware_image_filename: firmware image to select
        :return: 1 if action was successful, else -1
        """

        ret_val = -1
        self.utils.print_info(f"Opening Context Menu of Firmware Image Name {firmware_image_filename}")

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_table_rows()
                if rows:
                    for row in rows:
                        if firmware_image_filename in row.text:
                            self.utils.print_debug(
                                f"Found firmware image {firmware_image_filename} in row {self.xiqse_table.format_table_row(row.text)}")
                            row_selected = row.get_attribute("aria-selected")
                            if row_selected and row_selected == "true":
                                self.utils.print_info(f"Row for firmware image {firmware_image_filename} is already selected")
                            else:
                                self.utils.print_info(f"Opening context menu of firmware image {firmware_image_filename}")
                                self.auto_actions.right_click(row)
                            ret_val = 1
                            break
                    break
                else:
                    self.utils.print_info("Did not find any rows in table")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to open context menu of {firmware_image_filename}")
            self.screen.save_screen_shot()
        return ret_val
