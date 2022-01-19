from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.site.vrf_vlan.NetworkDevicesSiteVrfVlanWebElements import NetworkDevicesSiteVrfVlanWebElements
from xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscover import XIQSE_NetworkDevicesSiteDiscover
from xiqse.flows.network.devices.site.actions.XIQSE_NetworkDevicesSiteActions import XIQSE_NetworkDevicesSiteActions
from xiqse.flows.common.XIQSE_CommonOperationsPanel import XIQSE_CommonOperationsPanel


class XIQSE_NetworkDevicesSiteVrfVlan(NetworkDevicesSiteVrfVlanWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_site_create_vlan(self, name, vid="2"):
        """
         - This keyword creates a new VLAN in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Site Create VLAN  test_vlan_1``
          - ``XIQSE Site Create VLAN  test_vlan_1  2 ``
        :param name: value to enter in the VLAN Name field
        :param id: value to select for the VLAN VID field 
        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        add_btn = self.get_vlan_add_button()
        if add_btn:
            self.utils.print_info("Clicking 'Add...' toolbar button")
            self.auto_actions.click(add_btn)
            sleep(1)

            # Enter VLAN Name
            name_field = self.get_vlan_add_name_field()
            if name_field:
                self.utils.print_info(f"Entering VLAN Name '{name}'")
                self.auto_actions.send_keys(name_field, name)
            else:
                self.utils.print_info("Could not find VLAN Name field in Add VLAN dialog")
                self.screen.save_screen_shot()
                ret_val = -1

            # Enter VLAN VID
            vid_field = self.get_vlan_add_vid_field()
            if vid_field:
                self.utils.print_info(f"Entering VLAN VID '{vid}'")
                self.auto_actions.send_keys(vid_field, vid)
            else:
                self.utils.print_info("Could not find VLAN VID field in Add VLAN dialog")
                self.screen.save_screen_shot()
                ret_val = -1

            # Hit Update Button
            update_button = self.get_vlan_update_button()
            if update_button:
                update_disabled = update_button.get_attribute("aria-disabled")
                if update_disabled and update_disabled == "true":
                    self.utils.print_info("Update button is disabled")
                    self.screen.save_screen_shot()
                    self.xiqse_site_cancel_vlan()
                    ret_val = -1
                else:
                    self.utils.print_info("Clicking Update button")
                    self.auto_actions.click(update_button)
                    ret_val = 1
                    sleep(2)
            else:
                self.utils.print_info("Could not find Update button in Add VLAN row edit")
                self.screen.save_screen_shot()
                self.xiqse_site_cancel_vlan()
                ret_val = -1
        else:
            self.utils.print_info("Unable to find Add VLAN toolbar button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_cancel_vlan(self):
        """
         - This keyword clicks Cancel in the VLAN row editor.
         - It is assumed the VLAN row editor is open.
         - Keyword Usage
          - ``XIQSE Site Cancel VLAN``
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.vlan_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in VLAN row editor")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
