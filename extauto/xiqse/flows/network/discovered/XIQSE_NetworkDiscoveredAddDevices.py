from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.discovered.NetworkDiscoveredAddDevicesWebElements import NetworkDiscoveredAddDevicesWebElements


class XIQSE_NetworkDiscoveredAddDevices(NetworkDiscoveredAddDevicesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_discovered_add_devices_dialog_click_add(self):
        """
         - This keyword clicks 'Add' in the Add Device dialog.
         - Keyword Usage
          - ``XIQSE Discovered Add Devices Dialog Click Add``

        :return:   1 if action was successful, else -1
        """
        ret_val = -1

        add_dlg_btn = self.get_add_button()
        if add_dlg_btn:
            self.utils.print_info("Clicking Add button in Add Devices dialog")
            self.auto_actions.click(add_dlg_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Add button in Add Devices dialog")
            self.screen.save_screen_shot()

        return ret_val
