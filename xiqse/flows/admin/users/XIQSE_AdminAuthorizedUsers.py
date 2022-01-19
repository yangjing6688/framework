# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.users.AdminAuthorizedUsersWebElements import AdminAuthorizedUsersWebElements
from xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsersDeleteUser import XIQSE_AdminAuthorizedUsersDeleteUser
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable


class XIQSE_AdminAuthorizedUsers(AdminAuthorizedUsersWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.xiqse_table = XIQSE_CommonTable()
        self.delete_authorized_user_dlg = XIQSE_AdminAuthorizedUsersDeleteUser()

    def xiqse_navigate_and_select_authorized_user(self, name, ignore_case=False):
        """
         - This keyword navigates to the Administration> Users tab and selects an existing Authorized User in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Select Authorized User  username  ignore_case=True``

        :param name: name of the Authorized User to select
        :param ignore_case: ignore case (optional) and defaults to False
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if ignore_case:
            name = name.lower()

        if self.xiqse_nav.xiqse_navigate_to_admin_users_tab():
            ret_val = self.xiqse_select_authorized_user(name)

        return ret_val

    def xiqse_navigate_and_delete_authorized_user(self, name, ignore_case=False):
        """
         - This keyword navigates to the Administration> Users tab and deletes an existing Authorized User in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Delete Authorized User  username  ignore_case=True``

        :param name: name of the Authorized User to delete
        :param ignore_case: ignore case (optional) and defaults to False
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if ignore_case:
            name = name.lower()

        if self.xiqse_nav.xiqse_navigate_to_admin_users_tab():
            ret_val = self.xiqse_delete_authorized_user(name)

        return ret_val

    def xiqse_delete_authorized_user(self, name, ignore_case=False):
        """
         - This keyword deletes an existing Authorized User in XIQ-SE.
         - It is assumed the view is already navigated to Administration > Users.
         - Keyword Usage
          - ``XIQSE Delete Authorized User  username  ignore_case=True``

        :param name: name of the Authorized User to delete
        :param ignore_case: ignore case (optional) and defaults to False
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if ignore_case:
            name = name.lower()

        if self.xiqse_select_authorized_user(name):
            delete_btn = self.get_delete_authorized_user_button()
            if delete_btn:
                btn_disabled = delete_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Delete' button is disabled")
                else:
                    self.utils.print_info("Clicking 'Delete' toolbar button")
                    self.auto_actions.click(delete_btn)
                    sleep(2)

                    # Confirm the deletion
                    ret_val = self.delete_authorized_user_dlg.xiqse_delete_authorized_user_confirm_delete()
            else:
                self.utils.print_info("Could not find 'Delete' button")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_authorized_user(self, name, ignore_case=False):
        """
         - This keyword selects an existing Authorized User in XIQ-SE.
         - It is assumed the view is already navigated to Administration > Users.
         - Keyword Usage
          - ``XIQSE Select Authorized User  username  ignore_case=True``

        :param name: name of the Authorized User to select
        :param ignore_case: ignore case (optional) and defaults to False
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if ignore_case:
            name = name.lower()

        sleep(2)
        rows = self.get_authorized_user_table_rows()
        for row in rows:
            if name in row.text:
                self.utils.print_debug(f"Found user {name} in row {self.xiqse_table.format_table_row(row.text)}")
                row_selected = row.get_attribute("aria-selected")
                if row_selected and row_selected == "true":
                    self.utils.print_info(f"Row for user {name} is already selected")
                else:
                    self.utils.print_info(f"Selecting user {name}")
                    self.auto_actions.click(row)
                ret_val = 1
                break
        if ret_val == -1:
            self.utils.print_info(f"Unable to select user {name}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_authorized_user(self, name, ignore_case=False):
        """
        - Searches for Authorized User matching the specified name.
        - Assumes the Administration > Users tab is already selected.
        - Keyword Usage
         - ``XIQSE Find Authorized User  username  ignore_case=True``

        :param name: Name of the Authorized User to search for
        :param ignore_case: ignore case (optional) and defaults to False
        :return: return 1 if the Authorized User is found, else -1
        """

        ret_val = -1

        if ignore_case:
            name = name.lower()

        rows = self.get_authorized_user_table_rows()
        if rows:
            self.utils.print_debug(f"Authorized Users row count: {len(rows)}")
            for row in rows:
                self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if name in row.text:
                    self.utils.print_info(f"Found row for Authorized User with name {name}")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find row for Authorized User with name {name}")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not obtain rows from Authorized Users table")
            self.screen.save_screen_shot()

        return ret_val
