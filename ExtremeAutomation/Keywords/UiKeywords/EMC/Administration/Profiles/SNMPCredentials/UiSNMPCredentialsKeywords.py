from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.SnmpcredentialsConstants\
    import SnmpcredentialsConstants


class UiSNMPCredentialsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiSNMPCredentialsKeywords, self).__init__()
        self.api_const = self.constants.API_SNMPCREDENTIALS
        self.cmd = SnmpcredentialsConstants()

    def snmpcredentials_select_credential(self, element_name, cred_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cred_name] -     Name of the SNMP credential to select

        Selects the specified SNMP credential, based on the Name value.
        """
        args = {"cred_name": cred_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_SELECT_CREDENTIAL, **kwargs)

    def snmpcredentials_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Refreshes the SNMP Credentials table by clicking the Refresh icon.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_REFRESH, **kwargs)

    def snmpcredentials_toolbar_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Add' toolbar button for the SNMP Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_TOOLBAR_CLICK_ADD, **kwargs)

    def snmpcredentials_toolbar_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Edit' toolbar button for the SNMP Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_TOOLBAR_CLICK_EDIT, **kwargs)

    def snmpcredentials_toolbar_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Delete' toolbar button for the SNMP Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_TOOLBAR_CLICK_DELETE, **kwargs)

    def snmpcredentials_dialog_add_set_credential_name(self, element_name, cred_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cred_name] -     Value to set in the Credential Name field

        Sets the 'Credential Name' field in the Add SNMP Credential dialog.
        """
        args = {"cred_name": cred_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_CREDENTIAL_NAME,
                                    **kwargs)

    def snmpcredentials_dialog_add_set_snmp_version(self, element_name, snmp_version, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_version] -  Value to set in the SNMP Version field

        Sets the 'SNMP Version' field in the Add SNMP Credential dialog.
        """
        args = {"snmp_version": snmp_version}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_SNMP_VERSION, **kwargs)

    def snmpcredentials_dialog_add_set_community_name(self, element_name, comm_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [comm_name] -     Value to set in the Community Name field

        Sets the 'Community Name' field in the Add SNMP Credential dialog (only available for SNMPv1 and SNMPv2).
        """
        args = {"comm_name": comm_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_COMMUNITY_NAME,
                                    **kwargs)

    def snmpcredentials_dialog_add_set_user_name(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Value to set in the User Name field

        Sets the 'User Name' field in the Add SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_USER_NAME, **kwargs)

    def snmpcredentials_dialog_add_set_authentication_type(self, element_name, auth_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [auth_type] -     Value to set in the Authentication Type field

        Sets the 'Authentication Type' field in the Add SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"auth_type": auth_type}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_AUTHENTICATION_TYPE,
                                    **kwargs)

    def snmpcredentials_dialog_add_set_authentication_password(self, element_name, auth_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [auth_pwd] -      Value to set in the Authentication Password field

        Sets the 'Authentication Password' field in the Add SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"auth_pwd": auth_pwd}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_AUTHENTICATION_PASSWORD,
                                    **kwargs)

    def snmpcredentials_dialog_add_set_privacy_type(self, element_name, priv_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [priv_type] -     Value to set in the Privacy Type field

        Sets the 'Privacy Type' field in the Add SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"priv_type": priv_type}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_PRIVACY_TYPE, **kwargs)

    def snmpcredentials_dialog_add_set_privacy_password(self, element_name, priv_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [priv_pwd] -      Value to set in the Privacy Password field

        Sets the 'Privacy Password' field in the Add SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"priv_pwd": priv_pwd}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_SET_PRIVACY_PASSWORD,
                                    **kwargs)

    def snmpcredentials_dialog_add_click_community_name_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Authentication Password field in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_CLICK_COMMUNITY_NAME_EYE,
                                    **kwargs)

    def snmpcredentials_dialog_add_click_authentication_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Authentication Password field in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.DIALOG_ADD_CLICK_AUTHENTICATION_PASSWORD_EYE,
                                    **kwargs)

    def snmpcredentials_dialog_add_click_privacy_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Privacy Password field in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_CLICK_PRIVACY_PASSWORD_EYE,
                                    **kwargs)

    def snmpcredentials_dialog_add_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Save' in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_CLICK_SAVE, **kwargs)

    def snmpcredentials_dialog_add_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_ADD_CLICK_CANCEL, **kwargs)

    def snmpcredentials_dialog_edit_set_credential_name(self, element_name, cred_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cred_name] -     Value to set in the Credential Name field

        Sets the 'Credential Name' field in the Edit SNMP Credential dialog.
        """
        args = {"cred_name": cred_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_CREDENTIAL_NAME,
                                    **kwargs)

    def snmpcredentials_dialog_edit_set_snmp_version(self, element_name, snmp_version, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_version] -  Value to set in the SNMP Version field

        Sets the 'SNMP Version' field in the Edit SNMP Credential dialog.
        """
        args = {"snmp_version": snmp_version}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_SNMP_VERSION, **kwargs)

    def snmpcredentials_dialog_edit_set_community_name(self, element_name, comm_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [comm_name] -     Value to set in the Community Name field

        Sets the 'Community Name' field in the Edit SNMP Credential dialog (only available for SNMPv1 and SNMPv2).
        """
        args = {"comm_name": comm_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_COMMUNITY_NAME,
                                    **kwargs)

    def snmpcredentials_dialog_edit_set_user_name(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Value to set in the User Name field

        Sets the 'User Name' field in the Edit SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_USER_NAME, **kwargs)

    def snmpcredentials_dialog_edit_set_authentication_type(self, element_name, auth_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [auth_type] -     Value to set in the Authentication Type field

        Sets the 'Authentication Type' field in the Edit SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"auth_type": auth_type}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_AUTHENTICATION_TYPE,
                                    **kwargs)

    def snmpcredentials_dialog_edit_set_authentication_password(self, element_name, auth_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [auth_pwd] -      Value to set in the Authentication Password field

        Sets the 'Authentication Password' field in the Edit SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"auth_pwd": auth_pwd}

        return self.execute_keyword(element_name, args,
                                    self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_AUTHENTICATION_PASSWORD, **kwargs)

    def snmpcredentials_dialog_edit_set_privacy_type(self, element_name, priv_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [priv_type] -     Value to set in the Privacy Type field

        Sets the 'Privacy Type' field in the Edit SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"priv_type": priv_type}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_PRIVACY_TYPE, **kwargs)

    def snmpcredentials_dialog_edit_set_privacy_password(self, element_name, priv_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [priv_pwd] -      Value to set in the Privacy Password field

        Sets the 'Privacy Password' field in the Edit SNMP Credential dialog (only available for SNMPv3).
        """
        args = {"priv_pwd": priv_pwd}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_SET_PRIVACY_PASSWORD,
                                    **kwargs)

    def snmpcredentials_dialog_edit_click_community_name_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Authentication Password field in the Add SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_COMMUNITY_NAME_EYE,
                                    **kwargs)

    def snmpcredentials_dialog_edit_click_authentication_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Authentication Password field in the Edit SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.DIALOG_EDIT_CLICK_AUTHENTICATION_PASSWORD_EYE, **kwargs)

    def snmpcredentials_dialog_edit_click_privacy_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Privacy Password field in the Edit SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_PRIVACY_PASSWORD_EYE,
                                    **kwargs)

    def snmpcredentials_dialog_edit_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Save' in the Edit SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_SAVE, **kwargs)

    def snmpcredentials_dialog_edit_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Edit SNMP Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_CANCEL, **kwargs)

    def snmpcredentials_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Yes' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_YES,
                                    **kwargs)

    def snmpcredentials_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'No' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.SNMPCREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_NO,
                                    **kwargs)

    def snmpcredentials_confirm_credential_exists(self, element_name, cred_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cred_name] -     Name of the SNMP credential to look for
        [exists] -        Boolean indicating if the credential is expected to exist or not (true/false)

        Confirms whether or not the specified SNMP credential exists.
        """
        args = {"cred_name": cred_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.SNMPCREDENTIALS_CONFIRM_CREDENTIAL_EXISTS, **kwargs)
