from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.site.discover.NetworkDevicesSiteDiscoverAddAddressWebElements import NetworkDevicesSiteDiscoverAddAddressWebElements


class XIQSE_NetworkDevicesSiteDiscoverAddAddress(NetworkDevicesSiteDiscoverAddAddressWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_discover_add_address_dialog_select_type(self, type):
        """
        - This keyword selects the Discover Type in the Add Address dialog.
        - It is assumed the Add Address dialog is already open.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Select Type    Address Range``
        - ``XIQSE Discover Add Address Dialog Select Type    Seed Address``
        - ``XIQSE Discover Add Address Dialog Select Type    Subnet``

        :param type: value to select in the Discover Type dropdown (Address Range, Seed Address, Subnet)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_address_discover_type_dropdown()
        if the_field:
            self.utils.print_info("Opening the Discover Type dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Discover Type items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, type):
                    self.utils.print_info(f"Selected {type} in the Discover Type dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {type} in the Discover Type dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Discover Type dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Discover Type dropdown in the Add Address dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_add_address_dialog_set_address_range(self, start_val, end_val):
        """
        - This keyword sets the Start Address and End Address values in the Add Address dialog.
        - It is assumed the dialog is already opened and on the Address Range discover type.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Set Address Range  ${START_IP}  ${END_IP}``

        :param start_val: Start Address value to enter in the Add Address dialog
        :param end_val:   End Address value to enter in the Add Address dialog
        :return: 1 if action was successful, else -1
        """

        ret_val = self.xiqse_discover_add_address_dialog_set_start_address(start_val)
        if ret_val != -1:
            ret_val = self.xiqse_discover_add_address_dialog_set_end_address(end_val)

        return ret_val

    def xiqse_discover_add_address_dialog_set_start_address(self, the_val):
        """
        - This keyword sets the Start Address value in the Add Address dialog.
        - It is assumed the dialog is already opened and on the Address Range discover type.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Set Start Address  ${START_IP}``

        :param the_val: Start Address value to enter in the Add Address dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        start_field = self.get_add_address_start_address_field()
        if start_field:
            self.utils.print_info(f"Entering Start Address value '{the_val}'")
            self.auto_actions.send_keys(start_field, the_val)
        else:
            self.utils.print_info("Could not find the Start Address field in the Add Address dialog")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_add_address_dialog_set_end_address(self, the_val):
        """
        - This keyword sets the End Address value in the Add Address dialog.
        - It is assumed the dialog is already opened and on the Address Range discover type.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Set End Address  ${END_IP}``

        :param the_val: End Address value to enter in the Add Address dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        end_field = self.get_add_address_end_address_field()
        if end_field:
            self.utils.print_info(f"Entering End Address value '{the_val}'")
            self.auto_actions.send_keys(end_field, the_val)
        else:
            self.utils.print_info("Could not find the End Address field in the Add Address dialog")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_add_address_dialog_set_subnet_mask(self, the_val):
        """
        - This keyword sets the Subnet/Mask value in the Add Address dialog.
        - It is assumed the dialog is already opened and on the Subnet discover type.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Set Subnet Mask  ${Subnet/Mask}``

        :param the_val: Subnet/Mask value to enter in the Add Address dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        subnet_field = self.get_add_address_subnet_mask_field()
        if subnet_field:
            self.utils.print_info(f"Entering Subnet/Mask value '{the_val}'")
            self.auto_actions.send_keys(subnet_field, the_val)
        else:
            self.utils.print_info("Could not find the Subnet/Mask field in the Add Address dialog")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_add_address_dialog_set_seed_address(self, the_val):
        """
        - This keyword sets the Seed Address value in the Add Address dialog.
        - It is assumed the dialog is already opened and on the Seed Address discover type.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Set Seed Address  ${SEED_IP}``

        :param the_val: Seed Address value to enter in the Add Address dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        seed_field = self.get_add_address_seed_address_field()
        if seed_field:
            self.utils.print_info(f"Entering Seed Address value '{the_val}'")
            self.auto_actions.send_keys(seed_field, the_val)
        else:
            self.utils.print_info("Could not find the Seed Address field in the Add Address dialog")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_add_address_dialog_click_ok(self):
        """
        - This keyword clicks the OK button in the Add Address dialog.
        - It is assumed the Add Address dialog is already open.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        ok_btn = self.get_add_address_dialog_ok_button()
        if ok_btn:
            ok_disabled = ok_btn.get_attribute("aria-disabled")
            if ok_disabled == 'true':
                self.utils.print_info("'OK' button is disabled")

                # Need to figure out what type of address this is
                sel_item = ""
                the_field = self.get_add_address_discover_type_dropdown()
                if the_field:
                    self.auto_actions.click(the_field)

                    # Obtain the dropdown items
                    the_id = self.view_el.get_dropdown_id(the_field)
                    self.utils.print_debug(f"Got dropdown ID {the_id}")
                    the_items = self.view_el.get_list_dropdown_items(the_id)
                    if the_items:
                        self.utils.print_debug(f"Discover Type items count is {len(the_items)}")
                        for item in the_items:
                            self.utils.print_info(f"Checking if '{item.text}' is selected")
                            class_attr = item.get_attribute("class")
                            if class_attr:
                                if "selected" in class_attr:
                                    self.utils.print_info(f"'{item.text}' is selected")
                                    sel_item = item.text
                                    break
                                else:
                                    self.utils.print_info(f"'{item.text}' is not selected")
                            else:
                                self.utils.print_info(f"Could not determine selection state for '{item.text}'")
                    else:
                        self.utils.print_info("Unable to obtain Discover Type dropdown items")
                        self.screen.save_screen_shot()

                    # Close the dropdown
                    self.auto_actions.click(the_field)

                # Handle the disabled OK button based on which discover type is selected
                if sel_item == "Address Range":
                    self.utils.print_info("Handle Disabled OK button for Address Range discovery type")
                    start_field = self.get_add_address_start_address_field()
                    end_field = self.get_add_address_end_address_field()
                    start_field_error = start_field.get_attribute("data-errorqtip")
                    end_field_error = end_field.get_attribute("data-errorqtip")
                    if "already in use" in end_field_error:
                        self.utils.print_info(f"Address Range already exists: {end_field_error}")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Error adding start address: '{start_field_error}'")
                        self.utils.print_info(f"Error adding end address: '{end_field_error}'")
                elif sel_item == "Subnet":
                    self.utils.print_info("Handle Disabled OK button for Subnet discovery type")
                    subnet_field = self.get_add_address_subnet_mask_field()
                    subnet_field_error = subnet_field.get_attribute("data-errorqtip")
                    if "already in use" in subnet_field_error:
                        self.utils.print_info(f"Subnet/Mask already exists: {subnet_field_error}")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Error adding subnet/mask address: {subnet_field_error}")
                        ret_val = -1
                elif sel_item == "Seed Address":
                    self.utils.print_info("Handle Disabled OK button for Seed Address discovery type")
                    seed_field = self.get_add_address_seed_address_field()
                    seed_field_error = seed_field.get_attribute("data-errorqtip")
                    if "already in use" in seed_field_error:
                        self.utils.print_info(f"Seed Address already exists: {seed_field_error}")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Error adding seed address: {seed_field_error}")
                else:
                    self.utils.print_info("Unable to determine current Discover Type value")

                # Click Cancel to close the dialog since OK is disabled
                self.utils.print_info("Clicking 'Cancel' to close Add Address dialog")
                self.xiqse_discover_add_address_dialog_click_cancel()
            else:
                self.utils.print_info("Clicking 'OK' button")
                self.auto_actions.click(ok_btn)
                ret_val = 1
        else:
            self.utils.print_info("Unable to find 'OK' button")
            self.screen.save_screen_shot()

            self.xiqse_discover_add_address_dialog_click_cancel()

        return ret_val

    def xiqse_discover_add_address_dialog_click_cancel(self):
        """
        - This keyword clicks the Cancel button in the Add Address dialog.
        - It is assumed the Add Address dialog is already open.
        - Keyword Usage
        - ``XIQSE Discover Add Address Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_add_address_dialog_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking 'Cancel' button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find 'Cancel' button")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
