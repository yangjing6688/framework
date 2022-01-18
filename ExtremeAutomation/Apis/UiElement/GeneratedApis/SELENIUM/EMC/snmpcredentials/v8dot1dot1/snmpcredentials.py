from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as SnmpcredentialsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Snmpcredentials(SnmpcredentialsBase):

    def snmpcredentials_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#snmpCredentialsGridId pagingtoolbar #refresh => .x-btn-icon-el")

        return ui_cmd_obj

    def snmpcredentials_select_credential(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj, '#snmpCredentialsGridId tableview', '[0]', 'name',
                                                  arg_dict['cred_name'])

        return ui_cmd_obj

    def snmpcredentials_toolbar_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#snmpCredentialsGridId #addSNMPCredButton => .x-btn-button")

        return ui_cmd_obj

    def snmpcredentials_toolbar_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#snmpCredentialsGridId #editSelectedSnmpCred => .x-btn-button")

        return ui_cmd_obj

    def snmpcredentials_toolbar_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#snmpCredentialsGridId #deleteSelectedSnmpCred => .x-btn-button")

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_credential_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_credential_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_snmp_version(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_snmp_version(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_community_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_community_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_user_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_user_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_authentication_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_authentication_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_authentication_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_authentication_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_privacy_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_privacy_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_set_privacy_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_privacy_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_click_community_name_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_community_name_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_click_authentication_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_authentication_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_click_privacy_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_privacy_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_add_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_credential_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_snmp_version(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_snmp_version(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_community_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_community_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_user_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_user_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_authentication_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_authentication_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_authentication_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_authentication_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_privacy_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_privacy_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_set_privacy_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_privacy_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_click_community_name_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_community_name_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_click_authentication_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_authentication_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_click_privacy_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_privacy_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_edit_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def snmpcredentials_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=Yes] => .x-btn-button")

        return ui_cmd_obj

    def snmpcredentials_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=No] => .x-btn-button")

        return ui_cmd_obj

    def snmpcredentials_confirm_credential_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#snmpCredentialsGridId tableview',
                                                           '[0]', 'name', arg_dict['cred_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nSNMP Credential '" + arg_dict['cred_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nSNMP Credential '" + arg_dict['cred_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    # HELPER METHODS

    def add_edit_dialog_set_credential_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['cred_name']),
                                    "credentialDlg #credentialFrame #snmpCredentialName => .x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_snmp_version(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "credentialDlg #credentialFrame combobox[name=snmpVersionId] => "
                                           ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combobox[name=snmpVersionId].getPicker() => "
                                           ".x-boundlist-item:contains(" + str(arg_dict['snmp_version']) + ")")

        return ui_cmd_obj

    def add_edit_dialog_set_community_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['comm_name']),
                                    "credentialDlg #credentialFrame passwordfield[name=communityNameId] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_user_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                    "credentialDlg #credentialFrame textfield[name=usernameId] => .x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_authentication_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "credentialDlg #credentialFrame combobox[name=authenticationId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=authenticationId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['auth_type']) + ")")

        return ui_cmd_obj

    def add_edit_dialog_set_authentication_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['auth_pwd']),
                                    "credentialDlg #credentialFrame passwordfield[name=authPasswdId] => .x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_privacy_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "credentialDlg #credentialFrame combobox[name=privTypeId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=privTypeId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['priv_type']) + ")")

        return ui_cmd_obj

    def add_edit_dialog_set_privacy_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['priv_pwd']),
                                    "credentialDlg #credentialFrame passwordfield[name=privacyPasswdId] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_click_community_name_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, "credentialDlg #credentialFrame passwordfield[name=communityNameId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_click_authentication_password_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, "credentialDlg #credentialFrame passwordfield[name=authPasswdId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_click_privacy_password_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, "credentialDlg #credentialFrame passwordfield[name=privacyPasswdId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_save(self, ui_cmd_obj):
        # Handle the case where the Save button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "credentialDlg button[text=Save]", "[0].disabled")

        # Only click the button if it is enabled
        if not ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, 'credentialDlg button[text=Save] => .x-btn-inner-blue-small')
            ui_cmd_obj.error_state = False

            # Handle any error that may have occurred during save
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0]")
            if ui_cmd_obj.return_data is not None:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0].hidden")
                if ui_cmd_obj.return_data is False:
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]",
                                                                  "[0].msg.html")
                    self.logger.log_info("\nSAVE FAILED: " + ui_cmd_obj.return_data + "\n")
                    if "already in use" in ui_cmd_obj.return_data:
                        # PASS - already exists so mark as passed and just continue
                        ui_cmd_obj.error_state = False
                    else:
                        # FAIL - another error condition so mark as failed
                        ui_cmd_obj.error_state = True

                    # Click OK in the error dialog
                    self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

                    # Click Cancel in the parent action dialog
                    self.add_edit_dialog_cancel(ui_cmd_obj)
        else:
            self.logger.log_info("\nSave button is disabled - clicking Cancel instead.\n")
            self.ext_builder.click(ui_cmd_obj, 'credentialDlg button[text=Cancel] => .x-btn-inner-default-small')
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def add_edit_dialog_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'credentialDlg button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj
