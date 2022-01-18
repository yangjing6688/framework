from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as OptionsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Options(OptionsBase):
    def options_expand_option(self, ui_cmd_obj, arg_dict):
        self.ext_builder.expand_tree_node(ui_cmd_obj, '#optionsNavigationTree', '[0]', 'name', arg_dict['option_name'])

        return ui_cmd_obj

    def options_collapse_option(self, ui_cmd_obj, arg_dict):
        self.ext_builder.collapse_tree_node(ui_cmd_obj, '#optionsNavigationTree', '[0]', 'name',
                                            arg_dict['option_name'])

        return ui_cmd_obj

    def options_select_option(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_tree_node(ui_cmd_obj, '#optionsNavigationTree', '[0]', 'name', arg_dict['option_name'])

        return ui_cmd_obj

    def options_restore_defaults(self, ui_cmd_obj, arg_dict):
        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#optionsActionToolbar button[actionId=restoreOptionsDefaults]",
                                                      "[0].disabled")
        # Only click the button if it is enabled
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj,
                                   '#optionsActionToolbar button[actionId=restoreOptionsDefaults] => .x-btn-button')
        else:
            self.logger.log_info("\nRestore Defaults button is disabled.\n")

        return ui_cmd_obj

    def options_reset(self, ui_cmd_obj, arg_dict):
        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#optionsActionToolbar button[actionId=resetOptions]",
                                                      "[0].disabled")
        # Only click the button if it is enabled
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#optionsActionToolbar button[actionId=resetOptions] => .x-btn-button')
        else:
            self.logger.log_info("\nReset button is disabled.\n")

        return ui_cmd_obj

    def options_save(self, ui_cmd_obj, arg_dict):
        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#optionsActionToolbar button[actionId=saveOptions]",
                                                      "[0].disabled")
        # Only click the button if it is enabled
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#optionsActionToolbar button[actionId=saveOptions] => .x-btn-button')
        else:
            self.logger.log_info("\nSave button is disabled.\n")

        return ui_cmd_obj

    def options_set_extreme_networks_updates_credentials(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                    'textfield[name=WebServerUpdateUsername] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['pwd']),
                                    'passwordfield[name=WebServerUpdatePassword] => .x-form-text')

        return ui_cmd_obj

    def options_set_db_backup_file_path(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'textfield[name=dboDatabaseBackupFilePath] => .x-form-text')

        return ui_cmd_obj

    def options_set_db_backup_include_additional_data(self, ui_cmd_obj, arg_dict):
        # Only click the check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[name=dboBackupReportingDatabase]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["option_value"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=dboBackupReportingDatabase] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["option_value"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=dboBackupReportingDatabase] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Include Additional Data' check button already at desired value.\n")

        return ui_cmd_obj

    def options_set_db_backup_schedule_file_format(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=dboDatabaseBackupDateFormat] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=dboDatabaseBackupDateFormat].getPicker() => '
                                           '.x-boundlist-item:contains(' + arg_dict['option_value'] + ')')

        return ui_cmd_obj

    def options_set_db_backup_schedule_occurrence(self, ui_cmd_obj, arg_dict):
        # Default the day to "Every Day" - this will deselect all current day selections
        # Only click the check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'checkbox[itemId=everyday]', '[0].rawValue')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, 'checkbox[itemId=everyday] => .x-form-cb-input')

        # If nothing was specified, deselect the Every Day check box;  otherwise, select each day, if not "Every Day"
        if arg_dict['on_day'] == "":
            self.ext_builder.click(ui_cmd_obj, 'checkbox[itemId=everyday] => .x-form-cb-input')
        elif arg_dict['on_day'] != "Every Day":
            day_list = arg_dict['on_day'].split(",")
            for day in day_list:
                self.ext_builder.click(ui_cmd_obj, 'checkbox[boxLabel=' + day + '] => .x-form-cb-input')

        # Set the "At" time, if days were specified
        if arg_dict['on_day'] != "":
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['at_time']),
                                        'timefield[name=timeofday] => .x-form-text')

        return ui_cmd_obj

    def options_set_db_backup_schedule_limit_backups(self, ui_cmd_obj, arg_dict):
        # Only click the check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'checkboxfield[name=dboLimitBackups]', '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["limit_files"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=dboLimitBackups] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["limit_files"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=dboLimitBackups] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Limit Number of Backups Saved' check button already at desired value.\n")

        # Only set the Maximum Backups Saved if the Limit Number of Backups Saved is selected
        if StringUtils.string_to_boolean(arg_dict["limit_files"]) is True:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['max_files']),
                                        'numberfield[name=dboMaxNumberDatabaseBackupsKept] => .x-form-text')

        return ui_cmd_obj

    def options_set_ftp_file_transfer(self, ui_cmd_obj, arg_dict):
        # Only click the Anonymous check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'checkboxfield[name=invsrvroFtpUseAnonymous]', '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroFtpUseAnonymous] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroFtpUseAnonymous] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Anonymous' check button already at desired value.\n")

        # Only set the user name and password if this is not an Anonymous user
        if StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                        'textfield[name=invsrvroFtpUsername] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['pwd']),
                                        'passwordfield[name=invsrvroFtpPassword] => .x-form-text')

        # Only set the firmware directory if it was specified
        if arg_dict["fw_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['fw_dir']),
                                        'textfield[name=invsrvroFtpServerFirmwareDir] => .x-form-text')

        # Only set the root directory if it was specified
        if arg_dict["root_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['root_dir']),
                                        'textfield[name=invsrvroFtpServerRootDir] => .x-form-text')

        # Only click the Use EMC check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'checkboxfield[name=invsrvroFtpUseNetsightServerIP]',
                                                      '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroFtpUseNetsightServerIP] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroFtpUseNetsightServerIP] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Use EMC' check button already at desired value.\n")

        # Only set the server IP if use_emc_ip is false
        if StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False and arg_dict["server_ip"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_ip']),
                                        'textfield[name=invsrvroFtpServerIp] => .x-form-text')

        # Set the server port, if specified
        if arg_dict["server_port"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_port']),
                                        'numberfield[name=invsrvroFtpServerPort] => .x-form-text')

        return ui_cmd_obj

    def options_set_scp_file_transfer(self, ui_cmd_obj, arg_dict):
        # Only click the Anonymous check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'checkboxfield[name=invsrvroScpUseAnonymous]', '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroScpUseAnonymous] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroScpUseAnonymous] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Anonymous' check button already at desired value.\n")

        # Only set the user name and password if this is not an Anonymous user
        if StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                        'textfield[name=invsrvroScpUsername] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['pwd']),
                                        'passwordfield[name=invsrvroScpPassword] => .x-form-text')

        # Only set the firmware directory if it was specified
        if arg_dict["fw_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['fw_dir']),
                                        'textfield[name=invsrvroScpServerFirmwareDir] => .x-form-text')

        # Only set the root directory if it was specified
        if arg_dict["root_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['root_dir']),
                                        'textfield[name=invsrvroScpServerRootDir] => .x-form-text')

        # Only click the Use EMC check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'checkboxfield[name=invsrvroScpUseNetsightServerIP]',
                                                      '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroScpUseNetsightServerIP] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroScpUseNetsightServerIP] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Use EMC' check button already at desired value.\n")

        # Only set the server IP if use_emc_ip is false
        if StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False and arg_dict["server_ip"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_ip']),
                                        'textfield[name=invsrvroScpServerIp] => .x-form-text')

        # Set the server port, if specified
        if arg_dict["server_port"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_port']),
                                        'numberfield[name=invsrvroScpServerPort] => .x-form-text')

        return ui_cmd_obj

    def options_set_sftp_file_transfer(self, ui_cmd_obj, arg_dict):
        # Only click the Anonymous check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'checkboxfield[name=invsrvroSftpUseAnonymous]', '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is True:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroSftpUseAnonymous] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[name=invsrvroSftpUseAnonymous] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Anonymous' check button already at desired value.\n")

        # Only set the user name and password if this is not an Anonymous user
        if StringUtils.string_to_boolean(arg_dict["anonymous_user"]) is False:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_name']),
                                        'textfield[name=invsrvroSftpUsername] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['pwd']),
                                        'passwordfield[name=invsrvroSftpPassword] => .x-form-text')

        # Only set the firmware directory if it was specified
        if arg_dict["fw_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['fw_dir']),
                                        'textfield[name=invsrvroSftpServerFirmwareDir] => .x-form-text')

        # Only set the root directory if it was specified
        if arg_dict["root_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['root_dir']),
                                        'textfield[name=invsrvroSftpServerRootDir] => .x-form-text')

        # Only click the Use EMC check button if it is not already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'checkboxfield[name=invsrvroSftpUseNetsightServerIP]',
                                                      '[0].rawValue')
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   'checkboxfield[name=invsrvroSftpUseNetsightServerIP] => .x-form-cb-input')
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   'checkboxfield[name=invsrvroSftpUseNetsightServerIP] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Use EMC' check button already at desired value.\n")

        # Only set the server IP if use_emc_ip is false
        if StringUtils.string_to_boolean(arg_dict["use_emc_ip"]) is False and arg_dict["server_ip"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_ip']),
                                        'textfield[name=invsrvroSftpServerIp] => .x-form-text')

        # Set the server port, if specified
        if arg_dict["server_port"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_port']),
                                        'numberfield[name=invsrvroSftpServerPort] => .x-form-text')

        return ui_cmd_obj

    def options_set_tftp_file_transfer(self, ui_cmd_obj, arg_dict):
        # Only set the firmware directory if it was specified
        if arg_dict["fw_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['fw_dir']),
                                        'textfield[name=invsrvroTftpServerFirmwareDir] => .x-form-text')

        # Only set the root directory if it was specified
        if arg_dict["root_dir"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['root_dir']),
                                        'textfield[name=invsrvroTftpServerRootDir] => .x-form-text')

        # Only set the server IP if it was specified
        if arg_dict["server_ip"] != '':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['server_ip']),
                                        'textfield[name=invsrvroTftpServerIPAddress] => .x-form-text')

        return ui_cmd_obj

    def options_set_device_tree_name_format(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=deviceDisplayFormat] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=deviceDisplayFormat].getPicker() => '
                                           '.x-boundlist-item:contains(' + arg_dict['option_value'] + ')')

        return ui_cmd_obj

    def options_set_access_control_collection_poll_rate(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=nacPollRate] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=nacPollRate] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=nacPollRate] combobox[inputType=text].getPicker() '
                                           '=> .x-boundlist-item:contains(' + arg_dict['option_units'] + ')')

        return ui_cmd_obj

    def options_set_device_collection_poll_rate(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=ovcDCsysPollRate] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcDCsysPollRate] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcDCsysPollRate] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['option_units'] + ')')

        return ui_cmd_obj

    def options_set_interface_collection_poll_rate(self, ui_cmd_obj, arg_dict):
        # Set the option value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=ovcICifPollRate] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcICifPollRate] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcICifPollRate] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['option_units'] + ')')

        return ui_cmd_obj

    def options_set_wireless_collection_access_point_poll_rate(self, ui_cmd_obj, arg_dict):
        # Set the option value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=ovcWapPollRate] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcWapPollRate] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcWapPollRate] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['option_units'] + ')')

        return ui_cmd_obj

    def options_set_wireless_collection_controller_poll_rate(self, ui_cmd_obj, arg_dict):
        # Set the option value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=ovcWcontrollerPollRate] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcWcontrollerPollRate] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=ovcWcontrollerPollRate] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['option_units'] + ')')

        return ui_cmd_obj

    def options_set_status_polling_default_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=spoDefaultPollGroup] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=spoDefaultPollGroup].getPicker() => '
                                           '.x-boundlist-item:contains(' + arg_dict['option_value'] + ')')

        return ui_cmd_obj

    def options_set_status_polling_poll_group_1(self, ui_cmd_obj, arg_dict):
        # Set the group name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['group_name']),
                                    'textfield[name=spoPollGroup1Name] => .x-form-text')

        # Set the group interval value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['interval_val']),
                                    'numberfield[name=spoGroup1Interval] => .x-form-text')

        # Set the group interval units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup1Interval] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup1Interval] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['interval_units'] + ')')

        return ui_cmd_obj

    def options_set_status_polling_poll_group_2(self, ui_cmd_obj, arg_dict):
        # Set the group name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['group_name']),
                                    'textfield[name=spoPollGroup2Name] => .x-form-text')

        # Set the group interval value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['interval_val']),
                                    'numberfield[name=spoGroup2Interval] => .x-form-text')

        # Set the group interval units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup2Interval] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup2Interval] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['interval_units'] + ')')

        return ui_cmd_obj

    def options_set_status_polling_poll_group_3(self, ui_cmd_obj, arg_dict):
        # Set the group name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['group_name']),
                                    'textfield[name=spoPollGroup3Name] => .x-form-text')

        # Set the group interval value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['interval_val']),
                                    'numberfield[name=spoGroup3Interval] => .x-form-text')

        # Set the group interval units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup3Interval] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=spoGroup3Interval] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['interval_units'] + ')')

        return ui_cmd_obj

    def options_set_trap_snmpv1_credential_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V1CredentialName] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V1CredentialName].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def options_set_trap_snmpv2_credential_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V2CredentialName] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V2CredentialName].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def options_set_trap_snmpv3_credential_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V3CredentialName] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=V3CredentialName].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def options_set_web_server_timeout(self, ui_cmd_obj, arg_dict):
        # Set the option value
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['option_value']),
                                    'numberfield[name=httpSessionTimeoutOpt] => .x-form-text')

        # Set the option units
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=httpSessionTimeoutOpt] combobox[inputType=text] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'timeintervalfield[name=httpSessionTimeoutOpt] '
                                           'combobox[inputType=text].getPicker() => .x-boundlist-item:contains(' +
                                           arg_dict['option_units'] + ')')

        return ui_cmd_obj
