# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from common.WebElementHandler import *
from xiqse.defs.common.CommonAccountWebElementsDefinitions import *


class CommonAccountWebElements(CommonAccountWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_account_menu_button(self):
        """
        :return: Account (hamburger icon) menu button
        """
        return self.weh.get_element(self.account_menu_button)

    def get_logout_menu_item(self):
        """
        :return: Logout menu item under the account menu
        """
        return self.weh.get_element(self.logout_menu_item)

    def get_xiqse_username(self):
        """
        Returns the ID for the XIQSE username field
        :return: ID for the XIQSE username field
        """
        return self.weh.get_element(self.xiqse_username_field)

    def get_xiqse_authorization_group(self):
        """
        Returns the ID for the XIQSE Authorization Group field
        :return:
        """
        return self.weh.get_element(self.xiqse_authorization_group_field)
