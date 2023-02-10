from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsDeleteCredWebElementsDefinitions import AdminProfilesSNMPCredentialsDeleteCredWebElementsDefinitions


class AdminProfilesSNMPCredentialsDeleteCredWebElements(AdminProfilesSNMPCredentialsDeleteCredWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_confirm_delete_snmp_credential_dialog(self):
        """
        :return: Confirm Delete SNMP Credential dialog
        """
        return self.weh.get_element(self.confirm_delete_snmp_credential_dialog)

    def get_delete_snmp_credential_confirm_dialog_yes_button(self):
        """
        :return: 'Yes' button in the Confirm Delete SNMP Credential dialog
        """
        return self.weh.get_element(self.delete_snmp_credential_confirm_dialog_yes_button)

    def get_delete_snmp_credential_confirm_dialog_no_button(self):
        """
        :return: 'No' button in the Confirm Delete SNMP Credential dialog
        """
        return self.weh.get_element(self.delete_snmp_credential_confirm_dialog_no_button)
