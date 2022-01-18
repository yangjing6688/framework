from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.DevicesConstants import DevicesConstants


class UiDevicesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDevicesKeywords, self).__init__()
        self.api_const = self.constants.API_DEVICES
        self.command_const = DevicesConstants()

    def devices_select_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name]      - Name of the tab to select

        Clicks any tab within the Devices group [Device/World/Site Summary/Flex Reports].
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_SUB_TAB, **kwargs)

    def devices_select_devices_summary_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name]      - Name of the tab to select under the World tab

        Clicks any tab within the World group [Discover/Actions/VLAN Definition/Port Templates/ZTP+ Device Defaults].
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICES_SUMMARY_SUB_TAB,
                                    **kwargs)

    def devices_select_device_tree_context(self, element_name, context, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [context]       - Name of the value within the Devices Tree top combo box

        Selects any value within the top combo box of the Device Tree [by IP, by Contact, Sites etc.].
        """
        args = {"tree_context": context}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICE_TREE_CONTEXT, **kwargs)

    def devices_expand_device_tree_node(self, element_name, tree_node, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tree_node]     - Name of the node value within the Devices Tree to expand

        Expands any node value within the Device Tree.
        """
        args = {"tree_node": tree_node}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EXPAND_DEVICE_TREE_NODE, **kwargs)

    def devices_select_device_tree_node(self, element_name, tree_node, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tree_node]     - Name of the node value within the Devices Tree to select

        Selects any node value within the Device Tree.
        """
        args = {"tree_node": tree_node}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICE_TREE_NODE, **kwargs)

    def devices_select_device_in_table(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - Name of the ipp value within the Devices table to select

        Selects any ip value within the Device Table.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICE_IN_TABLE, **kwargs)

    def devices_refresh_devices_table(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Refresh button at the bottom of the table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REFRESH_DEVICES_TABLE, **kwargs)

    def devices_select_context_menu(self, element_name, menu_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_name]     - Name of the menu to look for;  comma-separated list of strings if the menu is a sub menu

        Selects the specified device context menu.  If the menu is a sub menu, the menu_name argument should be a
        comma-separated list of menus to traverse.
        """
        args = {"menu_name": menu_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_CONTEXT_MENU, **kwargs)

    def devices_add_device(self, element_name, ip_address, snmp_profile, nickname, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ipp value within the Devices table to select
        [snmp_profile]  - Name of the Profile to use
        [nickname]      - Nickname for the device during the test

        Adds a device within the Device Table.
        """
        args = {"ip_address": ip_address,
                "snmp_profile": snmp_profile,
                "nickname": nickname}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_ADD_DEVICE, **kwargs)

    def devices_configure_device(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ipp value within the Devices table to select

        Selects a device within the Device Table then clicks the Configure Device toolbar button.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIGURE_DEVICE, **kwargs)

    def devices_open_device_terminal(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects a device within the Device Table then clicks the Open Device Terminal toolbar button.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_OPEN_DEVICE_TERMINAL, **kwargs)

    def devices_close_device_terminal(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Closes an open device terminal.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CLOSE_DEVICE_TERMINAL, **kwargs)

    def devices_confirm_device_terminal_enters_device_prompt(self, element_name, ip_address, prompt, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select
        [prompt]        - The expected prompt value to confirm device terminal worked properly.

        Verifies that the device terminal gets to the expected device prompt.
        """
        args = {"ip_address": ip_address,
                "prompt": prompt}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_TERMINAL_ENTERS_DEVICE_PROMPT, **kwargs)

    def devices_launch_webview(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects a device within the Device Table then clicks the Launch WebView toolbar button.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_LAUNCH_WEBVIEW, **kwargs)

    def devices_delete_device(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ipp value within the Devices table to select

        Deletes a device within the Device Table.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DELETE_DEVICE, **kwargs)

    def devices_refresh_device_tree_my_network(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Refreshes the device tree to reload devices.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REFRESH_DEVICE_TREE_MY_NETWORK,
                                    **kwargs)

    def devices_set_device_profile(self, element_name, ip_address, snmp_profile, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select
        [snmp_profile]  - Name of the Profile to use

        Selects an existing device within the Device Table, then chooses the menu option Set Profile which opens the
        dialog and edits the profile name value.
        """
        args = {"ip_address": ip_address,
                "snmp_profile": snmp_profile}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SET_DEVICE_PROFILE, **kwargs)

    def devices_register_trap_receiver(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Device Table, then chooses the menu option Register Trap Receiver.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REGISTER_TRAP_RECEIVER, **kwargs)

    def devices_unregister_trap_receiver(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Device Table, then chooses the menu option Unregister Trap Receiver.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_UNREGISTER_TRAP_RECEIVER, **kwargs)

    def devices_register_syslog_receiver(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Device Table, then chooses the menu option Register Syslog Receiver.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REGISTER_SYSLOG_RECEIVER, **kwargs)

    def devices_unregister_syslog_receiver(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Device Table, then chooses the menu option Unregister Syslog Receiver.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_UNREGISTER_SYSLOG_RECEIVER, **kwargs)

    def devices_collect_device_statistics(self, element_name, ip_address, stat_name, monitor_selection="Proceed",
                                          **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select
        [stat_name]     - Name of the Collection Statistic Type Disable/Monitor/Historical
        [monitor_selection="Proceed"] - If Monitor is chosen we default the Monitor selection dialog with Proceed

        Selects an existing device within the Device Table, then chooses the menu option Collect Device Statistics.
        """
        args = {"ip_address": ip_address,
                "stat_name": stat_name,
                "monitor_selection": monitor_selection}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_COLLECT_DEVICE_STATISTICS, **kwargs)

    def devices_collect_interface_statistics(self, element_name, device_ip, group_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - IP address of the device within the Devices table to select
        [group_name]    - Name of the Device Port Group
        [port_name]     - The port within the Port Group to collect statisics against

        Selects an existing device within the Device Port Group then selects a port within the table the menu option
        to Collect Port Statistics.
        """
        args = {"ip_address": device_ip,
                "group_name": group_name,
                "port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_COLLECT_INTERFACE_STATISTICS,
                                    **kwargs)

    def devices_collect_port_statistics(self, element_name, device_ip, group_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - IP address of the device within the Devices table to select
        [group_name]    - Name of the Device Port Group
        [port_name]     - The port within the Port Group to collect statistics against

        Selects an existing device within the Device Port Group then selects a port within the table the menu option
        to Collect Port Statistics.
        """
        args = {"ip_address": device_ip,
                "group_name": group_name,
                "port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_COLLECT_PORT_STATISTICS,
                                    **kwargs)

    def devices_enable_port(self, element_name, ip_address, group_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - Name of the ip value within the Devices table to select
        [group_name]    - Name of the Device Port Group
        [port_name]     - The port within the Port Group to enable the port

        Selects an existing device within the Device Port Group then selects a port within the table then the menu
        option to Enable Port.
        """
        args = {"ip_address": ip_address,
                "group_name": group_name,
                "port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_ENABLE_PORT, **kwargs)

    def devices_disable_port(self, element_name, ip_address, group_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - Name of the ip value within the Devices table to select
        [group_name]    - Name of the Device Port Group
        [port_name]     - The port within the Port Group to disable the port

        Selects an existing device within the Device Port Group then selects a port within the table then the menu
        option to Disable Port.
        """
        args = {"ip_address": ip_address,
                "group_name": group_name,
                "port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DISABLE_PORT, **kwargs)

    def devices_open_device_view(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Devices Table then selects the device view icon to launch dialog.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_OPEN_DEVICE_VIEW, **kwargs)

    def devices_add_device_to_group(self, element_name, group_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name]    - Name of the Group to create and add IP address to
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device within the Devices Table then selects creates a new group to add the ip address to
        """
        args = {"group_name": group_name,
                "ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_ADD_DEVICE_TO_GROUP, **kwargs)

    def devices_remove_device_from_group(self, element_name, group_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name]    - Name of the Group to remove IP address from.
        [ip_address]    - Name of the ip value within the Devices table to select

        Selects an existing device group and removes a specific ip address.
        """
        args = {"group_name": group_name,
                "ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REMOVE_DEVICE_FROM_GROUP, **kwargs)

    def devices_wait_for_device_add(self, element_name, device_ip, timeout=60, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - Name of the ip value within the Devices table to select

        Waits for a specific ip address to appear within the devices table.
        """
        args = {"device_ip": device_ip,
                "timeout": timeout}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_WAIT_FOR_DEVICE_ADD, **kwargs)

    def devices_wait_for_device_remove(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - Name of the ip value within the Devices table to select

        Waits for a specific ip address to clear within the devices table.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_WAIT_FOR_DEVICE_REMOVE, **kwargs)

    def devices_wait_for_device_value(self, element_name, device_ip, col_name, expected_value, wait_time=60, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [device_ip]      - IP address of the device to check
        [col_name]       - Name of the column to check
        [expected_value] - Value to wait for
        [wait_time]      - Amount of time to wait for the value

        Waits until the device has the expected value for the specified attribute in the specified column.
        If the value doesn't match within the specified wait_time, the test will fail.
        """
        args = {"device_ip": device_ip,
                "col_name": col_name,
                "expected_value": expected_value,
                "wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_WAIT_FOR_DEVICE_VALUE, **kwargs)

    def devices_confirm_firmware_version(self, element_name, ip_address, version, max_attempts=0, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - Name of the ip value within the Devices table to select
        [version]       - The version of the firmware to confirm
        [max_attempts]  - The number of attempts to verify the firmware version

        Verifies the firmware version of a device ip within the devices table.
        """
        args = {"ip_address": ip_address,
                "version": version,
                "max_attempts": max_attempts}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_FIRMWARE_VERSION, **kwargs)

    def devices_confirm_ip_exists(self, element_name, ip, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip]            - Name of the ip value within the Devices table to confirm exists or not
        [exists]        - Either True or False to check whether the device ip exists or not

        Verifies the ip of the device within the devices table.
        """
        args = {"ip": ip,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_EXISTS, **kwargs)

    def devices_confirm_ip_admin_profile(self, element_name, admin_profile, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [admin_profile] - Name of the admin profile value within the Devices table to confirm exists or not
        [exists]        - Either True or False to check whether the device ip exists or not

        Verifies the admin profile of a device ip within the devices table.
        """
        args = {"admin_profile": admin_profile,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_ADMIN_PROFILE, **kwargs)

    def devices_confirm_ip_stats(self, element_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [exists]        - Either True or False to check whether the device ip exists or not

        Verifies the statistics of a device ip within the devices table.
        """
        args = {"exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_STATS, **kwargs)

    def devices_confirm_ip_collection_statistics(self, element_name, collection, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [collection]    - The collection type value to confirm
        [exists]        - Either True or False to check whether the statistic is exists or not

        Verifies the statistics setting of a device ip within the devices table.
        """
        args = {"collection": collection,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_COLLECTION_STATISTICS,
                                    **kwargs)

    def devices_confirm_ip_syslog_status(self, element_name, syslog_status, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [syslog_status] - The syslog value to confirm
        [exists]        - Either True or False to check whether the syslog_status is exists or not

        Verifies the sys log setting of a device ip within the devices table.
        """
        args = {"syslog_status": syslog_status,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_SYSLOG_STATUS, **kwargs)

    def devices_confirm_ip_trap_status(self, element_name, trap_status, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [trap_status]   - The trap_status value to confirm
        [exists]        - Either True or False to check whether the syslog_status is exists or not

        Verifies the trap_status setting of a device ip within the devices table.
        """
        args = {"trap_status": trap_status,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_IP_TRAP_STATUS, **kwargs)

    def devices_select_all_devices_in_table(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects All devices within the devices table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_ALL_DEVICES_IN_TABLE,
                                    **kwargs)

    def devices_delete_selected_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Deletes All selected devices within the devices table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DELETE_SELECTED_DEVICES, **kwargs)

    def devices_confirm_status(self, element_name, ip_address, status, max_attempts, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - The ip address to check the status value
        [status]        - The status to confirm
        [max_attempts]  - The number of attempts to confirm the status

        This will confirm a devices status.
        """
        args = {"ip_address": ip_address,
                "status": status,
                "max_attempts": max_attempts}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_STATUS, **kwargs)

    def devices_refresh_rediscover_device(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will confirm a devices status after adding the device it will perform a Refresh and Rediscover.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REFRESH_REDISCOVER_DEVICE, **kwargs)

    def devices_confirm_system_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the system name value

        This will confirm a devices system name within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_SYSTEM_NAME, **kwargs)

    def devices_confirm_contact(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the contact name value

        This will confirm a devices contact name within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_CONTACT, **kwargs)

    def devices_confirm_location(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the location value

        This will confirm a devices location value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_LOCATION, **kwargs)

    def devices_confirm_admin_profile(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the admin profile value

        This will confirm a devices admin profile value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_ADMIN_PROFILE, **kwargs)

    def devices_confirm_serial_number(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the serial number value

        This will confirm a devices serial number value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_SERIAL_NUMBER, **kwargs)

    def devices_confirm_remove_from_service(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the Remove From Service value

        This will confirm a devices Remove From Service value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_REMOVE_FROM_SERVICE,
                                    **kwargs)

    def devices_confirm_default_site(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the Site value

        This will confirm a devices Site value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEFAULT_SITE, **kwargs)

    def devices_confirm_poll_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the Poll Group value

        This will confirm a devices Poll Group value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_POLL_GROUP, **kwargs)

    def devices_confirm_poll_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the Poll Type value

        This will confirm a devices Poll Type value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_POLL_TYPE, **kwargs)

    def devices_confirm_snmp_timeout(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the SNMP Timeout value

        This will confirm a devices SNMP Timeout value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_SNMP_TIMEOUT, **kwargs)

    def devices_confirm_snmp_retries(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the SNMP Retries value

        This will confirm a devices SNMP Retries value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_SNMP_RETRIES, **kwargs)

    def devices_confirm_topology_layer(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the Topology Layer value

        This will confirm a devices Topology Layer value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_TOPOLOGY_LAYER, **kwargs)

    def devices_confirm_nickname(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the nickname value

        This will confirm a devices nickname value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_NICKNAME, **kwargs)

    def devices_confirm_asset_tag(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the asset tag value

        This will confirm a devices asset tag value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_ASSET_TAG, **kwargs)

    def devices_confirm_user_data(self, element_name, the_value, data_num, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the user data value
        [data_num]      - The User Data number 1/2/3/4

        This will confirm a devices User Data value within the Devices Table.
        """
        args = {'the_value': the_value,
                'data_num': data_num}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_USER_DATA, **kwargs)

    def devices_confirm_note(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Confirm the note value

        This will confirm a devices note value within the Devices Table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_NOTE, **kwargs)

    def devices_confirm_firmware_version_and_rediscover(self, element_name, ip_address, version, max_attempts=0,
                                                        delay_rediscover=1, **kwargs):
        """
        Keyword Arguments:
        [element_names]      - List of elements the keyword will be run against
        [ip_address]         - ip address rto confirmfirmware version on
        [version]            - The version to confirm
        [max_attempts=0]     - The number of attempts to make
        [delay_rediscover=1] - Whether to use the delay rediscover checkbox

        This will confirm a devices firmware and rediscover device within the Devices Table.
        """
        args = {"ip_address": ip_address,
                "version": version,
                "max_attempts": max_attempts,
                "delay_rediscover": delay_rediscover}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_FIRMWARE_VERSION_AND_REDISCOVER, **kwargs)

    def devices_confirm_device_is_collecting_statistics(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - IP address of the device to check
        [the_value]     - Indicates if the device is expected to be collecting statistics or not (True/False)

        Checks if the specified device is collecting statistics (historical or monitored) or not (disabled).
        NOTE: To check the actual type of statistic being collected (disabled/historical/monitored), use
        "devices_confirm_table_value", passing "Stats" as the column name and "0" (disabled), "2" (historical), or
        "4" (monitored) for the value.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_IS_COLLECTING_STATISTICS, **kwargs)

    def devices_confirm_table_value(self, element_name, device_ip, col_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - IP address of the device to check
        [col_name]      - Name of the table column to check
        [the_value]     - Value to check

        Checks whether or not the specified device has the expected value in the specified column of the Devices table.
        """
        args = {"device_ip": device_ip,
                "col_name": col_name,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_TABLE_VALUE, **kwargs)

    def devices_edit_device_set_nickname(self, element_name, nick_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [nick_name]     - The nickname within the Devices/Configure Devices Dialog

        This will set the devices nickname the Devices/Configure Devices Table.
        """
        args = {'nick_name': nick_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_NICKNAME, **kwargs)

    def devices_edit_device_set_asset_tag(self, element_name, asset_tag, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [asset_tag]     - The asset_tag within the Devices/Configure Devices Dialog

        This will set the asset_tag the Devices/Configure Devices Table.
        """
        args = {'asset_tag': asset_tag}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_ASSET_TAG, **kwargs)

    def devices_edit_device_set_user_data(self, element_name, the_field, user_data, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_field]     - The asset_tag within the Devices/Configure Devices Dialog
        [user_data]     - The user_data field number to set 1/2/3/4

        This will set the user data of the Devices/Configure Devices Table.
        """
        args = {'the_field': the_field,
                'user_data': user_data}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_USER_DATA, **kwargs)

    def devices_edit_device_set_note(self, element_name, the_note, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_note]      - The note value within the Devices/Configure Devices Dialog

        This will set the note value of the Devices/Configure Devices Table.
        """
        args = {'the_note': the_note}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_NOTE, **kwargs)

    def devices_edit_device_vlan_definition_select_row(self, element_name, vlan_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [vlan_name]     - The vlan_name value within the Devices/Configure Devices Dialog VLAN Table to select

        This will select the vlan_name of the Devices/Configure VLAN Definition Table.
        """
        args = {'vlan_name': vlan_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SELECT_ROW, **kwargs)

    def devices_edit_device_vlan_definition_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        After a vlan_name is selected this keyword will click the Add button of the Devices/Configure VLAN
        Definition Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_ADD,
                                    **kwargs)

    def devices_edit_device_vlan_definition_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        After a vlan_name is selected this keyword will click the Edit button of the Devices/Configure VLAN
        Definition Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_EDIT,
                                    **kwargs)

    def devices_edit_device_vlan_definition_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        After a vlan_name is selected this keyword will click the Delete button of the Devices/Configure VLAN
        Definition Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_DELETE,
                                    **kwargs)

    def devices_edit_device_vlan_definition_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        After a vlan row is modified this keyword will click the Update button of the Devices/Configure VLAN
        Definition Table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_UPDATE,
                                    **kwargs)

    def devices_edit_device_vlan_definition_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The name of the vlan

        This will set the name of the Devices/Configure VLAN Definition Table row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_NAME,
                                    **kwargs)

    def devices_edit_device_vlan_definition_set_vid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VID of the vlan

        This will set the VID of the Devices/Configure VLAN Definition Table row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_VID,
                                    **kwargs)

    def devices_edit_device_vlan_definition_set_vrf(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The VRF of the vlan

        This will set the VRF of the Devices/Configure VLAN Definition Table row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_VRF,
                                    **kwargs)

    def devices_edit_device_vlan_definition_set_always_write_to_devices(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - This will set the Always Write to Devices checkbox of the vlan

        This will set the Always Write to Devices checkbox of the Devices/Configure VLAN Definition Table row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_ALWAYS_WRITE_TO_DEVICES,
                                    **kwargs)

    def devices_confirm_vlan_definition_name(self, element_name, vlan_name, exists='True', **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - This will confirm the name value of the vlan

        This will confirm the name value of the Devices/Configure VLAN Definition Table row.
        """
        args = {"vlan_name": vlan_name,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_VLAN_NAME, **kwargs)

    def devices_confirm_vlan_definition_vid(self, element_name, vlan_name, vid_id, exists='True', **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - This will confirm the VID value of the vlan

        This will confirm the VID value of the Devices/Configure VLAN Definition Table row.
        """
        args = {"vlan_name": vlan_name,
                "vid_id": vid_id,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_VLAN_VID, **kwargs)

    def devices_confirm_vlan_definition_write_to_device(self, element_name, vlan_name, write_to_device, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - This will confirm the Always Write To Devices value of the vlan

        This will confirm the Always Write To Devices value of the Devices/Configure VLAN Definition Table row selected.
        """
        args = {"vlan_name": vlan_name,
                "write_to_device": write_to_device}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_VLAN_WRITE_TO_DEVICE,
                                    **kwargs)

    def devices_confirm_device_port_alias(self, element_name, port_id, port_alias, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [port_alias]    - This will confirm the Port Alias value of the port row

        This will confirm the Port Alias value of the Devices/Configure Ports Table row selected.
        """
        args = {"port_id": port_id,
                "port_alias": port_alias}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_ALIAS, **kwargs)

    def devices_edit_device_ports_select_row(self, element_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_name]     - This will select the port row

        This will select the Devices/Configure Ports Table row.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_SELECT_ROW,
                                    **kwargs)

    def devices_edit_device_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name]      - This will select the tab within the Devices/Configure Devices Dialog

        This will select a tab Devices/Configure Device Dialog.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SELECT_TAB, **kwargs)

    def devices_edit_device_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will click the Save button within the Devices/Configure Device Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SAVE, **kwargs)

    def devices_edit_device_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will click the Cancel button within the Devices/Configure Device Dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_CANCEL, **kwargs)

    def devices_confirm_device_port_authentication(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of authentication

        This will confirm the authentication value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_AUTHENTICATION,
                                    **kwargs)

    def devices_confirm_device_port_pvid(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of PVID

        This will confirm the PVID value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_PVID, **kwargs)

    def devices_confirm_device_port_tagged(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of tagged column

        This will confirm the tagged value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_TAGGED, **kwargs)

    def devices_confirm_device_port_untagged(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of untagged column

        This will confirm the untagged value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_UNTAGGED,
                                    **kwargs)

    def devices_confirm_device_port_nickname(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port nickname column

        This will confirm the port nickname value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_NICKNAME,
                                    **kwargs)

    def devices_confirm_device_port_duplex(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port duplex column

        This will confirm the port duplex value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_DUPLEX, **kwargs)

    def devices_confirm_device_port_auto_negotiation(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port auto negotiation column

        This will confirm the port auto negotiation value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_AUTO_NEGOTIATION,
                                    **kwargs)

    def devices_confirm_device_port_speed(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port speed column

        This will confirm the port speed value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_SPEED, **kwargs)

    def devices_confirm_device_port_configuration(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port configuration column

        This will confirm the port configuration value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_CONFIGURATION,
                                    **kwargs)

    def devices_confirm_device_port_lag(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port lag column

        This will confirm the port lag value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_LAG, **kwargs)

    def devices_confirm_device_port_node_alias(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port node alias column

        This will confirm the port node alias value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_NODE_ALIAS,
                                    **kwargs)

    def devices_confirm_device_port_span_guard(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port span guard column

        This will confirm the port span guard value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_SPAN_GUARD,
                                    **kwargs)

    def devices_confirm_device_port_loop_protect(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of port loop protect column

        This will confirm the port loop protect value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_LOOP_PROTECT,
                                    **kwargs)

    def devices_confirm_device_port_mvrp(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The id of the row to confirm
        [the_value]     - The confirm value of MVRP column

        This will confirm the port MVRP value of the port row within the Devices/Configure Device Dialog.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_MVRP, **kwargs)

    def devices_confirm_device_ztp_configure_device(self, element_name, is_enabled, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - The expected value of the ZTP Configuration Checkbox

        This will confirm the Configure ZTP Checkbox within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_CONFIGURE_DEVICE,
                                    **kwargs)

    def devices_confirm_device_ztp_serial_number(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device Serial Number

        This will confirm the Serial Number within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_SERIAL_NUMBER,
                                    **kwargs)

    def devices_confirm_device_ztp_ip_address_subnet(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device IP address subnet

        This will confirm the IP address subnet within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_IP_ADDRESS_SUBNET,
                                    **kwargs)

    def devices_confirm_device_ztp_management_interface(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device management interface

        This will confirm the management interface within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_MANAGEMENT_INTERFACE, **kwargs)

    def devices_confirm_device_ztp_domain_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device domain name

        This will confirm the domain name within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_DOMAIN_NAME,
                                    **kwargs)

    def devices_confirm_device_ztp_dns_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device DNS Server

        This will confirm the DNS Server within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_DNS_SERVER,
                                    **kwargs)

    def devices_confirm_device_ztp_lacp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - whether the checkbox should be enabled
        [the_value]     - The expected value of the device LACP

        This will confirm the LACP within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"is_enabled": is_enabled,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_LACP, **kwargs)

    def devices_confirm_device_ztp_mstp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - Whether the checkbox should be enabled
        [the_value]     - The expected value of the device MSTP

        This will confirm the MSTP within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_MSTP, **kwargs)

    def devices_confirm_device_ztp_mvrp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - Whether the checkbox should be enabled
        [the_value]     - The expected value of the device MVRP

        This will confirm the MVRP within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_MVRP, **kwargs)

    def devices_confirm_device_ztp_poe(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - Whether the checkbox should be enabled
        [the_value]     - The expected value of the device POE

        This will confirm the POE within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_POE, **kwargs)

    def devices_confirm_device_ztp_xvlan(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - Whether the checkbox should be enabled
        [the_value]     - The expected value of the device XVLAN

        This will confirm the XVLAN within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_XVLAN, **kwargs)

    def devices_confirm_device_ztp_ntp_server(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device NTP

        This will confirm the NTP within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_NTP_SERVER,
                                    **kwargs)

    def devices_confirm_device_ztp_lldp(self, element_name, is_enabled, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_enabled]    - Whether the checkbox should be enabled
        [the_value]     - The expected value of the device LLDP

        This will confirm the LLDP within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_LLDP, **kwargs)

    def devices_confirm_device_ztp_gateway_address(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device gateway address

        This will confirm the gateway address within the Devices/Configure Device Dialog ZTP+ Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_ZTP_GATEWAY_ADDRESS,
                                    **kwargs)

    def devices_confirm_device_vendor_profile_device_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device type

        This will confirm the device type within the Devices/Configure Device Dialog Vendor Profile tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_DEVICE_TYPE, **kwargs)

    def devices_confirm_device_vendor_profile_vendor(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device vendor

        This will confirm the vendor within the Devices/Configure Device Dialog Vendor Profile tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_VENDOR,
                                    **kwargs)

    def devices_confirm_device_vendor_profile_company(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device company

        This will confirm the company within the Devices/Configure Device Dialog Vendor Profile tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_COMPANY, **kwargs)

    def devices_confirm_device_vendor_profile_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device family

        This will confirm the family within the Devices/Configure Device Dialog Vendor Profile tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_FAMILY,
                                    **kwargs)

    def devices_confirm_device_vendor_profile_sub_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The expected value of the device sub family

        This will confirm the sub family within the Devices/Configure Device Dialog Vendor Profile tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_SUB_FAMILY, **kwargs)

    def devices_edit_device_set_system_name(self, element_name, sys_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [sys_name]      - The sys name value set

        This will set the sys name within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"sys_name": sys_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_SYSTEM_NAME,
                                    **kwargs)

    def devices_edit_device_set_contact(self, element_name, contact, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [contact]       - The contact value set

        This will set the contact within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"contact": contact}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_CONTACT, **kwargs)

    def devices_edit_device_set_location(self, element_name, location, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [location]      - The location value set

        This will set the location within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"location": location}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_LOCATION, **kwargs)

    def devices_edit_device_set_admin_profile(self, element_name, profile, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile]       - The profile value set

        This will set the profile within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"profile": profile}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_ADMIN_PROFILE,
                                    **kwargs)

    def devices_edit_device_remove_from_service(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The remove from service value set

        This will set the remove from service within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_REMOVE_FROM_SERVICE,
                                    **kwargs)

    def devices_edit_device_set_default_site(self, element_name, site_name, import_site, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [site_name]     - The remove from service value set
        [import_site]   - Whether or not to import the site chosen

        This will set the site name within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"site_name": site_name,
                "import_site": import_site}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_DEFAULT_SITE,
                                    **kwargs)

    def devices_edit_device_set_poll_group(self, element_name, poll_group, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [poll_group]    - poll group value to set

        This will set the poll group within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"poll_group": poll_group}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_POLL_GROUP, **kwargs)

    def devices_edit_device_set_poll_type(self, element_name, poll_type, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [poll_type]     - poll type value to set

        This will set the poll type within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"poll_type": poll_type}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_POLL_TYPE, **kwargs)

    def devices_edit_device_set_snmp_timeout(self, element_name, snmp_timeout, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_timeout]  - snmp_timeout value to set

        This will set the snmp_timeout within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {'snmp_timeout': snmp_timeout}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_SNMP_TIMEOUT,
                                    **kwargs)

    def devices_edit_device_set_snmp_retries(self, element_name, snmp_retries, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [snmp_retries]  - snmp_retries value to set

        This will set the snmp_retries within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {'snmp_retries': snmp_retries}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_SNMP_RETRIES,
                                    **kwargs)

    def devices_edit_device_set_topology_layer(self, element_name, topology_layer, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [topology_layer] - topology_layer value to set

        This will set the topology_layer within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {'topology_layer': topology_layer}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_SET_TOPOLOGY_LAYER,
                                    **kwargs)

    def devices_edit_device_ports_select_port(self, element_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_name]     - port_name value to set

        This will set the port_name within the Devices/Configure Device Dialog Devices Tab.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_SELECT_PORT,
                                    **kwargs)

    def devices_edit_device_ports_edit_row(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will set the edit row within the Devices/Configure Device Dialog Ports tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW, **kwargs)

    def devices_edit_device_ports_row_editor_update(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will set the edit row update button within the Devices/Configure Device Dialog Ports tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_ROW_EDITOR_UPDATE,
                                    **kwargs)

    def devices_edit_device_ports_row_editor_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will set the cancel row button within the Devices/Configure Device Dialog Ports tab.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_ROW_EDITOR_CANCEL,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_alias(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the port alias

        This will set the value of the alias within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_ALIAS,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_enabled(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the enabled column

        This will set the value of the enabled column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_ENABLED,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_auto_negotiation(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the auto negotiation column

        This will set the value of the auto negotiation column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_AUTO_NEGOTIATION, **kwargs)

    def devices_edit_device_ports_edit_row_nickname(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the nickname column

        This will set the value of the nickname column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_NICKNAME,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_speed(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the speed column

        This will set the value of the speed column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_SPEED,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_duplex(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the duplex column

        This will set the value of the duplex column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_DUPLEX,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_configuration(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the configuration column

        This will set the value of the configuration column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CONFIGURATION, **kwargs)

    def devices_edit_device_ports_edit_row_pvid(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the PVID column

        This will set the value of the PVID column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_PVID,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_authentication(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the authentication column

        This will set the value of the authentication column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_AUTHENTICATION, **kwargs)

    def devices_edit_device_ports_edit_row_lag(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the lag column

        This will set the value of the lag column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_LAG,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_tagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the tagged column

        This will set the value of the tagged column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_TAGGED,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_untagged(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the untagged column

        This will set the value of the untagged column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_UNTAGGED,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_node_alias(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the node alias column

        This will set the value of the node alias column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_NODE_ALIAS, **kwargs)

    def devices_edit_device_ports_edit_row_span_guard(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the span guard column

        This will set the value of the span guard column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_SPAN_GUARD, **kwargs)

    def devices_edit_device_ports_edit_row_loop_protect(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the loop protect column

        This will set the value of the loop protect column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_LOOP_PROTECT, **kwargs)

    def devices_edit_device_ports_edit_row_mvrp(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the mvrp column

        This will set the value of the mvrp column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_MVRP,
                                    **kwargs)

    def devices_edit_device_vendor_profile_device_type(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the device type

        This will set the value of the device type within the Devices/Configure Device Dialog Vendor Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_DEVICE_TYPE, **kwargs)

    def devices_edit_device_vendor_profile_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the device family

        This will set the value of the device family within the Devices/Configure Device Dialog Vendor Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_FAMILY,
                                    **kwargs)

    def devices_edit_device_vendor_profile_sub_family(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the device sub family

        This will set the value of the device sub family within the Devices/Configure Device Dialog Ports Tab.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_SUB_FAMILY, **kwargs)

    def devices_confirm_device_port_enabled(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The port id of the column to confirm
        [the_value]     - The expected value of the device enabled column

        This will confirm the value of the enabled column within the Devices/Configure Device Dialog Ports Tab.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_ENABLED,
                                    **kwargs)

    def devices_confirm_device_port_device_nickname(self, element_name, port_id, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_id]       - The port id of the column to confirm
        [the_value]     - The expected value of the device nickname column

        This will confirm the value of the device nickname column within the Devices/Configure Device Dialog Ports Tab.
        """
        args = {"port_id": port_id,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_PORT_DEVICE_NICKNAME,
                                    **kwargs)

    def devices_edit_device_ports_show_columns(self, element_name, col_list, show_col, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [column_list]   - The list of columns to show or hide
        [show_col]      - Whether to show or hide the columns

        This will launch the menu pick to show or hide columns within the Devices/Configure Device Dialog Ports Tab.
        """
        args = {"col_list": col_list,
                "show_col": show_col}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_PORTS_SHOW_COLUMNS,
                                    **kwargs)

    def devices_confirm_device_ip_archived(self, element_name, device_ip, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip]     - IP of the device to check
        [the_value]     - The expected value (True/False)

        This will confirm whether the device ip is archived within the Devices table.
        """
        args = {"device_ip": device_ip,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_DEVICE_IP_ARCHIVED, **kwargs)

    def devices_edit_device_enforce_preview(self, element_name, enforce_system, enforce_vlan=False, enforce_vrf=False,
                                            enforce_port=False, enforce_clip_address=False,
                                            enforce_toplogies=False, enforce_services=False, enforce_lag=False,
                                            **kwargs):
        """
        Keyword Arguments:
        [element_names]      - List of elements the keyword will be run against
        [enforce_system]     - True or False to include in Enforce
        [enforce_vlan]       - True or False to include in Enforce
        [enforce_port_alias] - True or False to include in Enforce
        [enforce_port_vlan]  - True or False to include in Enforce

        This will Enforce changes made within the Devices/Configure Device Dialog.
        """
        args = {"enforce_system": enforce_system,
                "enforce_vlan": enforce_vlan,
                "enforce_vrf": enforce_vrf,
                "enforce_port": enforce_port,
                "enforce_clip_address": enforce_clip_address,
                "enforce_topologies": enforce_toplogies,
                "enforce_services": enforce_services,
                "enforce_lag": enforce_lag}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_ENFORCE_PREVIEW,
                                    **kwargs)

    def devices_open_device_view_flexview(self, element_name, flexview, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [flexview]      - Desired flexview statistics

        This will select and view the desired flexview statistics for the specified device.
        """
        args = {"flexview": flexview}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_OPEN_DEVICE_VIEW_FLEXVIEW, **kwargs)

    def devices_open_device_view_physical_entity_summary(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will select and view the Physical Entity Summary for the desired device.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_OPEN_DEVICE_VIEW_PHYSICAL_ENTITY_SUMMARY, **kwargs)

    def devices_open_device_view_interface_statistics(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will select and view the Interface statistics for the desired device.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_OPEN_DEVICE_VIEW_INTERFACE_STATISTICS, **kwargs)

    def devices_confirm_context_menu_exists(self, element_name, menu_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_name]     - Name of the menu to look for;  comma-separated list of strings if the menu is a sub menu
        [exists]        - Indicates if the menu should be present or not (True/False)

        This will confirm if the specified menu exists on the device context menu.  If the menu is a sub menu, the
        menu_name argument should be a comma-separated list of menus to traverse.  The keyword passes if the menu is
        found and the exists argument is True or if the menu does not exist and the exists argument is False;
        otherwise, the keyword fails.
        """
        args = {"menu_name": menu_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CONFIRM_CONTEXT_MENU_EXISTS,
                                    **kwargs)

    def devices_device_view_verify_vlan_name_and_tag(self, element_name, vlan_name, vlan_tag, device_type="eos",
                                                     max_attempts='0', exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address] - The ip address to match
        [action_status] - the action status to match
        [max_attempts] - the maximum attempts to check for items before failing the keyword

        Verifies the VLAN name and VLAN ID for the given element.
        """
        args = {'vlan_name': vlan_name,
                'vlan_tag': vlan_tag,
                'max_attempts': max_attempts,
                'exists': exists}

        if device_type.upper() in [self.ne_const.OS_VOSS,
                                   self.ne_const.OS_BOSS]:
            device_type_command_const = self.command_const.DEVICES_DEVICE_VIEW_VERIFY_VLAN_NAME_AND_TAG_VOSS
        else:
            device_type_command_const = self.command_const.DEVICES_DEVICE_VIEW_VERIFY_VLAN_NAME_AND_TAG

        return self.execute_keyword(element_name, args, device_type_command_const, **kwargs)

    def devices_device_view_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        """
        args = {'tab_name': tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DEVICE_VIEW_SELECT_TAB, **kwargs)

    def devices_device_view_ports_verify_pvid(self, element_name, port_name, pvid, max_attempts='0',
                                              exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        """
        args = {'port_name': port_name,
                'pvid': pvid,
                'max_attempts': max_attempts,
                'exists': exists}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_DEVICE_VIEW_PORTS_VERIFY_PVID, **kwargs)

    def devices_device_view_ports_verify_vlan_id_vlan_name_untag_tag(self, element_name, port_name, vlan_id, vlan_name,
                                                                     taggedoruntagged='untagged', max_attempts='0',
                                                                     exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        """
        args = {'port_name': port_name,
                'vlan_id': vlan_id,
                'vlan_name': vlan_name,
                'taggedoruntagged': taggedoruntagged,
                'max_attempts': max_attempts,
                'exists': exists}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_DEVICE_VIEW_PORTS_VERIFY_VLAN_ID_VLAN_NAME_UNTAG_TAG,
                                    **kwargs)

    def devices_device_view_ports_expand_tree(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        """
        args = {'tab_name': tab_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DEVICE_VIEW_PORTS_EXPAND_TREE,
                                    **kwargs)

    def devices_edit_device_ports_edit_row_clear_tagged(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will set the value of the tagged column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CLEAR_TAGGED, **kwargs)

    def devices_edit_device_ports_edit_row_clear_untagged(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will set the value of the tagged column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {}
        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CLEAR_UNTAGGED, **kwargs)

    def devices_edit_device_reload_device(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Refreshed Device selected in Edit Device window.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_EDIT_DEVICE_RELOAD_DEVICE, **kwargs)

    def devices_refresh_port_status(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        This will confirm a devices status after adding the device it will perform a Refresh and Rediscover.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_REFRESH_PORT_STATUS, **kwargs)

    def devices_device_view_enable_port(self, element_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_name}     - The port to enable in the device view.

        This will enable the specified port within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DEVICE_VIEW_ENABLE_PORT, **kwargs)

    def devices_device_view_disable_port(self, element_name, port_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [port_name}     - The port to disable in the device view.

        This will disable the specified port within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DEVICE_VIEW_DISABLE_PORT, **kwargs)

    def devices_maps_add_to_map(self, element_name, map_path, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_path}     - path to map to add to


        """
        args = {"map_path": map_path}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_MAPS_ADD_TO_MAP, **kwargs)

    def devices_device_view_vlan_vlan_table_verify_tag_and_ports(self, element_name, vlan_tag, port_list='\x00',
                                                                 device_type="voss", max_attempts='0',
                                                                 exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address] - The ip address to match
        [action_status] - the action status to match
        [max_attempts] - the maximum attempts to check for items before failing the keyword

        Verifies the VLAN name and VLAN ID for the given element.
        """
        args = {'vlan_tag': vlan_tag,
                'port_list': port_list,
                'device_type': device_type,
                'max_attempts': max_attempts,
                'exists': exists}
        if device_type.upper() in [self.ne_const.OS_VOSS,
                                   self.ne_const.OS_BOSS]:
            device_type_command_const = self.command_const.DEVICES_DEVICE_VIEW_VLAN_VLAN_TABLE_VERIFY_TAG_AND_PORTS_VOSS
        else:
            device_type_command_const = self.command_const.DEVICES_DEVICE_VIEW_VLAN_VLAN_TABLE_VERIFY_TAG_AND_PORTS

        return self.execute_keyword(element_name, args, device_type_command_const, **kwargs)

    def devices_device_view_vlan_vlan_port_table_verify_port_and_pvid(self, element_name, port_value, port_pvid,
                                                                      device_type, exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address] - The ip address to match
        [action_status] - the action status to match
        [max_attempts] - the maximum attempts to check for items before failing the keyword

        Verifies the VLAN name and VLAN ID for the given element.
        """
        args = {'port_value': port_value,
                'port_pvid': port_pvid,
                'device_type': device_type,
                'exists': exists}
        if device_type.upper() in [self.ne_const.OS_VOSS,
                                   self.ne_const.OS_BOSS]:
            device_type_command_const = \
                self.command_const.DEVICES_DEVICE_VIEW_VLAN_VLAN_PORT_TABLE_VERIFY_PORT_AND_PVID_VOSS

        else:
            device_type_command_const = self.command_const.DEVICES_DEVICE_VIEW_VLAN_VLAN_PORT_TABLE_VERIFY_PORT_AND_PVID
        return self.execute_keyword(element_name, args, device_type_command_const, **kwargs)

    def devices_edit_device_ports_edit_row_port_template(self, element_name, port_template, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - The value of the enabled column

        This will set the value of the enabled column within the Devices/Configure Device Dialog Ports tab row.
        """
        args = {"port_template": port_template}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_PORT_TEMPLATE, **kwargs)
