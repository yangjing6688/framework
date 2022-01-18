from common.WebElementHandler import *
from xiqse.defs.admin.profiles.cli_credentials.AdminProfilesCLICredentialsAddCredWebElementsDefinitions import *


class AdminProfilesCLICredentialsAddCredWebElements(AdminProfilesCLICredentialsAddCredWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_cli_credential_dialog_description_field(self):
        """
        :return: 'Description' field in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_desc_field)

    def get_add_cli_credential_dialog_user_name_field(self):
        """
        :return: 'User Name' field in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_user_name_field)

    def get_add_cli_credential_dialog_type_dropdown(self):
        """
        :return: 'Type' dropdown in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_type_dropdown)

    def get_add_cli_credential_dialog_login_pwd_field(self):
        """
        :return: 'Login Password' field in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_login_pwd_field)

    def get_add_cli_credential_dialog_enable_pwd_field(self):
        """
        :return: 'Enable Password' field in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_enable_pwd_field)

    def get_add_cli_credential_dialog_config_pwd_field(self):
        """
        :return: 'Configuration Password' field in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_config_pwd_field)

    def get_add_cli_credential_dialog_cancel_button(self):
        """
        :return: 'Cancel' button in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_cancel_btn)

    def get_add_cli_credential_dialog_save_button(self):
        """
        :return: 'Save' button in the Add CLI Credential dialog
        """
        return self.weh.get_element(self.add_cli_credential_dialog_save_btn)
