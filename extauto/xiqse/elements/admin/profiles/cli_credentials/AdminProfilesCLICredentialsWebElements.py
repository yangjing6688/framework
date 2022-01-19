from extauto.common.WebElementHandler import *
from xiqse.defs.admin.profiles.cli_credentials.AdminProfilesCLICredentialsWebElementsDefinitions import *


class AdminProfilesCLICredentialsWebElements(AdminProfilesCLICredentialsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_cli_credentials_refresh_table_button(self):
        """
        :return: Refresh button element for CLI Credentials table
        """
        return self.weh.get_element(self.cli_credentials_refresh_table_button)

    def get_cli_credentials_table_rows(self):
        """
        :return: All the rows in the CLI Credentials table
        """
        return self.weh.get_elements(self.cli_credentials_table_rows)

    def get_add_cli_credential_button(self):
        """
        :return: "Add..." button element on CLI Credentials tab toolbar
        """
        return self.weh.get_element(self.cli_credential_add_button)

    def get_edit_cli_credential_button(self):
        """
        :return: "Edit..." button element on CLI Credentials tab toolbar
        """
        return self.weh.get_element(self.cli_credential_add_button)

    def get_delete_cli_credential_button(self):
        """
        :return: "Delete" button element on CLI Credentials tab toolbar
        """
        return self.weh.get_element(self.cli_credential_delete_button)
