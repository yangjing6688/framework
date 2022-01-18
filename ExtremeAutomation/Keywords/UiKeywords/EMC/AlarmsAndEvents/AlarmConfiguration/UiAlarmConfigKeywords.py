from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AlarmconfigConstants import AlarmconfigConstants


class UiAlarmConfigKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAlarmConfigKeywords, self).__init__()
        self.api_const = self.constants.API_ALARMCONFIG
        self.cmd = AlarmconfigConstants()

    def alarmconfig_select_alarm_definition(self, element_name, the_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_name] -      Name of the alarm definition to select

        Selects the specified alarm definition in the Alarm Configuration table.
        """
        args = {"the_name": the_name}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_SELECT_ALARM_DEFINITION, **kwargs)

    def alarmconfig_set_table_filter(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     String to enter into the table's search field

        Filters the Alarm Configuration table by entering the specified string into the Search field.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_SET_TABLE_FILTER, **kwargs)

    def alarmconfig_clear_table_filter(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the filter set on the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLEAR_TABLE_FILTER, **kwargs)

    def alarmconfig_click_next_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">" button to go to the next page in the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_NEXT_PAGE, **kwargs)

    def alarmconfig_click_prev_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<" button to go to the previous page in the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_PREV_PAGE, **kwargs)

    def alarmconfig_click_first_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<<" button to go to the first page in the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_FIRST_PAGE, **kwargs)

    def alarmconfig_click_last_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">>" button to go to the last page in the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_LAST_PAGE, **kwargs)

    def alarmconfig_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Refresh" button for the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_REFRESH, **kwargs)

    def alarmconfig_click_reset(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Reset" button for the Alarm Configuration table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_RESET, **kwargs)

    def alarmconfig_click_add(self, element_name, add_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [add_type] -      Type of alarm configuration to create;  possible values:
                          Custom Criteria Alarm
                          Flow Alarm
                          Selected Trap Alarm
                          Severity Alarm
                          Status Change Alarm
                          Threshold Alarm

        Clicks 'Add' on the toolbar and selects the specified alarm type.
        """
        args = {"add_type": add_type}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_CLICK_ADD, **kwargs)

    def alarmconfig_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Edit' on the toolbar.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_EDIT, **kwargs)

    def alarmconfig_click_copy(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Copy' on the toolbar.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_COPY, **kwargs)

    def alarmconfig_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Delete' on the toolbar.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_CLICK_DELETE, **kwargs)

    def alarmconfig_dialog_add_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -      Value to enter into the "Name" field

        Enters the specified value into the "Name" field of the Create Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_SET_NAME, **kwargs)

    def alarmconfig_dialog_add_set_severity(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -      Value to select in the "Severity" field

        Selects the specified value in the "Severity" field of the Create Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_SET_SEVERITY, **kwargs)

    def alarmconfig_dialog_add_set_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the "Enabled" field (True/False)

        Sets the specified value for the "Enabled" field of the Create Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_SET_ENABLED, **kwargs)

    def alarmconfig_dialog_add_select_tab(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the tab to select (Criteria, Actions, Other Options)

        Selects the specified tab in the Create Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_SELECT_TAB, **kwargs)

    def alarmconfig_dialog_add_criteria_traps_click_select_traps(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Select Traps" button on the Criteria tab of the Create Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_SELECT_TRAPS,
                                    **kwargs)

    def alarmconfig_dialog_add_criteria_traps_set_selected(self, element_name, trap_list, select_traps, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [trap_list] -     Comma-separated list of traps to select
        [select_traps] -  Indicates whether to select or deselect the traps (True/False)

        Selects or deselects the specified traps in the Select Traps dialog, depending on the value of the
        "select_traps" argument.
        """
        args = {"trap_list": trap_list,
                "select_traps": select_traps}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_SET_SELECTED,
                                    **kwargs)

    def alarmconfig_dialog_add_criteria_traps_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the Select Traps dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_SAVE,
                                    **kwargs)

    def alarmconfig_dialog_add_criteria_traps_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Cancel" button in the Select Traps dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_CANCEL,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_click_add(self, element_name, add_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [add_type] -      Type of action to create (Email, Syslog, Trap, Custom)

        Creates an action of the specified type on the Actions tab in the Add Alarm Definition dialog.
        """
        args = {"add_type": add_type}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_CLICK_ADD, **kwargs)

    def alarmconfig_dialog_add_actions_syslog_set_syslog_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to use for the field

        Sets the value of the Syslog Server(s) field in the Add Syslog Action dialog accessed from the Actions tab in
        the Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_SYSLOG_SERVER, **kwargs)

    def alarmconfig_dialog_add_actions_syslog_select_override_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Indicates whether to select the check button or not (True/False)

        Sets the state of the Override Content check button in the Add Syslog Action dialog accessed from the Actions
        tab in the Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SELECT_OVERRIDE_CONTENT, **kwargs)

    def alarmconfig_dialog_add_actions_syslog_set_tag(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Tag field in the Add Syslog Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_TAG,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_syslog_set_message(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Message field in the Add Syslog Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_MESSAGE,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_syslog_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Add Syslog Action dialog accessed from the Actions tab in the Add Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_CLICK_SAVE,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_syslog_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Add Syslog Action dialog accessed from the Actions tab in the Add Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_CLICK_CANCEL,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_trap_set_trap_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Trap Server field in the Set Trap Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_SERVER,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_trap_set_snmp_credential(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the SNMP Credential field in the Set Trap Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_SNMP_CREDENTIAL, **kwargs)

    def alarmconfig_dialog_add_actions_trap_select_override_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Indicates whether to select the check button or not (True/False)

        Sets the state of the Override Content check button in the Set Trap Action dialog accessed from the Actions tab
        in the Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SELECT_OVERRIDE_CONTENT, **kwargs)

    def alarmconfig_dialog_add_actions_trap_set_trap_oid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Trap OID field in the Set Trap Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_OID,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_trap_set_trap_message(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Trap Message field in the Set Trap Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_MESSAGE,
                                    **kwargs)

    def alarmconfig_dialog_add_actions_trap_set_trap_message_oid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use for the field

        Sets the value of the Trap Message OID field in the Set Trap Action dialog accessed from the Actions tab in the
        Add Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_MESSAGE_OID, **kwargs)

    def alarmconfig_dialog_add_actions_trap_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Set Trap Action dialog accessed from the Actions tab in the Add Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_CLICK_SAVE, **kwargs)

    def alarmconfig_dialog_add_actions_trap_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Set Trap Action dialog accessed from the Actions tab in the Add Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_CLICK_CANCEL,
                                    **kwargs)

    def alarmconfig_dialog_add_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the Create Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_CLICK_SAVE, **kwargs)

    def alarmconfig_dialog_add_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the Create Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_ADD_CLICK_CANCEL, **kwargs)

    def alarmconfig_dialog_edit_set_severity(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -      Value to select in the "Severity" field

        Selects the specified value in the "Severity" field of the Edit Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_EDIT_SET_SEVERITY, **kwargs)

    def alarmconfig_dialog_edit_set_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the "Enabled" field (True/False)

        Sets the specified value for the "Enabled" field of the Edit Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_EDIT_SET_ENABLED, **kwargs)

    def alarmconfig_dialog_edit_select_tab(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the tab to select (Criteria, Actions, Other Options)

        Selects the specified tab in the Edit Alarm Definition dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_EDIT_SELECT_TAB, **kwargs)

    def alarmconfig_dialog_edit_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the Create Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_EDIT_CLICK_SAVE, **kwargs)

    def alarmconfig_dialog_edit_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the Create Alarm Definition dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_EDIT_CLICK_CANCEL, **kwargs)

    def alarmconfig_dialog_copy_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -      Value to enter into the "Name" field

        Enters the specified value into the "Name" field of the Copy dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_DIALOG_COPY_SET_NAME, **kwargs)

    def alarmconfig_dialog_copy_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Save' in the Copy dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_COPY_CLICK_SAVE, **kwargs)

    def alarmconfig_dialog_copy_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Copy dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_COPY_CLICK_CANCEL, **kwargs)

    def alarmconfig_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Yes' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_CONFIRM_DELETE_CLICK_YES, **kwargs)

    def alarmconfig_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'No' in the Confirm Delete dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ALARMCONFIG_DIALOG_CONFIRM_DELETE_CLICK_NO, **kwargs)

    def alarmconfig_confirm_alarm_definition_exists(self, element_name, the_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_name] -      Name of the alarm definition to look for
        [exists] -        Indicates whether or not the entry is expected to exist (True/False)

        Confirms whether an entry with the specified name exists in the Alarm Configuration table.
        Passes/fails based on whether the alarm is expected to be found or not, as specified in the "exists" argument.
        If source_ip is empty or undefined, it will just search all devices.
        NOTE: The Alarm History dialog must be displayed before calling this keyword.
        """
        args = {"the_name": the_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ALARMCONFIG_CONFIRM_ALARM_DEFINITION_EXISTS, **kwargs)
