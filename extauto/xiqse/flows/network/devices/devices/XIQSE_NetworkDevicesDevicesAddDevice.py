from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesAddDeviceWebElements import NetworkDevicesDevicesAddDeviceWebElements


class XIQSE_NetworkDevicesDevicesAddDevice(NetworkDevicesDevicesAddDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_add_device_dialog_set_ip(self, the_value):
        """
         - This keyword sets the IP Address value in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Set IP  ${IP}``

        :param the_value:  IP address value to enter in the Add Device dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        ip_field = self.get_ip_field()
        if ip_field:
            self.utils.print_info(f"Entering IP Address {the_value}")
            self.auto_actions.send_keys(ip_field, the_value)
        else:
            self.utils.print_info("Could not find IP Address field in Add Device dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_device_dialog_select_profile(self, the_value):
        """
         - This keyword sets the IP Address value in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Select Profile  public_v2_Profile``

        :param the_value:  profile value to select in the Add Device dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_profile_dropdown()
        if the_field:
            self.utils.print_info("Opening Profile dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_div_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected profile {the_value} in the Profile dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find profile {the_value} in the Profile dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Profile dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find Profile field in Add Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_device_dialog_set_nickname(self, the_value):
        """
         - This keyword sets the Nickname value in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Set Nickname  ${device_nickname}``

        :param the_value:  nickname value to enter in the Add Device dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if the_value != "":
            nickname_field = self.get_nickname_field()
            if nickname_field:
                self.utils.print_info(f"Entering Nickname {the_value}")
                self.auto_actions.send_keys(nickname_field, the_value)
            else:
                self.utils.print_info("Could not find Nickname field in Add Device dialog")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_debug("Nickname not specified")

        return ret_val

    def xiqse_add_device_dialog_set_poll_status_only(self, the_value="true"):
        """
         - This keyword sets the value of the Poll Status Only checkbox in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Set Poll Status Only``
          - ``XIQSE Add Device Dialog Set Poll Status Only  true``
          - ``XIQSE Add Device Dialog Set Poll Status Only  false``

        :param the_value:  true/false to indicate if the checkbox should be selected or not
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        status_only_cb = self.get_status_only_checkbox()
        if status_only_cb:
            if the_value.lower() == "true":
                self.utils.print_info("Selecting Poll Status Only check box")
                self.auto_actions.enable_check_box(status_only_cb)
            else:
                self.utils.print_info("Deselecting Poll Status Only check box")
                self.auto_actions.disable_check_box(status_only_cb)
        else:
            self.utils.print_info("Could not find Poll Status Only checkbox in Add Device dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_device_dialog_click_ok(self):
        """
         - This keyword clicks OK in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        ok_btn = self.get_ok_button()
        if ok_btn:
            ok_disabled = ok_btn.get_attribute("aria-disabled")
            if ok_disabled and ok_disabled == "true":
                ret_val = -1  # Assume this is an error case

                # If button is disabled, see if it's because the device already exists
                self.utils.print_info("OK button is disabled")
                ip_field = self.get_ip_field()
                if ip_field:
                    ip_qtip = ip_field.get_attribute("data-errorqtip")
                    if ip_qtip:
                        self.utils.print_info(f"IP Address Field Error Message: '{ip_qtip}'")
                        if "A device with this address exists" in ip_qtip:
                            ret_val = 1  # Device already exists so this is not an error
                            self.utils.print_info("Device already exists")
                            self.xiqse_add_device_dialog_click_close()
            else:
                self.utils.print_info("Clicking OK button")
                self.auto_actions.click(ok_btn)
        else:
            self.utils.print_info("Could not find OK button in Add Device dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_device_dialog_click_close(self):
        """
         - This keyword clicks Close in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Click Close``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        close_btn = self.get_close_button()
        if close_btn:
            self.utils.print_info("Clicking Close button")
            self.auto_actions.click(close_btn)
        else:
            self.utils.print_info("Could not find Close button in Add Device dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
