from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.SitesConstants import SitesConstants


class UiSitesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiSitesKeywords, self).__init__()
        self.api_const = self.constants.API_SITES
        self.command_const = SitesConstants()

    def sites_create_site(self, element_name, site_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to create

        Creates a new site with the specified name.
        """
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CREATE_SITE, **kwargs)

    def sites_delete_site(self, element_name, site_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to delete

        Deletes the site with the specified name.
        """
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DELETE_SITE, **kwargs)

    def sites_rename_site(self, element_name, site_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to delete

        Renames selected site
        """
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_RENAME_SITE, **kwargs)

    def sites_select_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the tab to select

        Selects the specified sub tab for the Sites tab (Discovered, Actions, VLAN Definition, Port Templates,
        ZTP+ Device Defaults).
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_SELECT_SUB_TAB, **kwargs)

    def sites_configure_addresses_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Add' button in the Addresses panel on the Sites Discover tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ADDRESSES_CLICK_ADD,
                                    **kwargs)

    def sites_configure_addresses_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Delete' button in the Addresses panel on the Sites Discover tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ADDRESSES_CLICK_DELETE,
                                    **kwargs)

    def sites_configure_addresses_select_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Address entry to select

        Selects the specified address value in the Addresses panel on the Sites Discover tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ADDRESSES_SELECT_ADDRESS,
                                    **kwargs)

    def sites_configure_addresses_set_enabled(self, element_name, the_address, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_address] -   Address to set the Enabled check button state for
        [btn_state] -     Indicates whether to enable or disable the Enabled check button (True/False)

        Sets the state of the Enabled check button for the specified address in the Addresses panel on
        the Sites Discover tab.
        """
        args = {"the_address": the_address,
                "btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ADDRESSES_SET_ENABLED,
                                    **kwargs)

    def sites_configure_profiles_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Add' button in the Profiles panel on the Sites Discover tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_CLICK_ADD, **kwargs)

    def sites_configure_profiles_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Edit' button in the Profiles panel on the Sites Discover tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_CLICK_EDIT,
                                    **kwargs)

    def sites_configure_profiles_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Delete' button in the Profiles panel on the Sites Discover tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_CLICK_DELETE,
                                    **kwargs)

    def sites_configure_profiles_select_profile(self, element_name, the_profile, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_profile] -   Profile to select

        Selects the specified profile in the Profiles panel on the Sites Discover tab.
        """
        args = {"the_profile": the_profile}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_SELECT_PROFILE,
                                    **kwargs)

    def sites_configure_profiles_set_accept(self, element_name, the_profile, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_profile] -   Profile to set the Accept check button state for
        [btn_state] -     Indicates whether to enable or disable the Accept check button (True/False)

        Sets the state of the Accept check button for the specified profile in the Profiles panel on the
        Sites Discover tab.
        """
        args = {"the_profile": the_profile,
                "btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_SET_ACCEPT,
                                    **kwargs)

    def sites_configure_profiles_set_reject(self, element_name, the_profile, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_profile] -   Profile to set the Reject check button state for
        [btn_state] -     Indicates whether to enable or disable the Reject check button (True/False)

        Sets the state of the Reject check button for the specified profile in the Profiles panel on the
        Sites Discover tab.
        """
        args = {"the_profile": the_profile,
                "btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PROFILES_SET_REJECT,
                                    **kwargs)

    def sites_configure_actions_set_automatically_add_devices(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Automatically Add Devices check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_AUTOMATICALLY_ADD_DEVICES, **kwargs)

    def sites_configure_actions_set_add_trap_receiver(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add Trap Receiver check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ADD_TRAP_RECEIVER, **kwargs)

    def sites_configure_actions_set_add_syslog_receiver(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add Syslog Receiver check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ADD_SYSLOG_RECEIVER, **kwargs)

    def sites_configure_actions_set_enable_collection(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Enable Collection check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ENABLE_COLLECTION, **kwargs)

    def sites_configure_actions_set_add_to_archive(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add to Archive check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ADD_TO_ARCHIVE, **kwargs)

    def sites_configure_actions_set_add_to_map(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add to Map check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ADD_TO_MAP, **kwargs)

    def sites_configure_actions_set_map(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to select

        Selects the specified map on the Sites Action tab.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ACTIONS_SET_MAP, **kwargs)

    def sites_configure_actions_set_add_device_to_policy_domain(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add Device to Policy Domain check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ADD_DEVICE_TO_POLICY_DOMAIN,
                                    **kwargs)

    def sites_configure_actions_set_policy_domain(self, element_name, policy_domain, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [policy_domain] - Name of the policy domain to select

        Selects the specified policy domain on the Sites Action tab.
        """
        args = {"policy_domain": policy_domain}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ACTIONS_SET_POLICY_DOMAIN,
                                    **kwargs)

    def sites_configure_actions_set_add_device_to_access_control_engine_group(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Add Device to Access Control engine Group check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.command_const.
                                    SITES_CONFIGURE_ACTIONS_SET_ADD_DEVICE_TO_ACCESS_CONTROL_ENGINE_GROUP, **kwargs)

    def sites_configure_actions_set_access_control_engine_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the access control engine group to select

        Sets the state of the Automatically Add Devices check button on the Sites Action tab.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_ACTIONS_SET_ACCESS_CONTROL_ENGINE_GROUP,
                                    **kwargs)

    def sites_configure_actions_set_enable_authentication_using_port_template(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether to enable or disable the check button (True/False)

        Sets the state of the Enable Authentication Using Port Template check button on the Sites Action tab.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.command_const.
                                    SITES_CONFIGURE_ACTIONS_SET_ENABLE_AUTHENTICATION_USING_PORT_TEMPLATE, **kwargs)

    def sites_configure_vlan_select_vlan(self, element_name, the_vlan, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_vlan] -      Name of the VLAN to select

        Selects the specified VLAN on the Sites VLAN Definition tab.
        """
        args = {"the_vlan": the_vlan}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_SELECT_VLAN, **kwargs)

    def sites_configure_vlan_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Add' on the Sites VLAN Definition tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_CLICK_ADD, **kwargs)

    def sites_configure_vlan_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Edit' on the Sites VLAN Definition tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_CLICK_EDIT, **kwargs)

    def sites_configure_vlan_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Delete' on the Sites VLAN Definition tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_CLICK_DELETE, **kwargs)

    def sites_configure_vlan_row_click_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Update' in the row editor on the Sites VLAN Definition tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_ROW_CLICK_UPDATE,
                                    **kwargs)

    def sites_configure_vlan_row_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the row editor on the Sites VLAN Definition tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_ROW_CLICK_CANCEL,
                                    **kwargs)

    def sites_configure_vlan_row_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Name field in the row editor

        Sets the specified value in the Name field of the row editor on the Sites VLAN Definition tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_ROW_SET_NAME, **kwargs)

    def sites_configure_vlan_row_set_vid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the VID field in the row editor

        Sets the specified value in the VID field of the row editor on the Sites VLAN Definition tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_VLAN_ROW_SET_VID, **kwargs)

    def sites_configure_vlan_row_set_always_write_to_devices(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Always Write to Devices check button field in the row editor

        Sets the specified value in the Always Write to Devices check button field of the row editor on the
        Sites VLAN Definition tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_VLAN_ROW_SET_ALWAYS_WRITE_TO_DEVICES, **kwargs)

    def sites_configure_ports_select_port_configuration(self, element_name, port_config, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_config] -   Port configuration to select

        Selects the specified port configuration on the Sites Port Templates tab.
        """
        args = {"port_config": port_config}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_PORTS_SELECT_PORT_CONFIGURATION, **kwargs)

    def sites_configure_ports_show_columns(self, element_name, col_list, show_col, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [column_list] - The list of columns to show or hide
        [show_col] - Whether to show or hide the columns

        This will launch the menu pick to show or hide columns within the Devices/Configure Device Dialog Ports Tab.
        """
        args = {"col_list": col_list,
                "show_col": show_col}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_SHOW_COLUMNS, **kwargs)

    def sites_configure_ports_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Edit' on the Sites Port Templates tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_CLICK_EDIT, **kwargs)

    def sites_configure_ports_row_click_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Update' in the row editor on the Sites Port Templates tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_CLICK_UPDATE,
                                    **kwargs)

    def sites_configure_ports_row_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the row editor on the Sites Port Templates tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_CLICK_CANCEL,
                                    **kwargs)

    def sites_configure_ports_row_set_pvid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the PVID field in the row editor

        Sets the specified value in the PVID field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_PVID, **kwargs)

    def sites_configure_ports_row_set_policy(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Policy field in the row editor

        Sets the specified value in the Policy field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_POLICY,
                                    **kwargs)

    def sites_configure_ports_row_set_authentication(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Authentication field in the row editor

        Sets the specified value in the Authentication field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_AUTHENTICATION,
                                    **kwargs)

    def sites_configure_ports_row_set_tagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Tagged field in the row editor

        Sets the specified value in the Tagged field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_TAGGED,
                                    **kwargs)

    def sites_configure_ports_row_set_untagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Untagged field in the row editor

        Sets the specified value in the Untagged field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_UNTAGGED,
                                    **kwargs)

    def sites_configure_ports_row_set_node_alias(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Node Alias field in the row editor

        Sets the specified value in the Node Alias field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_NODE_ALIAS,
                                    **kwargs)

    def sites_configure_ports_row_set_span_guard(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Span Guard field in the row editor

        Sets the specified value in the Span Guard field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_SPAN_GUARD,
                                    **kwargs)

    def sites_configure_ports_row_set_loop_protect(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Loop Protect field in the row editor

        Sets the specified value in the Loop Protect field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_LOOP_PROTECT,
                                    **kwargs)

    def sites_configure_ports_row_set_mvrp(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the MVRP field in the row editor

        Sets the specified value in the MVRP field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_MVRP, **kwargs)

    def sites_configure_ports_row_set_auto_negotiation(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Auto Negotiation field in the row editor

        Sets the specified value in the Auto Negotiation field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_AUTO_NEGOTIATION, **kwargs)

    def sites_configure_ports_row_set_collection(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Collection field in the row editor

        Sets the specified value in the Collection field of the row editor on the Sites Port Templates tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_PORTS_ROW_SET_COLLECTION,
                                    **kwargs)

    def sites_configure_ztp_set_configure_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Configure Device check button (True/False)

        Sets the enabled state of the Configure Device check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_CONFIGURE_DEVICE,
                                    **kwargs)

    def sites_configure_ztp_set_use_discovered_ip(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Use Discovered IP check button (True/False)

        Sets the enabled state of the Use Discovered IP check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_USE_DISCOVERED_IP,
                                    **kwargs)

    def sites_configure_ztp_set_subnet_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Subnet Address field

        Sets the value of the Subnet Address field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_SUBNET_ADDRESS,
                                    **kwargs)

    def sites_configure_ztp_set_gateway_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Gateway Address field

        Sets the value of the Gateway Address field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_GATEWAY_ADDRESS,
                                    **kwargs)

    def sites_configure_ztp_set_management_interface(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Management Interface field

        Sets the value of the Management Interface field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_MANAGEMENT_INTERFACE,
                                    **kwargs)

    def sites_configure_ztp_set_domain_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Domain Name field

        Sets the value of the Domain Name field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_DOMAIN_NAME,
                                    **kwargs)

    def sites_configure_ztp_set_dns_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the DNS Server field

        Sets the value of the DNS Server field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_DNS_SERVER, **kwargs)

    def sites_configure_ztp_set_ntp_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the NTP Server field

        Sets the value of the NTP Server field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_NTP_SERVER, **kwargs)

    def sites_configure_ztp_set_starting_ip_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Starting IP Address field

        Sets the value of the Starting IP Address field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_STARTING_IP_ADDRESS,
                                    **kwargs)

    def sites_configure_ztp_set_ending_ip_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Ending IP Address field

        Sets the value of the Ending IP Address field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_ENDING_IP_ADDRESS,
                                    **kwargs)

    def sites_configure_ztp_set_admin_profile(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Admin Profile field

        Sets the value of the Admin Profile field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_ADMIN_PROFILE,
                                    **kwargs)

    def sites_configure_ztp_set_poll_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Poll Group field

        Sets the value of the Poll Group field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_POLL_GROUP, **kwargs)

    def sites_configure_ztp_set_poll_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Poll Type field

        Sets the value of the Poll Type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_POLL_TYPE, **kwargs)

    def sites_configure_ztp_set_lacp_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the LACP Enabled check button (True/False)

        Sets the enabled state of the LACP Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_LACP_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_lacp_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the LACP type field

        Sets the value of the LACP type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_LACP_TYPE, **kwargs)

    def sites_configure_ztp_set_lldp_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the LLDP Enabled check button (True/False)

        Sets the enabled state of the LLDP Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_LLDP_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_lldp_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the LLDP type field

        Sets the value of the LLDP type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_LLDP_TYPE, **kwargs)

    def sites_configure_ztp_set_mstp_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the MSTP Enabled check button (True/False)

        Sets the enabled state of the MSTP Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_MSTP_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_mstp_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the MSTP type field

        Sets the value of the MSTP type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_MSTP_TYPE,
                                    **kwargs)

    def sites_configure_ztp_set_mvrp_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the MVRP Enabled check button (True/False)

        Sets the enabled state of the MVRP Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_MVRP_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_mvrp_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the MVRP type field

        Sets the value of the MVRP type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_MVRP_TYPE, **kwargs)

    def sites_configure_ztp_set_poe_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the POE Enabled check button (True/False)

        Sets the enabled state of the POE Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_POE_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_poe_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the POE type field

        Sets the value of the POE type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_POE_TYPE, **kwargs)

    def sites_configure_ztp_set_vxlan_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the VXLAN Enabled check button (True/False)

        Sets the enabled state of the VXLAN Enabled check button on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_VXLAN_ENABLED,
                                    **kwargs)

    def sites_configure_ztp_set_vxlan_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the VXLAN type field

        Sets the value of the VXLAN type field on the Sites ZTP+ Device Defaults tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_ZTP_SET_VXLAN_TYPE, **kwargs)

    def sites_configure_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Cancel' button on the Sites tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_CLICK_CANCEL, **kwargs)

    def sites_configure_click_configure_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Configure Devices' button on the Sites tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_CLICK_CONFIGURE_DEVICES,
                                    **kwargs)

    def sites_configure_devices_select_device(self, element_name, ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Configure Devices' button on the Sites tab.
        """
        args = {'ip': ip}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_DEVICES_SELECT_DEVICE,
                                    **kwargs)

    def sites_configure_click_discover(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Discover' button on the Sites tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_CLICK_DISCOVER, **kwargs)

    def sites_configure_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Save' button on the Sites tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_CLICK_SAVE, **kwargs)

    def sites_configure_click_scheduler(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Scheduler' button on the Sites tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIGURE_CLICK_SCHEDULER, **kwargs)

    def sites_dialog_address_set_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Discover Type field

        Sets the value of the Discover Type field in the Add Address dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_SET_TYPE, **kwargs)

    def sites_dialog_address_set_subnet(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Subnet field

        Sets the value of the Subnet field in the Add Address dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_SET_SUBNET, **kwargs)

    def sites_dialog_address_set_seed_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Seed Address field

        Sets the value of the Seed Address field in the Add Address dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_SET_SEED_ADDRESS,
                                    **kwargs)

    def sites_dialog_address_set_start_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the Start Address field

        Sets the value of the Start Address field in the Add Address dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_SET_START_ADDRESS,
                                    **kwargs)

    def sites_dialog_address_set_end_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select for the End Address field

        Sets the value of the End Address field in the Add Address dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_SET_END_ADDRESS,
                                    **kwargs)

    def sites_dialog_address_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'OK' in the Add Address dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_CLICK_OK, **kwargs)

    def sites_dialog_address_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Cancel' in the Add Address dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DIALOG_ADDRESS_CLICK_CANCEL, **kwargs)

    def sites_confirm_site_exists(self, element_name, site_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to check for
        [exists] -        Indicates whether or not the site is expected to exist (True/False)

        Verifies whether or not the specified site exists.
        Passes/fails the test based on the expected value, as indicated by the "exists" argument.
        """
        args = {"site_name": site_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIRM_SITE_EXISTS, **kwargs)

    def sites_wait_for_site_add(self, element_name, site_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to wait for being added

        Waits for the specified site to be added to the tree.
        """
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_WAIT_FOR_SITE_ADD, **kwargs)

    def sites_wait_for_site_remove(self, element_name, site_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to wait for being removed

        Waits for the specified site to be removed from the tree.
        """
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_WAIT_FOR_SITE_REMOVE, **kwargs)

    def sites_validate_all_site_summary_parameters(self, element_name, site_path, seed_address, subnet_address,
                                                   address_range, vlan_summary, ztp_summary, policy_summary,
                                                   access_control, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to wait for being removed

        Waits for the specified site to be removed from the tree.
        """
        args = {"site_path": site_path,
                'seed_address': seed_address,
                'subnet_address': subnet_address,
                'address_range': address_range,
                'vlan_summary': vlan_summary,
                'ztp_summary': ztp_summary,
                'policy_summary': policy_summary,
                'access_control': access_control
                }

        return self.execute_keyword(element_name, args, self.command_const.SITES_VALIDATE_ALL_SITE_SUMMARY_PARAMETERS,
                                    **kwargs)

    def sites_confirm_sites_menu_exists(self, element_name, menu_name, exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name] -     Name of the site to wait for being removed

        Waits for the specified site to be removed from the tree.
        """
        args = {"menu_name": menu_name,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CONFIRM_SITES_MENU_EXISTS, **kwargs)
