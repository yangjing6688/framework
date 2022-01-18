from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.GroupsConstants import GroupsConstants


class UiGroupsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGroupsKeywords, self).__init__()
        self.api_const = self.constants.API_GROUPS
        self.command_const = GroupsConstants()

    def access_control_groups_click_add_group_button(self, element_name, **kwargs):
        """Returns the result of access_control_groups_click_add_group_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_CLICK_ADD_GROUP_BUTTON, **kwargs)

    def access_control_groups_click_delete_group_button(self, element_name, **kwargs):
        """Returns the result of access_control_groups_click_delete_group_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_CLICK_DELETE_GROUP_BUTTON, **kwargs)

    def access_control_groups_click_edit_group_button(self, element_name, **kwargs):
        """Returns the result of access_control_groups_click_edit_group_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_CLICK_EDIT_GROUP_BUTTON, **kwargs)

    def access_control_groups_click_refresh_button(self, element_name, **kwargs):
        """Returns the result of access_control_groups_click_refresh_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_CLICK_REFRESH_BUTTON, **kwargs)

    def access_control_groups_select_group(self, element_name, group_name, **kwargs):
        """Returns the result of access_control_groups_select_group."""
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_SELECT_GROUP, **kwargs)

    def access_control_groups_dialog_set_group_name(self, element_name, group_name, **kwargs):
        """Returns the result of access_control_groups_dialog_set_group_name."""
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_SET_GROUP_NAME, **kwargs)

    def access_control_groups_dialog_select_group_type(self, element_name, group_type, **kwargs):
        """Returns the result of access_control_groups_dialog_select_group_type."""
        args = {"group_type": group_type}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_SELECT_GROUP_TYPE, **kwargs)

    def access_control_groups_dialog_click_create_new_group(self, element_name, **kwargs):
        """Returns the result of access_control_groups_dialog_click_create_new_group."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_CLICK_CREATE_NEW_GROUP,
                                    **kwargs)

    def access_control_groups_dialog_add_ldap_user_group_entry(self, element_name, attribute_name, attribute_value,
                                                               **kwargs):
        """Returns the result of access_control_groups_dialog_add_ldap_user_group_entry."""
        args = {"attribute_name": attribute_name,
                "attribute_value": attribute_value}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_ADD_LDAP_USER_GROUP_ENTRY,
                                    **kwargs)

    def access_control_groups_dialog_add_location_group_entry(self, element_name, ip_list, intf_type, port_or_ssid_list,
                                                              ap_list, **kwargs):
        """Returns the result of access_control_groups_dialog_add_location_group_entry."""
        args = {"ip_list": ip_list,
                "intf_type": intf_type,
                "port_or_ssid_list": port_or_ssid_list,
                "ap_list": ap_list}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_ADD_LOCATION_GROUP_ENTRY,
                                    **kwargs)

    def access_control_groups_dialog_save_group_entry(self, element_name, **kwargs):
        """Returns the result of access_control_groups_dialog_save_group_entry."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_SAVE_GROUP_ENTRY, **kwargs)

    def access_control_groups_dialog_save_and_close_group(self, element_name, **kwargs):
        """Returns the result of access_control_groups_dialog_save_and_close_group."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DIALOG_SAVE_AND_CLOSE_GROUP, **kwargs)

    def access_control_groups_delete_group(self, element_name, group_name, **kwargs):
        """Returns the result of access_control_groups_delete_group."""
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.GROUPS_DELETE_GROUP, **kwargs)
