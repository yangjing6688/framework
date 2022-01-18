"""
Keyword class for all port cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.PortConstants import \
    PortConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.PortConstants import \
    PortConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import \
    NetworkElementSnmpUtils as SnmpUtils


class NetworkElementPortGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementPortGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "port"

    def port_enable_state(self, device_name, port='', **kwargs):
        """
        Description: Enables the admin-state on the port.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: EOS, EXOS, VOSS
            REST: SNAPROUTE
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_STATE,
                                    **kwargs)

    def port_disable_state(self, device_name, port='', **kwargs):
        """
        Description: Disables the admin-state on the port.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: EOS, EXOS, VOSS
            REST: SNAPROUTE
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_STATE,
                                    **kwargs)

    def port_enable_jumbo(self, device_name, port='', **kwargs):
        """
        Description: Enables jumbo frame reception on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_JUMBO,
                                    **kwargs)

    def port_disable_jumbo(self, device_name, port='', **kwargs):
        """
        Description: Disables jumbo frame reception on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_JUMBO,
                                    **kwargs)

    def port_set_speed(self, device_name, port='', speed='', duplex='', state='', **kwargs):
        """
        Description: Sets the speed and duplex settings on the given port.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "duplex": duplex,
            "port": port,
            "speed": speed,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SPEED,
                                    **kwargs)

    def port_clear_speed(self, device_name, port='', **kwargs):
        """
        Description: Sets the speed and duplex settings to default values on the given port.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SPEED,
                                    **kwargs)

    def port_set_alias(self, device_name, port='', name='', **kwargs):
        """
        Description: The user-defined name for the Network Element port.

        Supported Agents and OS:
            SNMP: EOS, EXOS, VOSS
            CLI: VOSS, SLX
        """
        args = {
            "name": name,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ALIAS,
                                    **kwargs)

    def port_set_rate_egress_mbps(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a rate-limit in Mbps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_EGRESS_MBPS,
                                    **kwargs)

    def port_set_rate_egress_gbps(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a rate-limit in Gbps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_EGRESS_GBPS,
                                    **kwargs)

    def port_set_rate_egress_kbps(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a rate-limit in Kbps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_EGRESS_KBPS,
                                    **kwargs)

    def port_set_rate_egress_no_limit(self, device_name, port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_EGRESS_NO_LIMIT,
                                    **kwargs)

    def port_set_rate_flood_bcast(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a flood broadcast rate-limit in pps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_FLOOD_BCAST,
                                    **kwargs)

    def port_set_rate_flood_mcast(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a flood multicast rate-limit in pps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_FLOOD_MCAST,
                                    **kwargs)

    def port_set_rate_flood_unknown(self, device_name, port='', rate='', **kwargs):
        """
        Description: Configures a flood unknown-destmac rate-limit in pps on the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "rate": rate
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RATE_FLOOD_UNKNOWN,
                                    **kwargs)

    def port_set_restart(self, device_name, port='', **kwargs):
        """
        Description: Restarts the given port(s) on a network element.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RESTART,
                                    **kwargs)

    def port_enable_flex_uni(self, device_name, port='', **kwargs):
        """
        Description: Enables the given port(s) for flex-uni (VOSS Only).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_FLEX_UNI,
                                    **kwargs)

    def port_disable_flex_uni(self, device_name, port='', **kwargs):
        """
        Description: Disables the given port(s) for flex-uni (VOSS Only).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_FLEX_UNI,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def port_verify_jumbo_frame_reception_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) that jumbo frame reception should be enabled on.

        Verifies that jumbo frame reception is enabled on a given port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_JUMBO,
                                           self.parse_const.VALIDATE_JUMBO_FRAME_RECEPTION, True,
                                           "Jumbo Frame Reception is correctly enabled on {port}.",
                                           "Jumbo Frame Reception is INCORRECTLY DISABLED on {port}!",
                                           **kwargs)

    def port_verify_jumbo_frame_reception_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) that jumbo frame reception should be enabled on.

        Verifies that jumbo frame reception is enabled on a given port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_JUMBO,
                                           self.parse_const.VALIDATE_JUMBO_FRAME_RECEPTION, False,
                                           "Jumbo Frame Reception is correctly disabled on {port}.",
                                           "Jumbo Frame Reception is INCORRECTLY ENABLED on {port}!",
                                           **kwargs)

    def port_verify_admin_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the admin state is being verified.

        Verifies that the port admin state is set to enabled.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_STATUS,
                                           self.parse_const.VERIFY_PORT_ENABLED, True,
                                           "Port {port}'s admin state is enabled.",
                                           "Port {port}'s admin state is disabled!",
                                           **kwargs)

    def port_verify_admin_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the priority is being verified.

        Verifies that the port admin state is disabled.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_STATUS,
                                           self.parse_const.VERIFY_PORT_ENABLED, False,
                                           "Port {port}'s admin state is disabled.",
                                           "Port {port}'s admin state is enabled!",
                                           **kwargs)

    def port_verify_operational(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the operational state is being verified.

        Verifies that the port operational state is up.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OPER_STATUS,
                                           self.parse_const.VERIFY_PORT_OPERATIONAL, True,
                                           "Port {port}'s operational state is up.",
                                           "Port {port}'s operational state is down!",
                                           **kwargs)

    def port_verify_not_operational(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the operational state is being verified.

        Verifies that the port operational state is down.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OPER_STATUS,
                                           self.parse_const.VERIFY_PORT_OPERATIONAL, False,
                                           "Port {port}'s operational state is down.",
                                           "Port {port}'s operational state is up!",
                                           **kwargs)

    def port_verify_flex_uni_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which flex-uni is being verified.

        Verifies that the port flex-uni state is set to enabled.
        This keyword applies to VOSS.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FLEX_UNI_STATUS,
                                           self.parse_const.CHECK_PORT_FLEX_UNI_STATUS, True,
                                           "Port {port}'s flex-uni state is enabled.",
                                           "Port {port}'s flex-uni state is disabled!",
                                           **kwargs)

    def port_verify_flex_uni_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which flex-uni is being verified.

        Verifies that the port flex-uni state is set to disabled.
        This keyword applies to VOSS.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FLEX_UNI_STATUS,
                                           self.parse_const.CHECK_PORT_FLEX_UNI_STATUS, False,
                                           "Port {port}'s flex-uni state is disabled.",
                                           "Port {port}'s flex-uni state is enabled!",
                                           **kwargs)

    def port_verify_alias(self, device_name, port='', alias='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the alias is being verified.
        [alias]       - The alias the port should be configured with.

        Verifies that the port alias is the value provided.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "alias": alias}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALIAS,
                                           self.parse_const.VERIFY_PORT_ALIAS, True,
                                           "Port {port}'s alias is properly set to {alias}.",
                                           "Port {port}'s alias is NOT properly set to {alias}!",
                                           **kwargs)

    def port_verify_not_alias(self, device_name, port='', alias='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the alias is being verified.
        [alias]       - The alias the port should NOT be configured with.

        Verifies that the port alias is NOT the value provided.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "alias": alias}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALIAS,
                                           self.parse_const.VERIFY_PORT_ALIAS, False,
                                           "Port {port}'s alias is correctly NOT set to {alias}.",
                                           "Port {port}'s alias is incorrectly set to {alias}!",
                                           **kwargs)

    def port_verify_mtu(self, device_name, port='', mtu='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the mtu is being verified.
        [mtu]         - The expected mtu.

        Verifies that the port mtu setting is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "mtu": mtu}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MTU,
                                           self.parse_const.VERIFY_PORT_MTU, True,
                                           "Port {port}'s mtu of {mtu} is correct.",
                                           "Port {port}'s mtu of {mtu} is NOT correct!",
                                           **kwargs)

    def port_verify_mac_address(self, device_name, port='', mac='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the mtu is being verified.
        [mac]         - The expected mac address.

        Verifies that the port mac address is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "mac": mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAC_ADDRESS,
                                           self.parse_const.VERIFY_PORT_MAC_ADDRESS, True,
                                           "Port {port}'s mac address of {mac} is correct.",
                                           "Port {port}'s mac address of {mac} is NOT correct!",
                                           **kwargs)

    def port_verify_high_speed(self, device_name, port='', speed='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the mtu is being verified.
        [speed]       - The expected port bandwidth in megabits per second.

        Verifies that the port high speed setting is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "speed": speed}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HIGH_SPEED,
                                           self.parse_const.VERIFY_PORT_HIGH_SPEED, True,
                                           "Port {port}'s high speed of {speed} is correct.",
                                           "Port {port}'s high speed of {speed} is NOT correct!",
                                           **kwargs)

    def port_verify_in_octets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the port in octet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_OCTETS,
                                           self.parse_const.CHECK_PORT_IN_OCTETS, True,
                                           "Port {port}'s in octets {count_operator} {count}.",
                                           "Port {port}'s in octets in NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_in_unicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound unicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_UNICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_UNICAST_PACKETS, True,
                                           "Port {port}'s in unicast packets {count_operator} {count}.",
                                           "Port {port}'s in unicast packets is NOT {count_operator} !",
                                           **kwargs)

    def port_verify_in_discard_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound discard packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_DISCARD_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_DISCARD_PACKETS, True,
                                           "Port {port}'s in discard packets {count_operator} {count}.",
                                           "Port {port}'s in discard packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_in_error_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound error packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_ERROR_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_ERROR_PACKETS, True,
                                           "Port {port}'s in error packets {count_operator} {count}.",
                                           "Port {port}'s in error packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_in_unknown_protocol_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound unknown protocol packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_IN_UNKNOWN_PROTOCOL_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_UNKNOWN_PROTOCOL_PACKETS, True,
                                           "Port {port}'s in unknown protocol packets {count_operator} {count}.",
                                           "Port {port}'s in unknown protocol packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_out_octets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound octet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_OCTETS,
                                           self.parse_const.CHECK_PORT_OUT_OCTETS, True,
                                           "Port {port}'s out octets {count_operator} {count}.",
                                           "Port {port}'s out octets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_out_unicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound unicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_UNICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_OUT_UNICAST_PACKETS, True,
                                           "Port {port}'s out unicast packets {count_operator} {count}.",
                                           "Port {port}'s out unicast packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_out_discard_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound discard packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_DISCARD_PACKETS,
                                           self.parse_const.CHECK_PORT_OUT_DISCARD_PACKETS, True,
                                           "Port {port}'s out discard packets {count_operator} {count}.",
                                           "Port {port}'s out discard packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_out_error_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound error packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_ERROR_PACKETS,
                                           self.parse_const.CHECK_PORT_OUT_ERROR_PACKETS, True,
                                           "Port {port}'s out error packets {count_operator} {count}.",
                                           "Port {port}'s out error packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_in_multicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound multicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_MULTICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_MULTICAST_PACKETS, True,
                                           "Port {port}'s in multicast packets {count_operator} {count}.",
                                           "Port {port}'s in multicast packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_in_broadcast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the inbound broadcast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IN_BROADCAST_PACKETS,
                                           self.parse_const.CHECK_PORT_IN_BROADCAST_PACKETS, True,
                                           "Port {port}'s in broadcast packets {count_operator} {count}.",
                                           "Port {port}'s in broadcast packets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_out_multicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound multicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_MULTICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_OUT_MULTICAST_PACKETS, True,
                                           "Port {port}'s out multicast packets {count_operator} {count}.",
                                           "Port {port}'s out multicast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_out_broadcast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the outbound broadcast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_OUT_BROADCAST_PACKETS,
                                           self.parse_const.CHECK_PORT_OUT_BROADCAST_PACKETS, True,
                                           "Port {port}'s out broadcast packets {count_operator} {count}.",
                                           "Port {port}'s out broadcast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_in_octets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit inbound octet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_64_BIT_IN_OCTETS,
                                           self.parse_const.CHECK_PORT_64_BIT_IN_OCTETS, True,
                                           "Port {port}'s 64 bit in octets {count_operator} {count} is correct.",
                                           "Port {port}'s 64 bit in octets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_64_bit_in_unicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit inbound unicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_64_BIT_IN_UNICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_IN_UNICAST_PACKETS, True,
                                           "Port {port}'s 64 bit in unicast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit in unicast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_in_multicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit inbound multicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_64_BIT_IN_MULTICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_IN_MULTICAST_PACKETS, True,
                                           "Port {port}'s 64 bit in multicast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit in multicast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_in_broadcast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit inbound broadcast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_64_BIT_IN_BROADCAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_IN_BROADCAST_PACKETS, True,
                                           "Port {port}'s 64 bit in broadcast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit in broadcast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_out_octets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit outbound octet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_64_BIT_OUT_OCTETS,
                                           self.parse_const.CHECK_PORT_64_BIT_OUT_OCTETS, True,
                                           "Port {port}'s 64 bit out octets {count_operator} {count}.",
                                           "Port {port}'s 64 bit out octets is NOT {count_operator} {count} !",
                                           **kwargs)

    def port_verify_64_bit_out_unicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit outbound unicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_64_BIT_OUT_UNICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_OUT_UNICAST_PACKETS, True,
                                           "Port {port}'s 64 bit out unicast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit out unicast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_out_multicast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit outbound multicast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_64_BIT_OUT_MULTICAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_OUT_MULTICAST_PACKETS, True,
                                           "Port {port}'s 64 bit out multicast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit out multicast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_64_bit_out_broadcast_packets(self, device_name, port='', count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which the mtu is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies that the 64 bit outbound broadcast packet count value is correct.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_64_BIT_OUT_BROADCAST_PACKETS,
                                           self.parse_const.CHECK_PORT_64_BIT_OUT_BROADCAST_PACKETS, True,
                                           "Port {port}'s 64 bit out broadcast packets {count_operator} {count}.",
                                           "Port {port}'s 64 bit out broadcast packets is NOT {count_operator} "
                                           "{count} !",
                                           **kwargs)

    def port_verify_rate_egress(self, device_name, port='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the egress rate-limit is being verified.
        [rate]        - The rate-limit that should be set on the port, in Kbps.

        Verifies that the port has the correct rate-limit in Kbps.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_EGRESS, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_broadcast(self, device_name, port='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the broadcast rate-limit is being verified.
        [rate]        - The rate-limit that should be set on the port, in pps.

        Verifies that the port has the correct rate-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_BROADCAST, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_broadcast_none(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the broadcast rate-limit is being verified.

        Verifies that the port has the rate-limit set to no-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": "No-limit"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_BROADCAST, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_multicast(self, device_name, port='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the multicast rate-limit is being verified.
        [rate]        - The rate-limit that should be set on the port, in pps.

        Verifies that the port has the correct rate-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_MULTICAST, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_multicast_none(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the multicast rate-limit is being verified.

        Verifies that the port has the rate-limit set to no-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": "No-limit"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_MULTICAST, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_unknown_destmac(self, device_name, port='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the unknown_destmac rate-limit is being verified.
        [rate]        - The rate-limit that should be set on the port, in pps.

        Verifies that the port has the correct rate-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_UNKNOWN_DESTMAC, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_rate_unknown_destmac_none(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) in which the unknown_destmac rate-limit is being verified.

        Verifies that the port has the rate-limit set to no-limit.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "rate": "No-limit"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RATE_LIMIT,
                                           self.parse_const.VERIFY_PORT_RATE_UNKNOWN_DESTMAC, True,
                                           "Port {port}'s has a rate-limit of {rate}.",
                                           "Port {port}'s does NOT have a rate-limit of {rate}!",
                                           **kwargs)

    def port_verify_advertised_speed_and_duplex(self, device_name, port='', speed='', duplex='', flags='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify the speed, duplex, and flags on.
        [speed]       - The speed of the port: 10BaseT,100BaseT,100X,1000BaseT,1000X.
        [duplex]      - The duplex of the port: Half,Full.
        [flags]       - The flags to verify for the given speed and duplex. C,L,R , or any combo of the three flags.

        Verifies that the port has the correct flags for the given speed and duplex.
        This keyword applies to EXOS.
        """
        args = {"port": port,
                "speed": speed,
                "duplex": duplex,
                "flags": flags}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADVERTISED,
                                           self.parse_const.VERIFY_PORT_ADVERTISED_SPEED_DUPLEX, True,
                                           "Port {port} has the correct flags set for {speed} {duplex}.",
                                           "Port {port} does NOT have the correct flags set for {speed} {duplex}!",
                                           **kwargs)

    def port_verify_attributes(self, device_name, port='', admin_state='', oper_state='', jumbo_state='',
                               alias_state='', flex_uni_state='', mtu='', mac_addr='', high_speed='',
                               alias='', in_octets='', in_ucast='', in_discard='', in_error='',
                               out_octets='', out_ucast='', out_discard='', out_error='', in_mcast='',
                               in_bcast='', out_mcast='', out_bcast='', in_64_octets='', in_64_ucast='',
                               in_64_mcast='', in_64_bcast='', out_64_octets='', out_64_ucast='',
                               out_64_mcast='', out_64_bcast='',
                               # Port Counter Operators
                               in_octets_oper="=", in_ucast_oper="=", in_discard_oper="=", in_error_oper="=",
                               out_octets_oper="=", out_ucast_oper="=", out_discard_oper="=", out_error_oper="=",
                               in_mcast_oper="=", in_bcast_oper="=", out_mcast_oper="=", out_bcast_oper="=",
                               in_64_octets_oper="=", in_64_ucast_oper="=", in_64_mcast_oper="=", in_64_bcast_oper="=",
                               out_64_octets_oper="=", out_64_ucast_oper="=", out_64_mcast_oper="=",
                               out_64_bcast_oper="=", use_cached=True, **kwargs):
        """
        Bulk verify of all (or None) possible keywords.

        [admin_state]   - Verify the admin_state is enabled or disabled (True | False).
        [oper_state]    - Verify the operational_state is enabled or disabled (True | False).
        [jumbo_state]   - Verify jumbo frame reception is enabled or disabled (True | False)
        [alias_state]   - Verify the alias is or it not the supplied value {alias} (True | False).
        [mtu]           - Verify the mtu, this argument is the mtu value.
        [high_speed]    - Verify the high_speed, this argument is the high_speed value.
        [in_octets]     - Verify the in_octets counter, this argument is the count.
        [in_ucast]      - Verify the in_unicast counter, this argument is the count.
        [in_discard]    - Verify the in_discard counter, this argument is the count.
        [in_error]      - Verify the in_error counter, this argument is the count.
        [out_octets]    - Verify the out_octets counter, this argument is the count.
        [out_ucast]     - Verify the out_unicast counter, this argument is the count.
        [out_discard]   - Verify the out_discard counter, this argument is the count.
        [out_error]     - Verify the out_error counter, this argument is the count.
        [in_mcast]      - Verify the in_multicast counter, this argument is the count.
        [in_bcast]      - Verify the in_broadcast counter, this argument is the count.
        [out_mcast]     - Verify the out_multicast counter, this argument is the count.
        [out_bcast]     - Verify the out_broadcast counter, this argument is the count.
        [in_64_octets]  - Verify the in_64-bit_octets counter, this argument is the count.
        [in_64_ucast]   - Verify the in_64-bit_unicast counter, this argument is the count.
        [in_64_mcast]   - Verify the in_64-bit_multicast counter, this argument is the count.
        [in_64_bcast]   - Verify the in_64-bit_broadcast counter, this argument is the count.
        [out_64_octets] - Verify the out_64-bit_octets counter, this argument is the count.
        [out_64_ucast]  - Verify the out_64-bit_unicast counter, this argument is the count.
        [out_64_mcast]  - Verify the out_64-bit_multicast counter, this argument is the count.
        [out_64_bcast]  - Verify the out_64-bit_broadcast counter, this argument is the count.

        Note: Counter verification uses the associated '<counter>_oper' operator for comparisons.
        """
        return_dict = {}
        if admin_state is not None:
            if admin_state:
                return_dict["admin_state"] = self.port_verify_admin_enabled(device_name, port, use_cached=use_cached,
                                                                            log_keyword=False, **kwargs)
            else:
                return_dict["admin_state"] = self.port_verify_admin_disabled(device_name, port, use_cached=use_cached,
                                                                             log_keyword=False, **kwargs)
        if oper_state is not None:
            if oper_state:
                return_dict["oper_state"] = self.port_verify_operational(device_name, port, use_cached=use_cached,
                                                                         log_keyword=False, **kwargs)
            else:
                return_dict["oper_state"] = self.port_verify_not_operational(device_name, port, use_cached=use_cached,
                                                                             log_keyword=False, **kwargs)
        if jumbo_state is not None:
            if jumbo_state:
                return_dict["jumbo_state"] = \
                    self.port_verify_jumbo_frame_reception_enabled_on_port(device_name, port, use_cached=use_cached,
                                                                           log_keyword=False, **kwargs)
            else:
                return_dict["jumbo_state"] = \
                    self.port_verify_jumbo_frame_reception_disabled_on_port(device_name, port, use_cached=use_cached,
                                                                            log_keyword=False, **kwargs)
        if alias_state is not None:
            if alias_state:
                return_dict["alias"] = self.port_verify_alias(device_name, port, alias, use_cached=use_cached,
                                                              log_keyword=False, **kwargs)
            else:
                return_dict["alias"] = self.port_verify_not_alias(device_name, port, alias, use_cached=use_cached,
                                                                  **kwargs)
        if flex_uni_state is not None:
            if flex_uni_state:
                return_dict["flex_uni_state"] = self.port_verify_flex_uni_enabled(device_name, port,
                                                                                  use_cached=use_cached,
                                                                                  log_keyword=False, **kwargs)
            else:
                return_dict["flex_uni_state"] = self.port_verify_flex_uni_disabled(device_name, port,
                                                                                   use_cached=use_cached,
                                                                                   log_keyword=False, **kwargs)
        if mtu is not None:
            return_dict["mtu"] = self.port_verify_mtu(device_name, port, mtu, use_cached=use_cached, log_keyword=False,
                                                      **kwargs)
        if mac_addr is not None:
            return_dict["mac_addr"] = self.port_verify_mac_address(device_name, port, mac_addr, use_cached=use_cached,
                                                                   log_keyword=False, **kwargs)
        if high_speed is not None:
            return_dict["high_speed"] = self.port_verify_high_speed(device_name, port, high_speed,
                                                                    use_cached=use_cached, log_keyword=False, **kwargs)
        if in_octets is not None:
            return_dict["in_octets"] = self.port_verify_in_octets(device_name, port, in_octets, in_octets_oper,
                                                                  use_cached=use_cached, log_keyword=False, **kwargs)
        if in_ucast is not None:
            return_dict["in_ucast"] = self.port_verify_in_unicast_packets(device_name, port, in_ucast, in_ucast_oper,
                                                                          use_cached=use_cached, log_keyword=False,
                                                                          **kwargs)
        if in_discard is not None:
            return_dict["in_discard"] = self.port_verify_in_discard_packets(device_name, port, in_discard,
                                                                            in_discard_oper, use_cached=use_cached,
                                                                            log_keyword=False, **kwargs)
        if in_error is not None:
            return_dict["in_error"] = self.port_verify_in_error_packets(device_name, port, in_error, in_error_oper,
                                                                        use_cached=use_cached, log_keyword=False,
                                                                        **kwargs)
        if out_octets is not None:
            return_dict["out_octets"] = self.port_verify_out_octets(device_name, port, out_octets, out_octets_oper,
                                                                    use_cached=use_cached, log_keyword=False, **kwargs)
        if out_ucast is not None:
            return_dict["out_ucast"] = self.port_verify_out_unicast_packets(device_name, port, out_ucast,
                                                                            out_ucast_oper, use_cached=use_cached,
                                                                            log_keyword=False, **kwargs)
        if out_discard is not None:
            return_dict["out_discard"] = self.port_verify_out_discard_packets(device_name, port, out_discard,
                                                                              out_discard_oper, use_cached=use_cached,
                                                                              log_keyword=False, **kwargs)
        if out_error is not None:
            return_dict["out_error"] = self.port_verify_out_error_packets(device_name, port, out_error, out_error_oper,
                                                                          use_cached=use_cached, log_keyword=False,
                                                                          **kwargs)
        if in_mcast is not None:
            return_dict["in_mcast"] = self.port_verify_in_multicast_packets(device_name, port, in_mcast, in_mcast_oper,
                                                                            use_cached=use_cached, log_keyword=False,
                                                                            **kwargs)
        if in_bcast is not None:
            return_dict["in_bcast"] = self.port_verify_in_broadcast_packets(device_name, port, in_bcast, in_bcast_oper,
                                                                            use_cached=use_cached, log_keyword=False,
                                                                            **kwargs)
        if out_mcast is not None:
            return_dict["out_mcast"] = self.port_verify_out_multicast_packets(device_name, port, out_mcast,
                                                                              out_mcast_oper, use_cached=use_cached,
                                                                              log_keyword=False, **kwargs)
        if out_bcast is not None:
            return_dict["out_bcast"] = self.port_verify_out_broadcast_packets(device_name, port, out_bcast,
                                                                              out_bcast_oper, use_cached=use_cached,
                                                                              log_keyword=False, **kwargs)
        if in_64_octets is not None:
            return_dict["in_64_octets"] = self.port_verify_64_bit_in_octets(device_name, port, in_64_octets,
                                                                            in_64_octets_oper, use_cached=use_cached,
                                                                            log_keyword=False, **kwargs)
        if in_64_ucast is not None:
            return_dict["in_64_ucast"] = self.port_verify_64_bit_in_unicast_packets(device_name, port, in_64_ucast,
                                                                                    in_64_ucast_oper,
                                                                                    use_cached=use_cached,
                                                                                    log_keyword=False, **kwargs)
        if in_64_mcast is not None:
            return_dict["in_64_mcast"] = self.port_verify_64_bit_in_multicast_packets(device_name, port, in_64_mcast,
                                                                                      in_64_mcast_oper,
                                                                                      use_cached=use_cached,
                                                                                      log_keyword=False, **kwargs)
        if in_64_bcast is not None:
            return_dict["in_64_bcast"] = self.port_verify_64_bit_in_broadcast_packets(device_name, port, in_64_bcast,
                                                                                      in_64_bcast_oper,
                                                                                      use_cached=use_cached,
                                                                                      log_keyword=False, **kwargs)
        if out_64_octets is not None:
            return_dict["out_64_octets"] = self.port_verify_64_bit_out_octets(device_name, port, out_64_octets,
                                                                              out_64_octets_oper, use_cached=use_cached,
                                                                              log_keyword=False, **kwargs)
        if out_64_ucast is not None:
            return_dict["out_64_ucast"] = self.port_verify_64_bit_out_unicast_packets(device_name, port, out_64_ucast,
                                                                                      out_64_ucast_oper,
                                                                                      use_cached=use_cached,
                                                                                      log_keyword=False, **kwargs)
        if out_64_mcast is not None:
            return_dict["out_64_mcast"] = self.port_verify_64_bit_out_multicast_packets(device_name, port,
                                                                                        out_64_mcast, out_64_mcast_oper,
                                                                                        use_cached=use_cached,
                                                                                        log_keyword=False, **kwargs)
        if out_64_bcast is not None:
            return_dict["out_64_bcast"] = self.port_verify_64_bit_out_broadcast_packets(device_name, port,
                                                                                        out_64_bcast, out_64_bcast_oper,
                                                                                        use_cached=use_cached,
                                                                                        log_keyword=False, **kwargs)
        return return_dict
