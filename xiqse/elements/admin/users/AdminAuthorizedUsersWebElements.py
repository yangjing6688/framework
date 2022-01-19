# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from common.WebElementHandler import *
from xiqse.defs.admin.users.AdminAuthorizedUsersWebElementsDefinitions import *


class AdminAuthorizedUsersWebElements(AdminAuthorizedUsersWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_authorized_user_table_rows(self):
        """
        :return: All the rows in the Authorized Users table
        """
        return self.weh.get_elements(self.authorized_user_table_rows)

    def get_add_authorized_user_button(self):
        """
        :return: "Add..." button element on the Authorized Users table toolbar
        """
        return self.weh.get_element(self.authorized_user_add_button)

    def get_edit_authorized_user_button(self):
        """
        :return: "Edit..." button element on the Authorized Users table toolbar
        """
        return self.weh.get_element(self.authorized_user_edit_button)

    def get_delete_authorized_user_button(self):
        """
        :return: "Delete" button element on the Authorized Users table toolbar
        """
        return self.weh.get_element(self.authorized_user_delete_button)
