from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainAssignDeviceWebElements import ControlPolicyDomainAssignDeviceWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave import XIQSE_ControlPolicyDomainSave
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu


class XIQSE_ControlPolicyDomainAssignDevice(ControlPolicyDomainAssignDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_domain_els = XIQSE_ControlPolicyDomainOpenManageMenu()
        self.save_domain_els = XIQSE_ControlPolicyDomainSave()

    def xiqse_control_policy_assign_device_to_domain(self, device_ip):
        """
         - This keyword adds a device to the current policy domain
         - It is assumed that:
         -     the Assign Device(s) to Domain window is already open. This window can be launched from either the
         -         Open/Manage Domains menu, or popup menu from the Devices tree view.
         -     the device is already created on XIQ-SE,
         -     the Devices tree displays the devices with IP addresses (not nickname nor sysName)
         - Keyword Usage
         -     xiqse control policy assign device to domain    <device_ip>

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Actions in the Assign Device(s) to Domain process
        #select_device = self._select_device(device_ip)
        #add_device = self._click_add_button()
        #click_ok = self._click_ok_button()

        # Verify that the Assign Device(s) to Domain window is launched successfully
        assign_window = self.openmanage_domain_els.get_assign_devices_to_domain_menu()
        if assign_window:
            if self._select_device(device_ip) == 1:
                if self._click_add_button() == 1:
                    if self._click_ok_button() == 1:
                        # Save domain
                        # If not saved, then the "cache" dialog will popup which will mess up the logout procedure
                        self.save_domain_els.xiqse_control_policy_save_domain()
                        ret_val = 1
        else:
            self.utils.print_info("'Assign Device(s) to Domain' window is not launched successfully.")

        return ret_val

    def _select_device(self, device_ip):
        """
        - Select the device in the Assign Device(s) in Domain window.
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        all_devices = self.get_assign_all_devices_node()
        if all_devices:
            self.utils.print_info("Expanding the 'All Devices' node in the Devices tree (left panel).")
            self.auto_actions.click(all_devices)
            device_els = self.get_assign_find_device(device_ip)
            if device_els:
                self.utils.print_info(f"Selecting the device {device_ip} in the left panel")
                self.auto_actions.click(device_els)
                # need this delay to give enough time for the ">" button to become active after selecting device
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info(f"Device '{device_ip}' is either not created in XIQ-SE, an unsupported Policy Mgr device, "
                                      "or it is already added to the current Policy domain.")
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.get_assign_cancel_button)
        else:
            self.utils.print_info("Unable to locate 'All Devices' node in the Devices tree "
                                  "in Assign Device(s) to Domain window.")

        return ret_val

    def _click_add_button(self):
        """
        - Click Add (or '>') button in the Assign Device(s) to Domain window.
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_bttn = self.get_assign_add_button()
        if add_bttn:
            add_disabled = add_bttn.get_attribute("aria-disabled")
            if add_disabled == 'true':
                self.utils.print_info("The Add (or '>') button is disabled in the Assign Device(s) to Domain window.")
                # Close the Assign Device(s) to Domain window
                self.auto_actions.click_reference(self.get_assign_cancel_button)
            else:
                self.utils.print_info("clicking Add (or '>') button in the Assign Device(s) to Domain window.")
                self.auto_actions.click(add_bttn)
                sleep(2)
                ret_val = 1
        else:
            self.utils.print_info("Unable to locate the Add (or '>') button in Assign Device(s) to Domain window.")

        return ret_val

    def _click_ok_button(self):
        """
        - Click the OK button in the "Assign Device(s) to Domain" window
        :param self:
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        ok_bttn = self.get_assign_ok_button()
        if ok_bttn:
            self.utils.print_info("Clicking OK button in the Assign Device(s) to Domain window")
            self.auto_actions.click(ok_bttn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to locate OK button in the Assign Device(s) to Domain window")
            self.screen.save_screen_shot()
        return ret_val