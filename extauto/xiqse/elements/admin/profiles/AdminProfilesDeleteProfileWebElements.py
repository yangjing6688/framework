from common.WebElementHandler import *
from xiqse.defs.admin.profiles.AdminProfilesDeleteProfileWebElementsDefinitions import *


class AdminProfilesDeleteProfileWebElements(AdminProfilesDeleteProfileWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_confirm_delete_profile_dialog(self):
        """
        :return: Confirm Delete Profile dialog
        """
        return self.weh.get_element(self.confirm_delete_profile_dialog)

    def get_delete_profile_confirm_dialog_yes_button(self):
        """
        :return: 'Yes' button in the Confirm Delete Profile dialog
        """
        return self.weh.get_element(self.delete_profile_confirm_dialog_yes_button)

    def get_delete_profile_confirm_dialog_no_button(self):
        """
        :return: 'No' button in the Confirm Delete Profile dialog
        """
        return self.weh.get_element(self.delete_profile_confirm_dialog_no_button)
