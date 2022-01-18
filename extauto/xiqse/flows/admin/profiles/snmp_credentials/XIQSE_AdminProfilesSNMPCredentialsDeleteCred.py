from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsDeleteCredWebElements import AdminProfilesSNMPCredentialsDeleteCredWebElements


class XIQSE_AdminProfilesSNMPCredentialsDeleteCred(AdminProfilesSNMPCredentialsDeleteCredWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_delete_snmp_credential_confirm_delete(self):
        """
         - This keyword confirms the SNMP Credential deletion.
         - It is assumed the Confirm Delete dialog is already open.
         - Keyword Usage
          - ``XIQSE Delete SNMP Credential Confirm Delete``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        confirm_dlg = self.get_confirm_delete_snmp_credential_dialog()
        if confirm_dlg:
            self.xiqse_delete_snmp_credential_confirm_dialog_click_yes()
        else:
            self.utils.print_info("No confirmation dialog present for Delete SNMP Credential")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_snmp_credential_confirm_dialog_click_yes(self):
        """
         - This keyword clicks the Yes button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the SNMP Credential is already open.
         - Keyword Usage
          - ``XIQSE Delete SNMP Credential Confirm Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_delete_snmp_credential_confirm_dialog_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' button")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_snmp_credential_confirm_dialog_click_no(self):
        """
         - This keyword clicks the No button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the SNMP Credential is already open.
         - Keyword Usage
          - ``XIQSE Delete SNMP Credential Confirm Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_delete_snmp_credential_confirm_dialog_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find 'No' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
