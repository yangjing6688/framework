from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.AdminProfilesDeleteProfileWebElements import AdminProfilesDeleteProfileWebElements


class XIQSE_AdminProfilesDeleteProfile(AdminProfilesDeleteProfileWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_delete_profile_confirm_delete(self):
        """
         - This keyword confirms the Profile deletion.
         - It is assumed the Confirm Delete dialog is already open.
         - Keyword Usage
          - ``XIQSE Delete Profile Confirm Delete``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        confirm_dlg = self.get_confirm_delete_profile_dialog()
        if confirm_dlg:
            self.xiqse_delete_profile_confirm_dialog_click_yes()
        else:
            self.utils.print_info("No confirmation dialog present for Delete Profile")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_profile_confirm_dialog_click_yes(self):
        """
         - This keyword clicks the Yes button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the SNMP Credential is already open.
         - Keyword Usage
          - ``XIQSE Delete Site Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_delete_profile_confirm_dialog_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' button")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_profile_confirm_dialog_click_no(self):
        """
         - This keyword clicks the No button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the SNMP Credential is already open.
         - Keyword Usage
          - ``XIQSE Delete Site Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_delete_profile_confirm_dialog_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find 'No' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_profile(self, name):
        """
         - This keyword deletes an existing profile in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles.
         - Keyword Usage
          - ``XIQSE Delete Profile  test_profile_1``

        :param name: name of the profile to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_profile(name):
            delete_btn = self.get_delete_profile_button()
            if delete_btn:
                btn_disabled = delete_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Delete' button is disabled")
                    self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Clicking 'Delete' toolbar button")
                    self.auto_actions.click(delete_btn)
                    sleep(2)

                    # Confirm the deletion
                    yes_btn = self.get_delete_profile_confirm_dialog_yes_button()
                    if yes_btn:
                        self.utils.print_info("Clicking 'Yes' in Confirm Delete dialog")
                        self.auto_actions.click(yes_btn)
                        ret_val = 1
                    else:
                        self.utils.print_info("Could not find the 'Yes' button to confirm the deletion")
                        self.screen.save_screen_shot()
            else:
                self.utils.print_info("Could not find 'Delete' button")
                self.screen.save_screen_shot()

        return ret_val
