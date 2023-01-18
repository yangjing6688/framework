from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.profiles.AdminProfilesWebElementsDefinitions import AdminProfilesWebElementsDefinitions


class AdminProfilesWebElements(AdminProfilesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_snmp_credentials_tab(self):
        """
        :return: SNMP Credentials tab element
        """
        return self.weh.get_element(self.snmp_credentials_tab)

    def get_cli_credentials_tab(self):
        """
        :return: CLI Credentials tab element
        """
        return self.weh.get_element(self.cli_credentials_tab)

    def get_device_mapping_tab(self):
        """
        :return: Device Mapping tab element
        """
        return self.weh.get_element(self.device_mapping_tab)

    def get_profiles_refresh_table_button(self):
        """
        :return: Refresh button element for Profiles table
        """
        return self.weh.get_element(self.profiles_refresh_table_button)

    def get_profiles_table_rows(self):
        """
        :return: All the rows in the Profiles table
        """
        return self.weh.get_elements(self.profiles_table_rows)

    def get_add_profile_button(self):
        """
        :return: "Add..." button element on Profiles tab toolbar
        """
        return self.weh.get_element(self.profile_add_button)

    def get_edit_profile_button(self):
        """
        :return: "Edit..." button element on Profiles tab toolbar
        """
        return self.weh.get_element(self.profile_edit_button)

    def get_delete_profile_button(self):
        """
        :return: "Delete" button element on Profiles tab toolbar
        """
        return self.weh.get_element(self.profile_delete_button)
