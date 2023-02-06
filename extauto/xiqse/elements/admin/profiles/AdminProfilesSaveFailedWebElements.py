from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.profiles.AdminProfilesSaveFailedWebElementsDefinitions import AdminProfilesSaveFailedWebElementsDefinitions


class AdminProfilesSaveFailedWebElements(AdminProfilesSaveFailedWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_profile_save_failed_dialog(self):
        """
        :return: 'Save Failed' dialog for the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_save_failed_dialog)

    def get_add_profile_save_failed_dialog_message(self):
        """
        :return: Message in the 'Save Failed' dialog for the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_save_failed_dialog_message)

    def get_add_profile_save_failed_dialog_ok_button(self):
        """
        :return: OK button in the 'Save Failed' dialog for the Add Profile dialog
        """
        return self.weh.get_element(self.add_profile_save_failed_dialog_ok_button)
