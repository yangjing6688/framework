from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AlarmsConstants import AlarmsConstants


class UiAlarmsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAlarmsKeywords, self).__init__()
        self.api_const = self.constants.API_ALARMS
        self.cmd = AlarmsConstants()

    def alarms_menu_clear_selected_alarms(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Clear Selected Alarm(s)" from the context menu for the currently selected alarm.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_MENU_CLEAR_SELECTED_ALARMS, **kwargs)

    def alarms_menu_clear_selected_alarms_with_reason(self, element_name, clear_reason, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [clear_reason] -  Reason to enter in the Clear Alarm(s) Reason dialog

        Selects "Clear Selected Alarm(s) w/ Reason" from the context menu for the currently selected alarm,
        enters the reason into the resulting Clear Alarm(s) Reason dialog, and clicks OK.
        """
        args = {"clear_reason": clear_reason}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_MENU_CLEAR_SELECTED_ALARMS_WITH_REASON,
                                    **kwargs)

    def alarms_menu_clear_all_alarms(self, element_name, clear_reason, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [clear_reason] -  Reason to enter in the Clear Alarm(s) Reason dialog

        Selects "Clear All Alarms" from the context menu, enters the reason into the resulting
        Clear Alarm(s) Reason dialog, and clicks OK.
        """
        args = {"clear_reason": clear_reason}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_MENU_CLEAR_ALL_ALARMS, **kwargs)

    def alarms_menu_edit_alarm_definition(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Edit Alarm Definition..." from the context menu for the currently selected alarm.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_MENU_EDIT_ALARM_DEFINITION, **kwargs)

    def alarms_menu_history_all(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Alarm History> All" from the context menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_MENU_HISTORY_ALL, **kwargs)

    def alarms_menu_history_by_source(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Alarm History> By Source" from the context menu for the currently selected alarm.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_MENU_HISTORY_BY_SOURCE, **kwargs)

    def alarms_menu_history_by_name(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Alarm History> By Name" from the context menu for the currently selected alarm.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_MENU_HISTORY_BY_NAME, **kwargs)

    def alarms_dialog_edit_alarm_definition_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Cancel" in the Edit Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_DIALOG_EDIT_ALARM_DEFINITION_CANCEL, **kwargs)

    def alarms_dialog_history_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Close" in the Alarm History dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_DIALOG_HISTORY_CLOSE, **kwargs)

    def alarms_click_next_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">" button to go to the next page in the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLICK_NEXT_PAGE, **kwargs)

    def alarms_click_prev_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<" button to go to the previous page in the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLICK_PREV_PAGE, **kwargs)

    def alarms_click_first_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<<" button to go to the first page in the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLICK_FIRST_PAGE, **kwargs)

    def alarms_click_last_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">>" button to go to the last page in the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLICK_LAST_PAGE, **kwargs)

    def alarms_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Refresh" button for the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLICK_REFRESH, **kwargs)

    def alarms_set_table_filter(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     String to enter into the table's search field

        Filters the Alarms table by entering the specified string into the Search field.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_SET_TABLE_FILTER, **kwargs)

    def alarms_clear_table_filter(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the filter set on the Alarms table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMS_CLEAR_TABLE_FILTER, **kwargs)

    def alarms_select_alarm_by_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the alarm to select

        Filters the Alarms table by entering the specified string into the Search field.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_SELECT_ALARM_BY_NAME, **kwargs)

    def alarms_select_alarm_by_source_ip(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Source IP of the alarm to select

        Filters the Alarms table by entering the specified string into the Search field.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_SELECT_ALARM_BY_SOURCE_IP, **kwargs)

    def alarms_confirm_alarm_name_exists(self, element_name, source_ip, alarm_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [source_ip] -     IP address of the source device to check (optional - if empty/undefined, will check all
                          devices)
        [alarm_name] -    Name of the alarm to look for
        [exists] -        Indicates whether or not the alarm is expected to exist (True/False)

        Confirms whether or not an alarm with the specified alarm name exists on the specified source device.
        Passes/fails based on whether the alarm is expected to be found or not, as specified in the "exists" argument.
        If source_ip is empty or undefined, it will just search all devices.
        """
        args = {"source_ip": source_ip,
                "alarm_name": alarm_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_CONFIRM_ALARM_NAME_EXISTS, **kwargs)

    def alarms_confirm_alarm_info_contains(self, element_name, source_ip, alarm_str_list, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] -  List of elements the keyword will be run against
        [source_ip] -      IP address of the source device to check (optional - if empty/undefined, will check all
                           devices)
        [alarm_str_list] - Comma-separated list of alarm strings to look for
        [exists] -         Indicates whether or not the alarm is expected to exist (True/False)

        Confirms whether or not an alarm contains the specified strings in the Information column for the specified
        source device.
        Passes/fails based on whether the alarm is expected to be found or not, as specified in the "exists" argument.
        If source_ip is empty or undefined, it will just search all devices.
        """
        args = {"alarm_str_list": alarm_str_list,
                "source_ip": source_ip,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_CONFIRM_ALARM_INFO_CONTAINS, **kwargs)

    def alarms_confirm_alarm_history_reason_exists(self, element_name, source_ip, the_reason, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [source_ip] -     IP address of the source device to check (optional - if empty/undefined, will check all
                          devices)
        [the_reason] -    String to look for in the Reason column
        [exists] -        Indicates whether or not the entry is expected to exist (True/False)

        Confirms whether an entry with the specified reason exists in the alarm history dialog for the specified source
        device.
        Passes/fails based on whether the alarm is expected to be found or not, as specified in the "exists" argument.
        If source_ip is empty or undefined, it will just search all devices.
        NOTE: The Alarm History dialog must be displayed before calling this keyword.
        """
        args = {"the_reason": the_reason,
                "source_ip": source_ip,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ALARMS_CONFIRM_ALARM_HISTORY_REASON_EXISTS, **kwargs)
