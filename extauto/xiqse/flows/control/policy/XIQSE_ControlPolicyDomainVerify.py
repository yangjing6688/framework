from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainVerifyWebElements import ControlPolicyDomainVerifyWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave import XIQSE_ControlPolicyDomainSave
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu


class XIQSE_ControlPolicyDomainVerify(ControlPolicyDomainVerifyWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.policy_save = XIQSE_ControlPolicyDomainSave()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()

    def xiqse_control_policy_verify_domain(self):
        """
         - This keyword performs Verify Domain action.
         - It is assumed that:
         -     the current view is Control>Policy,
         -     the Verify action is initiated by the user, from one of these places on Policy Mgr view:
         -          * Open/Manage Domain(s) dropdown menu
         -          * popup menu from a device
         -          * dropdown menu from the lower-left corner
         -     the device(s) is already added to the current policy domain,
         - Keyword Usage
         -     xiqse control policy verify domain

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # max wait ([max_wait * 4secs(wait 1 sec, and 1 sec for each message check in each IF statement)] in seconds) for Verify action
        max_wait = 5

        # to track if Verify takes more than 20 seconds (max_wait * 4).
        loop = 0

        # There are 4 possible Verify Domain results:
        # 0. Verify hangs
        # 1. Success (all devices are green)
        # 2. Fail (some devices are red)
        # 3. Error (no devices in the current domain)

        self.utils.print_info("Verify policy domain is initiated successfully...")
        for i in range(max_wait):
            sleep(1)
            if self.get_verify_domain_success_msg():
                #1. Success (all devices are green)
                sleep(1)
                self.utils.print_info("Verify is successful!")
                verify_success_ok_bttn = self.get_verify_domain_success_ok_bttn()
                if verify_success_ok_bttn:
                    self.auto_actions.click(verify_success_ok_bttn)
                else:
                    self.utils.print_info(
                        "Cannot locate 'OK' button in the Enforce Success confirmation dialog.")
                    self.screen.save_screen_shot()
                ret_val = 1
                loop = 1
                break
            elif self.get_verify_domain_fail_msg():
                #2. Fail (some devices are red)
                self.utils.print_info("Verify failed!  Please refer to the errors/warnings in the screenshot.")
                self.screen.save_screen_shot()
                # Close the Verify Fail error dialog
                verify_fail_ok_bttn = self.get_verify_domain_fail_ok_bttn()
                if verify_fail_ok_bttn:
                    self.auto_actions.click(verify_fail_ok_bttn)
                else:
                    self.utils.print_info(
                        "Cannot locate 'OK' button in the Verify Failure dialog.")
                loop = 1
                break
            elif self.get_cannot_verify_domain_error_msg():
                #3. Verify Error dialog is detected (i.e. Cannot Verify - No devices in domain)
                self.utils.print_info("Cannot verify domain!  No device(s) exist in this domain to verify.")
                self.screen.save_screen_shot()
                # Close the Error dialog
                sleep(1)
                cannot_verify_ok_bttn = self.get_cannot_verify_domain_ok_bttn()
                if cannot_verify_ok_bttn:
                    self.auto_actions.click(cannot_verify_ok_bttn)
                else:
                    self.utils.print_info(
                        "Cannot locate 'OK' button in the Cannot Verify Error dialog.")
                loop = 1
                break
            else:
                # Enforce is still in progress
                self.utils.print_info("Verify is still in progress...")

        if (loop == 0):
            self.utils.print_info(f"Verify Domain takes more than {max_wait*4} seconds, and it is still not finished.")
            self.screen.save_screen_shot()

        return ret_val
