from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ProfilesConstants import ProfilesConstants


class UiProfilesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiProfilesKeywords, self).__init__()
        self.api_const = self.constants.API_PROFILES
        self.cmd = ProfilesConstants()

    def profiles_select_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects the specified sub tab of the Profiles tab.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_SELECT_SUB_TAB, **kwargs)

    def profiles_set_default_profile(self, element_name, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name]  - Name of the profile to set as the default profile

        Sets the default profile to the specified profile.
        """
        args = {"profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_SET_DEFAULT_PROFILE, **kwargs)

    def profiles_set_default_access_control_engine_profile(self, element_name, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name]  - Name of the profile to set as the default access control engine profile

        Sets the default access control engine profile to the specified profile.
        """
        args = {"profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_SET_DEFAULT_ACCESS_CONTROL_ENGINE_PROFILE,
                                    **kwargs)

    def profiles_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Refreshes the profile table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_REFRESH, **kwargs)

    def profiles_select_profile(self, element_name, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name]  - Name of the profile to select

        Selects the specified profile in the table.
        """
        args = {"profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_SELECT_PROFILE, **kwargs)

    def profiles_toolbar_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Add" toolbar button.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_TOOLBAR_CLICK_ADD, **kwargs)

    def profiles_toolbar_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Edit" toolbar button.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_TOOLBAR_CLICK_EDIT, **kwargs)

    def profiles_toolbar_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Delete" toolbar button.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_TOOLBAR_CLICK_DELETE, **kwargs)

    def profiles_dialog_add_profile_set_profile_name(self, element_name, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name]  - Name of the profile to set

        Sets the "Profile Name" field in the Add Profile dialog.
        """
        args = {"profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_PROFILE_NAME, **kwargs)

    def profiles_dialog_add_profile_set_snmp_version(self, element_name, snmp_version, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_version]  - SNMP Version to select (SNMPv1, SNMPv2, SNMPv3)

        Sets the "SNMP Version" field in the Add Profile dialog.
        """
        args = {"snmp_version": snmp_version}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_SNMP_VERSION, **kwargs)

    def profiles_dialog_add_profile_set_read(self, element_name, read_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [read_access]   - Value of the Read field (e.g., public_v1, private_v1, etc.)

        Sets the "Read" field in the Add Profile dialog.
        """
        args = {"read_access": read_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_READ, **kwargs)

    def profiles_dialog_add_profile_set_write(self, element_name, write_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [write_access]  - Value of the Write field (e.g., public_v1, private_v1, etc.)

        Sets the "Write" field in the Add Profile dialog.
        """
        args = {"write_access": write_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_WRITE, **kwargs)

    def profiles_dialog_add_profile_set_max_access(self, element_name, max_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [max_access]    - Value of the Max Access field (e.g., public_v1, private_v1, etc.)

        Sets the "Max Access" field in the Add Profile dialog.
        """
        args = {"max_access": max_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_MAX_ACCESS, **kwargs)

    def profiles_dialog_add_profile_set_read_security(self, element_name, read_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [read_sec]      - Value of the Read Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Read Security" field in the Add Profile dialog.
        """
        args = {"read_sec": read_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_READ_SECURITY,
                                    **kwargs)

    def profiles_dialog_add_profile_set_write_security(self, element_name, write_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [write_sec]     - Value of the Write Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Write Security" field in the Add Profile dialog.
        """
        args = {"write_sec": write_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_WRITE_SECURITY,
                                    **kwargs)

    def profiles_dialog_add_profile_set_max_security(self, element_name, max_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [max_sec]       - Value of the Max Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Max Security" field in the Add Profile dialog.
        """
        args = {"max_sec": max_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_MAX_SECURITY, **kwargs)

    def profiles_dialog_add_profile_set_cli_credential(self, element_name, cli_cred, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_cred]      - Name of the CLI Credential to select in the drop down

        Sets the "CLI Credential" field in the Add Profile dialog.
        """
        args = {"cli_cred": cli_cred}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_ADD_PROFILE_SET_CLI_CREDENTIAL,
                                    **kwargs)

    def profiles_dialog_add_profile_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button in the Add Profile dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_ADD_PROFILE_CLICK_SAVE, **kwargs)

    def profiles_dialog_add_profile_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button in the Add Profile dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_ADD_PROFILE_CLICK_CANCEL, **kwargs)

    def profiles_dialog_edit_profile_set_read(self, element_name, read_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [read_access]   - Value of the Read field (e.g., public_v1, private_v1, etc.)

        Sets the "Read" field in the Edit Profile dialog.
        """
        args = {"read_access": read_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_READ, **kwargs)

    def profiles_dialog_edit_profile_set_write(self, element_name, write_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [write_access]  - Value of the Write field (e.g., public_v1, private_v1, etc.)

        Sets the "Write" field in the Edit Profile dialog.
        """
        args = {"write_access": write_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_WRITE, **kwargs)

    def profiles_dialog_edit_profile_set_max_access(self, element_name, max_access, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [max_access]    - Value of the Max Access field (e.g., public_v1, private_v1, etc.)

        Sets the "Max Access" field in the Edit Profile dialog.
        """
        args = {"max_access": max_access}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_MAX_ACCESS, **kwargs)

    def profiles_dialog_edit_profile_set_read_security(self, element_name, read_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [read_sec]      - Value of the Read Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Read Security" field in the Edit Profile dialog.
        """
        args = {"read_sec": read_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_READ_SECURITY,
                                    **kwargs)

    def profiles_dialog_edit_profile_set_write_security(self, element_name, write_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [write_sec]     - Value of the Write Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Write Security" field in the Edit Profile dialog.
        """
        args = {"write_sec": write_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_WRITE_SECURITY,
                                    **kwargs)

    def profiles_dialog_edit_profile_set_max_security(self, element_name, max_sec, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [max_sec]       - Value of the Max Security field (NoAuthNoPriv, AuthNoPriv, AuthPriv)

        Sets the "Max Security" field in the Edit Profile dialog.
        """
        args = {"max_sec": max_sec}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_MAX_SECURITY,
                                    **kwargs)

    def profiles_dialog_edit_profile_set_cli_credential(self, element_name, cli_cred, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [cli_cred]      - Name of the CLI Credential to select in the drop down

        Sets the "CLI Credential" field in the Edit Profile dialog.
        """
        args = {"cli_cred": cli_cred}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_SET_CLI_CREDENTIAL,
                                    **kwargs)

    def profiles_dialog_edit_profile_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button in the Edit Profile dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_CLICK_SAVE, **kwargs)

    def profiles_dialog_edit_profile_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button in the Edit Profile dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_EDIT_PROFILE_CLICK_CANCEL, **kwargs)

    def profiles_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Yes button in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_CONFIRM_DELETE_CLICK_YES, **kwargs)

    def profiles_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the No button in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.PROFILES_DIALOG_CONFIRM_DELETE_CLICK_NO, **kwargs)

    def profiles_confirm_profile_exists(self, element_name, profile_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name]  - Name of the profile to confirm the existence of
        [exists]        - Boolean indicating if the profile is expected to exist or not (true/false)

        Confirms whether or not the specified profile exists.
        """
        args = {"profile_name": profile_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.PROFILES_CONFIRM_PROFILE_EXISTS, **kwargs)
