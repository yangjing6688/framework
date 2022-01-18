from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.archives.NetworkArchivesCreateArchiveWebElements import NetworkArchivesCreateArchiveWebElements


class XIQSE_NetworkArchivesCreateArchive(NetworkArchivesCreateArchiveWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_archives_create_dialog_enter_name(self, value):
        """
         - This keyword populates the Name field of the Create Archive dialog
         - It is assumed the Create Archive dialog is already open.
         - Keyword Usage
          - ``XIQSE Archives Create Enter Name  MY_ARCHIVE``

        :param value: name of the archive to create
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_field = self.get_create_name_field()
        if the_field:
            self.utils.print_info(f"Entering Name {value}")
            self.auto_actions.send_keys(the_field, value)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Name field")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_dialog_expand_all_devices(self):
        """
         - This keyword expands the All Devices node in the Select Devices tree of the Create Archive dialog
         - It is assumed the Create Archive dialog is already open and on the device selection page.
         - Keyword Usage
          - ``XIQSE Archives Create Expand All Devices``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.get_create_select_device_expand_node("All Devices")
        if the_node:
            self.utils.print_info("Expanding All Devices")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the expander icon for All Devices")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_dialog_move_device_to_archive_members(self, ip):
        """
         - This keyword moves the specified device in the Select Devices tree of the Create Archive dialog to
         - the Archive Members list.
         - It is assumed the Create Archive dialog is already open and on the device selection page.
         - Keyword Usage
          - ``XIQSE Archives Create Move Device to Archive Members    1.2.3.4``

        :param ip: IP address of the device to select and move to the Archive Members list
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.get_create_select_device_node(ip)
        if the_node:
            self.utils.print_info(f"Double clicking {ip} to move to Archive Members list")
            self.auto_actions.double_click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to find {ip} in the Select Devices tree")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_dialog_select_device_and_move_to_archive_members(self, ip):
        """
         - This keyword selects the specified device in the Create Archive dialog and moves it to the
         - Archive Members list.
         - It is assumed the Create Archive dialog is already open and on the device selection page.
         - Keyword Usage
          - ``XIQSE Archives Create Select Device and Move to Archive Members    1.2.3.4``

        :param ip: IP address of the device to select and move to the Archive Members list
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_archives_create_dialog_expand_all_devices():
            if self.xiqse_archives_create_dialog_move_device_to_archive_members(ip):
                self.utils.print_info(f"Moved {ip} to Archive Members list")
                sleep(3)
                ret_val = 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to move {ip} to Archive Members list")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_archives_create_dialog_select_frequency(self, the_value):
        """
         - This keyword selects the value in the Frequency dropdown of the Create Archive dialog.
         - It is assumed the Create Archive dialog is already open and on the page containing the Frequency field.
         - Keyword Usage
          - ``XIQSE Archives Create Dialog Select Frequency    Daily``
          - ``XIQSE Archives Create Dialog Select Frequency    Never``
          - ``XIQSE Archives Create Dialog Select Frequency    Now``
          - ``XIQSE Archives Create Dialog Select Frequency    On Startup``
          - ``XIQSE Archives Create Dialog Select Frequency    Once``
          - ``XIQSE Archives Create Dialog Select Frequency    Weekly``

        :param the_value: frequency to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_create_frequency_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Frequency dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Frequency items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Frequency dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Frequency dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Frequency dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Frequency dropdown in the Create Archive dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_archives_create_dialog_click_next(self):
        """
         - This keyword clicks Next in the Create Archive dialog
         - It is assumed the Create Archive dialog is already open.
         - Keyword Usage
          - ``XIQSE Archives Create Click Next``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_btn = self.get_create_next_button()
        if the_btn:
            is_disabled = the_btn.get_attribute("aria-disabled")
            self.utils.print_debug(f"IS DISABLED? {is_disabled}")
            if is_disabled is None or is_disabled == "false":
                self.utils.print_info("Clicking Next Button")
                self.auto_actions.click(the_btn)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Next button is disabled")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Next button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_dialog_click_finish(self):
        """
         - This keyword clicks Finish in the Create Archive dialog
         - It is assumed the Create Archive dialog is already open.
         - Keyword Usage
          - ``XIQSE Archives Create Click Finish``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_btn = self.get_create_finish_button()
        if the_btn:
            is_disabled = the_btn.get_attribute("aria-disabled")
            self.utils.print_debug(f"IS DISABLED? {is_disabled}")
            if is_disabled is None or is_disabled == "false":
                self.utils.print_info("Clicking Finish Button")
                self.auto_actions.click(the_btn)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Finish button is disabled")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Finish button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Create Archive dialog
         - It is assumed the Create Archive dialog is already open.
         - Keyword Usage
          - ``XIQSE Archives Create Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_btn = self.get_create_cancel_button()
        if the_btn:
            self.utils.print_info("Clicking Cancel Button")
            self.auto_actions.click(the_btn)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Cancel button")
            self.screen.save_screen_shot()
        return ret_val
