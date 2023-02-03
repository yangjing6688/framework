from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsAddCredWebElementsDefinitions import AdminProfilesSNMPCredentialsAddCredWebElementsDefinitions


class AdminProfilesSNMPCredentialsAddCredWebElements(AdminProfilesSNMPCredentialsAddCredWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_snmp_credential_dialog_name_field(self):
        """
        :return: 'Credential Name' field in the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_name_field)

    def get_add_snmp_credential_dialog_version_dropdown(self):
        """
        :return: 'SNMP Version' dropdown in the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_version_dropdown)

    def get_add_snmp_credential_dialog_community_field(self):
        """
        :return: 'Community Name' field in the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_community_field)

    def get_add_snmp_credential_dialog_user_name_field(self):
        """
        :return: 'User Name' field in the Add SNMP Credential dialog for SNMPv3 version
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_user_name_field)

    def get_add_snmp_credential_dialog_auth_type_dropdown(self):
        """
        :return: 'Authentication Type' dropdown in the Add SNMP Credential dialog for SNMPv3 version
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_auth_type_dropdown)

    def get_add_snmp_credential_dialog_auth_pwd_field(self):
        """
        :return: 'Authentication Password' field in the Add SNMP Credential dialog for SNMPv3 version
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_auth_pwd_field)

    def get_add_snmp_credential_dialog_privacy_type_dropdown(self):
        """
        :return: 'Privacy Type' dropdown in the Add SNMP Credential dialog for SNMPv3 version
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_privacy_type_dropdown)

    def get_add_snmp_credential_dialog_privacy_pwd_field(self):
        """
        :return: 'Privacy Password' field in the Add SNMP Credential dialog for SNMPv3 version
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_privacy_pwd_field)

    def get_add_snmp_credential_dialog_cancel_button(self):
        """
        :return: 'Cancel' button in the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_cancel_btn)

    def get_add_snmp_credential_dialog_save_button(self):
        """
        :return: 'Save' button in the Add SNMP Credential dialog
        """
        return self.weh.get_element(self.add_snmp_credential_dialog_save_btn)
