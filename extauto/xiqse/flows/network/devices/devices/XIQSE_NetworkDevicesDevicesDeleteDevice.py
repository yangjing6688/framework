from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesDeleteDeviceWebElements import NetworkDevicesDevicesDeleteDeviceWebElements


class XIQSE_NetworkDevicesDevicesDeleteDevice(NetworkDevicesDevicesDeleteDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_confirm_delete_device_click_yes(self):
        """
         - This keyword clicks Yes in the Confirm Delete dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Confirm Delete Device Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        yes_btn = self.get_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' in Confirm Delete dialog")
            self.auto_actions.click(yes_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Yes' button in Confirm Delete dialog")
            self.screen.save_screen_shot()
            self.xiqse_confirm_delete_device_click_no()

        return ret_val

    def xiqse_confirm_delete_device_click_no(self):
        """
         - This keyword clicks No in the Confirm Delete dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Confirm Delete Device Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        no_btn = self.get_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' in Confirm Delete dialog")
            self.auto_actions.click(no_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'No' button in Confirm Delete dialog")
            self.screen.save_screen_shot()

        return ret_val
