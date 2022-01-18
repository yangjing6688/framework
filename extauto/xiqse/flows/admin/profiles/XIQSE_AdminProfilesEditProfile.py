from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.admin.profiles.AdminProfilesAddProfileWebElements import AdminProfilesAddProfileWebElements
from xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed import XIQSE_AdminProfilesSaveFailed


# This class uses the Add Profile web elements, as they are the same
class XIQSE_AdminProfilesEditProfile(AdminProfilesAddProfileWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.save_failed_dlg = XIQSE_AdminProfilesSaveFailed()

    def xiqse_edit_profile_dialog_select_read(self, the_value):
        """
         - This keyword selects the Read value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Select Read    public_v1``

        :param the_value: value to select in the Read field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_read_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Read dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Read items count is {len(the_items)}")
                self.utils.print_info("Opening the Read dropdown")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Read dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Read dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Read dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Read dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_write(self, the_value):
        """
         - This keyword selects the Write value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Select Write    public_v1``

        :param the_value: value to select in the Write field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_write_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Write dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Write items count is {len(the_items)}")
                self.utils.print_info("Opening the Write dropdown")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Write dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Write dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Write dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Write dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_max_access(self, the_value):
        """
         - This keyword selects the Max Access value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Select Max Access    public_v1``

        :param the_value: value to select in the Max Access field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_max_access_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Max Access dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Max Access items count is {len(the_items)}")
                self.utils.print_info("Opening the Max Access dropdown")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Max Access dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Max Access dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Max Access dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Max Access dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_read_security(self, the_value):
        """
         - This keyword selects the Read Security value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Read Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Read Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Read Security   AuthPriv``

        :param the_value: value to select in the Read Securityfield
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_read_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Read Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_info(f"Read Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Read Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Read Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Read Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Read Security dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_write_security(self, the_value):
        """
         - This keyword selects the Write Security value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Write Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Write Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Write Security   AuthPriv``

        :param the_value: value to select in the Write Security field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_write_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Write Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Write Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Write Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Write Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Write Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Write Security dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_max_security(self, the_value):
        """
         - This keyword selects the Max Security value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Max Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Max Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Max Security   AuthPriv``

        :param the_value: value to select in the Max Security field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_max_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Max Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Max Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Max Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Max Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Max Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Max Security dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_select_cli(self, the_value):
        """
         - This keyword selects the CLI Credential value in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Select CLI    Default``

        :param the_value: value to select in the CLI Credential field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_cli_dropdown()
        if the_field:
            self.utils.print_info("Clicking the CLI Credential dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"CLI Credentials items count is {len(the_items)}")
                self.utils.print_info("Opening the CLI Credentials dropdown")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the CLI Credentials dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the CLI Credentials dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the CLI Credentials dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the CLI Credentials dropdown in Edit Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile_dialog_click_save(self):
        """
         - This keyword clicks Save in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Click Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        save_btn = self.get_add_profile_dialog_save_button()
        if save_btn:
            save_disabled = save_btn.get_attribute("aria-disabled")
            if save_disabled and save_disabled == "true":
                self.utils.print_info("Save button is disabled - nothing changed - clicking Cancel to close dialog")
                self.xiqse_edit_profile_dialog_click_cancel()
            else:
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(save_btn)
                sleep(2)

                ret_val = self.save_failed_dlg.xiqse_save_failed_dialog_handle_failure()
                if ret_val != 1:
                    # A failure of some type occurred so we need to close the Edit Profile dialog
                    self.screen.save_screen_shot()
                    self.xiqse_edit_profile_dialog_click_cancel()

                    # if the failure was due to the item already existing, set the return value to 1
                    if ret_val == 2:
                        ret_val = 1
        else:
            self.utils.print_info("Could not find Save button in Edit Profile dialog")
            self.screen.save_screen_shot()
            self.xiqse_edit_profile_dialog_click_cancel()
            ret_val = -1

        return ret_val

    def xiqse_edit_profile_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Edit Profile dialog.
         - It is assumed the Edit Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Edit Profile Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_add_profile_dialog_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Edit Profile dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
