from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ScriptsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Scripts(ScriptsBase):
    def scripts_select_script(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'scriptGrid gridview => '
                               '.x-grid-cell-inner:textEquals(' + str(arg_dict['script_name']) + ')')

        return ui_cmd_obj

    def scripts_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Add] => .x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[actionId=newScript][text=' + arg_dict['add_type'] + '] => '
                                           '.x-menu-item-text')

        return ui_cmd_obj

    def scripts_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=editScript] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_click_run(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runGridScript] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=deleteScript] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=refreshScriptGrid] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_click_import(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=importScriptGrid] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_click_export(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=exportScriptGrid] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scripts_dialog_add_select_tab(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_select_tab(ui_cmd_obj, arg_dict['tab_name'])
        return ui_cmd_obj

    def scripts_dialog_add_content_add_variable(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_add_variable(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_content_add_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_add_content(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_content_clear_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_clear_content(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_content_set_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_set_content(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_content_hide_line_numbers(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_show_hide_line_numbers(ui_cmd_obj, False)
        return ui_cmd_obj

    def scripts_dialog_add_content_show_line_numbers(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_show_hide_line_numbers(ui_cmd_obj, True)
        return ui_cmd_obj

    def scripts_dialog_add_content_click_variables(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_click_variables(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_runtime_set_comments(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_runtime_set_comments(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_runtime_set_timeout(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_runtime_set_timeout(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_clear_authorization_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_clear_authorization_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_permissions_select_authorization_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_authorization_groups(ui_cmd_obj, arg_dict['group_list'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_set_category(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_set_category(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_clear_menus(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_clear_menus(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_permissions_select_menus(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_menus(ui_cmd_obj, arg_dict['menu_list'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_click_remove_all_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_click_remove_all_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_permissions_click_select_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_click_select_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_permissions_device_group_expand_node(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_expand_device_group(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_device_group_select_node(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_device_group(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_add_permissions_device_group_click_ok(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_prermissions_device_group_click_ok(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_permissions_device_group_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_prermissions_device_group_click_cancel(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_save(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_click_save_as(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_save_as(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_click_run(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_run(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_add_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_cancel(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_select_tab(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_select_tab(ui_cmd_obj, arg_dict['tab_name'])
        return ui_cmd_obj

    def scripts_dialog_edit_overview_set_variable(self, ui_cmd_obj, arg_dict):
        # Determine which type of field this variable is for

        # Check if it is a combo first, since a combo is also made up of a textfield so that query will also be valid
        self.ext_builder.component_query(ui_cmd_obj, '#addEditScriptTabPanel combo[name=' + arg_dict['var_name'] + ']',
                                         '[0]')
        if ui_cmd_obj.return_data is not None:
            field_type = "combo"
        else:
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#addEditScriptTabPanel textfield[name=' + arg_dict['var_name'] + ']',
                                             '[0]')
            field_type = "text"

        # Set the variable according to what type of field it is
        if field_type == "text":
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['var_value'],
                                        '#addEditScriptTabPanel textfield[name=' + arg_dict['var_name'] + '] => '
                                        '.x-form-text')
        elif field_type == "combo":
            self.ext_builder.click(ui_cmd_obj,
                                   '#addEditScriptTabPanel combo[name=' + arg_dict['var_name'] + '] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj,
                                   '#addEditScriptTabPanel combo[name=' + arg_dict['var_name'] + '] boundlist => '
                                   ':textEquals(' + arg_dict['var_value'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nUnknown field type for variable: '" + arg_dict['var_name'] +
                                 "'.  Supported types are 'text' and 'combo'.\n")

        return ui_cmd_obj

    def scripts_dialog_edit_content_add_variable(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_add_variable(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_content_add_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_add_content(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_content_clear_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_clear_content(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_content_set_content(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_set_content(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_content_hide_line_numbers(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_show_hide_line_numbers(ui_cmd_obj, False)
        return ui_cmd_obj

    def scripts_dialog_edit_content_show_line_numbers(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_show_hide_line_numbers(ui_cmd_obj, True)
        return ui_cmd_obj

    def scripts_dialog_edit_content_click_variables(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_content_click_variables(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_runtime_set_comments(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_runtime_set_comments(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_runtime_set_timeout(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_runtime_set_timeout(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_clear_authorization_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_clear_authorization_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_select_authorization_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_authorization_groups(ui_cmd_obj, arg_dict['group_list'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_set_category(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_set_category(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_clear_menus(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_clear_menus(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_select_menus(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_menus(ui_cmd_obj, arg_dict['menu_list'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_click_remove_all_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_click_remove_all_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_click_select_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_click_select_groups(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_device_group_expand_node(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_expand_device_group(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_device_group_select_node(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_select_device_group(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_device_group_click_ok(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_prermissions_device_group_click_ok(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_permissions_device_group_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_prermissions_device_group_click_cancel(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_save(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_click_save_as(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_save_as(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_click_run(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_run(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_edit_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_click_cancel(ui_cmd_obj)
        return ui_cmd_obj

    def scripts_dialog_save_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'], '#scriptName => .x-form-text')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Save Script' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Save Script' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_save_set_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'],
                                            'textfield[name=scriptComment] => .x-form-text')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Save Script' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Save Script' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_save_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       'saveScriptWindow button[actionId=saveAsSaveClicked] => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Save Script' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Save Script' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_save_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'saveScriptWindow', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       'saveScriptWindow button[actionId=saveAsCancelClicked] => '
                                       '.x-btn-inner-default-small')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Save Script' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Save Script' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_replace_script_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Replace Script?]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Replace Script?]', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Replace Script?' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Replace Script?' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_replace_script_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Replace Script?]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Replace Script?]', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Replace Script?' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Replace Script?' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_save_success_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Success]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Success]', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nThe 'Success' dialog is not visible.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nThe 'Success' dialog does not exist.\n")

        return ui_cmd_obj

    def scripts_dialog_run_collapse_device_group(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data
            self.ext_builder.collapse_tree_node(ui_cmd_obj,
                                                dialog_id + ' #runScriptDeviceSelector treeview',
                                                '[0]', 'text', arg_dict['device_group'], exact_match=False)
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_expand_device_group(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data
            self.ext_builder.expand_tree_node(ui_cmd_obj,
                                              dialog_id + ' #runScriptDeviceSelector treeview',
                                              '[0]', 'text', arg_dict['device_group'], exact_match=False)
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_select_device_group(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data

            # Select the specified device group (this is different from select device as it does a partial match)
            self.ext_builder.click(ui_cmd_obj, dialog_id + ' #runScriptDeviceSelector treeview => '
                                                           '.x-tree-node-text:contains(' + arg_dict['device_group'] +
                                                           ')')

            # Click the right arrow button to move the group to the list on the right
            self.ext_builder.click(ui_cmd_obj, dialog_id + r' button[text=\&\#9658\;] => .x-btn-button')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_select_device(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data

            # Select the specified device
            self.ext_builder.click(ui_cmd_obj, dialog_id + ' #runScriptDeviceSelector treeview => '
                                   '.x-tree-node-text:textEquals(' + arg_dict['device_ip'] + ')')

            # Click the right arrow button to move the device to the list on the right
            self.ext_builder.click(ui_cmd_obj, dialog_id + r' button[text=\&\#9658\;] => .x-btn-button')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_move_device_up(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data

            self.ext_builder.click(ui_cmd_obj, dialog_id + ' tableview(true) => .x-grid-cell-inner:textEquals(' +
                                   arg_dict['device_ip'] + ')')
            self.ext_builder.click(ui_cmd_obj, dialog_id + r' button[text=\&\#9650\;] => .x-btn-button')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_move_device_down(self, ui_cmd_obj, arg_dict):
        self.get_run_script_dialog_id(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            dialog_id = ui_cmd_obj.return_data

            self.ext_builder.click(ui_cmd_obj, dialog_id + ' tableview(true) => .x-grid-cell-inner:textEquals(' +
                                   arg_dict['device_ip'] + ')')
            self.ext_builder.click(ui_cmd_obj, dialog_id + r' button[text=\&\#9660\;] => .x-btn-button')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_set_variable(self, ui_cmd_obj, arg_dict):
        # Determine which type of field this variable is for
        field_type = "unknown"

        # Check if it is a combo first, since a combo is also made up of a textfield so that query will also be valid
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel #runScriptSettingsPanel '
                                         'combo[name=' + arg_dict['var_name'] + ']', '[0]')
        if ui_cmd_obj.return_data is not None:
            field_type = "combo"
        else:
            self.ext_builder.component_query(ui_cmd_obj, '#runScriptTabPanel #runScriptSettingsPanel '
                                                         'textfield[name=' + arg_dict['var_name'] + ']', '[0]')
            field_type = "text"

        # Set the variable according to what type of field it is
        if field_type == "text":
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['var_value'],
                                        '#runScriptTabPanel #runScriptSettingsPanel '
                                        'textfield[name=' + arg_dict['var_name'] + '] => .x-form-text')
        elif field_type == "combo":
            self.ext_builder.click(ui_cmd_obj, '#runScriptTabPanel #runScriptSettingsPanel '
                                               'combo[name=' + arg_dict['var_name'] + '] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, '#runScriptTabPanel #runScriptSettingsPanel '
                                               'combo[name=' + arg_dict['var_name'] + '] boundlist => '
                                               ':textEquals(' + arg_dict['var_value'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nUnknown field type for variable '" + arg_dict['var_name'] +
                                 "'.  Supported types are 'text' and 'combo'.\n")

        return ui_cmd_obj

    def scripts_dialog_run_set_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'],
                                    '#runScriptTabPanel numberfield[name=oneViewScriptTimeout] => .x-form-text')

        return ui_cmd_obj

    def scripts_dialog_run_set_run_now_no_save(self, ui_cmd_obj, arg_dict):
        # Select the "Run now, don't save as task" radio button
        self.ext_builder.click(ui_cmd_obj, '#runScriptTabPanel radio[inputValue=runNow] => .x-form-cb-input')

        return ui_cmd_obj

    def scripts_dialog_run_set_save_and_run_now(self, ui_cmd_obj, arg_dict):
        # Select the "Save as a task and run now" radio button
        self.ext_builder.click(ui_cmd_obj, '#runScriptTabPanel radio[inputValue=saveTaskAndRunNow] => .x-form-cb-input')
        # Enter the Task Name
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['task_name'],
                                    '#runScriptTabPanel textfield[name=oneViewScriptTaskName] => .x-form-text')

        return ui_cmd_obj

    def scripts_dialog_run_set_save_and_run_later(self, ui_cmd_obj, arg_dict):
        # Select the "Save as a task.  I'll run later" radio button
        self.ext_builder.click(ui_cmd_obj,
                               '#runScriptTabPanel radio[inputValue=saveTaskAndRunLater] => .x-form-cb-input')
        # Enter the task name
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['task_name'],
                                    '#runScriptTabPanel textfield[name=oneViewScriptTaskName] => .x-form-text')

        return ui_cmd_obj

    def scripts_dialog_run_results_select_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid gridview => '
                               ':textEquals(' + str(arg_dict['device_ip']) + ')')

        return ui_cmd_obj

    def scripts_dialog_run_results_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid button => '
                               '.x-btn-inner-white-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_next(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptNext] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_back(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptBack] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_run(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptRun] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_execute_cli(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=executeCliCommands] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_finish(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptFinish] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_run_click_cancel(self, ui_cmd_obj, arg_dict):
        self.is_run_script_dialog_cli(ui_cmd_obj)
        if ui_cmd_obj.error_state is False:
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptCancel] => .x-btn-inner-default-small')
            else:
                self.ext_builder.click(ui_cmd_obj, 'button[text=Cancel] => .x-btn-inner-default-small')
        else:
            self.logger.log_info("\nRun Script dialog has unusable component ID.\n")

        return ui_cmd_obj

    def scripts_dialog_run_click_close(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptCancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_execute_cli_click_execute(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=executeCommands] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_execute_cli_click_abort(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=abortAllCommands] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_execute_cli_click_save_results(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=saveAllResults] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_execute_cli_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=closeCommandWindow] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_execute_cli_click_view_results(self, ui_cmd_obj, arg_dict):
        # Find the index of the device
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#cliRunnerTabPanel gridview', '[0]', 'ipAddress', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            self.logger.log_info("\nNEED TO CLICK VIEW RESULTS FOR ROW '" + str(row_index) + "'\n")

            # Click the "View Results" link
            # self.ext_builder.click(ui_cmd_obj,
            #                                '#cliRunnerTabPanel gridview => .x-grid-item:nth-of-type(' +
            # str(row_index) + ') a')
            # self.ext_builder.click(ui_cmd_obj,
            #                                '#cliRunnerTabPanel gridview => .x-grid-item:nth-of-type(' +
            # str(row_index) +
            #                                ') .x-grid-cell-inner:textEquals(View Results)')
            # self.ext_builder.click(ui_cmd_obj,
            #                                '#cliRunnerTabPanel gridview => .x-grid-item:nth-of-type(' +
            # str(row_index) +
            #                                ') .x-grid-cell-last .x-grid-cell-inner')
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not in the table.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_dialog_execute_cli_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#cliRunnerTabPanel tab[text=' + arg_dict['tab_name'] + '] => .x-tab-inner')

        return ui_cmd_obj

    def scripts_dialog_command_results_click_save_results(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#commandResultsWindow button[name=downloadResults] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_command_results_click_close(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#commandResultsWindow button[name=closeWin] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def scripts_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_dialog_variables_clear_scope(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#selectDevicesForCliRunner multicombobox[name=variableTypeCombo] => '
                               '.x-form-clear-trigger')
        return ui_cmd_obj

    def scripts_dialog_variables_select_scope(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#selectDevicesForCliRunner multicombobox[name=variableTypeCombo] => '
                               '.x-form-arrow-trigger')
        scope_list = str(arg_dict["scope_list"]).split(",")
        for scope_name in scope_list:
            self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                  '#selectDevicesForCliRunner multicombobox[name=variableTypeCombo]',
                                                  '[0]', 'variableType', scope_name)
            if ui_cmd_obj.return_data is True:
                self.ext_builder.click(ui_cmd_obj,
                                       '#selectDevicesForCliRunner multicombobox[name=variableTypeCombo] '
                                       'boundlist => :textEquals(' + scope_name + ')')
            else:
                self.logger.log_info("\nCould not find scope '" + scope_name + "'\n")

        return ui_cmd_obj

    def scripts_dialog_variables_select_variables(self, ui_cmd_obj, arg_dict):
        first_click = True
        var_list = str(arg_dict["var_list"]).split(",")
        for var in var_list:
            self.ext_builder.is_item_in_component(ui_cmd_obj, '#selectDevicesForCliRunner gridview', '[0]', 'name', var)
            if ui_cmd_obj.return_data is True:
                if first_click is True:
                    self.ext_builder.click(ui_cmd_obj,
                                           '#selectDevicesForCliRunner gridview => '
                                           '.x-grid-cell-inner:textEquals(' + var + ')')
                    first_click = False
                else:
                    self.ext_builder.click(ui_cmd_obj,
                                           '#selectDevicesForCliRunner gridview => '
                                           '.x-grid-cell-inner:textEquals(' + var + ')', shift=True)
            else:
                self.logger.log_info("\nCould not find variable with name '" + var + "'\n")

        return ui_cmd_obj

    def scripts_dialog_variables_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#selectDevicesForCliRunner button[name=closeWin] => .x-btn-inner-default-small')
        return ui_cmd_obj

    def scripts_dialog_variables_click_insert(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#selectDevicesForCliRunner button[name=insertVariables] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def scripts_dialog_import_click_close(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=closeBulkImportClicked] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def scripts_wait_for_script_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'scriptGrid gridview', '[0]', 'name',
                                                arg_dict['script_name'], None, arg_dict['wait_time'])
        return ui_cmd_obj

    def scripts_wait_for_script_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, 'scriptGrid gridview', '[0]', 'name',
                                                    arg_dict['script_name'], None, arg_dict['wait_time'])
        return ui_cmd_obj

    def scripts_wait_for_run_script_device_status(self, ui_cmd_obj, arg_dict):
        # Find the index of the device
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#runScriptTabPanel #validScriptResultsPanel '
                                             '#runningScriptDeviceGrid gridview', '[0]', 'oneViewScriptDeviceIpAddress',
                                             arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Wait for the status of the specified device to match what is expected
            self.ext_builder.wait_for_attribute(ui_cmd_obj,
                                                '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid '
                                                'gridview', '[0].store.data.items[' + str(row_index) +
                                                '].data.oneViewScriptDeviceStatus', arg_dict['the_value'],
                                                arg_dict['wait_time'])
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not in the Device List.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_wait_for_run_script_overall_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_attribute(ui_cmd_obj,
                                            "#runScriptTabPanel #validScriptResultsPanel #runningScriptOverallStatus",
                                            "[0].html", arg_dict['the_value'], arg_dict['wait_time'])

        return ui_cmd_obj

    def scripts_wait_for_execute_cli_results_status(self, ui_cmd_obj, arg_dict):
        # Find the index of the device
        self.ext_builder.get_component_index(ui_cmd_obj, '#cliRunnerTabPanel gridview', '[0]', 'ipAddress',
                                             arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Wait for the status of the specified device to match what is expected
            self.ext_builder.wait_for_attribute(ui_cmd_obj, '#cliRunnerTabPanel gridview',
                                                '[0].store.data.items[' + str(row_index) + '].data.status',
                                                arg_dict['the_value'], arg_dict['wait_time'])
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not in the table.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_wait_for_execute_cli_results_progress(self, ui_cmd_obj, arg_dict):
        # Find the index of the device
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#cliRunnerTabPanel gridview', '[0]', 'ipAddress', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Wait for the progress of the specified device to match what is expected
            self.ext_builder.wait_for_attribute(ui_cmd_obj, '#cliRunnerTabPanel gridview',
                                                '[0].store.data.items[' + str(row_index) + '].data.progress',
                                                arg_dict['the_value'], arg_dict['wait_time'])
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not in the table.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_confirm_dialog_add_permissions_selected_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_confirm_groups(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_confirm_dialog_edit_permissions_selected_groups(self, ui_cmd_obj, arg_dict):
        self.add_edit_dialog_permissions_confirm_groups(ui_cmd_obj, arg_dict['the_value'])
        return ui_cmd_obj

    def scripts_confirm_dialog_edit_overview_variable(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#addEditScriptTabPanel textfield[name=' + arg_dict['var_name'] + ']',
                                         '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#addEditScriptTabPanel textfield[name=' + arg_dict['var_name'] + ']',
                                             '[0].rawValue')

            if ui_cmd_obj.return_data == arg_dict['var_value']:
                self.logger.log_info("\nVariable '" + arg_dict['var_name'] + "' has the expected value of '" +
                                     arg_dict['var_value'] + "'.\n")
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nVariable '" + arg_dict['var_name'] +
                                     "' does not have the expected value of '" + arg_dict['var_value'] + "'.\n" +
                                     "The actual value is '" + ui_cmd_obj.return_data + "'\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nVariable '" + arg_dict['var_name'] + "' does not exist.\n")

        return ui_cmd_obj

    def scripts_confirm_run_verify_task_information(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel panel[title=Verify your run script information] '
                                         'ovdisplayfield[name=runScriptVerifyTaskInfo]', '[0].rawValue')

        if ui_cmd_obj.return_data == arg_dict['the_value']:
            self.logger.log_info("\nTask Information field is the expected value of '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nTask Information field is not the expected value of '" + arg_dict['the_value'] +
                                 "'.\n" + "Task Information field is '" + ui_cmd_obj.return_data + "'\n")

        return ui_cmd_obj

    def scripts_confirm_run_verify_script_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel panel[title=Verify your run script information] '
                                         'ovdisplayfield[name=runScriptVerifyScriptName]', '[0].rawValue')

        if ui_cmd_obj.return_data == arg_dict['the_value']:
            self.logger.log_info("\nScript Name field is the expected value of '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nScript Name field is not the expected value of '" + arg_dict['the_value'] + "'.\n" +
                                 "Script Name field is '" + ui_cmd_obj.return_data + "'\n")

        return ui_cmd_obj

    def scripts_confirm_run_verify_task_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel panel[title=Verify your run script information] '
                                         'ovdisplayfield[name=runScriptVerifyScriptTask]', '[0].rawValue')

        if ui_cmd_obj.return_data == arg_dict['the_value']:
            self.logger.log_info("\nTask Name field is the expected value of '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nTask Name field is not the expected value of '" + arg_dict['the_value'] + "'.\n" +
                                 "Task Name field is '" + ui_cmd_obj.return_data + "'\n")

        return ui_cmd_obj

    def scripts_confirm_run_verify_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel panel[title=Verify your run script information] '
                                         'ovdisplayfield[name=runScriptVerifyTimeout]', '[0].rawValue')

        if str(ui_cmd_obj.return_data) == arg_dict['the_value']:
            self.logger.log_info("\nTimeout field is the expected value of '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nTimeout field is not the expected value of '" + arg_dict['the_value'] + "'.\n" +
                                 "Timeout field is '" + str(ui_cmd_obj.return_data) + "'\n")

        return ui_cmd_obj

    def scripts_confirm_run_verify_device(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           '#runScriptTabPanel runScriptVerifyPanel gridview', '[0]',
                                                           'oneViewScriptDeviceIpAddress', arg_dict['device_ip'])

        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nDevice List contains '" + arg_dict['device_ip'] + "'\n")
            # PASS
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nDevice List does not contain '" + arg_dict['device_ip'] + "'\n")
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_confirm_run_script_device_status(self, ui_cmd_obj, arg_dict):
        # Find the index of the device
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid '
                                             'gridview', '[0]', 'oneViewScriptDeviceIpAddress', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Query the status of the specified device
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid '
                                             'gridview', '[0].store.data.items[' + str(row_index) +
                                             '].data.oneViewScriptDeviceStatus')

            # Determine if the status is what was expected or not
            if ui_cmd_obj.return_data == arg_dict['the_value']:
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' has the expected status of '" +
                                     arg_dict['the_value'] + "'.\n")
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' does not have the expected status of '" +
                                     arg_dict['the_value'] + "'.\n" +
                                     "The status is '" + ui_cmd_obj.return_data + "'\n")
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not in the Device List.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_confirm_run_script_overall_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel #validScriptResultsPanel #runningScriptOverallStatus',
                                         '[0].html')

        if ui_cmd_obj.return_data == arg_dict['the_value']:
            self.logger.log_info("\nOverall Status is the expected value of '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nOverall Status is not the expected value of '" + arg_dict['the_value'] + "'.\n" +
                                 "Overall Status is '" + ui_cmd_obj.return_data + "'\n")

        return ui_cmd_obj

    def scripts_confirm_run_script_results(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel #validScriptResultsPanel '
                                         'textarea[name=oneViewScriptResults]', '[0].rawValue')

        if arg_dict['the_value'] in ui_cmd_obj.return_data:
            self.logger.log_info("\nResults panel contains '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nResults panel does not contain '" + arg_dict['the_value'] + "'.\n" +
                                 "Results text is:\n\n" + ui_cmd_obj.return_data + "\n")

        return ui_cmd_obj

    def scripts_confirm_run_script_results_for_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#runScriptTabPanel #validScriptResultsPanel #runningScriptDeviceGrid gridview => '
                               ':textEquals(' + str(arg_dict['device_ip']) + ')')

        self.ext_builder.component_query(ui_cmd_obj,
                                         '#runScriptTabPanel #validScriptResultsPanel '
                                         'textarea[name=oneViewScriptResults]', '[0].rawValue')

        if arg_dict['the_value'] in ui_cmd_obj.return_data:
            self.logger.log_info("\nResults panel contains '" + arg_dict['the_value'] + "'.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nResults panel does not contain '" + arg_dict['the_value'] + "'.\n" +
                                 "Results text is:\n\n" + ui_cmd_obj.return_data + "\n")

        return ui_cmd_obj

    def scripts_confirm_execute_cli_results_status(self, ui_cmd_obj, arg_dict):
        # Get the index of the row we want to check
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj, '#cliRunnerTabPanel gridview', '[0]', 'ipAddress',
                                                          arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Get the column's value
            self.ext_builder.component_query(ui_cmd_obj, '#cliRunnerTabPanel gridview',
                                             '[0].store.data.items[' + str(row_index) + '].data.status')
            row_value = ui_cmd_obj.return_data.strip()
            expected_value = arg_dict['the_value']

            if row_value == expected_value:
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' has expected Status value '" +
                                     expected_value + "'.")
            else:
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' does not have expected Status value '" +
                                     expected_value + "'. The value is '" + str(row_value) + "'.\n")
                ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' was not found in the table.\n")

        return ui_cmd_obj

    def scripts_confirm_execute_cli_results_progress(self, ui_cmd_obj, arg_dict):
        # Get the index of the row we want to check
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj, '#cliRunnerTabPanel gridview', '[0]', 'ipAddress',
                                                          arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data

            # Get the column's value
            self.ext_builder.component_query(ui_cmd_obj, '#cliRunnerTabPanel gridview',
                                             '[0].store.data.items[' + str(row_index) + '].data.progress')
            row_value = ui_cmd_obj.return_data.strip()
            expected_value = arg_dict['the_value']

            if row_value == expected_value:
                self.logger.log_info(
                    "\nDevice '" + arg_dict['device_ip'] + "' has expected Progress value '" + expected_value + "'.")
            else:
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] +
                                     "' does not have expected Progress value '" + expected_value +
                                     "'. The value is '" + str(row_value) + "'.\n")
                ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' was not found in the table.\n")

        return ui_cmd_obj

    def scripts_confirm_command_results_results(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#commandResultsWindow textarea[name=txtResults]', '[0].rawValue')

        found_value = False
        self.logger.log_info("\nResults:\n" + ui_cmd_obj.return_data + "\n")
        if arg_dict['the_value'] in ui_cmd_obj.return_data:
            found_value = True
            self.logger.log_info("\nResults contains '" + arg_dict['the_value'] + "'\n")
        else:
            self.logger.log_info("\nResults does not contain '" + arg_dict['the_value'] + "'\n")

        # Pass or fail based on the expected value
        if found_value is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_confirm_script_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, 'scriptGrid gridview', '[0]', 'name',
                                                           arg_dict['script_name'])

        # Pass or fail based on the expected value
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scripts_confirm_table_value(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj, 'scriptGrid gridview', '[0]', 'name',
                                                          arg_dict['script_name'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            col_name = arg_dict['col_name']
            self.get_column_attribute(ui_cmd_obj, col_name)
            col_attr = ui_cmd_obj.return_data
            if col_attr != "":
                # Determine which type of data this column holds (String or Boolean)
                self.get_column_type(ui_cmd_obj, col_name)
                col_type = ui_cmd_obj.return_data

                # Get the column's value
                self.ext_builder.component_query(ui_cmd_obj, 'scriptGrid gridview',
                                                 '[0].store.data.items[' + str(row_index) + '].data.' + col_attr)
                row_value = ui_cmd_obj.return_data
                expected_value = arg_dict['the_value']

                if col_type == "boolean":
                    if row_value is StringUtils.string_to_boolean(expected_value):
                        self.logger.log_info("\nScript '" + arg_dict['script_name'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nScript '" + arg_dict['script_name'] + "' does not have expected value '" +
                            expected_value + "' for column '" + col_name + "'. The row value is '" + str(row_value) +
                            "'.\n")
                        ui_cmd_obj.error_state = True
                elif col_type == "integer":
                    if row_value == int(expected_value):
                        self.logger.log_info("\nScript '" + arg_dict['script_name'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nScript '" + arg_dict['script_name'] + "' does not have expected value '" +
                            expected_value + "' for column '" + col_name + "'. The row value is '" + str(row_value) +
                            "'.\n")
                        ui_cmd_obj.error_state = True
                else:
                    if row_value == expected_value:
                        self.logger.log_info("\nScript '" + arg_dict['script_name'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nScript '" + arg_dict['script_name'] + "' does not have expected value '" +
                            expected_value + "' for column '" + col_name + "'. The row value is '" + str(row_value) +
                            "'.\n")
                        ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nColumn '" + col_name + "' did not map to a known column attribute.\n")
                ui_cmd_obj.error_state = True

        else:
            self.logger.log_info("\nScript '" + arg_dict['script_name'] + "' was not found in the table.\n")

        return ui_cmd_obj

    # HELPER METHODS --------------------------------------------------------------------------------------------------

    def add_edit_dialog_select_tab(self, ui_cmd_obj, tab_name):
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel tab[text=' + tab_name + '] => .x-tab-inner')
        return ui_cmd_obj

    def add_edit_dialog_content_add_content(self, ui_cmd_obj, add_content):
        # Determine if there is any existing content
        self.ext_builder.component_query(ui_cmd_obj, 'scriptContentPanel', '[0].scriptBean.content')
        existing_content = ui_cmd_obj.return_data
        if existing_content != "":
            # Prepend a newline to the content we are adding so it is placed on a fresh line
            add_content = "\n" + add_content

        # Split any existing content on newlines to determine the number of lines
        split_content = existing_content.splitlines()
        line_count = len(split_content)

        # Add the new content to the end of any existing content
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel component(true) => :nth-of-type(' + str(line_count) +
                               ') .CodeMirror-line')
        self.ext_builder.enter_text(ui_cmd_obj, add_content,
                                    '#addEditScriptTabPanel component(true) => .CodeMirror textarea')

        return ui_cmd_obj

    def add_edit_dialog_content_clear_content(self, ui_cmd_obj):
        # Get the existing content
        self.ext_builder.component_query(ui_cmd_obj, 'scriptContentPanel', '[0].scriptBean.content')
        existing_content = ui_cmd_obj.return_data

        # Split the existing content on newlines to determine the number of lines
        split_content = existing_content.splitlines()
        line_count = len(split_content)

        # Select all of the existing content and erase it (mouse down on last line, mouse up on line number
        # toolbar button)
        self.ext_builder.mouse_down(ui_cmd_obj, '#addEditScriptTabPanel component(true) => '
                                                ':nth-of-type(' + str(line_count) + ') .CodeMirror-line')
        self.ext_builder.mouse_up(ui_cmd_obj, '#addEditScriptTabPanel button[name=lineNumbers] => .fa')
        self.ext_builder.enter_text(ui_cmd_obj, "[BACKSPACE]", '#addEditScriptTabPanel component(true) => '
                                                               '.CodeMirror textarea')

        return ui_cmd_obj

    def add_edit_dialog_content_set_content(self, ui_cmd_obj, the_value):
        # This method cannot simply ues the clear content and add content keywords, since the code mirror still contains
        # the previous value after the clear, so add content would try to access an invalid line number.
        # This method will instead highlight all existing text, then type the new text in place of the highlighted text.

        # Get the existing content
        self.ext_builder.component_query(ui_cmd_obj, 'scriptContentPanel', '[0].scriptBean.content')
        existing_content = ui_cmd_obj.return_data

        # Split the existing content on newlines to determine the number of lines
        split_content = existing_content.splitlines()
        line_count = len(split_content)

        # Select all of the existing content (mouse down on last line, mouse up on line number toolbar button)
        self.ext_builder.mouse_down(ui_cmd_obj, '#addEditScriptTabPanel component(true) => '
                                                ':nth-of-type(' + str(line_count) + ') .CodeMirror-line')
        self.ext_builder.mouse_up(ui_cmd_obj, '#addEditScriptTabPanel button[name=lineNumbers] => .fa')

        # Enter the new content
        self.ext_builder.enter_text(ui_cmd_obj, the_value,
                                    '#addEditScriptTabPanel component(true) => .CodeMirror textarea')

        return ui_cmd_obj

    def add_edit_dialog_content_show_hide_line_numbers(self, ui_cmd_obj, is_show):
        self.logger.log_info("\nTO DO: need to query for current state of line number visibility.\n")
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel button[name=lineNumbers] => .fa')
        return ui_cmd_obj

    def add_edit_dialog_content_add_variable(self, ui_cmd_obj, the_value):
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel title[text=Variables] => .x-title-text')
        self.ext_builder.double_click(ui_cmd_obj, '#addEditScriptTabPanel treeview => '
                                                  '.x-tree-node-text:textEquals(' + the_value + ')')
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel title[text=Variables] => .x-title-text')

        return ui_cmd_obj

    def add_edit_dialog_content_click_variables(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel #cliVariables => .x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def add_edit_dialog_runtime_set_comments(self, ui_cmd_obj, the_value):
        self.ext_builder.enter_text(ui_cmd_obj, the_value,
                                    '#addEditScriptTabPanel textfield[name=oneViewScriptComments] => .x-form-text')
        return ui_cmd_obj

    def add_edit_dialog_runtime_set_timeout(self, ui_cmd_obj, the_value):
        self.ext_builder.enter_text(ui_cmd_obj, the_value,
                                    '#addEditScriptTabPanel numberfield[name=oneViewScriptTimeout] => .x-form-text')
        return ui_cmd_obj

    def add_edit_dialog_permissions_clear_authorization_groups(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptRoles] => .x-form-clear-trigger')
        return ui_cmd_obj

    def add_edit_dialog_permissions_select_authorization_groups(self, ui_cmd_obj, group_list):
        # Open the drop down
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptRoles] => .x-form-arrow-trigger')

        # Parse the comma-separated list of groups to select
        values = str(group_list).split(",")
        for value in values:
            # Make sure the group exists in the drop down
            self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                  '#addEditScriptTabPanel multicombobox[name=oneViewScriptRoles]',
                                                  '[0]', 'displayName', value, exact_match=True)
            if ui_cmd_obj.return_data is True:
                # Select the group
                self.ext_builder.click(ui_cmd_obj,
                                       '#addEditScriptTabPanel multicombobox[name=oneViewScriptRoles] boundlist => '
                                       ':textEquals(' + value + ')')
            else:
                # Report the error
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nDrop down does not contain '" + value + "'\n")

        # Close the drop down
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptRoles] => .x-form-arrow-trigger')

        return ui_cmd_obj

    def add_edit_dialog_permissions_set_category(self, ui_cmd_obj, the_value):
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel combo[name=oneViewScriptCategory] => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#addEditScriptTabPanel combo[name=oneViewScriptCategory] boundlist => '
                                           ':textEquals(' + the_value + ')')

        return ui_cmd_obj

    def add_edit_dialog_permissions_clear_menus(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptMenus] => .x-form-clear-trigger')
        return ui_cmd_obj

    def add_edit_dialog_permissions_select_menus(self, ui_cmd_obj, menu_list):
        # Open the drop down
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptMenus] => .x-form-arrow-trigger')

        # Parse the comma-separated list of menus to select
        values = str(menu_list).split(",")
        for value in values:
            # Make sure the menu exists in the drop down
            self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                  '#addEditScriptTabPanel multicombobox[name=oneViewScriptMenus]',
                                                  '[0]', 'displayName', value, exact_match=True)
            if ui_cmd_obj.return_data is True:
                # Select the menu
                self.ext_builder.click(ui_cmd_obj,
                                       '#addEditScriptTabPanel multicombobox[name=oneViewScriptMenus] boundlist => '
                                       ':textEquals(' + value + ')')
            else:
                # Report the error
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nDrop down does not contain '" + value + "'\n")

        # Close the drop down
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel multicombobox[name=oneViewScriptMenus] => .x-form-arrow-trigger')

        return ui_cmd_obj

    def add_edit_dialog_permissions_click_remove_all_groups(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel button[actionId=removeScriptTreeGroups] => '
                               '.x-btn-inner-gray-small')
        return ui_cmd_obj

    def add_edit_dialog_permissions_click_select_groups(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#addEditScriptTabPanel button[actionId=selectScriptTreeGroups] => '
                               '.x-btn-inner-gray-small')
        return ui_cmd_obj

    def add_edit_dialog_permissions_expand_device_group(self, ui_cmd_obj, device_group):
        self.ext_builder.expand_tree_node(ui_cmd_obj, '#scriptingGroupSelector treeview', '[0]', 'text',
                                          device_group, exact_match=False)

        return ui_cmd_obj

    def add_edit_dialog_permissions_select_device_group(self, ui_cmd_obj, device_group):
        # Find the index of the device group
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#scriptingGroupSelector treeview', '[0]', 'groupname', device_group)

        # Click the check box for the specified device group if it isn't already selected
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data + 1
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#scriptingGroupSelector treeview',
                                             '[0].store.data.items[' + str(row_index) + '].data.checked')

            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#scriptingGroupSelector treeview => '
                                       ':nth-of-type(' + str(row_index) + ') .x-tree-checkbox')
            else:
                self.logger.log_info("\nGroup '" + device_group + "' is already selected.\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nCould not find device group '" + device_group + "'\n")

        return ui_cmd_obj

    def add_edit_dialog_prermissions_device_group_click_ok(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#scriptingGroupSelector button[actionId=groupSelection] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def add_edit_dialog_prermissions_device_group_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj,
                               '#scriptingGroupSelector button[actionId=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def add_edit_dialog_permissions_confirm_groups(self, ui_cmd_obj, group_name):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#addEditScriptTabPanel grid[itemId=supportedGroups]',
                                         '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        found_index = -1
        for item_index in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj, '#addEditScriptTabPanel grid[itemId=supportedGroups]',
                                             '[0].store.data.items[' + str(item_index) + '].data.pathName')
            if group_name in ui_cmd_obj.return_data:
                found_index = item_index
                break

        if found_index != -1:
            self.logger.log_info("\nSelected Groups contains '" + group_name + "' at index '" + str(found_index) +
                                 "'\n")
            # PASS
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nSelected Groups does not contain '" + group_name + "'\n")
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def add_edit_dialog_click_save(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def add_edit_dialog_click_save_as(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save As] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def add_edit_dialog_click_run(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Run] => .x-btn-inner-default-small')
        return ui_cmd_obj

    def add_edit_dialog_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Cancel] => .x-btn-inner-default-small')
        return ui_cmd_obj

    def is_run_script_dialog_cli(self, ui_cmd_obj):
        # Assume the run script dialog is not CLI (CLI uses a different dialog identifier)
        is_cli = False

        # Check if this run script dialog is CLI (CLI uses a different dialog identifier)
        self.ext_builder.component_query(ui_cmd_obj, '#selectDevicesForCliRunner #cliRunnerDeviceSelector', '[0]')
        if ui_cmd_obj.return_data is not None:
            is_cli = True
        else:
            # Make sure the dialog component is actually usable
            self.ext_builder.component_query(ui_cmd_obj, '#runScriptTabPanel #runScriptDeviceSelector', '[0]')
            if ui_cmd_obj.return_data is None:
                ui_cmd_obj.error_state = True

        # Return the identifier for the run script dialog
        ui_cmd_obj.return_data = is_cli

        return ui_cmd_obj

    def get_run_script_dialog_id(self, ui_cmd_obj):
        # Assume the run script dialog is not CLI (CLI uses a different dialog identifier)
        dialog_id = "#runScriptTabPanel #runScriptDeviceSelector"

        # Check if this run script dialog is CLI (CLI uses a different dialog identifier)
        self.ext_builder.component_query(ui_cmd_obj, '#selectDevicesForCliRunner #cliRunnerDeviceSelector', '[0]')
        if ui_cmd_obj.return_data is not None:
            dialog_id = "#selectDevicesForCliRunner #cliRunnerDeviceSelector"
        else:
            # Make sure the dialog component is actually usable
            self.ext_builder.component_query(ui_cmd_obj, '#runScriptTabPanel #runScriptDeviceSelector', '[0]')
            if ui_cmd_obj.return_data is None:
                ui_cmd_obj.error_state = True

        # Return the identifier for the run script dialog
        ui_cmd_obj.return_data = dialog_id

        return ui_cmd_obj

    def get_column_attribute(self, ui_cmd_obj, col_name):
        ui_cmd_obj.return_data = ""

        if col_name == "Script Type":
            ui_cmd_obj.return_data = "scriptType"
        elif col_name == "Category":
            ui_cmd_obj.return_data = "category"
        elif col_name == "Scheduled":
            ui_cmd_obj.return_data = "usedInTask"
        elif col_name == "Comments":
            ui_cmd_obj.return_data = "comments"
        elif col_name == "Modified By":
            ui_cmd_obj.return_data = "modifiedBy"

        return ui_cmd_obj

    def get_column_type(self, ui_cmd_obj, col_name):
        ui_cmd_obj.return_data = "string"

        # if col_name == "":
        #     ui_cmd_obj.return_data = "boolean"
        # elif col_name == "":
        #     ui_cmd_obj.return_data = "integer"

        return ui_cmd_obj
