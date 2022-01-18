from common.WebElementHandler import *
from xiqse.defs.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsSaveFailedWebElementsDefinitions import *


class AdminProfilesSNMPCredentialsSaveFailedWebElements(AdminProfilesSNMPCredentialsSaveFailedWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_snmp_credential_save_failed_dialog(self):
        """
        :return: 'Save Failed' dialog for the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_save_failed_dialog)

    def get_add_snmp_credential_save_failed_dialog_message(self):
        """
        :return: Message in the 'Save Failed' dialog for the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_save_failed_dialog_message)

    def get_add_snmp_credential_save_failed_dialog_ok_button(self):
        """
        :return: OK button in the 'Save Failed' dialog for the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_save_failed_dialog_ok_button)
