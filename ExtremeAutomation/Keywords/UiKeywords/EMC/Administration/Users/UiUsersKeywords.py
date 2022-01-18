from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.UsersConstants import UsersConstants


class UiUsersKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiUsersKeywords, self).__init__()
        self.api_const = self.constants.API_USERS
        self.cmd = UsersConstants()

    def users_handle_lock(self, element_name, revoke_lock, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [revoke_lock] -   Indicates whether to click Yes or No in the Revoke Lock dialog (True/False)

        Clicks the specified button (Yes or No) in the Revoke Lock dialog, if the dialog is displayed.
        """
        args = {"revoke_lock": revoke_lock}

        return self.execute_keyword(element_name, args, self.cmd.USERS_HANDLE_LOCK, **kwargs)

    def users_click_add_user(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Add..." toolbar button for the Authorized Users table on the Users tab.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_ADD_USER, **kwargs)

    def users_click_edit_user(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Edit..." toolbar button for the Authorized Users table on the Users tab.
        Assumes the user to edit is already selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_EDIT_USER, **kwargs)

    def users_click_delete_user(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Delete" toolbar button for the Authorized Users table on the Users tab.
        Assumes the user to delete is already selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_DELETE_USER, **kwargs)

    def users_click_add_group(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Add..." toolbar button for the Authorization Groups table on the Users tab.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_ADD_GROUP, **kwargs)

    def users_click_edit_group(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Edit..." toolbar button for the Authorization Groups table on the Users tab.
        Assumes the group to edit is already selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_EDIT_GROUP, **kwargs)

    def users_click_copy_group(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Copy..." toolbar button for the Authorization Groups table on the Users tab.
        Assumes the group to copy is already selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_COPY_GROUP, **kwargs)

    def users_click_delete_group(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Delete" toolbar button for the Authorization Groups table on the Users tab.
        Assumes the group to delete is already selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_CLICK_DELETE_GROUP, **kwargs)

    def users_dialog_add_user_set_name(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Name of the user to set in the Add User dialog

        Sets the User Name field in the Add User dialog.
        Assumes the Add User dialog is already displayed.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_USER_SET_NAME, **kwargs)

    def users_dialog_add_user_set_domain(self, element_name, domain_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [domain_name] -   Name of the domain to set in the Add User dialog

        Sets the Domain/Host Name field in the Add User dialog.
        Assumes the Add User dialog is already displayed.
        """
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_USER_SET_DOMAIN, **kwargs)

    def users_dialog_add_user_set_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the authorization group to set in the Add User dialog

        Sets the Authorization Group field in the Add User dialog.
        Assumes the Add User dialog is already displayed.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_USER_SET_GROUP, **kwargs)

    def users_dialog_add_user_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Add User dialog.
        Assumes the Add User dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_ADD_USER_CLICK_SAVE, **kwargs)

    def users_dialog_add_user_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Add User dialog.
        Assumes the Add User dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_ADD_USER_CLICK_CANCEL, **kwargs)

    def users_dialog_edit_user_set_domain(self, element_name, domain_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [domain_name] -   Name of the domain to set in the Edit User dialog

        Sets the Domain/Host Name field in the Edit User dialog.
        Assumes the Edit User dialog is already displayed.
        """
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_USER_SET_DOMAIN, **kwargs)

    def users_dialog_edit_user_set_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the authorization group to set in the Edit User dialog

        Sets the Authorization Group field in the Edit User dialog.
        Assumes the Edit User dialog is already displayed.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_USER_SET_GROUP, **kwargs)

    def users_dialog_edit_user_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Edit User dialog.
        Assumes the Edit User dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_EDIT_USER_CLICK_SAVE, **kwargs)

    def users_dialog_edit_user_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Edit User dialog.
        Assumes the Edit User dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_EDIT_USER_CLICK_CANCEL, **kwargs)

    def users_dialog_confirm_delete_user_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete dialog.  This is for deleting a user.
        Assumes the Confirm Delete dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_CONFIRM_DELETE_USER_CLICK_YES, **kwargs)

    def users_dialog_confirm_delete_user_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete dialog.  This is for deleting a user.
        Assumes the Confirm Delete dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_CONFIRM_DELETE_USER_CLICK_NO, **kwargs)

    def users_dialog_add_group_set_name(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the authorization group to create

        Sets the Name field in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_SET_NAME, **kwargs)

    def users_dialog_add_group_set_membership_criteria(self, element_name, member_crit, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [member_crit] -   Value to set in the Membership Criteria field

        Sets the Membership Criteria field in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"member_crit": member_crit}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_SET_MEMBERSHIP_CRITERIA,
                                    **kwargs)

    def users_dialog_add_group_set_snmp_redirect(self, element_name, snmp_redirect, **kwargs):
        """
        Keyword Arguments:
        [element_names] -  List of elements the keyword will be run against
        [snmp_redirect] -  Value to select in the SNMP Redirect drop down

        Sets the SNMP Redirect field in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"snmp_redirect": snmp_redirect}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_SET_SNMP_REDIRECT, **kwargs)

    def users_dialog_add_group_expand_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to expand

        Expands the specified capability in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_EXPAND_CAPABILITY, **kwargs)

    def users_dialog_add_group_collapse_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to collapse

        Collapses the specified capability in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_COLLAPSE_CAPABILITY, **kwargs)

    def users_dialog_add_group_enable_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to enable

        Enables the specified capability in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_ENABLE_CAPABILITY, **kwargs)

    def users_dialog_add_group_disable_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to disable

        Disables the specified capability in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_ADD_GROUP_DISABLE_CAPABILITY, **kwargs)

    def users_dialog_add_group_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_ADD_GROUP_CLICK_SAVE, **kwargs)

    def users_dialog_add_group_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Add Authorization Group dialog.
        Assumes the Add Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_ADD_GROUP_CLICK_CANCEL, **kwargs)

    def users_dialog_edit_group_set_membership_criteria(self, element_name, member_crit, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [member_crit] -   Value to set in the Membership Criteria field

        Sets the Membership Criteria field in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"member_crit": member_crit}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_SET_MEMBERSHIP_CRITERIA,
                                    **kwargs)

    def users_dialog_edit_group_set_snmp_redirect(self, element_name, snmp_redirect, **kwargs):
        """
        Keyword Arguments:
        [element_names] -  List of elements the keyword will be run against
        [snmp_redirect] -  Value to select in the SNMP Redirect drop down

        Sets the SNMP Redirect field in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"snmp_redirect": snmp_redirect}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_SET_SNMP_REDIRECT, **kwargs)

    def users_dialog_edit_group_expand_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to expand

        Expands the specified capability in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_EXPAND_CAPABILITY, **kwargs)

    def users_dialog_edit_group_collapse_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to collapse

        Collapses the specified capability in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_COLLAPSE_CAPABILITY, **kwargs)

    def users_dialog_edit_group_enable_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to enable

        Enables the specified capability in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_ENABLE_CAPABILITY, **kwargs)

    def users_dialog_edit_group_disable_capability(self, element_name, capability, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [capability] -    Name of the capability to disable

        Disables the specified capability in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        args = {"capability": capability}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_EDIT_GROUP_DISABLE_CAPABILITY, **kwargs)

    def users_dialog_edit_group_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_EDIT_GROUP_CLICK_SAVE, **kwargs)

    def users_dialog_edit_group_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Edit Authorization Group dialog.
        Assumes the Edit Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_EDIT_GROUP_CLICK_CANCEL, **kwargs)

    def users_dialog_copy_group_set_name(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Value to set in the Name field

        Sets the value of the Name field in the Copy Authorization Group dialog.
        Assumes the Copy Authorization Group dialog is already displayed.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_DIALOG_COPY_GROUP_SET_NAME, **kwargs)

    def users_dialog_copy_group_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Copy Authorization Group dialog.
        Assumes the Copy Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_COPY_GROUP_CLICK_SAVE, **kwargs)

    def users_dialog_copy_group_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Copy Authorization Group dialog.
        Assumes the Copy Authorization Group dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_COPY_GROUP_CLICK_CANCEL, **kwargs)

    def users_dialog_confirm_delete_group_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete dialog.  This is for deleting a group.
        Assumes the Confirm Delete dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_CONFIRM_DELETE_GROUP_CLICK_YES, **kwargs)

    def users_dialog_confirm_delete_group_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete dialog.  This is for deleting a group.
        Assumes the Confirm Delete dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.USERS_DIALOG_CONFIRM_DELETE_GROUP_CLICK_NO, **kwargs)

    def users_select_user(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Name of the user to select

        Selects the specified user in the Authorized Users table.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_SELECT_USER, **kwargs)

    def users_select_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the group to select

        Selects the specified group in the Authorization Groups table.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_SELECT_GROUP, **kwargs)

    def users_wait_for_user_add(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Name of the user to wait for

        Waits for the specified user to be added to the Authorized Users table.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_WAIT_FOR_USER_ADD, **kwargs)

    def users_wait_for_user_remove(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Name of the user to wait for

        Waits for the specified user to be removed from the Authorized Users table.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_WAIT_FOR_USER_REMOVE, **kwargs)

    def users_wait_for_group_add(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the group to wait for

        Waits for the specified group to be added to the Authorization Groups table.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_WAIT_FOR_GROUP_ADD, **kwargs)

    def users_wait_for_group_remove(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the group to wait for

        Waits for the specified group to be removed from the Authorization Groups table.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_WAIT_FOR_GROUP_REMOVE, **kwargs)

    def users_confirm_user_exists(self, element_name, user_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Name of the user to select
        [exists] -        Indicates whether or not the user is expected to exist (True/False)

        Confirms whether or not the specified user is present in the Authorized Users table.
        """
        args = {"user_name": user_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.USERS_CONFIRM_USER_EXISTS, **kwargs)

    def users_confirm_group_exists(self, element_name, group_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the group to select
        [exists] -        Indicates whether or not the user is expected to exist (True/False)

        Confirms whether or not the specified group is present in the Authorization Groups table.
        """
        args = {"exists": exists,
                "group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_CONFIRM_GROUP_EXISTS, **kwargs)

    def users_confirm_user_logged_in(self, element_name, group_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the group the user should belong to
        [user_name] -     Name of the user who should be logged in

        Confirms whether or not the specified user is the currently logged-in user.
        """
        args = {"user_name": user_name,
                "group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.USERS_CONFIRM_USER_LOGGED_IN, **kwargs)
