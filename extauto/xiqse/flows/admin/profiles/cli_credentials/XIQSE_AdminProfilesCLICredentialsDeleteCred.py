from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.cli_credentials.AdminProfilesCLICredentialsDeleteCredWebElements import AdminProfilesCLICredentialsDeleteCredWebElements


class XIQSE_AdminProfilesCLICredentialsDeleteCred(AdminProfilesCLICredentialsDeleteCredWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_delete_cli_credential_confirm_delete(self):
        """
        - This keyword confirms the CLI Credential deletion.
        - It is assumed the Confirm Delete dialog is already open.
        - Keyword Usage
        - ``XIQSE Delete CLI Credential Confirm Delete``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        confirm_dlg = self.get_confirm_delete_cli_credential_dialog()
        if confirm_dlg:
            self.xiqse_delete_cli_credential_confirm_dialog_click_yes()
        else:
            self.utils.print_info("No confirmation dialog present for Delete CLI Credential")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_cli_credential_confirm_dialog_click_yes(self):
        """
        - This keyword clicks the Yes button in the Confirm Delete dialog.
        - It is assumed the confirmation dialog for deleting the CLI Credential is already open.
        - Keyword Usage
        - ``XIQSE Delete CLI Credential Confirm Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_delete_cli_credential_confirm_dialog_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' button")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_cli_credential_confirm_dialog_click_no(self):
        """
        - This keyword clicks the No button in the Confirm Delete dialog.
        - It is assumed the confirmation dialog for deleting the CLI Credential is already open.
        - Keyword Usage
        - ``XIQSE Delete CLI Credential Confirm Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_delete_cli_credential_confirm_dialog_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find 'No' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
