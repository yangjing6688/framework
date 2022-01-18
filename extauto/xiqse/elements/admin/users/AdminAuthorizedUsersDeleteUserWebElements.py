# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from common.WebElementHandler import *
from xiqse.defs.admin.users.AdminAuthorizedUsersDeleteUserWebElementsDefinitions import *


class AdminAuthorizedUsersDeleteUserWebElements(AdminAuthorizedUsersDeleteUserWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_confirm_delete_authorized_user_dialog(self):
        """
        :return: Confirm Delete Authorized User dialog
        """
        return self.weh.get_element(self.confirm_delete_authorized_user_dialog)

    def get_delete_authorized_user_confirm_dialog_yes_button(self):
        """
        :return: 'Yes' button in the Confirm Delete Authorized User dialog
        """
        return self.weh.get_element(self.delete_authorized_user_confirm_dialog_yes_button)

    def get_delete_authorized_user_confirm_dialog_no_button(self):
        """
        :return: 'No' button in the Confirm Delete Authorized User dialog
        """
        return self.weh.get_element(self.delete_authorized_user_confirm_dialog_no_button)
