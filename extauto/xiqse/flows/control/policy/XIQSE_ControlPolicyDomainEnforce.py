from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainEnforceWebElements import ControlPolicyDomainEnforceWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforcePreview import XIQSE_ControlPolicyDomainEnforcePreview



class XIQSE_ControlPolicyDomainEnforce(ControlPolicyDomainEnforceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.enforce_preview = XIQSE_ControlPolicyDomainEnforcePreview()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()

    def xiqse_control_policy_enforce_domain(self):
        """
         - This keyword performs Enforce Domain action.
         - It is assumed that:
         -     the current view is Control>Policy,
         -     the Enforce action is initiated by the user, from one of these places on Policy Mgr view:
         -          * Open/Manage Domain(s) dropdown menu
         -          * popup menu from a device
         -          * dropdown menu from the lower-left corner
         -     the device(s) is already added to the current policy domain,
         - NOTE: On every automation run, Enforce Preview window is always launched during the Enforce, even though
                 I uncheck the "Show on Enforce" checkbox in the Enforce Preview window before the automation starts.
         - Keyword Usage
         -     xiqse control policy enforce domain

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # If the domain does not have any devices in it, then the Enforce Preview will be launched, and "No Devices"
        #    dialog will popup if you try to go ahead and enforce without any devices.
        # If at least 1 device is in the domain, then a dialog will popup asking if you would like to enforce
        #    to the device(s). When this happens, dismiss this dialog box and the Enforce Preview will be launched.
        #
        if self.openmanage_menu.xiqse_control_policy_select_enforce_domain_menu():
            self.utils.print_info("Enforce is initiated successfully...")
            if self._not_empty_domain() == 1:
                # Domain has some devices in it.  Initiate the Enforce...
                ret_val = self._enforce_domain()
        else:
            self.utils.print_info("ERROR:  Cannot initiate the Enforce Domain action!")
            self.screen.save_screen_shot()

        return ret_val

    # Does the domain has at least 1 device in it??
    # if domain does not have any devices in it, then return -1
    # if domain has some devices in it, then return 1
    def _not_empty_domain(self):
        ret_val = -1
        if self.get_enforce_domain_data_question():
            self.auto_actions.click_reference(self.get_enforce_domain_data_yes_button)
            self.utils.print_info("Domain has at least 1 device in it. Continue...")
            ret_val = 1
        else:
            self.utils.print_info("No Device(s) are found in Enforce Preview window. Cancel the Enforce action.")
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.enforce_preview.get_enforce_preview_cancel_button)

        return ret_val

    # Start the Enforce action
    # if enforce is successful, return 1.  Else, returns -1
    def _enforce_domain(self):
        ret_val = -1

        # max wait time (in seconds) for the Enforce action
        max_wait = 30

        # Click Enforce button in the Enforce Preview window.
        if self.enforce_preview.click_enforce_button() == 1:
            for i in range(max_wait):
                sleep(1)
                if self.get_enforce_domain_success_msg():
                    # Enforce Success dialog is detected.
                    self.utils.print_info("Enforce is successful!")
                    success_ok_bttn = self.get_enforce_domain_success_ok_bttn()
                    if success_ok_bttn:
                        self.auto_actions.click(success_ok_bttn)
                    else:
                        self.utils.print_info("Cannot locate 'OK' button in the Enforce Success confirmation dialog.")
                        self.screen.save_screen_shot()
                    ret_val = 1
                    break
                elif self.get_enforce_domain_errors_warnings_msg():
                    # Enforce Errors/Warnings dialog is detected (i.e. Enforce failure)
                    self.utils.print_info("Enforce failed!  Please refer to the errors/warnings in the screenshot.")
                    self.screen.save_screen_shot()
                    # Close the Errors/Warnings dialog
                    fail_ok_bttn = self.get_enforce_domain_errors_warnings_ok_bttn()
                    if fail_ok_bttn:
                        self.auto_actions.click(fail_ok_bttn)
                    else:
                        self.utils.print_info(
                            "Cannot locate 'OK' button in the Enforce Failure message dialog.")
                        self.screen.save_screen_shot()
                    break
                else:
                    # Enforce is still in progress
                    self.utils.print_info("Enforce is still in progress...")
        else:
            self.utils.print_info(f"Enforce Domain takes more than {max_wait} seconds, and it is still not finished.")
            self.screen.save_screen_shot()

        return ret_val