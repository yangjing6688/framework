from common.WebElementHandler import *
from xiqse.defs.admin.profiles.AdminProfilesAddProfileWebElementsDefinitions import *
import re


class AdminProfilesAddProfileWebElements(AdminProfilesAddProfileWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_profile_dialog_name_field(self):
        """
        :return: 'Profile Name' field in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_name_field)

    def get_add_profile_dialog_version_dropdown(self):
        """
        :return: 'SNMP Version' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_version_dropdown)

    def get_add_profile_dialog_read_dropdown(self):
        """
        :return: 'Read' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_read_dropdown)

    def get_add_profile_dialog_write_dropdown(self):
        """
        :return: 'Write' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_write_dropdown)

    def get_add_profile_dialog_max_access_dropdown(self):
        """
        :return: 'Max Access' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_max_access_dropdown)

    def get_add_profile_dialog_read_security_dropdown(self):
        """
        :return: 'Read Security' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_read_security_dropdown)

    def get_add_profile_dialog_write_security_dropdown(self):
        """
        :return: 'Write Security' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_write_security_dropdown)

    def get_add_profile_dialog_max_security_dropdown(self):
        """
        :return: 'Max Security' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_max_security_dropdown)

    def get_add_profile_dialog_cli_dropdown(self):
        """
        :return: 'CLI Credential' dropdown in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_cli_dropdown)

    def get_add_profile_dialog_cancel_button(self):
        """
        :return: 'Cancel' button in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_cancel_btn)

    def get_add_profile_dialog_save_button(self):
        """
        :return: 'Save' button in the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_dialog_save_btn)
