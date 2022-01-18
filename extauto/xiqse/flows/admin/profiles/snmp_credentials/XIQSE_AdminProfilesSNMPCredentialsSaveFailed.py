from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsSaveFailedWebElements import AdminProfilesSNMPCredentialsSaveFailedWebElements


class XIQSE_AdminProfilesSNMPCredentialsSaveFailed(AdminProfilesSNMPCredentialsSaveFailedWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_save_failed_dialog_handle_failure(self):
        """
         - This keyword handles a failure saving a credential in the Add SNMP Credential dialog.
         - Keyword Usage
          - ``XIQSE Save Failed Dialog Handle Failure``

        :return: 1 if no failure occurred, 2 if the failure is due to the entry already existing, else -1
        """
        ret_val = 1

        # Check for errors saving the credential
        error_dlg = self.get_add_snmp_credential_save_failed_dialog()
        if error_dlg:
            error_hidden = error_dlg.get_attribute("aria-hidden")
            if error_hidden == "false":
                ret_val = -1

                # Get the error message
                error_msg = self.get_add_snmp_credential_save_failed_dialog_message()
                if error_msg:
                    error_text = error_msg.text
                    self.utils.print_info(f"Save Failed: {error_text}")
                    if "is already in use" in error_text:
                        # Ignore error if it is just that the credential already exists
                        ret_val = 2

                # Close the error dialog
                error_ok_btn = self.get_add_snmp_credential_save_failed_dialog_ok_button()
                if error_ok_btn:
                    self.utils.print_info("Clicking OK to close error dialog")
                    self.auto_actions.click(error_ok_btn)
                else:
                    self.utils.print_info("Could not find OK button to close error dialog")
                    self.screen.save_screen_shot()

        return ret_val
