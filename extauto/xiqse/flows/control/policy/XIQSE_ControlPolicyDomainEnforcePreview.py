from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainEnforcePreviewWebElements import ControlPolicyDomainEnforcePreviewWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu


class XIQSE_ControlPolicyDomainEnforcePreview(ControlPolicyDomainEnforcePreviewWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_els = XIQSE_ControlPolicyDomainOpenManageMenu()


    def xiqse_control_policy_enforce_preview_show_on_enforce_setting(self):
        """
        - Check for the "Show on enforce" checkbox setting:
        -        checked = show Enforce Preview window during the Enforce Domain process
        -    not-checked = do NOT show the Enforce Preview window during the Enforce Domain process
        - NOTE: it looks like the checkbox is always checked every time XIQ-SE client is launched by the automation.
        -       I tried to uncheck it, and it is still checked on the next launch.
        -       this checkbox setting is per user, and it looks like automation uses a new-user for every launch.
        :return:  1 if checkbox is checked.  -1 if checkbox is not checked
        """
        ret_val = -1

        # Launch the Enforce Preview window
        self.openmanage_els.xiqse_control_policy_select_enforce_preview_menu()

        if self.get_show_on_enforce_checkbox():
            self.utils.print_info("'Show on Enforce' checkbox is currently checked in Enforce Preview window.")
            ret_val = 1
        else:
            self.utils.print_info("'Show on Enforce' checkbox is currently NOT checked in Enforce Preview window.")

        # close the Enforce Preview window
        self.get_enforce_preview_close_button()

        return ret_val

    def click_enforce_button(self):
        """
        - Click the "Enforce" button.

        :return:  1 if button is clicked, else -1
        """
        ret_val = -1

        enforce_bttn = self.get_enforce_preview_enforce_button()
        if enforce_bttn:
            self.utils.print_info("Clicking 'Enforce' button in the Enforce Preview window")
            self.auto_actions.click(enforce_bttn)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find the 'Enforce' button in the Enforce Preview window")
        return ret_val