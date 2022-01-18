from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ClicredentialsConstants import ClicredentialsConstants


class UiCLICredentialsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiCLICredentialsKeywords, self).__init__()
        self.api_const = self.constants.API_CLICREDENTIALS
        self.cmd = ClicredentialsConstants()

    def clicredentials_select_credential(self, element_name, cli_desc, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_desc] -      Description of the CLI credential to select

        Selects the specified CLI credential, based on the Description value.
        """
        args = {"cli_desc": cli_desc}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_SELECT_CREDENTIAL, **kwargs)

    def clicredentials_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Refreshes the CLI Credentials table by clicking the Refresh icon.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_REFRESH, **kwargs)

    def clicredentials_toolbar_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Add' toolbar button for the CLI Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_TOOLBAR_CLICK_ADD, **kwargs)

    def clicredentials_toolbar_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Edit' toolbar button for the CLI Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_TOOLBAR_CLICK_EDIT, **kwargs)

    def clicredentials_toolbar_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Delete' toolbar button for the CLI Credentials table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_TOOLBAR_CLICK_DELETE, **kwargs)

    def clicredentials_dialog_add_set_description(self, element_name, cli_desc, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_desc] -      Value to set in the Description field

        Sets the 'Description' field in the Add CLI Credential dialog.
        """
        args = {"cli_desc": cli_desc}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_DESCRIPTION, **kwargs)

    def clicredentials_dialog_add_set_user_name(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Value to set in the User Name field

        Sets the 'User Name' field in the Add CLI Credential dialog.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_USER_NAME, **kwargs)

    def clicredentials_dialog_add_set_type(self, element_name, cli_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_type] -      Value to set in the Type field

        Sets the 'Type' field in the Add CLI Credential dialog.
        """
        args = {"cli_type": cli_type}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_TYPE, **kwargs)

    def clicredentials_dialog_add_set_login_password(self, element_name, login_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [login_pwd] -     Value to set in the Login Password field

        Sets the 'Login Password' field in the Add CLI Credential dialog.
        """
        args = {"login_pwd": login_pwd}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_LOGIN_PASSWORD, **kwargs)

    def clicredentials_dialog_add_set_enable_password(self, element_name, enable_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [enable_pwd] -    Value to set in the Enable Password field

        Sets the 'Enable Password' field in the Add CLI Credential dialog.
        """
        args = {"enable_pwd": enable_pwd}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_ENABLE_PASSWORD,
                                    **kwargs)

    def clicredentials_dialog_add_set_configuration_password(self, element_name, config_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_pwd] -    Value to set in the Configuration Password field

        Sets the 'Configuration Password' field in the Add CLI Credential dialog.
        """
        args = {"config_pwd": config_pwd}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_ADD_SET_CONFIGURATION_PASSWORD,
                                    **kwargs)

    def clicredentials_dialog_add_click_login_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Login Password field in the Add CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_ADD_CLICK_LOGIN_PASSWORD_EYE,
                                    **kwargs)

    def clicredentials_dialog_add_click_enable_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Enable Password field in the Add CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_ADD_CLICK_ENABLE_PASSWORD_EYE,
                                    **kwargs)

    def clicredentials_dialog_add_click_configuration_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Configuration Password field in the Add CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.IALOG_ADD_CLICK_CONFIGURATION_PASSWORD_EYE, **kwargs)

    def clicredentials_dialog_add_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Save' in the Add CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_ADD_CLICK_SAVE, **kwargs)

    def clicredentials_dialog_add_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Add CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_ADD_CLICK_CANCEL, **kwargs)

    def clicredentials_dialog_edit_cli_set_description(self, element_name, cli_desc, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_desc] -      Value to set in the Description field

        Sets the 'Description' field in the Edit CLI Credential dialog.
        """
        args = {"cli_desc": cli_desc}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_DESCRIPTION,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_set_user_name(self, element_name, user_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_name] -     Value to set in the User Name field

        Sets the 'User Name' field in the Edit CLI Credential dialog.
        """
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_USER_NAME, **kwargs)

    def clicredentials_dialog_edit_cli_set_type(self, element_name, cli_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_type] -      Value to set in the Type field

        Sets the 'Type' field in the Edit CLI Credential dialog.
        """
        args = {"cli_type": cli_type}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_TYPE, **kwargs)

    def clicredentials_dialog_edit_cli_set_login_password(self, element_name, login_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [login_pwd] -     Value to set in the Login Password field

        Sets the 'Login Password' field in the Edit CLI Credential dialog.
        """
        args = {"login_pwd": login_pwd}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_LOGIN_PASSWORD,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_set_enable_password(self, element_name, enable_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [enable_pwd] -    Value to set in the Enable Password field

        Sets the 'Enable Password' field in the Edit CLI Credential dialog.
        """
        args = {"enable_pwd": enable_pwd}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_ENABLE_PASSWORD,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_set_configuration_password(self, element_name, config_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_pwd] -    Value to set in the Configuration Password field

        Sets the 'Configuration Password' field in the Edit CLI Credential dialog.
        """
        args = {"config_pwd": config_pwd}

        return self.execute_keyword(element_name, args,
                                    self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_SET_CONFIGURATION_PASSWORD, **kwargs)

    def clicredentials_dialog_edit_cli_click_login_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Login Password field in the Edit CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_CLICK_LOGIN_PASSWORD_EYE,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_click_enable_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Enable Password field in the Edit CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_CLICK_ENABLE_PASSWORD_EYE,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_click_configuration_password_eye(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'eye' icon for the Configuration Password field in the Edit CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.IALOG_EDIT_CLI_CLICK_CONFIGURATION_PASSWORD_EYE,
                                    **kwargs)

    def clicredentials_dialog_edit_cli_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Save' in the Edit CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_CLICK_SAVE, **kwargs)

    def clicredentials_dialog_edit_cli_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Edit CLI Credential dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_EDIT_CLI_CLICK_CANCEL, **kwargs)

    def clicredentials_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Yes' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_YES, **kwargs)

    def clicredentials_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'No' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.CLICREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_NO, **kwargs)

    def clicredentials_confirm_credential_exists(self, element_name, cli_desc, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_desc] -      Description value for the CLI credential to look for
        [exists] -        Boolean indicating if the credential is expected to exist or not (true/false)

        Confirms whether or not the specified CLI credential exists.
        """
        args = {"exists": exists,
                "cli_desc": cli_desc}

        return self.execute_keyword(element_name, args, self.cmd.CLICREDENTIALS_CONFIRM_CREDENTIAL_EXISTS, **kwargs)
