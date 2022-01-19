from common.WebElementHandler import *
from xiqse.defs.admin.profiles.cli_credentials.AdminProfilesCLICredentialsDeleteCredWebElementsDefinitions import *


class AdminProfilesCLICredentialsDeleteCredWebElements(AdminProfilesCLICredentialsDeleteCredWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_confirm_delete_cli_credential_dialog(self):
        """
        :return: Confirm Delete CLI Credential dialog
        """
        return self.weh.get_element(self.confirm_delete_cli_credential_dialog)

    def get_delete_cli_credential_confirm_dialog_yes_button(self):
        """
        :return: 'Yes' button in the Confirm Delete CLI Credential dialog
        """
        return self.weh.get_element(self.delete_cli_credential_confirm_dialog_yes_button)

    def get_delete_cli_credential_confirm_dialog_no_button(self):
        """
        :return: 'No' button in the Confirm Delete CLI Credential dialog
        """
        return self.weh.get_element(self.delete_cli_credential_confirm_dialog_no_button)
