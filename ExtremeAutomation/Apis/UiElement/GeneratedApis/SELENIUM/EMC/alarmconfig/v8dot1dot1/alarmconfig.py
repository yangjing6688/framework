from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as AlarmconfigBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Alarmconfig(AlarmconfigBase):

    def alarmconfig_select_alarm_definition(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj, 'grid[stateId=AlarmDefinitions]',
                                                  '[0]', 'name', str(arg_dict['the_name']))

        return ui_cmd_obj

    def alarmconfig_set_table_filter(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_set_table_filter(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_clear_table_filter(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_clear_table_filter(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_click_next_page(self, ui_cmd_obj, arg_dict):
        # self.click_paging_button(ui_cmd_obj, "#next")
        # return ui_cmd_obj
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid #first', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid #first', '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid #first => .x-btn-button')
            else:
                self.logger.log_info("\n'First Page' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'First Page' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_prev_page(self, ui_cmd_obj, arg_dict):
        # self.click_paging_button(ui_cmd_obj, "#prev")
        # return ui_cmd_obj
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid #prev', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid #prev', '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid #prev => .x-btn-button')
            else:
                self.logger.log_info("\n'Prev Page' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'Prev Page' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_first_page(self, ui_cmd_obj, arg_dict):
        # self.click_paging_button(ui_cmd_obj, "#first")
        # return ui_cmd_obj
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid #first', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid #first', '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid #first => .x-btn-button')
            else:
                self.logger.log_info("\n'First Page' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'First Page' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_last_page(self, ui_cmd_obj, arg_dict):
        # self.click_paging_button(ui_cmd_obj, "#last")
        # return ui_cmd_obj
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid #last', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid #last', '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid #last => .x-btn-button')
            else:
                self.logger.log_info("\n'Last Page' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'Last Page' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_refresh(self, ui_cmd_obj, arg_dict):
        # self.click_paging_button(ui_cmd_obj, "#refresh")
        # return ui_cmd_obj
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid #refresh', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid #refresh',
                                                          '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid #refresh => .x-btn-button')
            else:
                self.logger.log_info("\n'Refresh' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'Refresh' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_reset(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel alarmDefsGrid button[text=Reset]', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel alarmDefsGrid button[text=Reset]',
                                                          '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel alarmDefsGrid button[text=Reset] => '
                                       '.x-btn-inner-default-toolbar-small')
            else:
                self.logger.log_info("\n'Reset' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find 'Reset' button.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_add(self, ui_cmd_obj, arg_dict):
        menu_pick = None
        if arg_dict["add_type"] == "Custom Criteria Alarm":
            menu_pick = "#addCustomCriteria"
        elif arg_dict["add_type"] == "Flow Alarm":
            menu_pick = "#addFlow"
        elif arg_dict["add_type"] == "Selected Trap Alarm":
            menu_pick = "#addSelectedTrap"
        elif arg_dict["add_type"] == "Severity Alarm":
            menu_pick = "#addSeverity"
        elif arg_dict["add_type"] == "Status Change Alarm":
            menu_pick = "#addStatusChange"
        elif arg_dict["add_type"] == "Threshold Alarm":
            menu_pick = "#addThreshold"

        if menu_pick is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel panel[title=Alarm Configuration] panel alarmDefsGrid '
                                   '#addButtons => .x-btn-arrow')
            self.ext_builder.click(ui_cmd_obj, menu_pick + ' => .x-menu-item-text')
        else:
            self.logger.log_info("\nUnknown Alarm Configuration type '" + arg_dict["add_type"] + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmconfig_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel panel[title=Alarm Configuration] panel alarmDefsGrid '
                               '#editSelectedAlarm => .x-btn-button')

        return ui_cmd_obj

    def alarmconfig_click_copy(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel panel[title=Alarm Configuration] panel alarmDefsGrid '
                               '#duplicateAlarmDefAction => .x-btn-button')

        return ui_cmd_obj

    def alarmconfig_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel panel[title=Alarm Configuration] panel alarmDefsGrid '
                               '#deleteSelectedAlarms => .x-btn-button')

        return ui_cmd_obj

    def alarmconfig_dialog_add_set_name(self, ui_cmd_obj, arg_dict):
        self.alarmdef_set_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_set_severity(self, ui_cmd_obj, arg_dict):
        self.alarmdef_set_severity(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_set_enabled(self, ui_cmd_obj, arg_dict):
        self.alarmdef_set_enabled(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_select_tab(self, ui_cmd_obj, arg_dict):
        self.alarmdef_select_tab(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_criteria_custom_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_severity_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_severity_select_match_selected(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_severity_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_severity_select_exclude_selected(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_severity_select_severities(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_severity_select_severities(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_severity_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_severity_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_severity_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_severity_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_category_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_category_select_match_selected(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_category_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_category_select_exclude_selected(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_category_select_categories(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_category_select_categories(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_category_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_category_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_category_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_category_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_type_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_type_select_match_selected(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_type_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_type_select_exclude_selected(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_type_select_types(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_type_select_types(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_type_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_type_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_type_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_type_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_event_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_event_select_match_selected(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_event_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_event_select_exclude_selected(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_event_select_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_event_select_events(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_event_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_event_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_event_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_event_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_select_match_selected(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_select_exclude_selected(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_select_hostips(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_select_hostips(ui_cmd_obj,
                                                                                                  arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_click_edit_list(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_add(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_remove(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_save(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_cancel(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_row(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_host_name(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_ip_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_ip_mask(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_host_name(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_ip_address(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_ip_address(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_mask(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_log_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_log_select_match_selected(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_log_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_log_select_exclude_selected(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_log_select_logs(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_log_select_logs(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_log_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_log_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_log_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_log_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_select_match_any_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_select_match_any_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_select_match_all_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_select_match_all_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_select_phrases(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_select_phrases(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_click_edit_list(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_click_cancel(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_click_add(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_click_remove(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_click_save(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_click_cancel(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_select_row(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_select_contains(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_select_contains(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_select_does_not_contain(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(
                Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_select_does_not_contain(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_custom_information_editlist_set_phrase(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_custom_information_editlist_set_phrase(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_match(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_match(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_invert(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_invert(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_from_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_from_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_to_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_to_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_from_port(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_from_port(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_ttl(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_ttl(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_alarm_source(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_alarm_source(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_flow_set_alarm_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_flow_set_alarm_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_severity_set_event_alarm_severity(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_severity_set_event_alarm_severity(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_severity_select_traps_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_severity_select_traps_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_severity_select_events_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_severity_select_events_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_severity_select_traps_and_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_severity_select_traps_and_events(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_status_select_contact_lost(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_status_select_contact_lost(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_status_select_contact_established(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_status_select_contact_established(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_status_select_both(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_status_select_both(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_threshold_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_threshold_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_collector(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_collector(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_target_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_target_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_application(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_application(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_application_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_application_any(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_location(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_location(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_location_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_location_any(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_statistic(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_statistic(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_statistic_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_statistic_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_statistic_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_statistic_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_cross_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_cross_when_value(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_engines(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_engines(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_threshold_set_rearm_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_threshold_set_rearm_when_value(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_criteria_traps_click_select_traps(self, ui_cmd_obj, arg_dict):
        self.alarmdef_criteria_traps_click_select_traps(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_criteria_traps_set_selected(self, ui_cmd_obj, arg_dict):
        self.alarmdef_criteria_traps_set_selected(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_criteria_traps_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_criteria_traps_click_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_criteria_traps_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_criteria_traps_click_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_criteria_select_groups(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_criteria_select_groups(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_click_add(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_click_add(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_click_test(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_click_test(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_select_enable_alarm_action_limit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_select_enable_alarm_action_limit(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_set_max_count(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_set_max_count(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_set_reset_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_set_reset_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_set_destination(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_set_destination(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_set_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_set_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_set_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_set_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_click_edit_email_lists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_click_edit_email_lists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_set_list_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_set_list_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_set_addresses(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_set_addresses(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_email_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_email_editlist_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_syslog_set_syslog_server(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_syslog_server(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_syslog_select_override_content(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_select_override_content(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_syslog_set_tag(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_tag(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_syslog_set_message(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_message(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_syslog_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_syslog_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_set_trap_server(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_server(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_set_snmp_credential(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_snmp_credential(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_select_override_content(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_select_override_content(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_set_trap_oid(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_oid(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_set_trap_message(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_message(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_set_trap_message_oid(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_message_oid(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_trap_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_add_actions_custom_set_program(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_set_program(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_custom_set_working_directory(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_set_working_directory(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_custom_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_custom_set_custom_arguments(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_set_custom_arguments(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_custom_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_actions_custom_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_actions_custom_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_other_options_select_no_current_alarm(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_other_options_select_no_current_alarm(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_other_options_select_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_other_options_select_cleared_by_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_other_options_set_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_add_other_options_set_cleared_by_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_add_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_click_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_add_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_click_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_set_severity(self, ui_cmd_obj, arg_dict):
        self.alarmdef_set_severity(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_set_enabled(self, ui_cmd_obj, arg_dict):
        self.alarmdef_set_enabled(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_select_tab(self, ui_cmd_obj, arg_dict):
        self.alarmdef_select_tab(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_criteria_custom_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_severity_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_severity_select_match_selected(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_severity_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_severity_select_exclude_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_severity_select_severities(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_severity_select_severities(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_severity_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_severity_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_severity_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_severity_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_category_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_category_select_match_selected(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_category_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_category_select_exclude_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_category_select_categories(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_category_select_categories(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_category_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_category_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_category_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_category_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_type_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_type_select_match_selected(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_type_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_type_select_exclude_selected(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_type_select_types(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_type_select_types(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_type_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_type_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_type_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_type_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_event_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_event_select_match_selected(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_event_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_event_select_exclude_selected(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_event_select_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_event_select_events(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_event_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_event_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_event_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_event_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_select_match_selected(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_select_exclude_selected(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_select_hostips(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_select_hostips(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_click_edit_list(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_add(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_remove(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_save(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_cancel(ui_cmd_obj,
                                                                                                          arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_row(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_host_name(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_ip_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_ip_mask(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_host_name(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_ip_address(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_ip_address(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_mask(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_log_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_log_select_match_selected(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_log_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_log_select_exclude_selected(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_log_select_logs(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_log_select_logs(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_log_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_log_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_log_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_log_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_select_match_any_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_select_match_any_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_select_match_all_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_select_match_all_selected(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_select_phrases(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_select_phrases(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_click_edit_list(ui_cmd_obj,
                                                                                                         arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_click_save(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_click_cancel(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_click_add(ui_cmd_obj,
                                                                                                            arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_click_remove(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_click_save(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_click_cancel(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_select_row(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_select_contains(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_select_contains(
                ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_select_does_not_contain(self, ui_cmd_obj,
                                                                                             arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).\
                alarmconfig_dialog_edit_criteria_custom_information_editlist_select_does_not_contain(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_custom_information_editlist_set_phrase(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_custom_information_editlist_set_phrase(ui_cmd_obj,
                                                                                                             arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_match(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_match(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_invert(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_invert(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_from_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_from_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_to_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_to_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_from_port(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_from_port(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_ttl(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_ttl(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_alarm_source(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_alarm_source(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_flow_set_alarm_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_flow_set_alarm_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_severity_set_event_alarm_severity(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_severity_set_event_alarm_severity(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_severity_select_traps_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_severity_select_traps_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_severity_select_events_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_severity_select_events_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_severity_select_traps_and_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_severity_select_traps_and_events(ui_cmd_obj,
                                                                                                       arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_status_select_contact_lost(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_status_select_contact_lost(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_status_select_contact_established(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_status_select_contact_established(ui_cmd_obj,
                                                                                                        arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_status_select_both(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_status_select_both(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_threshold_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_threshold_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_collector(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_collector(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_target_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_target_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_application(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_application(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_application_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_application_any(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_location(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_location(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_location_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_location_any(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_statistic(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_statistic(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_statistic_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_statistic_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_statistic_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_statistic_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_cross_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_cross_when_value(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_engines(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_engines(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_threshold_set_rearm_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_threshold_set_rearm_when_value(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_traps_click_select_traps(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_traps_click_select_traps(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_traps_set_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_traps_set_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_traps_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_traps_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_traps_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_traps_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_criteria_select_groups(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_criteria_select_groups(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_click_add(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_click_add(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_click_test(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_click_test(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_select_enable_alarm_action_limit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_select_enable_alarm_action_limit(ui_cmd_obj,
                                                                                                      arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_set_max_count(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_set_max_count(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_set_reset_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_set_reset_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_set_destination(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_set_destination(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_set_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_set_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_set_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_set_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_click_edit_email_lists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_click_edit_email_lists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_set_list_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_set_list_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_set_addresses(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_set_addresses(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_email_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_email_editlist_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_syslog_set_syslog_server(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_syslog_server(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_syslog_select_override_content(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_select_override_content(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_syslog_set_tag(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_tag(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_syslog_set_message(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_set_message(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_syslog_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_syslog_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_syslog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_set_trap_server(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_server(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_set_snmp_credential(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_snmp_credential(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_select_override_content(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_select_override_content(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_set_trap_oid(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_oid(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_set_trap_message(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_message(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_set_trap_message_oid(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_set_trap_message_oid(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_trap_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_actions_trap_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_actions_custom_set_program(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_set_program(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_custom_set_working_directory(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_set_working_directory(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_custom_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_select_override_content(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_custom_set_custom_arguments(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_set_custom_arguments(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_custom_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_actions_custom_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_actions_custom_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_other_options_select_no_current_alarm(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_other_options_select_no_current_alarm(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_other_options_select_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_other_options_select_cleared_by_alarms(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_other_options_set_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmconfig_dialog_edit_other_options_set_cleared_by_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmconfig_dialog_edit_click_save(self, ui_cmd_obj, arg_dict):
        self.alarmdef_click_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_edit_click_cancel(self, ui_cmd_obj, arg_dict):
        self.alarmdef_click_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def alarmconfig_dialog_copy_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), '#alarmDefsName => .x-form-text')

        return ui_cmd_obj

    def alarmconfig_dialog_copy_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=copyAlarmDef] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def alarmconfig_dialog_copy_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def alarmconfig_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-button')

        return ui_cmd_obj

    def alarmconfig_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-button')

        return ui_cmd_obj

    def alarmconfig_confirm_alarm_definition_exists(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: implement paging\n")
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, 'grid[stateId=AlarmDefinitions]',
                                                           '[0]', 'name', arg_dict['the_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nAlarm Definition '" + arg_dict['the_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nAlarm Definition '" + arg_dict['the_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmdef_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), 'textfield[name=alarmName] => .x-form-text')

        return ui_cmd_obj

    def alarmdef_set_severity(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=severityId] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=severityId] boundlist => .x-boundlist-item:contains(' +
                               str(arg_dict['the_value']) + ')')

        return ui_cmd_obj

    # HELPER METHODS ---------------------------------------------------------------------------------------------------

    def click_paging_button(self, ui_cmd_obj, btn_id):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel #alarmDefsGrid ' + btn_id, '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel #alarmDefsGrid ' + btn_id,
                                                          '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel #alarmDefsGrid ' + btn_id + ' => .x-btn-button')
            else:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#alarmsEventsTabPanel #alarmDefsGrid ' + btn_id,
                                                              '[0].tooltip')
                self.logger.log_info("\n'" + ui_cmd_obj.return_data + "' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find button with ID '" + btn_id + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmdef_set_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'checkboxfield[name=alarmEnabled]', '[0].checked')

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, 'checkbox[name=alarmEnabled] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def alarmdef_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(
            ui_cmd_obj, '#AlarmCfgMainTabPanel tab[text=' + str(arg_dict['the_value']) + '] => .x-tab-inner')

        return ui_cmd_obj

    def alarmdef_criteria_custom_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_severity_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_severity_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_severity_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_severity_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_severity_select_severities(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_severity_select_severities(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_severity_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_severity_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_severity_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_severity_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_category_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_category_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_category_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_category_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_category_select_categories(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_category_select_categories(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_category_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_category_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_category_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_category_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_type_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_type_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_type_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_type_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_type_select_types(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_type_select_types(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_type_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_type_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_type_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_type_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_event_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_event_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_event_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_event_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_event_select_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_event_select_events(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_event_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_event_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_event_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_event_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_select_hostips(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_select_hostips(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_click_edit_list(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_select_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_select_host_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_select_ip_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_select_ip_mask(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_set_host_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_set_host_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_set_ip_address(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_set_ip_address(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_hostip_editlist_set_mask(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_hostip_editlist_set_mask(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_log_select_match_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_log_select_match_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_log_select_exclude_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_log_select_exclude_selected(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_log_select_logs(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_log_select_logs(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_log_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_log_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_log_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_log_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_select_match_any_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_select_match_any_selected(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_select_match_all_selected(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_select_match_all_selected(ui_cmd_obj,
                                                                                                    arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_select_phrases(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_select_phrases(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_click_edit_list(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_click_edit_list(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_select_contains(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_select_contains(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_select_does_not_contain(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_select_does_not_contain(ui_cmd_obj,
                                                                                                           arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_custom_information_editlist_set_phrase(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_custom_information_editlist_set_phrase(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_match(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_match(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_invert(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_invert(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_from_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_from_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_to_network(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_to_network(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_from_port(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_from_port(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_ttl(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_ttl(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_alarm_source(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_alarm_source(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_flow_set_alarm_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_flow_set_alarm_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_severity_set_event_alarm_severity(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_severity_set_event_alarm_severity(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_severity_select_traps_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_severity_select_traps_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_severity_select_events_only(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_severity_select_events_only(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_severity_select_traps_and_events(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_severity_select_traps_and_events(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_status_select_contact_lost(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_status_select_contact_lost(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_status_select_contact_established(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_status_select_contact_established(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_status_select_both(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_status_select_both(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_threshold_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_threshold_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_collector(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_collector(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_target_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_target_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_application(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_application(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_application_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_application_any(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_location(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_location(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_location_any(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_location_any(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_statistic(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_statistic(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_statistic_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_statistic_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_statistic_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_statistic_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_cross_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_cross_when_value(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_engines(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_engines(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_threshold_set_rearm_when_value(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_threshold_set_rearm_when_value(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_criteria_traps_click_select_traps(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(
            ui_cmd_obj,
            '#AlarmCfgMainTabPanel panel[title=Criteria] panel[title=Selected Traps] gridpanel '
            'button[text=Select Traps...] => .x-btn-button')

        return ui_cmd_obj

    def alarmdef_criteria_traps_set_selected(self, ui_cmd_obj, arg_dict):
        # Make sure the trap table exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'SelectTrapsDialog', '[0].AlarmTrapsGrid')

        if ui_cmd_obj.return_data is not None:
            # Make sure the traps table contains items
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          'SelectTrapsDialog',
                                                          '[0].AlarmTrapsGrid.store.data.length')
            if int(ui_cmd_obj.return_data) != 0:
                # Loop through each of the traps in the comma-separated list and toggle the selection state
                # appropriately
                traps = arg_dict['trap_list'].split(',')
                for trap_name in traps:
                    # Get the index of the item to act upon
                    ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj,
                                                                      'SelectTrapsDialog', '[0].AlarmTrapsGrid',
                                                                      'name', trap_name)
                    if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
                        trap_index = ui_cmd_obj.return_data
                        # Check the current selection state of the node
                        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'SelectTrapsDialog',
                                                                      '[0].AlarmTrapsGrid.store.data.items[' +
                                                                      str(trap_index) + '].data.selected')
                        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['select_traps']):
                            scroll_index = int(trap_index + 1)
                            self.ext_builder.scroll_to_index(ui_cmd_obj, 'SelectTrapsDialog', '[0].AlarmTrapsGrid',
                                                             scroll_index)
                            self.ext_builder.click(
                                ui_cmd_obj,
                                'SelectTrapsDialog[title=Select Traps] form gridpanel => table.x-grid-item:contains(' +
                                trap_name + ')')
                        else:
                            self.logger.log_info("\nTrap '" + trap_name + "' is already at desired selection state (" +
                                                 arg_dict['select_traps'] + ").\n")
                    else:
                        self.logger.log_info("\nCould not find trap '" + trap_name + "' in table.\n")
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nTraps table is empty.\n")

            return ui_cmd_obj

    def alarmdef_criteria_traps_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'SelectTrapsDialog[title=Select Traps] button[text=Save] => .x-btn-button')

        return ui_cmd_obj

    def alarmdef_criteria_traps_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'SelectTrapsDialog[title=Select Traps] button[text=Cancel] => .x-btn-button')

        return ui_cmd_obj

    def alarmdef_criteria_select_groups(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_criteria_select_groups(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_click_add(self, ui_cmd_obj, arg_dict):
        menu_pick = None
        if arg_dict["add_type"] == "Email Action":
            menu_pick = "#createEmailAction"
        elif arg_dict["add_type"] == "Syslog Action":
            menu_pick = "#createSyslogAction"
        elif arg_dict["add_type"] == "Trap Action":
            menu_pick = "#createTrapAction"
        elif arg_dict["add_type"] == "Custom Action":
            menu_pick = "#createCustomAction"

        if menu_pick is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   '#actionsTab #alarmActionsPanelGrid #addActionButtons => .x-btn-arrow')
            self.ext_builder.click(ui_cmd_obj, menu_pick + ' => .x-menu-item-text')
        else:
            self.logger.log_info("\nUnknown Action type '" + arg_dict["add_type"] + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def alarmdef_actions_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_click_test(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_click_test(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_select_enable_alarm_action_limit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_select_enable_alarm_action_limit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_set_max_count(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_set_max_count(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_set_reset_interval(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_set_reset_interval(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_set_destination(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_set_destination(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_set_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_set_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_set_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_set_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_click_edit_email_lists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_click_edit_email_lists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_select_row(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_select_row(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_remove(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_remove(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_set_list_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_set_list_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_set_addresses(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_set_addresses(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_email_editlist_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_email_editlist_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_syslog_set_syslog_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#syslogCard textfield[name=syslogServersAction] => .x-form-text')

        return ui_cmd_obj

    def alarmdef_actions_syslog_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_syslog_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_syslog_set_tag(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_syslog_set_tag(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_syslog_set_message(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_syslog_set_message(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_syslog_click_save(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'alarmActionDialog button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def alarmdef_actions_syslog_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'alarmActionDialog button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def alarmdef_actions_trap_set_trap_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#trapCard #trapServerActionField => .x-form-text')

        return ui_cmd_obj

    def alarmdef_actions_trap_set_snmp_credential(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#trapCard snmpCredentialsCombobox[name=trapServerCredentialsId] => .x-form-trigger')
        self.ext_builder.click(
            ui_cmd_obj,
            '#trapCard snmpCredentialsCombobox[name=trapServerCredentialsId] boundlist => div:textEquals(' +
            str(arg_dict['the_value']) + ')')

        return ui_cmd_obj

    def alarmdef_actions_trap_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_trap_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_trap_set_trap_oid(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_trap_set_trap_oid(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_trap_set_trap_message(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_trap_set_trap_message(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_trap_set_trap_message_oid(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_trap_set_trap_message_oid(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_trap_click_save(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'alarmActionDialog button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def alarmdef_actions_trap_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'alarmActionDialog button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def alarmdef_actions_custom_set_program(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_set_program(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_custom_set_working_directory(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_set_working_directory(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_custom_select_override_content(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_select_override_content(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_custom_set_custom_arguments(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_set_custom_arguments(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_custom_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_actions_custom_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_actions_custom_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_other_options_select_no_current_alarm(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_other_options_select_no_current_alarm(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_other_options_select_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_other_options_select_cleared_by_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_other_options_set_cleared_by_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarmconfig, self).alarmdef_other_options_set_cleared_by_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarmdef_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#alarmCfgSaveBtn => .x-btn-inner-blue-small')

        # Handle an error saving
        self.handle_error(ui_cmd_obj)

        return ui_cmd_obj

    def alarmdef_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'AlarmCfgDialog button[actionId=alarmCfgCancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def handle_error(self, ui_cmd_obj):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0]")
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0].hidden")
            if ui_cmd_obj.return_data is False:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]",
                                                              "[0].msg.html")
                self.logger.log_info("\nSAVE FAILED: " + ui_cmd_obj.return_data + "\n")
                if "Alarm names must be unique" in ui_cmd_obj.return_data:
                    # PASS - already exists so mark as passed and just continue
                    ui_cmd_obj.error_state = False
                else:
                    # FAIL - another error condition so mark as failed
                    ui_cmd_obj.error_state = True

                # Click OK in the error dialog
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
                self.alarmdef_click_cancel(ui_cmd_obj, '')

        return ui_cmd_obj
