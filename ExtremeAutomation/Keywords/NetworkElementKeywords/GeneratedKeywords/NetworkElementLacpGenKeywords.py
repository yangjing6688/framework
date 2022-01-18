"""
Keyword class for all lacp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.LacpConstants import \
    LacpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.LacpConstants import \
    LacpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementLacpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementLacpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "lacp"

    def lacp_enable_global(self, device_name, **kwargs):
        """
        Description: Enables LACP at the Global level.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def lacp_disable_global(self, device_name, **kwargs):
        """
        Description: Disables LACP at the Global level.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def lacp_create_lag(self, device_name, main_lag_port='', port='', key='', **kwargs):
        """
        Description: Specifies the LACP 'Group', otherwise known as the 'Master' or main_lag_port and adds the
                     physicallag_port to the Group.

        Supported Agents and OS:
            CLI: VOSS, SLX, EOS, EXOS
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LAG,
                                    **kwargs)

    def lacp_delete_lag(self, device_name, main_lag_port='', key='', port='', **kwargs):
        """
        Description: Removes the LACP Group and associated port(s).

        Supported Agents and OS:
            CLI: VOSS, SLX, EOS, EXOS
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_LAG,
                                    **kwargs)

    def lacp_set_lag_port(self, device_name, main_lag_port='', port='', key='', **kwargs):
        """
        Description: Add a 'physical' port to the lag group.

        Supported Agents and OS:
            CLI: VOSS, SLX, EOS, EXOS
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LAG_PORT,
                                    **kwargs)

    def lacp_clear_lag_port(self, device_name, key='', main_lag_port='', port='', **kwargs):
        """
        Description: Remove a 'physical' port from the lag group.

        Supported Agents and OS:
            CLI: VOSS, SLX, EOS, EXOS
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LAG_PORT,
                                    **kwargs)

    def lacp_set_mlt_actor_key(self, device_name, actor_admin_key='', mlt_id='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {
            "actor_admin_key": actor_admin_key,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ACTOR_KEY,
                                    **kwargs)

    def lacp_set_mlt_actor_system_priority(self, device_name, actor_system_priority='', mlt_id='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {
            "actor_system_priority": actor_system_priority,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ACTOR_SYSTEM_PRIORITY,
                                    **kwargs)

    def lacp_disable_port(self, device_name, key='', main_lag_port='', **kwargs):
        """
        Description: Disables LACP on the specified port.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def lacp_enable_port(self, device_name, key='', main_lag_port='', **kwargs):
        """
        Description: Enables LACP on the specified port.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "key": key,
            "main_lag_port": main_lag_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def lacp_set_port_priority(self, device_name, main_lag_port='', priority='', **kwargs):
        """
        Description: Sets the LACP priority on a port.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "main_lag_port": main_lag_port,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_PRIORITY,
                                    **kwargs)

    def lacp_set_system_priority(self, device_name, priority='', **kwargs):
        """
        Description: Sets the LACP system priority.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SYSTEM_PRIORITY,
                                    **kwargs)

    def lacp_clear_counters(self, device_name, port_channel='', **kwargs):
        """
        Description: Clears the LACP counters on a specified port channel.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "port_channel": port_channel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_COUNTERS,
                                    **kwargs)

    def lacp_clear_all_counters(self, device_name, **kwargs):
        """
        Description: Clears the LACP counters on all ports.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_COUNTERS,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def lacp_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that LACP is enabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_LACP_ENABLED, True,
                                           "LACP is enabled on {device_name}.",
                                           "LACP is NOT enabled on {device_name}!",
                                           **kwargs)

    def lacp_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that LACP is disabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_LACP_ENABLED, False,
                                           "LACP is disabled on {device_name}.",
                                           "LACP is NOT disabled on {device_name}!",
                                           **kwargs)

    def lacp_verify_group_exists(self, device_name, main_lag_port='', lag_port='', key='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [main_lag_port] - The value of the main "logical" port or "Master" port.
                          Also serves as the group ID for the lag.
        [lag_port]      - The "physical" port of the lag group.
        [key]*          - This is used to indicate which port is eligible to be included in the lag.
                          *(Used for VOSS).

        Verifies that the LACP "Group" exists on the device.
        """
        args = {"main_lag_port": main_lag_port,
                "lag_port": lag_port,
                "key": key}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LAG_INFO,
                                           self.parse_const.CHECK_PORT_IS_IN_LAG, True,
                                           "The LACP Group exists on {device_name}.",
                                           "The LACP Group does NOT exist on {device_name}!",
                                           **kwargs)

    def lacp_verify_group_does_not_exist(self, device_name, main_lag_port='', lag_port='', key='', **kwargs):
        """
        [Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [main_lag_port] - The value of the main "logical" port or "Master" port.
                          Also serves as the group ID for the lag.
        [lag_port]      - The "physical" port of the lag group.
        [key]*          - This is used to indicate which port is eligible to be included in the lag.
                          *(Used for VOSS).

        Verifies that the LACP "Group" does not exist on the device.
        """
        args = {"main_lag_port": main_lag_port,
                "lag_port": lag_port,
                "key": key}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LAG_INFO,
                                           self.parse_const.CHECK_PORT_IS_IN_LAG, False,
                                           "The LACP Group does not exist on {device_name}.",
                                           "The LACP Group still EXISTS on {device_name}!",
                                           **kwargs)

    def lacp_verify_port_in_lag_group(self, device_name, main_lag_port='', lag_ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [main_lag_port] - The value of the main "logical" port or "Master" port.
                          Also serves as the group ID for the lag.
        [lag_port]      - The "physical" port to check if it is a member of the lag group.

        Verifies that the "physical" port is a member of the lag group
        """
        args = {"main_lag_port": main_lag_port,
                "lag_port": lag_ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_ALL,
                                           self.parse_const.CHECK_PORT_IS_IN_LAG, True,
                                           "Port {lag_port} is a member of the LAG on port {port}.",
                                           "Port {lag_port} is NOT a member of the LAG on port {port}!",
                                           **kwargs)

    def lacp_verify_port_not_in_lag_group(self, device_name, main_lag_port='', lag_ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [main_lag_port] - The value of the main "logical" port or "Master" port.
                          Also serves as the group ID for the lag.
        [lag_port]      - The "physical" port to check that it is NOT a member of the lag group.

        Verifies that the "physical" port is not a member of the specified lag group
        """
        args = {"main_lag_port": main_lag_port,
                "lag_port": lag_ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_ALL,
                                           self.parse_const.CHECK_PORT_IS_IN_LAG, False,
                                           "Port {lag_port} was properly removed from {port} on {device_name}.",
                                           "Port {lag_port} was NOT properly removed from {port} on "
                                           "{device_name}!",
                                           **kwargs)
