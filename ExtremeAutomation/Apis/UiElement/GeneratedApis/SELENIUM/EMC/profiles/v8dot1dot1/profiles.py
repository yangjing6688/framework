from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ProfilesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Profiles(ProfilesBase):

    def profiles_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'tab[text=' + str(arg_dict['tab_name']) + '] => .x-tab-inner')

        return ui_cmd_obj

    def profiles_set_default_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId combo[fieldLabel=Default Profile] => "
                                           ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId combo[fieldLabel=Default Profile] "
                                           "boundlist => "
                                           ".x-boundlist-item:textEquals(" + str(arg_dict['profile_name']) + ")")

        return ui_cmd_obj

    def profiles_set_default_access_control_engine_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId "
                                           "combo[fieldLabel=Default Access Control Engine Profile] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId "
                                           "combo[fieldLabel=Default Access Control Engine Profile] boundlist => "
                                           ".x-boundlist-item:textEquals(" + str(arg_dict['profile_name']) + ")")

        return ui_cmd_obj

    def profiles_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId pagingtoolbar #refresh => .x-btn-icon-el")

        return ui_cmd_obj

    def profiles_select_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj, '#adminProfilesCredentialsGridId gridview', '[0]', "name",
                                                  arg_dict['profile_name'])

        return ui_cmd_obj

    def profiles_toolbar_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId #addProfileButton => "
                                           ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def profiles_toolbar_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId #editSelectedProfile => "
                                           ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def profiles_toolbar_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#adminProfilesCredentialsGridId #deleteSelectedProfile => "
                                           ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def profiles_dialog_add_profile_set_profile_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['profile_name']),
                                    '#profileFrame #accessProfileName => .x-form-text')
        return ui_cmd_obj

    def profiles_dialog_add_profile_set_snmp_version(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combobox[name=snmpVersionId] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combobox[name=snmpVersionId] boundlist => '
                                           ':textEquals(' + str(arg_dict['snmp_version']) + ')')
        return ui_cmd_obj

    def profiles_dialog_add_profile_set_read(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_read_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_write(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_write_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_max_access(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_max_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_read_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_read_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_write_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_write_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_max_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_max_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_set_cli_credential(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_cli_credential(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_add_profile_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def profiles_dialog_add_profile_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_read(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_read_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_write(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_write_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_max_access(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_max_access(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_read_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_read_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_write_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_write_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_max_security(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_max_security(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_set_cli_credential(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_set_cli_credential(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_save(ui_cmd_obj)

        return ui_cmd_obj

    def profiles_dialog_edit_profile_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def profiles_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=Yes] => .x-btn-button")

        return ui_cmd_obj

    def profiles_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=No] => .x-btn-button")

        return ui_cmd_obj

    def profiles_confirm_profile_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#adminProfilesCredentialsGridId tableview',
                                                           '[0]', 'name', arg_dict['profile_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nProfile '" + arg_dict['profile_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nProfile '" + arg_dict['profile_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    # HELPER METHODS

    def add_edit_dialog_set_read_access(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=readCredId] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=readCredId] boundlist => '
                                           ':textEquals(' + str(arg_dict['read_access']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_write_access(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=writeCredId] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=writeCredId] boundlist => '
                                           ':textEquals(' + str(arg_dict['write_access']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_max_access(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=maxAccessCredId] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame snmpCredentialsCombobox[name=maxAccessCredId] boundlist => '
                                           ':textEquals(' + str(arg_dict['max_access']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_read_security(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=readSecLvlId] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=readSecLvlId] boundlist => '
                                           ':textEquals(' + str(arg_dict['read_sec']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_write_security(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=writeSecLvlId] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=writeSecLvlId] boundlist => '
                                           ':textEquals(' + str(arg_dict['write_sec']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_max_security(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=maxAccessSecLvlId] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame combo[name=maxAccessSecLvlId] boundlist => '
                                           ':textEquals(' + str(arg_dict['max_sec']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_set_cli_credential(self, ui_cmd_obj, arg_dict):
        # Have to click in the field first since the drop down is built on click (lazy-load)
        self.ext_builder.click(ui_cmd_obj, '#profileFrame cliCredentialsCombobox[name=cliCredId] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#profileFrame cliCredentialsCombobox[name=cliCredId] boundlist => '
                                           ':textEquals(' + str(arg_dict['cli_cred']) + ')')
        return ui_cmd_obj

    def add_edit_dialog_save(self, ui_cmd_obj):
        # Handle the case where the Save button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "AccessProfileDlg button[text=Save]", "[0].disabled")

        # Only click the button if it is enabled
        if not ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, 'AccessProfileDlg button[text=Save] => .x-btn-inner-blue-small')
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
            self.ext_builder.click(ui_cmd_obj, 'AccessProfileDlg button[text=Cancel] => .x-btn-inner-default-small')
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def add_edit_dialog_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'AccessProfileDlg button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj
