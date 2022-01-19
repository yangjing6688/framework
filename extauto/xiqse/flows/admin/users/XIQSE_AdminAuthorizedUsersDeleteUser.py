# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from xiqse.elements.admin.users.AdminAuthorizedUsersDeleteUserWebElements import AdminAuthorizedUsersDeleteUserWebElements


class XIQSE_AdminAuthorizedUsersDeleteUser(AdminAuthorizedUsersDeleteUserWebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.utils = Utils()

    def xiqse_delete_authorized_user_confirm_delete(self):
        """
         - This keyword confirms the Authorized User deletion.
         - It is assumed the Confirm Delete dialog is already open.
         - Keyword Usage
          - ``XIQSE Delete Authorized User Confirm Delete``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        confirm_dlg = self.get_confirm_delete_authorized_user_dialog()
        if confirm_dlg:
            self.xiqse_delete_authorized_user_confirm_dialog_click_yes()
        else:
            self.utils.print_info("No confirmation dialog present for Delete User")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_authorized_user_confirm_dialog_click_yes(self):
        """
         - This keyword clicks the Yes button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the Authorized User is already open.
         - Keyword Usage
          - ``XIQSE Delete Authorized User Confirm Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_delete_authorized_user_confirm_dialog_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking 'Yes' button")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_authorized_user_confirm_dialog_click_no(self):
        """
         - This keyword clicks the No button in the Confirm Delete dialog.
         - It is assumed the confirmation dialog for deleting the Authorized User is already open.
         - Keyword Usage
          - ``XIQSE Delete Site Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_delete_authorized_user_confirm_dialog_no_button()
        if no_btn:
            self.utils.print_info("Clicking 'No' button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find 'No' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
