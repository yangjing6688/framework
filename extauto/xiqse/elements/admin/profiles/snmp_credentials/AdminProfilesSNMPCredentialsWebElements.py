from extauto.common.WebElementHandler import *
from xiqse.defs.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsWebElementsDefinitions import *


class AdminProfilesSNMPCredentialsWebElements(AdminProfilesSNMPCredentialsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_snmp_credentials_refresh_table_button(self):
        """
        :return: Refresh button element for SNMP Credentials table
        """
        return self.weh.get_element(self.snmp_credentials_refresh_table_button)

    def get_snmp_credentials_table_rows(self):
        """
        :return: All the rows in the SNMP Credentials table
        """
        return self.weh.get_elements(self.snmp_credentials_table_rows)

    def get_add_snmp_credential_button(self):
        """
        :return: "Add..." button element on SNMP Credentials tab toolbar
        """
        return self.weh.get_element(self.snmp_credential_add_button)

    def get_delete_snmp_credential_button(self):
        """
        :return: "Delete" button element on SNMP Credentials tab toolbar
        """
        return self.weh.get_element(self.snmp_credential_delete_button)
