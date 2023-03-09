from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainSaveWebElements import ControlPolicyDomainSaveWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu


class XIQSE_ControlPolicyDomainSave(ControlPolicyDomainSaveWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()

    def xiqse_control_policy_save_domain(self):
        """
        - This keyword saves the current domain by selecting "Save Domain" menu from "Open/Manage Domain(s)"
             dropdown menu and goes through the save domain process.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse control policy save domain

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        save_domain = self.openmanage_menu.xiqse_control_policy_select_save_domain_menu()
        if save_domain == 1:
            self.utils.print_info("Saving current domain...")
            for i in range(10):
                sleep(1)
                save_status = self.get_save_success_msg()
                if save_status:
                    # Save Successful message is detected
                    self.utils.print_info("Save Domain...Successful!")
                    self.auto_actions.click_reference(self.get_save_ok_bttn)
                    ret_val = 1
                    break
                else:
                    if i == 10:
                        self.utils.print_info("Save Domain is not successful - Save action takes more than 10 seconds.")
                        self.screen.save_screen_shot()
        else:
            self.utils.print_info("'Save Domain' is not initiated successfully.")
            self.screen.save_screen_shot()

        return ret_val
