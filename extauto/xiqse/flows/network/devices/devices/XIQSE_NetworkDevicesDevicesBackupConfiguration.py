from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesBackupConfigurationWebElements import NetworkDevicesDevicesBackupConfigurationWebElements


class XIQSE_NetworkDevicesDevicesBackupConfiguration(NetworkDevicesDevicesBackupConfigurationWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_confirm_backup_configuration_click_yes(self):
        """
        - This keyword clicks Yes in the Backup Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Confirm Backup Configuration Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        yes_btn = self.get_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' in Backup Configuration dialog")
            self.auto_actions.click(yes_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Yes' button in Backup Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_confirm_backup_configuration_click_no(self):
        """
        - This keyword clicks No in the Backup Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Confirm Backup Configuration Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        no_btn = self.get_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' in Backup Configuration dialog")
            self.auto_actions.click(no_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'No' button in Backup Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_confirm_backup_configuration_click_ok(self):
        """
        - This keyword clicks OK in the Backup Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Confirm Backup Configuration Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        ok_btn = self.get_ok_button()
        if ok_btn:
            self.utils.print_info("Clicking 'OK' in Backup Configuration dialog")
            self.auto_actions.click(ok_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'OK' button in Backup Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val