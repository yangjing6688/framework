from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as AlarmsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Alarms(AlarmsBase):

    def alarms_menu_clear_selected_alarms(self, ui_cmd_obj, arg_dict):
        # Access the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#alarmsEventsTabPanel #alarmGridItemId button[iconCls=fa fa-bars] => .fa")

        # Select "Clear Selected Alarm(s)" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#alarmsEventsTabPanel #alarmGridItemId #alarmGridMenu menuitem[actionId=clearSelected] "
                               "=> .x-menu-item-text")

        return ui_cmd_obj

    def alarms_menu_clear_selected_alarms_with_reason(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_clear_selected_alarms_with_reason(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_menu_clear_all_alarms(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_clear_all_alarms(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_menu_edit_alarm_definition(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_edit_alarm_definition(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_menu_history_all(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_history_all(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_menu_history_by_source(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_history_by_source(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_menu_history_by_alarm_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_menu_history_by_alarm_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_dialog_edit_alarm_definition_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_dialog_edit_alarm_definition_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_dialog_history_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_dialog_history_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_click_next_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#next")
        return ui_cmd_obj

    def alarms_click_prev_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#prev")
        return ui_cmd_obj

    def alarms_click_first_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#first")
        return ui_cmd_obj

    def alarms_click_last_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#last")
        return ui_cmd_obj

    def alarms_click_refresh(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: wait for refresh button to be enabled - sometimes it isn't enabled right away\n")
        self.ext_builder.click(ui_cmd_obj,
                               'alarmHistoryGrid[viewId=AlarmHistory] pagingtoolbar #refresh => .x-btn-icon-el')
        return ui_cmd_obj

    def alarms_set_table_filter(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_set_table_filter(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_clear_table_filter(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_clear_table_filter(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_select_alarm_by_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_select_alarm_by_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_select_alarm_by_source_ip(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_select_alarm_by_source_ip(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_confirm_alarm_name_exists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_confirm_alarm_name_exists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_confirm_alarm_info_contains(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_confirm_alarm_info_contains(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def alarms_confirm_alarm_history_reason_exists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Alarms, self).alarms_confirm_alarm_history_reason_exists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    # HELPER METHODS

    def click_paging_button(self, ui_cmd_obj, btn_id):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel #alarmGridItemId ' + btn_id, '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel #alarmGridItemId ' + btn_id,
                                                          '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel #alarmGridItemId ' + btn_id + ' => .x-btn-button')
            else:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#alarmsEventsTabPanel #alarmGridItemId ' + btn_id,
                                                              '[0].tooltip')
                self.logger.log_info("\n'" + ui_cmd_obj.return_data + "' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find paging button with ID '" + btn_id + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
