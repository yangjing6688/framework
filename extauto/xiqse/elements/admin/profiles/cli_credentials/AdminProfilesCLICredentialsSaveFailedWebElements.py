from extauto.common.WebElementHandler import *
from xiqse.defs.admin.profiles.cli_credentials.AdminProfilesCLICredentialsSaveFailedWebElementsDefinitions import *


class AdminProfilesCLICredentialsSaveFailedWebElements(AdminProfilesCLICredentialsSaveFailedWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_cli_credential_save_failed_dialog(self):
        """
        :return: 'Save Failed' dialog for the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_save_failed_dialog)

    def get_add_cli_credential_save_failed_dialog_message(self):
        """
        :return: Message in the 'Save Failed' dialog for the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_save_failed_dialog_message)

    def get_add_cli_credential_save_failed_dialog_ok_button(self):
        """
        :return: OK button in the 'Save Failed' dialog for the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_save_failed_dialog_ok_button)
