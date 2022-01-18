from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ClicredentialsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Clicredentials(ClicredentialsBase):

    def clicredentials_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#authCredentialsGridId pagingtoolbar #refresh => .x-btn-icon-el")

        return ui_cmd_obj

    def clicredentials_select_credential(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#authCredentialsGridId tableview => .x-grid-cell-inner:textEquals(' +
                               str(arg_dict['cli_desc']) + ')')

        return ui_cmd_obj

    def clicredentials_toolbar_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#authCredentialsGridId #addCliCredButton => .x-btn-button")

        return ui_cmd_obj

    def clicredentials_toolbar_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#authCredentialsGridId #editSelectedCliCred => .x-btn-button")

        return ui_cmd_obj

    def clicredentials_toolbar_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#authCredentialsGridId #deleteSelectedCliCred => .x-btn-button")

        return ui_cmd_obj

    def clicredentials_dialog_add_set_description(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_description(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_set_user_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_user_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_set_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_set_login_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_login_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_set_enable_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_enable_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_set_configuration_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_configuration_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_add_click_login_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_login_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_add_click_enable_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_enable_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_add_click_configuration_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_configuration_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_add_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_add_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_description(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_description(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_user_name(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_user_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_type(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_type(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_login_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_login_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_enable_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_enable_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_set_configuration_password(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_configuration_password(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def clicredentials_dialog_edit_click_login_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_login_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_edit_click_enable_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_enable_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_edit_click_configuration_password_eye(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_configuration_password_eye(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_edit_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_edit_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def clicredentials_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=Yes] => .x-btn-button")

        return ui_cmd_obj

    def clicredentials_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=No] => .x-btn-button")

        return ui_cmd_obj

    def clicredentials_confirm_credential_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#authCredentialsGridId tableview',
                                                           '[0]', 'description', arg_dict['cli_desc'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nCLI Credential '" + arg_dict['cli_desc'] + "' exists.\n")
        else:
            self.logger.log_info("\nCLI Credential '" + arg_dict['cli_desc'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    # HELPER METHODS

    def add_edit_dialog_set_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['cli_desc']),
                                    "cliCredentialDlg #credentialFrame #cliCredentialDescription => .x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_user_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                    "cliCredentialDlg #credentialFrame textfield[name=usernameId] => .x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "cliCredentialDlg #credentialFrame combobox[name=typeId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combobox[name=typeId].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['cli_type']) + ")")

        return ui_cmd_obj

    def add_edit_dialog_set_login_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['login_pwd']),
                                    "cliCredentialDlg #credentialFrame passwordfield[name=loginPasswdId] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_enable_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['enable_pwd']),
                                    "cliCredentialDlg #credentialFrame passwordfield[name=enablePasswdId] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_set_configuration_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['config_pwd']),
                                    "cliCredentialDlg #credentialFrame passwordfield[name=configPasswordId] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def add_edit_dialog_click_login_password_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, "cliCredentialDlg #credentialFrame passwordfield[name=loginPasswdId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_click_enable_password_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               "cliCredentialDlg #credentialFrame passwordfield[name=enablePasswdId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_click_configuration_password_eye(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               "cliCredentialDlg #credentialFrame passwordfield[name=configPasswordId] => .fa")

        return ui_cmd_obj

    def add_edit_dialog_save(self, ui_cmd_obj):
        # Handle the case where the Save button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "cliCredentialDlg button[text=Save]", "[0].disabled")

        # Only click the button if it is enabled
        if not ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, 'cliCredentialDlg button[text=Save] => .x-btn-inner-blue-small')
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
            self.logger.log_info("\nSave button is disabled - clicking Cancel instead\n")
            self.ext_builder.click(ui_cmd_obj, 'cliCredentialDlg button[text=Cancel] => .x-btn-inner-default-small')
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def add_edit_dialog_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'cliCredentialDlg button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj
