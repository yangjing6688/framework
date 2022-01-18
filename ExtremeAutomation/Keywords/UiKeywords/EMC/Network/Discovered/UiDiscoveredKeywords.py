from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.DiscoveredConstants import DiscoveredConstants


class UiDiscoveredKeywords(UiKeywordBaseClass):

    def __init__(self):
        super(UiDiscoveredKeywords, self).__init__()
        self.api_const = self.constants.API_DISCOVERED
        self.command_const = DiscoveredConstants()

    def click_clear_selected(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Clear Selected Button which removes the selected devices from the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_CLEAR_SELECTED, **kwargs)

    def discovered_select_device_in_table(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - The device ip to select in the table

        Clicks the device ip within the Discovered Table.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_SELECT_DEVICE_IN_TABLE, **kwargs)

    def discovered_select_row_by_column_value(self, element_name, col_name, col_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_name]      - Name of the column to query
        [col_value]     - Value of the column to look for

        Selects the first row in the table which matches the value in the specified column.
        """
        args = {"col_name": col_name,
                "col_value": col_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_SELECT_ROW_BY_COLUMN_VALUE,
                                    **kwargs)

    def discovered_wait_for_device_add(self, element_name, device_ip, timeout=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - The device ip to select in the table

        Waits for the device to appear within the Discovery Table.
        """
        args = {"device_ip": device_ip,
                "timeout": timeout}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_WAIT_FOR_DEVICE_ADD, **kwargs)

    def discovered_confirm_device_ip_profile(self, element_name, ip_address, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - The device ip to select in the table
        [profile_name]  - The profile name to confirm

        Confirms the profile name for a device within the Discovery Table.
        """
        args = {"ip_address": ip_address,
                "profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CONFIRM_DEVICE_IP_PROFILE,
                                    **kwargs)

    def discovered_confirm_device_ip_status(self, element_name, ip_address, status, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - The device ip to select in the table
        [status]        - The status to confirm

        Confirms the ip status for a device within the Discovery Table.
        """
        args = {"ip_address": ip_address,
                "status": status}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CONFIRM_DEVICE_IP_STATUS,
                                    **kwargs)

    def discovered_wait_for_device_remove(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - The device ip to select in the table

        Waits for the device to be removed from the Discovery Table.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_WAIT_FOR_DEVICE_REMOVE, **kwargs)

    def discovered_click_clear_selected(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears the selected rows from the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_CLEAR_SELECTED, **kwargs)

    def discovered_click_clear_all_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clears all rows from the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_CLEAR_ALL_DEVICES, **kwargs)

    def discovered_click_pre_register_device(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Pre Register Device button within  the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_PRE_REGISTER_DEVICE,
                                    **kwargs)

    def discovered_click_add_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - Name of the element the keyword will be run against

        Clicks the "Add Devices..." toolbar button on the Discovered tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_ADD_DEVICES, **kwargs)

    def discovered_click_edit_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Edit Devices within  the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CLICK_EDIT_DEVICES, **kwargs)

    def discovered_refresh_table(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Refresh Table button within  the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_REFRESH_TABLE, **kwargs)

    def discovered_modify_table_refresh_time(self, element_name, time_string, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [time_string]   - The string of time you want to use such as "Refresh 30s", etc

        Clicks the Refresh Table button within  the Discovery Table.
        """
        args = {"time_string": time_string}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_MODIFY_TABLE_REFRESH_TIME,
                                    **kwargs)

    def discovered_reset_table(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Reset Table button within the Discovery Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_RESET_TABLE, **kwargs)

    # ADD DEVICE DIALOG -----------------------------------------------------------------------------------------------
    def discovered_add_device_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name]      - Name of the tab to select

        Selects the specified tab in the Add Device dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SELECT_TAB, **kwargs)

    # Device tab
    def discovered_add_device_set_system_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - String to enter into the field

        Sets the System Name field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_SYSTEM_NAME,
                                    **kwargs)

    def discovered_add_device_set_contact(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - String to enter into the field

        Sets the Contact field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_CONTACT, **kwargs)

    def discovered_add_device_set_location(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - String to enter into the field

        Sets the Location field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_LOCATION, **kwargs)

    def discovered_add_device_set_admin_profile(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to select in the field

        Sets the Admin Profile field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_ADMIN_PROFILE,
                                    **kwargs)

    def discovered_add_device_set_topology_layer(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to select in the field

        Sets the Topology Layer field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_TOPOLOGY_LAYER,
                                    **kwargs)

    def discovered_add_device_set_default_site(self, element_name, site_name, import_site, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name]     - Name of the site to select
        [import_site]   - Indicates whether or not to import settings from the site

        Sets the Default Site field in the Add Device dialog and answers the confirmation dialog on whether or not to
        import the settings.
        """
        args = {"site_name": site_name,
                "import_site": import_site}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_DEFAULT_SITE,
                                    **kwargs)

    def discovered_add_device_set_poll_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to select in the field

        Sets the Poll Group field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_POLL_GROUP,
                                    **kwargs)

    def discovered_add_device_set_poll_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to select in the field

        Sets the Poll Type field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_POLL_TYPE,
                                    **kwargs)

    def discovered_add_device_set_snmp_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to set in the field

        Sets the SNMP Timeout field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_SNMP_TIMEOUT,
                                    **kwargs)

    def discovered_add_device_set_snmp_retries(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value to set in the field

        Sets the SNMP Retries field in the Add Device dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_SET_SNMP_RETRIES,
                                    **kwargs)

    def discovered_add_device_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Add in the Add Device dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_CLICK_ADD, **kwargs)

    def discovered_add_device_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Add Device dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_ADD_DEVICE_CLICK_CANCEL, **kwargs)

    # EDIT DEVICE DIALOG ----------------------------------------------------------------------------------------------
    def discovered_edit_device_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name]      - Name of the tab to select

        Selects the specified tab in the Configure Devices dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SELECT_TAB, **kwargs)

    # DEVICE TAB
    def discovered_edit_device_set_system_name(self, element_name, sys_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [sys_name]      - value of the system name

        Set the sys name value within the Configure Devices Dialog Device Tab.
        """
        args = {"sys_name": sys_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_SYSTEM_NAME,
                                    **kwargs)

    def discovered_edit_device_set_contact(self, element_name, contact, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [contact]       - value of the contact name

        Set the contact name value within the Configure Devices Dialog Device Tab.
        """
        args = {"contact": contact}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_CONTACT, **kwargs)

    def discovered_edit_device_set_location(self, element_name, location, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [location]      - value of the location name

        Set the location value within the Configure Devices Dialog Device Tab.
        """
        args = {"location": location}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_LOCATION,
                                    **kwargs)

    def discovered_edit_device_set_admin_profile(self, element_name, profile, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile]       - value of the profile name

        Set the profile name value within the Configure Devices Dialog Device Tab.
        """
        args = {"profile": profile}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_ADMIN_PROFILE,
                                    **kwargs)

    def discovered_edit_device_set_topology_layer(self, element_name, topology_layer, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [topology_layer] - value of the system name

        Set the topology_layer value within the Configure Devices Dialog Device Tab.
        """
        args = {"topology_layer": topology_layer}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_TOPOLOGY_LAYER,
                                    **kwargs)

    def discovered_edit_device_set_remove_from_service(self, element_name, remove_from_service, **kwargs):
        """
        Keyword Arguments:
        [element_names]       - List of elements the keyword will be run against
        [remove_from_service] - Value of the remove_from_service checkbox

        Set the remove_from_service value within the Configure Devices Dialog Device Tab.
        """
        args = {"remove_from_service": remove_from_service}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_REMOVE_FROM_SERVICE, **kwargs)

    def discovered_edit_device_set_default_site(self, element_name, site_name, import_site, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name]     - Value of the site
        [import_site]   - Option to import the existing site

        Set the site_name value within the Configure Devices Dialog Device Tab
        """
        args = {"site_name": site_name,
                "import_site": import_site}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_DEFAULT_SITE,
                                    **kwargs)

    def discovered_edit_device_set_poll_group(self, element_name, poll_group, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [poll_group]    - Value of the poll_group

        Set the poll_group value within the Configure Devices Dialog Device Tab.
        """
        args = {"poll_group": poll_group}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_POLL_GROUP,
                                    **kwargs)

    def discovered_edit_device_set_poll_type(self, element_name, poll_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [poll_type]     - Value of the poll_type

        Set the poll_type value within the Configure Devices Dialog Device Tab.
        """
        args = {"poll_type": poll_type}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_POLL_TYPE,
                                    **kwargs)

    def discovered_edit_device_set_snmp_timeout(self, element_name, snmp_timeout, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_timeout]  - Value of the snmp_timeout

        Set the snmp_timeout value within the Configure Devices Dialog Device Tab.
        """
        args = {"snmp_timeout": snmp_timeout}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_SNMP_TIMEOUT,
                                    **kwargs)

    def discovered_edit_device_set_snmp_retries(self, element_name, snmp_retries, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_retries]  - Value of the snmp_retries

        Set the snmp_retries value within the Configure Devices Dialog Device Tab.
        """
        args = {"snmp_retries": snmp_retries}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_SNMP_RETRIES,
                                    **kwargs)

    def discovered_edit_device_set_replacement_serial_number(self, element_name, serial_num, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [serial_num]    - Value of the serial_num

        Set the serial_num value within the Configure Devices Dialog Device Tab.
        """
        args = {"serial_num": serial_num}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_REPLACEMENT_SERIAL_NUMBER, **kwargs)

    # ADD DEVICE ACTIONS - OPTIONS
    def discovered_edit_device_set_edit_trap_receiver(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value of the trap receiver checkbox

        Set the trap receiver value within the Configure Devices Dialog Device Actions Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_TRAP_RECEIVER, **kwargs)

    def discovered_edit_device_set_edit_syslog_receiver(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value of the sys_log receiver checkbox

        Set the sys log receiver value within the Configure Devices Dialog Device Actions Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_SYSLOG_RECEIVER, **kwargs)

    def discovered_edit_device_set_enable_collection(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value of the Enable collection checkbox

        Set the Enable collection value within the Configure Devices Dialog Device Actions Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_ENABLE_COLLECTION, **kwargs)

    def discovered_edit_device_set_edit_to_archive(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value of the Archive checkbox

        Set the Archive value within the Configure Devices Dialog Device Actions Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_ARCHIVE,
                                    **kwargs)

    def discovered_edit_device_set_edit_to_map(self, element_name, the_value, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Value of the Map checkbox
        [map_name]      - The map value

        Set the map value within the Configure Devices Dialog Device Actions Tab.
        """
        args = {"the_value": the_value,
                "map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_MAP,
                                    **kwargs)

    # ADD DEVICE ACTIONS - POLICY DOMAIN
    def discovered_edit_device_set_edit_to_policy_domain(self, element_name, add_to_domain, domain_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [add_to_domain] - Value of the add_to_domain checkbox
        [domain_name]   - The domain_name value

        Set the  domain value within the Configure Devices Dialog Device Actions Tab Policy.
        """
        args = {"add_to_domain": add_to_domain,
                "domain_name": domain_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_POLICY_DOMAIN, **kwargs)

    # ADD DEVICE ACTIONS - ACCESS CONTROL
    def discovered_edit_device_set_edit_to_access_control_group(self, element_name, add_to_access_control,
                                                                access_control_group, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [add_to_access_control] - Value of the add_to_access_control checkbox
        [access_control_group]  - The access_control_group value

        Set the  access_control_group value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"add_to_access_control": add_to_access_control,
                "access_control_group": access_control_group}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_ACCESS_CONTROL_GROUP,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_switch_type(self, element_name, switch_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [switch_type]   - Value of the switch_type

        Set the switch_type value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"switch_type": switch_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_SWITCH_TYPE,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_primary_engine(self, element_name, primary_gateway, **kwargs):
        """
        Keyword Arguments:
        [element_names]   - List of elements the keyword will be run against
        [primary_gateway] - Value of the primary_gateway

        Set the primary_gateway value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"primary_gateway": primary_gateway}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_PRIMARY_ENGINE,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_secondary_engine(self, element_name, secondary_gateway,
                                                                        **kwargs):
        """
        Keyword Arguments:
        [element_names]     - List of elements the keyword will be run against
        [secondary_gateway] - Value of the secondary_gateway

        Set the secondary_gateway value within the Configure Devices Dialog Device Actions Tab Access Control
        """
        args = {"secondary_gateway": secondary_gateway}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_SECONDARY_ENGINE,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_auth_access_type(self, element_name, auth_access_type, **kwargs):
        """
        Keyword Arguments:
        [element_names]    - List of elements the keyword will be run against
        [auth_access_type] - Value of the auth_access_type

        Set the auth_access_type value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"auth_access_type": auth_access_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_AUTH_ACCESS_TYPE,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_virtual_router_name(self, element_name, virtual_router,
                                                                           **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [virtual_router] - Value of the virtual_router

        Set the virtual_router value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"virtual_router": virtual_router}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_VIRTUAL_ROUTER_NAME, **kwargs)

    def discovered_edit_device_set_edit_access_control_radius_attrs_to_send(self, element_name, attr_to_send, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [attr_to_send]  - Value of the attr_to_send

        Set the attr_to_send value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"attr_to_send": attr_to_send}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_RADIUS_ATTRS_TO_SEND, **kwargs)

    def discovered_edit_device_set_edit_access_control_radius_accounting(self, element_name, radius_accounting,
                                                                         **kwargs):
        """
        Keyword Arguments:
        [element_names]     - List of elements the keyword will be run against
        [radius_accounting] - Value of the radius_accounting

        Set the radius_accounting value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"radius_accounting": radius_accounting}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_RADIUS_ACCOUNTING, **kwargs)

    def discovered_edit_device_set_edit_access_control_mgmt_radius_server_1(self, element_name, radius_server_1,
                                                                            **kwargs):
        """
        Keyword Arguments:
        [element_names]   - List of elements the keyword will be run against
        [radius_server_1] - Value of the radius_server_1

        Set the radius_server_1 value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"radius_server_1": radius_server_1}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_MGMT_RADIUS_SERVER_1, **kwargs)

    def discovered_edit_device_set_edit_access_control_mgmt_radius_server_2(self, element_name, radius_server_2,
                                                                            **kwargs):
        """
        Keyword Arguments:
        [element_names]   - List of elements the keyword will be run against
        [radius_server_2] - Value of the radius_server_2

        Set the radius_server_2 value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"radius_server_2": radius_server_2}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_MGMT_RADIUS_SERVER_2, **kwargs)

    def discovered_edit_device_set_edit_access_control_network_radius_server(self, element_name, network_radius_server,
                                                                             **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [network_radius_server] -    Value of the network_radius_server

        Set the network_radius_server value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"network_radius_server": network_radius_server}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_NETWORK_RADIUS_SERVER, **kwargs)

    def discovered_edit_device_set_edit_access_control_policy_enforcement_point_1(self, element_name,
                                                                                  policy_enforcement_point_1, **kwargs):
        """
        Keyword Arguments:
        [element_names]              - List of elements the keyword will be run against
        [policy_enforcement_point_1] - Value of the policy_enforcement_point_1

        Set the policy_enforcement_point_1 value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"policy_enforcement_point_1": policy_enforcement_point_1}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_POLICY_ENFORCEMENT_POINT_1, **kwargs)

    def discovered_edit_device_set_edit_access_control_policy_enforcement_point_2(self, element_name,
                                                                                  policy_enforcement_point_2, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [policy_enforcement_point_2] -    Value of the policy_enforcement_point_2

        Set the policy_enforcement_point_2 value within the Configure Devices Dialog Device Actions Tab Access Control.
        """
        args = {"policy_enforcement_point_2": policy_enforcement_point_2}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_POLICY_ENFORCEMENT_POINT_2, **kwargs)

    def discovered_edit_device_set_edit_access_control_enable_auth_using_port_template(self, element_name,
                                                                                       enable_auth_using_port_template,
                                                                                       **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [enable_auth_using_port_template] -    Value of enable_auth_using_port_template

        Set the enable_auth_using_port_template value within the Configure Devices Dialog Device Actions Tab
        Access Control.
        """
        args = {"enable_auth_using_port_template": enable_auth_using_port_template}

        return self.execute_keyword(element_name, args, self.command_const.
                                    ISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ENABLE_AUTH_USING_PORT_TEMPLATE,
                                    **kwargs)

    # ADD DEVICE ACTIONS - ACCESS CONTROL - ADVANCED SETTINGS
    def discovered_edit_device_set_edit_access_control_advanced_settings_open(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Access Control Advanced Settings button to launch Configure Devices Dialog Device Actions Tab
        Access Control Advanced Settings Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_OPEN, **kwargs)

    def discovered_edit_device_set_edit_access_control_advanced_settings_ip_subnet(self, element_name, ip_subnet,
                                                                                   **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_subnet]     - Value of ip_subnet

        Set the ip_subnet value within the Configure Devices Dialog Device Actions Tab Access Control Advanced
        Settings Dialog.
        """
        args = {"ip_subnet": ip_subnet}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_IP_ADDRESS_SUBNET, **kwargs)

    def discovered_edit_device_set_edit_access_control_advanced_settings_shared_secret(self, element_name,
                                                                                       shared_secret, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [shared_secret] - Value of shared_secret

        Set the shared_secret value within the Configure Devices Dialog Device Actions Tab Access Control Advanced
        Settings Dialog.
        """
        args = {"shared_secret": shared_secret}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_SHARED_SECRET,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_advanced_settings_reauth_type(self, element_name,
                                                                                     switch_reauth_config, **kwargs):
        """
        Keyword Arguments:
        [element_names]        - List of elements the keyword will be run against
        [switch_reauth_config] - Value of switch_reauth_config

        Set the switch_reauth_config value within the Configure Devices Dialog Device Actions Tab Access Control
        Advanced Settings Dialog.
        """
        args = {"switch_reauth_config": switch_reauth_config}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_REAUTH_TYPE,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_advanced_settings_enable_port_link(self, element_name, the_value,
                                                                                          **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -    Value of enable port link checkbox

        Set the enable port link checkbox value within the Configure Devices Dialog Device Actions Tab Access Control
        Advanced Settings Dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_ENABLE_PORT_LINK,
                                    **kwargs)

    def discovered_edit_device_set_edit_access_control_advanced_settings_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save button within the Configure Devices Dialog Device Actions Tab Access Control Advanced
        Settings Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_SAVE, **kwargs)

    # DEVICE ANNOTATIONS TAB
    def discovered_edit_device_set_nickname(self, element_name, nickname, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [nickname] - The value of the nickname

        Sets the value of the nickname within the Configure Devices Dialog Device Annotations Tab.
        """
        args = {"nickname": nickname}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_NICKNAME,
                                    **kwargs)

    def discovered_edit_device_set_asset_tag(self, element_name, asset_tag, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [asset_tag]     - The value of the asset_tag

        Sets the value of the asset_tag within the Configure Devices Dialog Device Annotations Tab.
        """
        args = {"asset_tag": asset_tag}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_ASSET_TAG,
                                    **kwargs)

    def discovered_edit_device_set_user_data(self, element_name, user_data, the_field, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [user_data]     - The value of the user_data
        [the_field]     - The value of the user data field 1/2/3/4

        Sets the value of the user data fields within the Configure Devices Dialog Device Annotations Tab.
        """
        args = {"user_data": user_data,
                "the_field": the_field}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_USER_DATA,
                                    **kwargs)

    def discovered_edit_device_set_note(self, element_name, the_note, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_note] - The value of the_note

        Sets the value of the note field within the Configure Devices Dialog Device Annotations Tab.
        """
        args = {"the_note": the_note}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_SET_NOTE, **kwargs)

    # VLAN DEFINITION TAB
    def discovered_edit_device_vlan_definition_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Add button within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_ADD,
                                    **kwargs)

    def discovered_edit_device_vlan_definition_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Edit button within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_EDIT,
                                    **kwargs)

    def discovered_edit_device_vlan_definition_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Delete button within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_DELETE, **kwargs)

    def discovered_edit_device_vlan_definition_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Update button within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_UPDATE, **kwargs)

    def discovered_edit_device_vlan_definition_select_row(self, element_name, vlan_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [vlan_name]     - The VLAN name to select within the table

        Selects the VLAN by name within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {"vlan_name": vlan_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SELECT_ROW, **kwargs)

    def discovered_edit_device_vlan_definition_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VLAN name value

        Sets the VLAN name within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_NAME, **kwargs)

    def discovered_edit_device_vlan_definition_set_vid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VLAN VID value

        Sets the VLAN VID within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_VID, **kwargs)

    def discovered_edit_device_vlan_definition_set_vrf(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VLAN VRF value

        Sets the VLAN VRF within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_VRF, **kwargs)

    def discovered_edit_device_vlan_definition_set_always_write_to_devices(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VLAN always_write_to_devices value

        Sets the VLAN always_write_to_devices within the Configure Devices Dialog Device VLAN Definition Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.
                                    DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_ALWAYS_WRITE_TO_DEVICES, **kwargs)

    # PORTS TAB METHODS
    def discovered_edit_device_ports_select_port(self, element_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_name]     - The port name to select value

        Selects the port by name within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_SELECT_PORT,
                                    **kwargs)

    def discovered_edit_device_ports_edit_row(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Edit button within the Configure Devices Dialog Device Ports Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW,
                                    **kwargs)

    def discovered_edit_device_ports_edit_row_alias(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port alias

        Sets the alias value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_ALIAS,
                                    **kwargs)

    def discovered_edit_device_ports_edit_row_nickname(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port nickname

        Sets the nickname value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_NICKNAME, **kwargs)

    def discovered_edit_device_ports_edit_row_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port enabled

        Sets the enabled value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}
        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_ENABLED, **kwargs)

    def discovered_edit_device_ports_edit_row_auto_negotiation(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port auto negotiation

        Sets the auto negotiation value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_AUTO_NEGOTIATION, **kwargs)

    def discovered_edit_device_ports_edit_row_speed(self, element_name, the_value, auto_neg_value, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [the_value]      - The value for the port auto negotiation
        [auto_neg_value] - The auto_neg_value row speed value

        Sets the auto negotiation row speed value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"auto_neg_value": auto_neg_value,
                "the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_SPEED, **kwargs)

    def discovered_edit_device_ports_edit_row_duplex(self, element_name, the_value, auto_neg_value, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [the_value]      - The value for the port duplex value
        [auto_neg_value] - The auto_neg_value row speed value

        Sets the duplex value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"auto_neg_value": auto_neg_value,
                "the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_DUPLEX, **kwargs)

    def discovered_edit_device_ports_edit_row_configuration(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port configuration value

        Sets the configuration value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_CONFIGURATION, **kwargs)

    def discovered_edit_device_ports_edit_row_pvid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port pvid value

        Sets the pvid value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_PVID,
                                    **kwargs)

    def discovered_edit_device_ports_edit_row_lag(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port lag value (comma separated for multi-select ge.1.1,ge.1.2)

        Sets the lag value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_LAG,
                                    **kwargs)

    def discovered_edit_device_ports_edit_row_authentication(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port authentication value

        Sets the authentication value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_AUTHENTICATION, **kwargs)

    def discovered_edit_device_ports_edit_row_tagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port tagged value

        Sets the tagged value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_TAGGED, **kwargs)

    def discovered_edit_device_ports_edit_row_untagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port untagged value

        Sets the untagged value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_UNTAGGED, **kwargs)

    def discovered_edit_device_ports_edit_row_node_alias(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port node alias value

        Sets the node alias value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_NODE_ALIAS, **kwargs)

    def discovered_edit_device_ports_edit_row_span_guard(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port span guard value

        Sets the span guard value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_SPAN_GUARD, **kwargs)

    def discovered_edit_device_ports_edit_row_loop_protect(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port loop protect value

        Sets the loop protect value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_LOOP_PROTECT, **kwargs)

    def discovered_edit_device_ports_edit_row_mvrp(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value for the port mvrp value

        Sets the mvrp value within the Configure Devices Dialog Device Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_MVRP,
                                    **kwargs)

    def discovered_edit_device_ports_row_editor_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Update button within the port table within the Configure Devices Dialog Device Ports Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_ROW_EDITOR_UPDATE, **kwargs)

    def discovered_edit_device_ports_row_editor_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button within the port table within the Configure Devices Dialog Device Ports Tab.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_ROW_EDITOR_CANCEL, **kwargs)

    # ZTP+ DEVICE SETTINGS
    def discovered_edit_device_ztp_set_configure_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Configure Device value

        Sets the Configure Device checkbox within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_CONFIGURE_DEVICE, **kwargs)

    def discovered_edit_device_ztp_set_serial_number(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Serial Number value

        Sets the serial number within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_SERIAL_NUMBER, **kwargs)

    def discovered_edit_device_ztp_set_ip_address_subnet(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the subnet value

        Sets the subnet within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_IP_ADDRESS_SUBNET, **kwargs)

    def discovered_edit_device_ztp_set_gateway_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the gateway address value

        Sets the gateway address within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_GATEWAY_ADDRESS, **kwargs)

    def discovered_edit_device_ztp_set_management_interface(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the management interface value

        Sets the management interface within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_MANAGEMENT_INTERFACE, **kwargs)

    def discovered_edit_device_ztp_set_domain_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the domain value

        Sets the domain within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_DOMAIN_NAME,
                                    **kwargs)

    def discovered_edit_device_ztp_set_dns_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the DNS Server value

        Sets the DNS Server within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_DNS_SERVER,
                                    **kwargs)

    def discovered_edit_device_ztp_set_ntp_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the NTP Server value

        Sets the NTP Server within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_NTP_SERVER,
                                    **kwargs)

    def discovered_edit_device_ztp_set_firmware_upgrade(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Firmware Upgrade value

        Sets the Firmware Upgrade within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE, **kwargs)

    def discovered_edit_device_ztp_set_firmware_upgrade_date(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Firmware Upgrade Date value

        Sets the Firmware Upgrade Date within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_DATE, **kwargs)

    def discovered_edit_device_ztp_set_firmware_upgrade_time(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Firmware Upgrade Time value

        Sets the Firmware Upgrade Time within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_TIME, **kwargs)

    def discovered_edit_device_ztp_set_firmware_upgrade_utc_offset(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Firmware Upgrade UTC value

        Sets the Firmware Upgrade UTC within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_UTC_OFFSET,
                                    **kwargs)

    def discovered_edit_device_ztp_set_lacp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the LACP value

        Sets LACP within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_LACP,
                                    **kwargs)

    def discovered_edit_device_ztp_set_lldp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the LLDP value

        Sets LLDP within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_LLDP,
                                    **kwargs)

    def discovered_edit_device_ztp_set_mstp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the MSTP value

        Sets MSTP within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_MSTP,
                                    **kwargs)

    def discovered_edit_device_ztp_set_mvrp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the MVRP value

        Sets MVRP within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_MVRP,
                                    **kwargs)

    def discovered_edit_device_ztp_set_poe(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the POE value

        Sets POE within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_POE, **kwargs)

    def discovered_edit_device_ztp_set_xvlan(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - To Enable or Disable the checkbox
        [the_value]     - Sets the XVLAN value

        Sets XVLAN within the Configure Devices Dialog Device ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_ZTP_SET_XVLAN,
                                    **kwargs)

    def discovered_edit_device_vendor_profile_device_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Device Type value

        Sets Device Type within the Configure Devices Dialog Device Vendor Profile Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_DEVICE_TYPE, **kwargs)

    def discovered_edit_device_vendor_profile_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Family value

        Sets Family within the Configure Devices Dialog Device Vendor Profile Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_FAMILY,
                                    **kwargs)

    def discovered_edit_device_vendor_profile_sub_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Sets the Sub Family value

        Sets Sub Family within the Configure Devices Dialog Device Vendor Profile Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_SUB_FAMILY, **kwargs)

    def discovered_edit_device_ports_show_columns(self, element_name, col_list, show_col, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_list]      - Comma-separated list of columns to show
        [show_col]      - Indicates if the specified columns should be shown or hidden (True/False)

        Shows or hides the specified columns in the Ports tab of the Edit Device dialog, depending on the value of
        the "show_col" argument.
        """
        args = {"col_list": col_list,
                "show_col": show_col}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_PORTS_SHOW_COLUMNS,
                                    **kwargs)

    def discovered_edit_device_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Save in the Configure Devices dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_CLICK_SAVE, **kwargs)

    def discovered_edit_device_save_configuration(self, element_name, **kwargs):
        """
        OBSOLETE: use discovered_edit_device_click_save
        Keyword should be updated to new method.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_CLICK_SAVE, **kwargs)

    def discovered_edit_device_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Configure Devices dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_CLICK_CANCEL,
                                    **kwargs)

    def discovered_edit_device_cancel(self, element_name, **kwargs):
        """
        OBSOLETE: use discovered_edit_device_click_cancel
        Keyword should be updated to new method.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_EDIT_DEVICE_CLICK_CANCEL,
                                    **kwargs)

    def discovered_confirm_device_ip_exists(self, element_name, ip_address, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - The ip address to confirm
        [exists]        - The value whether it exists or not

        Confirms that a device exists within the Discovery Table.
        """
        args = {"ip_address": ip_address,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_CONFIRM_DEVICE_IP_EXISTS,
                                    **kwargs)

    # PRE-REGISTERED SECTION
    def discovered_pre_register_device_set_default_site(self, element_name, default_site, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [default_site]  - The value of the default_site to set

        Sets the default_site within the Discovery Table Pre Register Dialog.
        """
        args = {"default_site": default_site}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_SET_DEFAULT_SITE, **kwargs)

    def discovered_pre_register_device_set_ip_address(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - The value of the ip address to set

        Sets the ip address within the Discovery Table Pre Register Dialog.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_SET_IP_ADDRESS, **kwargs)

    def discovered_pre_register_device_set_serial_numbers(self, element_name, serial_nums, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [serial_nums]   - The value of the serial number to set

        Sets the serial number within the Discovery Table Pre Register Dialog.
        """
        args = {"serial_nums": serial_nums}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_SET_SERIAL_NUMBERS, **kwargs)

    def discovered_pre_register_device_next(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Next button within the Discovery Table Pre Register Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_NEXT,
                                    **kwargs)

    def discovered_pre_register_device_previous(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Previous button within the Discovery Table Pre Register Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_PREVIOUS,
                                    **kwargs)

    def discovered_pre_register_device_create(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Create button within the Discovery Table Pre Register Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_CREATE,
                                    **kwargs)

    def discovered_pre_register_device_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Cancel button within the Discovery Table Pre Register Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DISCOVERED_PRE_REGISTER_DEVICE_CANCEL,
                                    **kwargs)

    def discovered_confirm_system_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The system name value to confirm

        Confirms the System Name within the Discovery Table Pre Register Dialog.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_SYSTEM_NAME, **kwargs)
