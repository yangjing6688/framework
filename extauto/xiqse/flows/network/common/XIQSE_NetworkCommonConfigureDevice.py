# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.common.NetworkCommonConfigureDeviceWebElements import NetworkCommonConfigureDeviceWebElements


class XIQSE_NetworkCommonConfigureDevice(NetworkCommonConfigureDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_configure_device_dialog_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab in the Configure Device dialog.
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Select Tab    Device``
        - ``XIQSE Configure Device Dialog Select Tab    Device Annotation``
        - ``XIQSE Configure Device Dialog Select Tab    VLAN Definitions``
        - ``XIQSE Configure Device Dialog Select Tab    Ports``
        - ``XIQSE Configure Device Dialog Select Tab    ZTP+ Device Settings``
        - ``XIQSE Configure Device Dialog Select Tab    Vendor Profile``

        :param tab_name:  Name of the tab to select in the Configure Device dialog
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        if tab_name == "Device":
            the_tab = self.get_device_tab()
        elif tab_name == "Device Annotation":
            the_tab = self.get_device_annotation_tab()
        elif tab_name == "VLAN Definitions":
            the_tab = self.get_vlan_definitions_tab()
        elif tab_name == "Ports":
            the_tab = self.get_ports_tab()
        elif tab_name == "ZTP+ Device Settings":
            the_tab = self.get_ztp_plus_device_settings_tab()
        elif tab_name == "Vendor Profile":
            the_tab = self.get_vendor_profile_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab in the Configure Device dialog")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    # CONFIGURE DEVICE PANEL ACTIONS
    def xiqse_configure_device_dialog_click_cancel(self):
        """
        - This keyword clicks Cancel in the Configure Device dialog.
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Click Cancel``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        cancel_btn = self.get_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button in the Configure Device dialog")
            self.auto_actions.click(cancel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Cancel button in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_click_save(self):
        """
        - This keyword clicks Save in the Configure Device dialog.
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Click Save``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        save_check = 1
        while save_check < 10:
            self.utils.print_debug(f"Save button check - loop save_check")
            save_btn = self.get_save_button()
            if save_btn:
                if save_btn.is_displayed() and save_btn.is_enabled():
                    self.utils.print_info("Clicking Save button in the Configure Device dialog")
                    self.auto_actions.click(save_btn)
                    ret_val = 1
                    break
                else:
                    self.utils.print_info("Save button in the Configure Device dialog is not yet available to click")
            else:
                self.utils.print_info("Unable to find Save button in the Configure Device dialog")
            save_check = save_check+1
            sleep(1)

        if ret_val == -1:
            self.utils.print_info("Unable to click Save button in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val
