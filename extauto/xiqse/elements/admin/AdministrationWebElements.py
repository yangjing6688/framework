from extauto.common.WebElementHandler import *
from xiqse.defs.admin.AdministrationWebElementsDefinitions import *


class AdministrationWebElements(AdministrationWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_profiles_tab(self):
        """
        :return: Profiles Tab on the Administration page
        """
        return self.weh.get_element(self.profiles_tab)

    def get_users_tab(self):
        """
        :return: Users Tab on the Administration page
        """
        return self.weh.get_element(self.users_tab)

    def get_server_information_tab(self):
        """
        :return: Server Information Tab on the Administration page
        """
        return self.weh.get_element(self.server_info_tab)

    def get_licenses_tab(self):
        """
        :return: Licenses Tab on the Administration page
        """
        return self.weh.get_element(self.licenses_tab)

    def get_certificates_tab(self):
        """
        :return: Certificates Tab on the Administration page
        """
        return self.weh.get_element(self.certificates_tab)

    def get_options_tab(self):
        """
        :return: Options Tab on the Administration page
        """
        return self.weh.get_element(self.options_tab)

    def get_device_types_tab(self):
        """
        :return: Device Types Tab on the Administration page
        """
        return self.weh.get_element(self.device_types_tab)

    def get_backup_restore_tab(self):
        """
        :return: Backup/Restore Tab on the Administration page
        """
        return self.weh.get_element(self.backup_restore_tab)

    def get_diagnostics_tab(self):
        """
        :return: Diagnostics Tab on the Administration page
        """
        return self.weh.get_element(self.diagnostics_tab)

    def get_client_api_access_tab(self):
        """
        :return: Client API Access Tab on the Administration page
        """
        return self.weh.get_element(self.client_api_access_tab)
