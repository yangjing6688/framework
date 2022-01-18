from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ScriptsConstants import ScriptsConstants


class UiScriptsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiScriptsKeywords, self).__init__()
        self.api_const = self.constants.API_SCRIPTS
        self.command_const = ScriptsConstants()

    def scripts_select_script(self, element_name, script_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script to select

        Selects the specified script.
        """
        args = {"script_name": script_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_SELECT_SCRIPT, **kwargs)

    # TOOLBAR BUTTONS -------------------------------------------------------------------------------------------------
    def scripts_click_add(self, element_name, add_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [add_type] -      Type of script to add (TCL, Python, JSON-RPC-Python, JSON-RPC-CLI)

        Clicks the "Add" toolbar button and selects the type of script to add.
        """
        args = {"add_type": add_type}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_ADD, **kwargs)

    def scripts_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Edit" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_EDIT, **kwargs)

    def scripts_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Run" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_RUN, **kwargs)

    def scripts_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Delete" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_DELETE, **kwargs)

    def scripts_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Refresh" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_REFRESH, **kwargs)

    def scripts_click_import(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Import" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_IMPORT, **kwargs)

    def scripts_click_export(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Export" toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CLICK_EXPORT, **kwargs)

    # ADD SCRIPT DIALOG -----------------------------------------------------------------------------------------------
    def scripts_dialog_add_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the tab to select in the Add Script dialog

        Selects the specified tab in the Add Script dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_SELECT_TAB, **kwargs)

    def scripts_dialog_add_content_add_variable(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the variable to add to the Content tab of the Add Script dialog

        Adds the specified variable to the Content tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_ADD_VARIABLE,
                                    **kwargs)

    def scripts_dialog_add_content_add_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to add to the Content tab of the Add Script dialog

        Adds the specified value to the end of the Content tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_ADD_CONTENT,
                                    **kwargs)

    def scripts_dialog_add_content_clear_content(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the existing text from the Content tab in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_CLEAR_CONTENT,
                                    **kwargs)

    def scripts_dialog_add_content_set_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Content tab of the Add Script dialog

        Replaces the Content tab with the specified value in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_SET_CONTENT,
                                    **kwargs)

    def scripts_dialog_add_content_hide_line_numbers(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Hides the line numbers on the Content tab of the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_HIDE_LINE_NUMBERS,
                                    **kwargs)

    def scripts_dialog_add_content_show_line_numbers(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Shows the line numbers on the Content tab of the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_SHOW_LINE_NUMBERS,
                                    **kwargs)

    def scripts_dialog_add_content_click_variables(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Variables toolbar button on the Content tab of the Add Script dialog for a CLI type script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CONTENT_CLICK_VARIABLES,
                                    **kwargs)

    def scripts_dialog_add_runtime_set_comments(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter for the Script Comments field in the Add Script dialog

        Sets the value of the Script Comments field on the Run-Time Settings tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_RUNTIME_SET_COMMENTS,
                                    **kwargs)

    def scripts_dialog_add_runtime_set_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter for the Timeout field in the Add Script dialog

        Sets the value of the Timeout field on the Run-Time Settings tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_RUNTIME_SET_TIMEOUT,
                                    **kwargs)

    def scripts_dialog_add_permissions_clear_authorization_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the Authorization Groups (Roles) drop down on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLEAR_AUTHORIZATION_GROUPS,
                                    **kwargs)

    def scripts_dialog_add_permissions_select_authorization_groups(self, element_name, group_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_list] -    Comma-separated list of authorization groups to select in the Add Script dialog

        Selects the specified authorization groups on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {"group_list": group_list}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_SELECT_AUTHORIZATION_GROUPS,
                                    **kwargs)

    def scripts_dialog_add_permissions_set_category(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Category in the Add Script dialog

        Selects the specified category on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_SET_CATEGORY,
                                    **kwargs)

    def scripts_dialog_add_permissions_clear_menus(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the Menus drop down on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLEAR_MENUS,
                                    **kwargs)

    def scripts_dialog_add_permissions_select_menus(self, element_name, menu_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_list] -     Comma-separated list of menus to select in the Add Script dialog

        Selects the specified menus on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {"menu_list": menu_list}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_SELECT_MENUS,
                                    **kwargs)

    def scripts_dialog_add_permissions_click_remove_all_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Remove All Groups button on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLICK_REMOVE_ALL_GROUPS, **kwargs)

    def scripts_dialog_add_permissions_click_select_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Select Groups button on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLICK_SELECT_GROUPS, **kwargs)

    def scripts_dialog_add_permissions_device_group_expand_node(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the device group to expand in the Edit Script dialog

        Expands the specified device group node on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_EXPAND_NODE,
                                    **kwargs)

    def scripts_dialog_add_permissions_device_group_select_node(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the device group to select in the Add Script dialog

        Selects the specified device group on the Permissions and Menus tab in the Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_SELECT_NODE,
                                    **kwargs)

    def scripts_dialog_add_permissions_device_group_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the Select Device Groups dialog, accessed from the Add Script dialog's Permissions ane Menus tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_CLICK_OK, **kwargs)

    def scripts_dialog_add_permissions_device_group_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Select Device Groups dialog, accessed from the Add Script dialog's Permissions ane Menus
        tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_CLICK_CANCEL,
                                    **kwargs)

    def scripts_dialog_add_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CLICK_SAVE, **kwargs)

    def scripts_dialog_add_click_save_as(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save As button in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CLICK_SAVE_AS, **kwargs)

    def scripts_dialog_add_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Run button in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CLICK_RUN, **kwargs)

    def scripts_dialog_add_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button in the Add Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_ADD_CLICK_CANCEL, **kwargs)

    # EDIT SCRIPT DIALOG -----------------------------------------------------------------------------------------------
    def scripts_dialog_edit_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the tab to select in the Edit Script dialog

        Selects the specified tab in the Edit Script dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_SELECT_TAB, **kwargs)

    def scripts_dialog_edit_overview_set_variable(self, element_name, var_name, var_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [var_name] -      Name of the variable to modify on the Overview tab
        [var_value] -     Value to set the specified variable to on the Overview tab

        Sets the specified variable's value on the Overview tab in the Edit Script dialog.
        """
        args = {"var_name": var_name,
                "var_value": var_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_OVERVIEW_SET_VARIABLE,
                                    **kwargs)

    def scripts_dialog_edit_content_add_variable(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the variable to add to the Content tab of the Edit Script dialog

        Adds the specified variable to the Content tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_ADD_VARIABLE,
                                    **kwargs)

    def scripts_dialog_edit_content_add_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to add to the Content tab of the Edit Script dialog

        Adds the specified value to the end of the Content tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_ADD_CONTENT,
                                    **kwargs)

    def scripts_dialog_edit_content_clear_content(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the existing text from the Content tab in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_CLEAR_CONTENT,
                                    **kwargs)

    def scripts_dialog_edit_content_set_content(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Content tab of the Edit Script dialog

        Replaces the Content tab with the specified value in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_SET_CONTENT,
                                    **kwargs)

    def scripts_dialog_edit_content_hide_line_numbers(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Hides the line numbers on the Content tab of the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_HIDE_LINE_NUMBERS, **kwargs)

    def scripts_dialog_edit_content_show_line_numbers(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Shows the line numbers on the Content tab of the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_SHOW_LINE_NUMBERS, **kwargs)

    def scripts_dialog_edit_content_click_variables(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Variables toolbar button on the Content tab of the Edit Script dialog for a CLI type script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CONTENT_CLICK_VARIABLES,
                                    **kwargs)

    def scripts_dialog_edit_runtime_set_comments(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter for the Script Comments field in the Edit Script dialog

        Sets the value of the Script Comments field on the Run-Time Settings tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_RUNTIME_SET_COMMENTS,
                                    **kwargs)

    def scripts_dialog_edit_runtime_set_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter for the Timeout field in the Edit Script dialog

        Sets the value of the Timeout field on the Run-Time Settings tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_RUNTIME_SET_TIMEOUT,
                                    **kwargs)

    def scripts_dialog_edit_permissions_clear_authorization_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the Authorization Groups (Roles) drop down on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLEAR_AUTHORIZATION_GROUPS,
                                    **kwargs)

    def scripts_dialog_edit_permissions_select_authorization_groups(self, element_name, group_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_list] -    Comma-separated list of authorization groups to select in the Edit Script dialog

        Selects the specified authorization groups on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {"group_list": group_list}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SELECT_AUTHORIZATION_GROUPS,
                                    **kwargs)

    def scripts_dialog_edit_permissions_set_category(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Category in the Edit Script dialog

        Selects the specified category on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SET_CATEGORY,
                                    **kwargs)

    def scripts_dialog_edit_permissions_clear_menus(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the Menus drop down on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLEAR_MENUS,
                                    **kwargs)

    def scripts_dialog_edit_permissions_select_menus(self, element_name, menu_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_list] -     Comma-separated list of menus to select in the Edit Script dialog

        Selects the specified menus on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {"menu_list": menu_list}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SELECT_MENUS,
                                    **kwargs)

    def scripts_dialog_edit_permissions_click_remove_all_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Remove All Groups button on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLICK_REMOVE_ALL_GROUPS,
                                    **kwargs)

    def scripts_dialog_edit_permissions_click_select_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Select Groups button on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLICK_SELECT_GROUPS, **kwargs)

    def scripts_dialog_edit_permissions_device_group_expand_node(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the device group to expand in the Edit Script dialog

        Expands the specified device group node on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_EXPAND_NODE,
                                    **kwargs)

    def scripts_dialog_edit_permissions_device_group_select_node(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the device group to select in the Edit Script dialog

        Selects the specified device group node on the Permissions and Menus tab in the Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_SELECT_NODE,
                                    **kwargs)

    def scripts_dialog_edit_permissions_device_group_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the Select Device Groups dialog, accessed from the Edit Script dialog's Permissions ane Menus tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_CLICK_OK, **kwargs)

    def scripts_dialog_edit_permissions_device_group_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Select Device Groups dialog, accessed from the Edit Script dialog's Permissions ane Menus
        tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_CLICK_CANCEL,
                                    **kwargs)

    def scripts_dialog_edit_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CLICK_SAVE, **kwargs)

    def scripts_dialog_edit_click_save_as(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save As button in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CLICK_SAVE_AS, **kwargs)

    def scripts_dialog_edit_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Run button in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CLICK_RUN, **kwargs)

    def scripts_dialog_edit_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button in the Edit Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EDIT_CLICK_CANCEL, **kwargs)

    # SAVE DIALOG -----------------------------------------------------------------------------------------------
    def scripts_dialog_save_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter in the Name field of the Save dialog

        Enters the specified value into the Name field for the Save Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_SAVE_SET_NAME, **kwargs)

    def scripts_dialog_save_set_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter in the Description field of the Save dialog

        Enters the specified value into the Description field for the Save Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_SAVE_SET_DESCRIPTION,
                                    **kwargs)

    def scripts_dialog_save_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button in the Save Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_SAVE_CLICK_SAVE, **kwargs)

    def scripts_dialog_save_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button in the Save Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_SAVE_CLICK_CANCEL, **kwargs)

    def scripts_dialog_replace_script_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Yes button in the Replace Script confirmation dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_REPLACE_SCRIPT_CLICK_YES,
                                    **kwargs)

    def scripts_dialog_replace_script_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the No button in the Replace Script confirmation dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_REPLACE_SCRIPT_CLICK_NO,
                                    **kwargs)

    def scripts_dialog_save_success_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the OK button in the Save Success dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_SAVE_SUCCESS_CLICK_OK,
                                    **kwargs)

    # IMPORT DIALOG -----------------------------------------------------------------------------------------------
    def scripts_dialog_import_click_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Close button in the Import dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_IMPORT_CLICK_CLOSE, **kwargs)

    # RUN SCRIPT DIALOG -----------------------------------------------------------------------------------------------
    def scripts_dialog_run_collapse_device_group(self, element_name, device_group, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_group] -  Name of the device group to collapse

        Collapses the specified device group on the Device Selection tab of the Run Script dialog.
        """
        args = {"device_group": device_group}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_COLLAPSE_DEVICE_GROUP,
                                    **kwargs)

    def scripts_dialog_run_expand_device_group(self, element_name, device_group, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_group] -  Name of the device group to expand

        Expands the specified device group on the Device Selection tab of the Run Script dialog.
        """
        args = {"device_group": device_group}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_EXPAND_DEVICE_GROUP,
                                    **kwargs)

    def scripts_dialog_run_select_device_group(self, element_name, device_group, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_list] -   Name of the device group to run the script against

        Moves all devices in the specified device group to the list of devices to run the script against on the
        Device Selection tab of the Run Script dialog.

        This method is different from select device in that it does a partial string match on the group name
        as opposed to an exact match on the device IP.
        """
        args = {"device_group": device_group}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SELECT_DEVICE_GROUP,
                                    **kwargs)

    def scripts_dialog_run_select_device(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -   Comma-separated list of devices to run the script against

        Moves the specified device to the list of devices to run the script against on the Device Selection tab
        of the Run Script dialog.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SELECT_DEVICE, **kwargs)

    def scripts_dialog_run_move_device_up(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to move up in the list of devices to run the script against

        Moves the specified device up one position in the list of devices to run the script against on the
        Device Selection tab of the Run Script dialog.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_MOVE_DEVICE_UP, **kwargs)

    def scripts_dialog_run_move_device_down(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to move down in the list of devices to run the script against

        Moves the specified device down one position in the list of devices to run the script against on the
        Device Selection tab of the Run Script dialog.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_MOVE_DEVICE_DOWN,
                                    **kwargs)

    def scripts_dialog_run_set_variable(self, element_name, var_name, var_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [var_name] -      Name of the variable to modify on the Device Settings tab
        [var_value] -     Value to set the specified variable to on the Device Settings tab

        Sets the specified variable's value on the Device Settings tab in the Run Script dialog.
        """
        args = {"var_name": var_name,
                "var_value": var_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SET_VARIABLE, **kwargs)

    def scripts_dialog_run_set_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the script timeout field

        Sets the script timeout value on the Run-Time Settings tab of the Run Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SET_TIMEOUT, **kwargs)

    def scripts_dialog_run_set_run_now_no_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects the "Run now, don't save as task" radio button on the Run-Time Settings tab of the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SET_RUN_NOW_NO_SAVE,
                                    **kwargs)

    def scripts_dialog_run_set_save_and_run_now(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Value to set in the Task Name field

        Selects the "Save as a task and run now" radio button and enters the task name on the Run-Time Settings tab
        of the Run Script dialog.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SET_SAVE_AND_RUN_NOW,
                                    **kwargs)

    def scripts_dialog_run_set_save_and_run_later(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Value to set in the Task Name field

        Selects the "Save as a task. I'll run later" radio button and enters the task name on the Run-Time Settings tab
        of the Run Script dialog.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_SET_SAVE_AND_RUN_LATER,
                                    **kwargs)

    def scripts_confirm_dialog_add_permissions_selected_groups(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the group to look for in the Selected Groups table

        Verifies the specified group is listed in the Selected Groups table on the Permissions and Menus tab of the
        Add Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_CONFIRM_DIALOG_ADD_PERMISSIONS_SELECTED_GROUPS, **kwargs)

    def scripts_confirm_dialog_edit_permissions_selected_groups(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the group to look for in the Selected Groups table

        Verifies the specified group is listed in the Selected Groups table on the Permissions and Menus tab of the
        Edit Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_CONFIRM_DIALOG_EDIT_PERMISSIONS_SELECTED_GROUPS,
                                    **kwargs)

    def scripts_confirm_dialog_edit_overview_variable(self, element_name, var_name, var_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [var_name] -      Name of the variable to confirm the value of on the Overview tab
        [var_value] -     Value of the variable to confirm

        Verifies the specified variable has the expected value on the Overview tab of the Edit Script dialog.
        """
        args = {"var_name": var_name,
                "var_value": var_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_CONFIRM_DIALOG_EDIT_OVERVIEW_VARIABLE, **kwargs)

    def scripts_confirm_run_verify_task_information(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Expected value of the field

        Verifies the value of the Task Information field on the Verify Run Script tab of the Run Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_VERIFY_TASK_INFORMATION,
                                    **kwargs)

    def scripts_confirm_run_verify_script_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Expected value of the field

        Verifies the value of the Script Name field on the Verify Run Script tab of the Run Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_VERIFY_SCRIPT_NAME,
                                    **kwargs)

    def scripts_confirm_run_verify_task_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Expected value of the field

        Verifies the value of the Task Name field on the Verify Run Script tab of the Run Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_VERIFY_TASK_NAME,
                                    **kwargs)

    def scripts_confirm_run_verify_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Expected value of the field

        Verifies the value of the Timeout field on the Verify Run Script tab of the Run Script dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_VERIFY_TIMEOUT, **kwargs)

    def scripts_confirm_run_verify_device(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to look for

        Verifies the Device List contains the specified device on the Verify Run Script tab of the Run Script dialog.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_VERIFY_DEVICE, **kwargs)

    def scripts_dialog_run_results_select_device(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to select

        Selects the specified device on the Results tab of the Run Script dialog.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_RESULTS_SELECT_DEVICE,
                                    **kwargs)

    def scripts_dialog_run_results_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Refresh button on the Resutls tab of the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_RESULTS_CLICK_REFRESH,
                                    **kwargs)

    def scripts_dialog_run_click_next(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Next" button in the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_NEXT, **kwargs)

    def scripts_dialog_run_click_back(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Back" button in the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_BACK, **kwargs)

    def scripts_dialog_run_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Run" button in the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_RUN, **kwargs)

    def scripts_dialog_run_click_execute_cli(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Execute CLI" button in the Run Script dialog for a CLI script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_EXECUTE_CLI,
                                    **kwargs)

    def scripts_dialog_run_click_finish(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Finish" button in the Run Script dialog.
        This button is seen if the script is to be saved as a task and run later.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_FINISH, **kwargs)

    def scripts_dialog_run_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Cancel" button in the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_CANCEL, **kwargs)

    def scripts_dialog_run_click_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Close" button in the Run Script dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_RUN_CLICK_CLOSE, **kwargs)

    # EXECUTE CLI -----------------------------------------------------------------------------------------------------
    def scripts_dialog_execute_cli_click_execute(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Execute" button in the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_EXECUTE,
                                    **kwargs)

    def scripts_dialog_execute_cli_click_abort(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Abort" button in the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_ABORT,
                                    **kwargs)

    def scripts_dialog_execute_cli_click_save_results(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save Results" button in the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_SAVE_RESULTS, **kwargs)

    def scripts_dialog_execute_cli_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Cancel" button in the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_CANCEL,
                                    **kwargs)

    def scripts_dialog_execute_cli_click_view_results(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to view the results of

        Clicks the "View Results" link in the Execute CLI Commands dialog for the specified device.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_VIEW_RESULTS, **kwargs)

    def scripts_dialog_execute_cli_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the tab to select

        Selects the specified tab in the Execute CLI Commands dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_EXECUTE_CLI_SELECT_TAB,
                                    **kwargs)

    # COMMAND RESULTS -------------------------------------------------------------------------------------------------
    def scripts_dialog_command_results_click_save_results(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save Results" button in the Command Results dialog, which is displayed when clicking the View
        Results link from the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_DIALOG_COMMAND_RESULTS_CLICK_SAVE_RESULTS, **kwargs)

    def scripts_dialog_command_results_click_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Close" button in the Command Results dialog, which is displayed when clicking the View Results
        link from the Execute CLI Commands dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_COMMAND_RESULTS_CLICK_CLOSE,
                                    **kwargs)

    # CONFIRM DELETE --------------------------------------------------------------------------------------------------
    def scripts_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Yes" in the delete confirmation dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_CONFIRM_DELETE_CLICK_YES,
                                    **kwargs)

    def scripts_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "No" in the delete confirmation dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_CONFIRM_DELETE_CLICK_NO,
                                    **kwargs)

    def scripts_dialog_variables_clear_scope(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the scope drop down in the Select Variables dialog, which is accessed from the Add/Edit dialog for a
        CLI script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_VARIABLES_CLEAR_SCOPE,
                                    **kwargs)

    def scripts_dialog_variables_select_scope(self, element_name, scope_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [scope_list] -    Comma-separated list of scope values to select

        Selects the specified scope in the Select Variables dialog, which is accessed from the Add/Edit dialog for a
        CLI script.
        """
        args = {"scope_list": scope_list}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_VARIABLES_SELECT_SCOPE,
                                    **kwargs)

    def scripts_dialog_variables_select_variables(self, element_name, var_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [var_list] -      Comma-separated list of variable names to select

        Selects the specified variables (by name) in the Select Variables dialog, which is accessed from the Add/Edit
        dialog for a CLI script.
        """
        args = {"var_list": var_list}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_VARIABLES_SELECT_VARIABLES,
                                    **kwargs)

    def scripts_dialog_variables_click_insert(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Cancel" in the Select Variables dialog, which is accessed from the Add/Edit dialog for a CLI script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_VARIABLES_CLICK_INSERT,
                                    **kwargs)

    def scripts_dialog_variables_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Cancel" in the Select Variables dialog, which is accessed from the Add/Edit dialog for a CLI script.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_DIALOG_VARIABLES_CLICK_CANCEL,
                                    **kwargs)

    # WAIT FOR METHODS ---------------------------------------------------------------------------------------------
    def scripts_wait_for_script_add(self, element_name, script_name, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script to wait for being added
        [wait_time] -     Number of seconds to wait before timing out

        Waits until the specified script has been added to the table.
        """
        args = {"script_name": script_name,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_WAIT_FOR_SCRIPT_ADD, **kwargs)

    def scripts_wait_for_script_remove(self, element_name, script_name, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script to wait for being removed
        [wait_time] -     Number of seconds to wait before timing out

        Waits until the specified script has been removed from the table.
        """
        args = {"script_name": script_name,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_WAIT_FOR_SCRIPT_REMOVE, **kwargs)

    def scripts_wait_for_run_script_device_status(self, element_name, device_ip, the_value, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check
        [the_value] -     Device Status value to wait for
        [wait_time] -     Number of seconds to wait before timing out

        Waits until the status of the device on the Results tab in the Run Script dialog has the specified value.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_WAIT_FOR_RUN_SCRIPT_DEVICE_STATUS,
                                    **kwargs)

    def scripts_wait_for_run_script_overall_status(self, element_name, the_value, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the 'Overall Status' field to wait for
        [wait_time] -     Number of seconds to wait before timing out

        Waits until the Overall Status field on the Results tab in the Run Script dialog has the specified value.
        """
        args = {"the_value": the_value,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_WAIT_FOR_RUN_SCRIPT_OVERALL_STATUS,
                                    **kwargs)

    def scripts_wait_for_execute_cli_results_status(self, element_name, device_ip, the_value, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the results of
        [the_value] -     Value to wait for
        [wait_time] -     Number of seconds to wait before timing out

        Waits for the Results tab in the Execute CLI Commands dialog to contain the expected text in the Status column
        for the specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_WAIT_FOR_EXECUTE_CLI_RESULTS_STATUS,
                                    **kwargs)

    def scripts_wait_for_execute_cli_results_progress(self, element_name, device_ip, the_value, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the results of
        [the_value] -     Value to wait for
        [wait_time] -     Number of seconds to wait before timing out

        Waits for the Results tab in the Execute CLI Commands dialog to contain the expected text in the Progress column
        for the specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCRIPTS_WAIT_FOR_EXECUTE_CLI_RESULTS_PROGRESS, **kwargs)

    # COFIRMATION METHODS ---------------------------------------------------------------------------------------------
    def scripts_confirm_run_script_device_status(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the status of
        [the_value] -     Status value to confirm

        Confirms the Results tab in the Run Script dialog contains the expected status for the specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_SCRIPT_DEVICE_STATUS,
                                    **kwargs)

    def scripts_confirm_run_script_overall_status(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to check

        Confirms the Results tab in the Run Script dialog contains the expected text in the Overall Status field.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_SCRIPT_OVERALL_STATUS,
                                    **kwargs)

    def scripts_confirm_run_script_results(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to check

        Confirms the Results tab in the Run Script dialog contains the expected text in the Results panel.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_SCRIPT_RESULTS, **kwargs)

    def scripts_confirm_run_script_results_for_device(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the results of
        [the_value] -     Value to check

        Confirms the Results tab in the Run Script dialog contains the expected text in the Results panel for the
        specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_RUN_SCRIPT_RESULTS, **kwargs)

    def scripts_confirm_execute_cli_results_status(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the results of
        [the_value] -     Value to check

        Confirms the Results tab in the Execute CLI Commands dialog contains the expected text in the Status column
        for the specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_EXECUTE_CLI_RESULTS_STATUS,
                                    **kwargs)

    def scripts_confirm_execute_cli_results_progress(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the results of
        [the_value] -     Value to check

        Confirms the Results tab in the Execute CLI Commands dialog contains the expected text in the Progress column
        for the specified device.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_EXECUTE_CLI_RESULTS_PROGRESS,
                                    **kwargs)

    def scripts_confirm_command_results_results(self, element_name, the_value, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to check
        [exists] -        Indicates if the specified value is expected to be found or not (True/False)

        Checks whether or not the Results field in the Command Results dialog contains the specified text;  passes or
        fails based on the expected value, as specified in the "exists" argument.
        The Command Results dialog is accessed by clicking the Show Results link in the Execute CLI Commands dialog.
        """
        args = {"the_value": the_value,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_COMMAND_RESULTS_RESULTS,
                                    **kwargs)

    def scripts_confirm_script_exists(self, element_name, script_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script to look for
        [exists] -        Indicates whether the script is expected to exist or not (True/False)

        Checks whether or not the script exists;  passes or fails based on the expected value.
        """
        args = {"script_name": script_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_SCRIPT_EXISTS, **kwargs)

    def scripts_confirm_table_value(self, element_name, script_name, col_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script to check
        [col_name] -      Name of the table column to check
        [the_value] -     Value to check

        Checks whether or not the specified script has the expected value in the specified column of the Scripts table.
        """
        args = {"script_name": script_name,
                "col_name": col_name,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SCRIPTS_CONFIRM_TABLE_VALUE, **kwargs)
