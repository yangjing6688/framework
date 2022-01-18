"""
Keyword class for all isis cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.IsisConstants import \
    IsisConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.IsisConstants import \
    IsisConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementIsisGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementIsisGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "isis"

    def isis_enable_global(self, device_name, **kwargs):
        """
        Description: Globally enables IS-IS.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def isis_disable_global(self, device_name, **kwargs):
        """
        Description: Globally disables IS-IS.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def isis_set_system_id(self, device_name, sys_id='', **kwargs):
        """
        Description: Creates the IS-IS System-Id.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "sys_id": sys_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SYSTEM_ID,
                                    **kwargs)

    def isis_clear_system_id(self, device_name, **kwargs):
        """
        Description: Removes the IS-IS System-Id.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SYSTEM_ID,
                                    **kwargs)

    def isis_set_manual_area(self, device_name, manual_area='', **kwargs):
        """
        Description: Configures the IS-IS Manual-area.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "manual_area": manual_area
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MANUAL_AREA,
                                    **kwargs)

    def isis_clear_manual_area(self, device_name, manual_area='', **kwargs):
        """
        Description: Removes the IS-IS Manual-area.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "manual_area": manual_area
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MANUAL_AREA,
                                    **kwargs)

    def isis_set_sys_name(self, device_name, name='', **kwargs):
        """
        Description: Configures the IS-IS hostname.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SYS_NAME,
                                    **kwargs)

    def isis_clear_sys_name(self, device_name, **kwargs):
        """
        Description: Removes the IS-IS hostname.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SYS_NAME,
                                    **kwargs)

    def isis_set_ipv4_source_address(self, device_name, ip='', **kwargs):
        """
        Description: Configures the IS-IS PLSB IP v4 address. Defines an existing router interface for management
                     (ping/traceroute).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_clear_ipv4_source_address(self, device_name, **kwargs):
        """
        Description: Removes the IS-IS PLSB IP v4 address. Define an existing router interface for management
                     (ping/traceroute).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_set_ipv6_source_address(self, device_name, ipv6_addr='', **kwargs):
        """
        Description: Configures the IS-IS IP v6 address. Defines an existing router interface for management
                     (ping/traceroute).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ipv6_addr": ipv6_addr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_clear_ipv6_source_address(self, device_name, **kwargs):
        """
        Description: Removes the IS-IS IPv6 address. Define an existing router interface for management
                     (ping/traceroute).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV6_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_set_ipv4_tunnel_source_address(self, device_name, ip='', **kwargs):
        """
        Description: Configures the IS-IS IP tunnel source address.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_TUNNEL_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_clear_ipv4_tunnel_source_address(self, device_name, **kwargs):
        """
        Description: Removes the IS-IS IP tunnel source address.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_TUNNEL_SOURCE_ADDRESS,
                                    **kwargs)

    def isis_set_inband_mgmt_ip(self, device_name, ip='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INBAND_MGMT_IP,
                                    **kwargs)

    def isis_clear_inband_mgmt_ip(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INBAND_MGMT_IP,
                                    **kwargs)

    def isis_set_metric_narrow(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_NARROW,
                                    **kwargs)

    def isis_clear_metric_narrow(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_METRIC_NARROW,
                                    **kwargs)

    def isis_set_metric_wide(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_WIDE,
                                    **kwargs)

    def isis_clear_metric_wide(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_METRIC_WIDE,
                                    **kwargs)

    def isis_set_overload(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_OVERLOAD,
                                    **kwargs)

    def isis_clear_overload(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_OVERLOAD,
                                    **kwargs)

    def isis_set_redistribute_bgp(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_BGP,
                                    **kwargs)

    def isis_clear_redistribute_bgp(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_BGP,
                                    **kwargs)

    def isis_enable_redistribute_bgp(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_BGP,
                                    **kwargs)

    def isis_disable_redistribute_bgp(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_BGP,
                                    **kwargs)

    def isis_set_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Configures IS-IS to redistribute directly attached routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def isis_clear_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Un-configures IS-IS redistribute directly attached routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def isis_enable_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Enables IS-IS to redistribute directly attached routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def isis_disable_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Disables IS-IS from redistributing directly attached routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def isis_enable_redistribute_direct_ipv6(self, device_name, **kwargs):
        """
        Description: Enables IS-IS redistribute direct for attached IPv6 routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_DIRECT_IPV6,
                                    **kwargs)

    def isis_disable_redistribute_direct_ipv6(self, device_name, **kwargs):
        """
        Description: Disables IS-IS redistribute direct for attached IPv6 routes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_DIRECT_IPV6,
                                    **kwargs)

    def isis_set_redistribute_direct_apply(self, device_name, **kwargs):
        """
        Description: Applies IS-IS redistribute direct configuration or changes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_DIRECT_APPLY,
                                    **kwargs)

    def isis_set_redistribute_direct_route_map_policy(self, device_name, policy_name='', **kwargs):
        """
        Description: Specify the route policy to achieve the final granularity in filtering to determine whether or
                     nota specific route should be advertised to the given protocol.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "policy_name": policy_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY,
                                    **kwargs)

    def isis_clear_redistribute_direct_route_map_policy(self, device_name, **kwargs):
        """
        Description: Removes the route policy for IS-IS redistribute direct.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY,
                                    **kwargs)

    def isis_set_redistribute_ospf(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_OSPF,
                                    **kwargs)

    def isis_clear_redistribute_ospf(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_OSPF,
                                    **kwargs)

    def isis_enable_redistribute_ospf(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_OSPF,
                                    **kwargs)

    def isis_disable_redistribute_ospf(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_OSPF,
                                    **kwargs)

    def isis_set_redistribute_rip(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_RIP,
                                    **kwargs)

    def isis_clear_redistribute_rip(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_RIP,
                                    **kwargs)

    def isis_enable_redistribute_rip(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_RIP,
                                    **kwargs)

    def isis_disable_redistribute_rip(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_RIP,
                                    **kwargs)

    def isis_set_redistribute_static(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def isis_clear_redistribute_static(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def isis_enable_redistribute_static(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def isis_disable_redistribute_static(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def isis_set_redistribute_apply(self, device_name, oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "oid_index": oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_APPLY,
                                    **kwargs)

    def isis_set_spf_delay(self, device_name, delay='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "delay": delay
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SPF_DELAY,
                                    **kwargs)

    def isis_clear_spf_delay(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SPF_DELAY,
                                    **kwargs)

    def isis_set_circuit_on_port(self, device_name, isis_circuit='', port='', **kwargs):
        """
        Description: Creates an ISIS circuit on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_circuit": isis_circuit,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CIRCUIT_ON_PORT,
                                    **kwargs)

    def isis_enable_circuit_on_port(self, device_name, port='', **kwargs):
        """
        Description: Enables an ISIS circuit on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CIRCUIT_ON_PORT,
                                    **kwargs)

    def isis_disable_circuit_on_port(self, device_name, port='', **kwargs):
        """
        Description: Disables an ISIS circuit on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CIRCUIT_ON_PORT,
                                    **kwargs)

    def isis_clear_circuit_on_port(self, device_name, port='', **kwargs):
        """
        Description: Removes an ISIS circuit from a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CIRCUIT_ON_PORT,
                                    **kwargs)

    def isis_set_circuit_on_mlt(self, device_name, isis_circuit='', mlt_id='', **kwargs):
        """
        Description: Creates an ISIS circuit on an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_circuit": isis_circuit,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CIRCUIT_ON_MLT,
                                    **kwargs)

    def isis_enable_circuit_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Enables an ISIS circuit on an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CIRCUIT_ON_MLT,
                                    **kwargs)

    def isis_disable_circuit_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Disables an ISIS circuit on an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CIRCUIT_ON_MLT,
                                    **kwargs)

    def isis_clear_circuit_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Removes an ISIS circuit from an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CIRCUIT_ON_MLT,
                                    **kwargs)

    def isis_set_auth_on_port(self, device_name, port='', auth_type='', key_id='', auth_key='', **kwargs):
        """
        Description: Configures ISIS authentication for IIH to be sent/received on the port circuit.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "auth_key": auth_key,
            "auth_type": auth_type,
            "key_id": key_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_ON_PORT,
                                    **kwargs)

    def isis_set_auth_on_mlt(self, device_name, mlt_id='', auth_type='', key_id='', auth_key='', **kwargs):
        """
        Description: Configures the authentication type for IIH to be sent/received on the circuit/interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "auth_key": auth_key,
            "auth_type": auth_type,
            "key_id": key_id,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_ON_MLT,
                                    **kwargs)

    def isis_clear_auth_on_port(self, device_name, port='', **kwargs):
        """
        Description: Removes authentication on the port circuit.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH_ON_PORT,
                                    **kwargs)

    def isis_clear_auth_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Removes authentication on the MLT circuit.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH_ON_MLT,
                                    **kwargs)

    def isis_set_l1_dr_priority_on_port(self, device_name, port='', priority='', **kwargs):
        """
        Description: Configures the priority for the becoming LAN Designated Intermediate System at level 1.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_DR_PRIORITY_ON_PORT,
                                    **kwargs)

    def isis_set_l1_dr_priority_on_mlt(self, device_name, mlt_id='', priority='', **kwargs):
        """
        Description: Configures the priority for the becoming LAN Designated Intermediate System at level 1.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_DR_PRIORITY_ON_MLT,
                                    **kwargs)

    def isis_set_l1_hello_interval_on_port(self, device_name, port='', interval='', **kwargs):
        """
        Description: Configures the period between Hellos on L1L2 point to point circuits.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interval": interval,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_INTERVAL_ON_PORT,
                                    **kwargs)

    def isis_set_l1_hello_interval_on_mlt(self, device_name, mlt_id='', interval='', **kwargs):
        """
        Description: Configures the period between Hellos on L1L2 point to point circuits.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interval": interval,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_INTERVAL_ON_MLT,
                                    **kwargs)

    def isis_set_l1_hello_multiplier_on_port(self, device_name, port='', multiplier='', **kwargs):
        """
        Description: Configures the multiplier of the corresponding HelloTimer that determines the holding time.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "multiplier": multiplier,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_MULTIPLIER_ON_PORT,
                                    **kwargs)

    def isis_set_l1_hello_multiplier_on_mlt(self, device_name, mlt_id='', multiplier='', **kwargs):
        """
        Description: Verifies the multiplier of the corresponding HelloTimer that determines the holding time.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "multiplier": multiplier
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_MULTIPLIER_ON_MLT,
                                    **kwargs)

    def isis_set_logical_interface_port(self, device_name, isis_id='', primary_vlan='', secondary_vlan='', port='',
                                        **kwargs):
        """
        Description: Creates an ISIS logical-interface on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "port": port,
            "primary_vlan": primary_vlan,
            "secondary_vlan": secondary_vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_PORT,
                                    **kwargs)

    def isis_set_logical_interface_port_name(self, device_name, isis_id='', primary_vlan='', secondary_vlan='',
                                             port='', name='', **kwargs):
        """
        Description: Creates an ISIS logical-interface on a port and adds a name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "name": name,
            "port": port,
            "primary_vlan": primary_vlan,
            "secondary_vlan": secondary_vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_PORT_NAME,
                                    **kwargs)

    def isis_set_logical_interface_mlt(self, device_name, isis_id='', primary_vlan='', secondary_vlan='', mlt_id='',
                                       **kwargs):
        """
        Description: Creates an ISIS logical-interface on a mlt.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "mlt_id": mlt_id,
            "primary_vlan": primary_vlan,
            "secondary_vlan": secondary_vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_MLT,
                                    **kwargs)

    def isis_set_logical_interface_mlt_name(self, device_name, isis_id='', primary_vlan='', secondary_vlan='',
                                            mlt_id='', name='', **kwargs):
        """
        Description: Creates an ISIS logical-interface on a mlt and adds a name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "mlt_id": mlt_id,
            "name": name,
            "primary_vlan": primary_vlan,
            "secondary_vlan": secondary_vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_MLT_NAME,
                                    **kwargs)

    def isis_set_logical_interface_ipv4(self, device_name, isis_id='', ip='', **kwargs):
        """
        Description: Creates an ISIS logical-interface for a destination IPv4 address.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip": ip,
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_IPV4,
                                    **kwargs)

    def isis_set_logical_interface_ipv4_name(self, device_name, isis_id='', ip='', name='', **kwargs):
        """
        Description: Creates an ISIS logical-interface for a destination IPv4 address and adds a name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip": ip,
            "isis_id": isis_id,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_IPV4_NAME,
                                    **kwargs)

    def isis_clear_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Removes an ISIS logical-interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_set_circuit_on_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Creates an ISIS circuit on a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CIRCUIT_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_enable_circuit_on_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Enables an ISIS circuit on a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CIRCUIT_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_disable_circuit_on_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Disables an ISIS circuit on a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CIRCUIT_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_clear_circuit_on_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Removes an ISIS circuit from a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CIRCUIT_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_set_auth_on_logical_interface(self, device_name, isis_id='', auth_type='', key_id='', auth_key='',
                                           **kwargs):
        """
        Description: Configures ISIS authentication for IIH to be sent/received on the logical interface circuit.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "auth_key": auth_key,
            "auth_type": auth_type,
            "isis_id": isis_id,
            "key_id": key_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_clear_auth_on_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Description: Removes authentication on the logical interface circuit.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_set_l1_dr_priority_on_logical_interface(self, device_name, isis_id='', priority='', **kwargs):
        """
        Description: Configures the priority for the becoming LAN Designated Intermediate System at level 1.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_DR_PRIORITY_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_set_l1_hello_interval_on_logical_interface(self, device_name, isis_id='', interval='', **kwargs):
        """
        Description: Configures the period between Hellos on L1L2 point to point circuits.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interval": interval,
            "isis_id": isis_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_INTERVAL_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    def isis_set_l1_hello_multiplier_on_logical_interface(self, device_name, isis_id='', multiplier='', **kwargs):
        """
        Description: Configures the multiplier of the corresponding HelloTimer that determines the holding time.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "multiplier": multiplier
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_HELLO_MULTIPLIER_ON_LOGICAL_INTERFACE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def isis_verify_enabled_globally(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS is enabled globally.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_GLOBALLY_ENABLED, True,
                                           "IS-IS is globally enabled on {device_name}.",
                                           "IS-IS is NOT globally enabled on {device_name}!",
                                           **kwargs)

    def isis_verify_disabled_globally(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS is disabled globally.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_GLOBALLY_DISABLED, True,
                                           "IS-IS is globally disabled on {device_name}.",
                                           "IS-IS is NOT globally disabled on {device_name}!",
                                           **kwargs)

    def isis_verify_system_id(self, device_name, sysid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [sysid]       - The IS-IS System-Id.

        Verifies the specified IS-IS System-Id is present.
        """
        args = {"sys_id": sysid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_SYS_ID, True,
                                           "IS-IS System-ID {sys_id} exists on {device_name}.",
                                           "IS-IS System-ID {sys_id} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def isis_verify_system_id_is_not(self, device_name, sysid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [sysid]       - The IS-IS System-Id.

        Verifies the specified IS-IS System-Id is not present.
        """
        args = {"sys_id": sysid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_SYS_ID, False,
                                           "IS-IS System-ID {sys_id} does not exist on {device_name}.",
                                           "IS-IS System-ID {sys_id} STILL exists on {device_name}!",
                                           **kwargs)

    def isis_verify_manual_area_exists(self, device_name, area='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [area]        - The IS-IS Manual-area.

        Verifies the specified IS-IS Manual-area is present.
        """
        args = {"manual_area": area}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MANUAL_AREA,
                                           self.parse_const.VERIFY_ISIS_MANUAL_AREA, True,
                                           "IS-IS manual-area {manual_area} exists on {device_name}.",
                                           "IS-IS manual-area {manual_area} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def isis_verify_manual_area_does_not_exist(self, device_name, area='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [area]        - The IS-IS Manual-area.

        Verifies the specified IS-IS Manual-area is not present.
        """
        args = {"manual_area": area}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MANUAL_AREA,
                                           self.parse_const.VERIFY_ISIS_MANUAL_AREA, False,
                                           "IS-IS manual-area {manual_area} does not exist on {device_name}.",
                                           "IS-IS manual-area {manual_area} STILL exists on {device_name}!",
                                           **kwargs)

    def isis_verify_system_name(self, device_name, sys_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [sys_name]      - The IS-IS System Name.

        Verifies the specified IS-IS System Name is correct.
        (NOTE:  On VOSS, this is the Router Name in the show isis command).
        """
        args = {"name": sys_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_SYS_NAME, True,
                                           "IS-IS System Name is {name}.",
                                           "IS-IS System Name is NOT {name}.!",
                                           **kwargs)

    def isis_verify_system_name_is_not(self, device_name, sys_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword will be run against.
        [sys_name]       - The IS-IS System-Name
        (NOTE:  On VOSS, this is the Router Name in the show isis command).

        Verifies the IS-IS System Name(Router Name) is not present.
        """
        args = {"name": sys_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_ISIS_SYS_NAME, False,
                                           "IS-IS System-Name {name} does not exist on {device_name}.",
                                           "IS-IS System-Name {name} STILL exists on {device_name}!",
                                           **kwargs)

    def isis_verify_circuit_on_port_exists(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on a port exists.
        """
        args = {"port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_PORT, True,
                                           "IS-IS circuit exists on port {port}.",
                                           "IS-IS circuit does NOT exist on port {port}!",
                                           **kwargs)

    def isis_verify_circuit_on_port_does_not_exist(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on a port does not exist.
        """
        args = {"port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_PORT, False,
                                           "IS-IS circuit does not exist on port {port}.",
                                           "IS-IS circuit does exist on port {port}!",
                                           **kwargs)

    def isis_verify_circuit_on_port_enabled(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on a port is administratively enabled.
        """
        args = {"port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_PORT, True,
                                           "IS-IS circuit is enabled on port {port}.",
                                           "IS-IS circuit is NOT enabled on port {port}!",
                                           **kwargs)

    def isis_verify_circuit_on_port_disabled(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on a port is administratively disabled
        """
        args = {"port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_PORT, False,
                                           "IS-IS circuit is disabled on port {port}.",
                                           "IS-IS circuit is NOT disabled on port {port}!",
                                           **kwargs)

    def isis_verify_circuit_on_mlt_exists(self, device_name, mlt_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_ids]       - The MLT(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on an MLT exists.
        """
        args = {"mlt_id": mlt_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_MLT, True,
                                           "IS-IS circuit exists on MLT {mlt_id}.",
                                           "IS-IS circuit does NOT exist on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_mlt_does_not_exist(self, device_name, mlt_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_ids]       - The MLT(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on an MLT does not exist.
        """
        args = {"mlt_id": mlt_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_MLT, False,
                                           "IS-IS circuit does not exist on MLT {mlt_id}.",
                                           "IS-IS circuit exists on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_mlt_enabled(self, device_name, mlt_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_ids]       - The MLT(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on an MLT is administratively enabled.
        """
        args = {"mlt_id": mlt_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_MLT, True,
                                           "IS-IS circuit is enabled on MLT {mlt_id}.",
                                           "IS-IS circuit is NOT enabled on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_mlt_disabled(self, device_name, mlt_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_ids]       - The MLT(s) on which to check an ISIS circuit.

        Verifies an ISIS circuit on an MLT is administratively disabled.
        """
        args = {"mlt_id": mlt_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_MLT, False,
                                           "IS-IS circuit is disabled on MLT {mlt_id}.",
                                           "IS-IS circuit is NOT disabled on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_logical_interface_exists(self, device_name, isis_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.

        Verifies an ISIS circuit on a port exists.
        """
        args = {"isis_id": isis_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS circuit exists on logical interface {isis_id}.",
                                           "IS-IS circuit does NOT exist on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_logical_interface_does_not_exist(self, device_name, isis_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.

        Verifies an ISIS circuit on a logical interface does not exist.
        """
        args = {"isis_id": isis_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE, False,
                                           "IS-IS circuit does not exist on logical interface {isis_id}.",
                                           "IS-IS circuit does exist on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_logical_interface_enabled(self, device_name, isis_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.

        Verifies an ISIS circuit on a logical interface is administratively enabled.
        """
        args = {"isis_id": isis_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS circuit is enabled on logical interface {isis_id}.",
                                           "IS-IS circuit is NOT enabled on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_circuit_on_logical_interface_disabled(self, device_name, isis_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.

        Verifies an ISIS circuit on a logical interface is administratively disabled
        """
        args = {"isis_id": isis_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_ENABLE_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE, False,
                                           "IS-IS circuit is disabled on logical interface {isis_id}.",
                                           "IS-IS circuit is NOT disabled on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_auth_type_port(self, device_name, port='', auth_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check an ISIS circuit.
        [auth_type]   - Authentication type for IIH to be sent/received on the circuit/interface.
                        Values:
                            none
                            simple
                            hmac-md5
                            hmac-sha-256

        Verifies the authentication type for IIH to be sent/received on the port circuit.
        """
        args = {"port": port,
                "auth_type": auth_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_PORT, True,
                                           "IS-IS circuit authentication type is {auth_type} on port {port}.",
                                           "IS-IS circuit authentication type is NOT {auth_type} on port {port}!",
                                           **kwargs)

    def isis_verify_auth_type_mlt(self, device_name, mlt_id='', auth_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check an ISIS circuit.
        [auth_type]   - Authentication type for IIH to be sent/received on the circuit/interface.
                        Values:
                            none
                            simple
                            hmac-md5
                            hmac-sha-256

        Verifies the authentication type for IIH to be sent/received on the MLT circuit.
        """
        args = {"mlt_id": mlt_id,
                "auth_type": auth_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_MLT, True,
                                           "IS-IS circuit authentication type is {auth_type} on MLT {mlt_id}.",
                                           "IS-IS circuit authentication type is NOT {auth_type} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_auth_type_logical_interface(self, device_name, isis_id='', auth_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.
        [auth_type]   - Authentication type for IIH to be sent/received on the circuit/interface.
                        Values:
                            none
                            simple
                            hmac-md5
                            hmac-sha-256

        Verifies the authentication type for IIH to be sent/received on the logical interface circuit.
        """
        args = {"isis_id": isis_id,
                "auth_type": auth_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS circuit authentication type is {auth_type} on"
                                           " logical interface {isis_id}.",
                                           "IS-IS circuit authentication type is NOT {auth_type} on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_auth_key_id_port(self, device_name, port='', key_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check an ISIS circuit.
        [key_id]      -  Authentication key id related to IIH key.  This can be set only if the auth-type is hmac-md5.
                        The value of 0 indicates KeyId is not configured.  Value range: 1..255

        Verifies the authentication key ID for IIH to be sent/received on the port circuit.
        """
        args = {"port": port,
                "key_id": key_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_PORT, True,
                                           "IS-IS circuit authentication key ID is {key_id} on port {port}.",
                                           "IS-IS circuit authentication key ID is NOT {key_id} on port {port}!",
                                           **kwargs)

    def isis_verify_auth_key_id_mlt(self, device_name, mlt_id='', key_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check an ISIS circuit.
        [key_id]      -  Authentication key id related to IIH key.  This can be set only if the auth-type is hmac-md5.
                         The value of 0 indicates KeyId is not configured.  Value range: 1..255

        Verifies the authentication key ID for IIH to be sent/received on the MLT circuit.
        """
        args = {"mlt_id": mlt_id,
                "key_id": key_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_MLT, True,
                                           "IS-IS circuit authentication key ID is {key_id} on MLT {mlt_id}.",
                                           "IS-IS circuit authentication key ID is NOT {key_id} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_auth_key_id_logical_interface(self, device_name, isis_id='', key_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.
        [key_id]      -  Authentication key id related to IIH key.  This can be set only if the auth-type is hmac-md5.
                        The value of 0 indicates KeyId is not configured.  Value range: 1..255

        Verifies the authentication key ID for IIH to be sent/received on the logical interface circuit.
        """
        args = {"isis_id": isis_id,
                "key_id": key_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS circuit authentication key ID is {key_id} on"
                                           " logical interface {isis_id}.",
                                           "IS-IS circuit authentication key ID is NOT {key_id} on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_auth_does_not_exist_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check an ISIS circuit.

        Verifies the authentication does not exist on the port circuit.
        """
        args = {"port": port,
                "auth_type": "none"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_PORT, True,
                                           "IS-IS circuit authentication type is {auth_type} on port {port}.",
                                           "IS-IS circuit authentication type is NOT {auth_type} on port {port}!",
                                           **kwargs)

    def isis_verify_auth_does_not_exist_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check an ISIS circuit.

        Verifies the authentication does not exist on the MLT circuit.
        """
        args = {"mlt_id": mlt_id,
                "auth_type": "none"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_MLT, True,
                                           "IS-IS circuit authentication type does not exist on MLT {mlt_id}.",
                                           "IS-IS circuit authentication type does not exist on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_auth_does_not_exist_logical_interface(self, device_name, isis_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check an ISIS circuit.

        Verifies the authentication does not exist on the logical interface circuit.
        """
        args = {"isis_id": isis_id,
                "auth_type": "none"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_AUTH,
                                           self.parse_const.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS circuit authentication type is {auth_type} on"
                                           " logical interface {isis_id}.",
                                           "IS-IS circuit authentication type is NOT {auth_type} on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_level_port(self, device_name, port='', level='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [level]       - The IS-IS level.  Values: 1, 2, and 3.
                        (1 = L1, 2 = L2, 3 = L1 & L2).
                        How is the adjacency used?  On a point-to-point link,
                        this might be level1and2, but on a LAN, the usage will
                        be level1 on the adjacency between peers at L1,
                        and level2 for the adjacency between peers at L2.

        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the IS-IS level of how the adjacency is used.
        """
        args = {"port": port,
                "level": level,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_LEVEL_ON_PORT, True,
                                           "IS-IS adjacency level is {level} on port {port}.",
                                           "IS-IS adjacency level is NOT {level} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_level_mlt(self, device_name, mlt_id='', level='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [level]       - The IS-IS level.  Values: 1, 2, and 3.
                        (1 = L1, 2 = L2, 3 = L1 & L2).
                        How is the adjacency used?  On a point-to-point link,
                        this might be level1and2, but on a LAN, the usage will
                        be level1 on the adjacency between peers at L1,
                        and level2 for the adjacency between peers at L2.

        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the IS-IS level of how the adjacency is used.
        """
        args = {"mlt_id": mlt_id,
                "level": level,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_LEVEL_ON_MLT, True,
                                           "IS-IS adjacency level is {level} on MLT {mlt_id}.",
                                           "IS-IS adjacency level is NOT {level} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_level_logical_interface(self, device_name, isis_id='', level='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [level]       - The IS-IS level.  Values: 1, 2, and 3.
                        (1 = L1, 2 = L2, 3 = L1 & L2).
                        How is the adjacency used?  On a point-to-point link,
                        this might be level1and2, but on a LAN, the usage will
                        be level1 on the adjacency between peers at L1,
                        and level2 for the adjacency between peers at L2.

        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the IS-IS level of how the adjacency is used.
        """
        args = {"isis_id": isis_id,
                "level": level,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_LEVEL_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency level is {level} on logical interface {isis_id}.",
                                           "IS-IS adjacency level is NOT {level} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_state_port(self, device_name, port='', state='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [state]       - The state of the IS-IS adjacency.
                        Values: down, initializing, up, and failed.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the state of the IS-IS adjacency.
        """
        args = {"port": port,
                "state": state,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATE_ON_PORT, True,
                                           "IS-IS adjacency state is {state} on port {port}.",
                                           "IS-IS adjacency state is NOT {state} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_state_mlt(self, device_name, mlt_id='', state='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [state]       - The state of the IS-IS adjacency.
                        Values: down, init, up, and failed.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the state of the IS-IS adjacency.
        """
        args = {"mlt_id": mlt_id,
                "state": state,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATE_ON_MLT, True,
                                           "IS-IS adjacency state is {state} on MLT {mlt_id}.",
                                           "IS-IS adjacency state is NOT {state} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_state_logical_interface(self, device_name, isis_id='', state='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [state]       - The state of the IS-IS adjacency.
                        Values: down, initializing, up, and failed.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the state of the IS-IS adjacency.
        """
        args = {"isis_id": isis_id,
                "state": state,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATE_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency state is {state} on logical interface {isis_id}.",
                                           "IS-IS adjacency state is NOT {state} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_active_port(self, device_name, port='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is active.
        """
        args = {"port": port,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_PORT, True,
                                           "IS-IS adjacency state is active on port {port}.",
                                           "IS-IS adjacency state is inactive on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_active_mlt(self, device_name, mlt_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is active.
        """
        args = {"mlt_id": mlt_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_MLT, True,
                                           "IS-IS adjacency state is active on MLT {mlt_id}.",
                                           "IS-IS adjacency state is inactive on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_active_logical_interface(self, device_name, isis_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is active.
        """
        args = {"isis_id": isis_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency state is active on logical interface {isis_id}.",
                                           "IS-IS adjacency state is inactive on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_inactive_port(self, device_name, port='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is inactive.
        """
        args = {"port": port,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_PORT, False,
                                           "IS-IS adjacency state is inactive on port {port}.",
                                           "IS-IS adjacency state is active on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_inactive_mlt(self, device_name, mlt_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is inactive.
        """
        args = {"mlt_id": mlt_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_MLT, False,
                                           "IS-IS adjacency state is inactive on MLT {mlt_id}.",
                                           "IS-IS adjacency state is active on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_inactive_logical_interface(self, device_name, isis_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies if the status of the IS-IS adjacency is inactive.
        """
        args = {"isis_id": isis_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_STATUS_ON_LOGICAL_INTERFACE, False,
                                           "IS-IS adjacency state is inactive on logical interface {isis_id}.",
                                           "IS-IS adjacency state is active on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_up_time_port(self, device_name, port='', time='', count_operator="=", adj_index="1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to check the adjacency.
        [time]            - The elapsed time that the adjacency has been up.
                            The value must take the form in the following examples: "21:57:55" or "1d:00:22:43".
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the up time of the adjacency.
        """
        args = {"port": port,
                "time": time,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_UPTIME_ON_PORT, True,
                                           "IS-IS adjacency up time is {count_operator} {time} on port {port}.",
                                           "IS-IS adjacency up time is NOT {count_operator} {time} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_up_time_mlt(self, device_name, mlt_id='', time='', count_operator="=", adj_index="1",
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT on which to check the adjacency.
        [time]            - The elapsed time that the adjacency has been up.
                            The value must take the form in the following examples: "21:57:55" or "1d:00:22:43".
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the up time of the adjacency.
        """
        args = {"mlt_id": mlt_id,
                "time": time,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_UPTIME_ON_MLT, True,
                                           "IS-IS adjacency up time is {count_operator} {time} on MLT {mlt_id}.",
                                           "IS-IS adjacency up time is NOT {count_operator} {time} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_up_time_logical_interface(self, device_name, isis_id='', time='', count_operator="=",
                                                        adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [time]            - The elapsed time that the adjacency has been up.
                            The value must take the form in the following examples: "21:57:55" or "1d:00:22:43".
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the up time of the adjacency.
        """
        args = {"isis_id": isis_id,
                "time": time,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_UPTIME_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency up time is {count_operator} {time} on"
                                           " logical interface {isis_id}.",
                                           "IS-IS adjacency up time is NOT {count_operator} {time} on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_priority_port(self, device_name, port='', priority='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [priority]    - The priority of the neighboring Intermediate System for becoming
                        the Designated Intermediate System.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the priority of the IS-IS adjacency.
        """
        args = {"port": port,
                "priority": priority,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_PRIORITY_ON_PORT, True,
                                           "IS-IS adjacency priority is {priority} on port {port}.",
                                           "IS-IS adjacency priority is NOT {priority} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_priority_mlt(self, device_name, mlt_id='', priority='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [priority]    - The priority of the neighboring Intermediate System for becoming
                        the Designated Intermediate System.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the priority of the IS-IS adjacency.
        """
        args = {"mlt_id": mlt_id,
                "priority": priority,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_PRIORITY_ON_MLT, True,
                                           "IS-IS adjacency priority is {priority} on MLT {mlt_id}.",
                                           "IS-IS adjacency priority is NOT {priority} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_priority_logical_interface(self, device_name, isis_id='', priority='', adj_index="1",
                                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [priority]    - The priority of the neighboring Intermediate System for becoming
                        the Designated Intermediate System.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the priority of the IS-IS adjacency.
        """
        args = {"isis_id": isis_id,
                "priority": priority,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_PRIORITY_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency priority is {priority} on logical interface {isis_id}.",
                                           "IS-IS adjacency priority is NOT {priority} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_hold_time_port(self, device_name, port='', holdtime='', count_operator='', adj_index="1",
                                             **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to check the adjacency.
        [holdtime]        - The holding time in seconds for this adjacency. This value is based on received IIH PDUs and
                            the elapsed time since receipt.
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the hold time of the IS-IS adjacency.
        """
        args = {"port": port,
                "holdtime": holdtime,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_PORT, True,
                                           "IS-IS adjacency hold time is {count_operator} {holdtime} on port {port}.",
                                           "IS-IS adjacency hold time is NOT {count_operator} "
                                           "{holdtime} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_hold_time_mlt(self, device_name, mlt_id='', holdtime='', count_operator='', adj_index="1",
                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT on which to check the adjacency.
        [holdtime]        - The holding time in seconds for this adjacency. This value is based on received IIH PDUs and
                             the elapsed time since receipt.
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the hold time of the IS-IS adjacency.
        """
        args = {"mlt_id": mlt_id,
                "holdtime": holdtime,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_MLT, True,
                                           "IS-IS adjacency hold time is {count_operator} {holdtime} on MLT {mlt_id}.",
                                           "IS-IS adjacency hold time is NOT {count_operator} "
                                           "{holdtime} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_hold_time_logical_interface(self, device_name, isis_id='', holdtime='', count_operator='',
                                                          adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [holdtime]        - The holding time in seconds for this adjacency. This value is based on received IIH PDUs and
                            the elapsed time since receipt.
        [count_operator]  - Used in conjunction with verifying the time value.  Can be ">", "<", or "=". Default is "="
        [adj_index]       - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies the hold time of the IS-IS adjacency.
        """
        args = {"isis_id": isis_id,
                "holdtime": holdtime,
                "count_operator": count_operator,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency hold time is {count_operator} {holdtime} on"
                                           " logical interface {isis_id}.",
                                           "IS-IS adjacency hold time is NOT {count_operator} {holdtime} on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_system_id_port(self, device_name, port='', sys_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [sys_id]      - The system ID of the neighboring Intermediate System in the form of "00bb.0000.4100".
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies system ID of the neighboring Intermediate System.
        """
        args = {"port": port,
                "sys_id": sys_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_SYSID_ON_PORT, True,
                                           "IS-IS adjacency system ID is {sys_id} on port {port}.",
                                           "IS-IS adjacency system ID is NOT {sys_id} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_system_id_mlt(self, device_name, mlt_id='', sys_id='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [sys_id]      - The The system ID of the neighboring Intermediate System in the form of "00bb.0000.4100".
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies system ID of the neighboring Intermediate System.
        """
        args = {"mlt_id": mlt_id,
                "sys_id": sys_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_SYSID_ON_MLT, True,
                                           "IS-IS adjacency system ID is {sys_id} on MLT {mlt_id}.",
                                           "IS-IS adjacency system ID is NOT {sys_id} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_system_id_logical_interface(self, device_name, isis_id='', sys_id='', adj_index="1",
                                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [sys_id]      - The system ID of the neighboring Intermediate System in the form of "00bb.0000.4100".
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies system ID of the neighboring Intermediate System.
        """
        args = {"isis_id": isis_id,
                "sys_id": sys_id,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_SYSID_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency system ID is {sys_id} on logical interface {isis_id}.",
                                           "IS-IS adjacency system ID is NOT {sys_id} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_adjacency_host_name_port(self, device_name, port='', hostname='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the adjacency.
        [hostname]    - The host name listed in LSP, or the system name if host name is not configured.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies host name of the neighboring Intermediate System.
        """
        args = {"port": port,
                "hostname": hostname,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_PORT, True,
                                           "IS-IS adjacency host name is {hostname} on port {port}.",
                                           "IS-IS adjacency host name is NOT {hostname} on port {port}!",
                                           **kwargs)

    def isis_verify_adjacency_host_name_mlt(self, device_name, mlt_id='', hostname='', adj_index="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the adjacency.
        [hostname]    - The host name listed in LSP, or the system name if host name is not configured.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies host name of the neighboring Intermediate System.
        """
        args = {"mlt_id": mlt_id,
                "hostname": hostname,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_MLT, True,
                                           "IS-IS adjacency host name is {hostname} on MLT {mlt_id}.",
                                           "IS-IS adjacency host name is NOT {hostname} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_adjacency_host_name_logical_interface(self, device_name, isis_id='', hostname='', adj_index="1",
                                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [hostname]    - The host name listed in LSP, or the system name if host name is not configured.
        [adj_index]   - A unique value identifying the IS adjacency from all other adjacencies on the circuit.

        Verifies host name of the neighboring Intermediate System.
        """
        args = {"isis_id": isis_id,
                "hostname": hostname,
                "adj_index": adj_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADJACENCIES,
                                           self.parse_const.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS adjacency host name is {hostname} on logical interface {isis_id}.",
                                           "IS-IS adjacency host name is NOT {hostname} on logical interface "
                                           "{isis_id}!",
                                           **kwargs)

    def isis_verify_l1_hello_interval_port(self, device_name, port='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the interval.
        [interval]    - The maximum period, in seconds, between IIH PDUs on multiaccess networks at this level for LANs.
                        The value at L1 is used as the period between Hellos on L1L2 point to point circuits.
                        Setting this value at level 2 on an L1L2 point to point circuit will result in an error
                        of InconsistentValue.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point circuits.
        """
        args = {"port": port,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_INTERVAL_ON_PORT, True,
                                           "IS-IS hello interval is {interval} on port {port}.",
                                           "IS-IS hello interval is NOT {interval} on port {port}!",
                                           **kwargs)

    def isis_verify_l1_hello_interval_mlt(self, device_name, mlt_id='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the interval.
        [interval]    - The maximum period, in seconds, between IIH PDUs on multiaccess networks at this level for LANs.
                        The value at L1 is used as the period between Hellos on L1L2 point to point circuits.
                        Setting this value at level 2 on an L1L2 point to point circuit will result in an error
                        of InconsistentValue.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point circuits.
        """
        args = {"mlt_id": mlt_id,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_INTERVAL_ON_MLT, True,
                                           "IS-IS hello interval is {interval} on MLT {mlt_id}.",
                                           "IS-IS hello interval is NOT {interval} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_l1_hello_interval_logical_interface(self, device_name, isis_id='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [interval]    - The maximum period, in seconds, between IIH PDUs on multiaccess networks at this level for LANs.
                        The value at L1 is used as the period between Hellos on L1L2 point to point circuits.
                        Setting this value at level 2 on an L1L2 point to point circuit will result in an error
                        of InconsistentValue.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point circuits.
        """
        args = {"isis_id": isis_id,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_INTERVAL_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS hello interval is {interval} on logical interface {isis_id}.",
                                           "IS-IS hello interval is NOT {interval} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_l1_hello_multiplier_port(self, device_name, port='', multiplier='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the multiplier.
        [multiplier]  - This value is multiplied by the corresponding HelloTimer and the result in seconds is used as
                        the holding time in transmitted hellos, to be used by receivers of hello packets from this IS.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the multiplier of the corresponding HelloTimer that determines the holding time.
        """
        args = {"port": port,
                "multiplier": multiplier}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_PORT, True,
                                           "IS-IS hello multiplier is {multiplier} on port {port}.",
                                           "IS-IS hello multiplier is NOT {multiplier} on port {port}!",
                                           **kwargs)

    def isis_verify_l1_hello_multiplier_mlt(self, device_name, mlt_id='', multiplier='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the multiplier.
        [multiplier]  - This value is multiplied by the corresponding HelloTimer and the result in seconds is used as
                        the holding time in transmitted hellos, to be used by receivers of hello packets from this IS.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the multiplier of the corresponding HelloTimer that determines the holding time.
        """
        args = {"mlt_id": mlt_id,
                "multiplier": multiplier}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_MLT, True,
                                           "IS-IS hello multiplier is {multiplier} on MLT {mlt_id}.",
                                           "IS-IS hello multiplier is NOT {multiplier} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_l1_hello_multiplier_logical_interface(self, device_name, isis_id='', multiplier='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [multiplier]  - This value is multiplied by the corresponding HelloTimer and the result in seconds is used as
                        the holding time in transmitted hellos, to be used by receivers of hello packets from this IS.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the multiplier of the corresponding HelloTimer that determines the holding time.
        """
        args = {"isis_id": isis_id,
                "multiplier": multiplier}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS hello multiplier is {multiplier} on logical interface {isis_id}.",
                                           "IS-IS hello multiplier is NOT {multiplier} on logical interface {isis_id}!",
                                           **kwargs)

    def isis_verify_l1_dr_hello_interval_port(self, device_name, port='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to check the dr hello interval.
        [interval]    - The period in seconds between Hello PDUs on multiaccess networks when the device is the
                        Designated Intermediate System.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point when the device is the Designated IS.
        """
        args = {"port": port,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_PORT, True,
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is {interval} on port {port}.",
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is {interval} on port {port}.",
                                           **kwargs)

    def isis_verify_l1_dr_hello_interval_mlt(self, device_name, mlt_id='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT on which to check the dr hello interval.
        [interval]    - The period in seconds between Hello PDUs on multiaccess networks when the device is the
                        Designated Intermediate System.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point when the device is the Designated IS.
        """
        args = {"mlt_id": mlt_id,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_MLT, True,
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is {interval} on MLT {mlt_id}.",
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is NOT {interval} on MLT {mlt_id}!",
                                           **kwargs)

    def isis_verify_l1_dr_hello_interval_logical_interface(self, device_name, isis_id='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface index on which to check.
        [interval]    - The period in seconds between Hello PDUs on multiaccess networks when the device is the
                        Designated Intermediate System.  This object follows the resettingTimer behavior.
                        Reference: ISIS.aoi iSISHelloTimer (45)

        Verifies the period between Hellos on L1L2 point to point when the device is the Designated IS.
        """
        args = {"isis_id": isis_id,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_TIMERS,
                                           self.parse_const.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_LOGICAL_INTERFACE, True,
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is {interval} on logical interface {isis_id}.",
                                           "IS-IS hello interval on this designated system {device_name}"
                                           " is {interval} on logical interface {isis_id}.",
                                           **kwargs)

    def isis_verify_lsdb_unicast_ip_and_hostname(self, device_name, address='', host_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [address]     - The unicast IP address. (Can be a host or network address).
        [host_name]   - The host name of the device where the address is reachable.

        Verifies the IS-IS reachable address from the expected host name.
        Note: This table (isisIPRATable) is not implemented in SNMP but is in the CLI using telnet or ssh as an agent.
        """
        args = {"address": address,
                "host_name": host_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LSDB_IP_UNICAST,
                                           self.parse_const.CHECK_ISIS_LSDB_IP_AND_HOSTNAME, True,
                                           "IS-IS address of {address} is associated with host name {host_name}",
                                           "IS-IS address of {address} is NOT associated with host name {host_name}!",
                                           **kwargs)

    def isis_verify_corrupted_lsps(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of corrupted in-memory LSPs detected.
        LSPs received from the wire with a bad checksum are silently dropped and not counted.
        LSPs received from the wire with parse errors are counted by isisSysStatLSPErrors.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_CORRUPTED_LSPS, True,
                                           "IS-IS number of corrupted in-memory LSPs detected is {count_operator}"
                                           " {count}",
                                           "IS-IS number of corrupted in-memory LSPs detected is NOT {count_operator}"
                                           " {count}!",
                                           **kwargs)

    def isis_verify_auth_key_fails(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of authentication key failures recognized by this Intermediate System.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_AUTHENTICATION_KEY_FAILS, True,
                                           "IS-IS number of authentication key failures is {count_operator}"
                                           " {count}",
                                           "IS-IS number of authentication key failures is NOT {count_operator}"
                                           " {count}!",
                                           **kwargs)

    def isis_verify_manual_addresses_dropped_from_area(self, device_name, count='', count_operator="=", level="1",
                                                       **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times a manual address has been dropped from the area.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_MANUAL_ADDRESSES_DROPPED_FROM_AREA, True,
                                           "IS-IS number of times a manual address has been dropped from the area is"
                                           " {count_operator} {count}",
                                           "IS-IS number of times a manual address has been dropped from the area is "
                                           "NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_maximum_sequence_number_exceeded_attempts(self, device_name, count='', count_operator="=",
                                                              level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times the IS has attempted to exceed the maximum sequence number.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_MAXIMUM_SEQUENCE_NUMBER_EXCEEDED_ATTEMPTS, True,
                                           "IS-IS number of times the IS has attempted to exceed the"
                                           " maximum sequence number is {count_operator} {count}",
                                           "IS-IS number of times the IS has attempted to exceed the"
                                           " maximum sequence number is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_sequence_number_skips(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times a sequence number skip has occurred.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_SEQUENCE_NUMBER_SKIPS, True,
                                           "IS-IS number of times a sequence number skip has occurred"
                                           " is {count_operator} {count}",
                                           "IS-IS number of times a sequence number skip has occurred"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_own_lsp_purges(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times a zero-aged copy of the system's own LSP is received from some other node.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_OWN_LSP_PURGES, True,
                                           "IS-IS number of times a  zero-aged copy of the system's own LSP is received"
                                           " from some other node is {count_operator} {count}",
                                           "IS-IS number of times a zero-aged copy of the system's own LSP is received"
                                           " from some other node is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_id_length_mismatches(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times a PDU is received with a different value for ID field length to
        that of the receiving system.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_ID_LENGTH_MISMATCHES, True,
                                           "IS-IS number of times the number of times a PDU is received with a "
                                           "different value for ID field length to that of the receiving system"
                                           " is {count_operator} {count}",
                                           "IS-IS number of times the number of times a PDU is received with a "
                                           "different value for ID field length to that of the receiving system"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_partition_changes(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of partition changes.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_PARTITION_CHANGES, True,
                                           "IS-IS number of partition changes is {count_operator} {count}",
                                           "IS-IS number of partition changes is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_lsp_database_overloads(self, device_name, count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times the LSP database has become overloaded.
        """
        args = {"count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_STATS,
                                           self.parse_const.CHECK_ISIS_LSP_DATABASE_OVERLOADS, True,
                                           "IS-IS number of times the LSP database has become overloaded"
                                           " is {count_operator} {count}",
                                           "IS-IS number of times the LSP database has become overloaded"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_exists_on_port(self, device_name, index='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [port]        - The ISIS logical-interface port to verify.

        Verifies an ISIS logical-interface index exists on a port.
        """
        args = {"index": index,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_PORT, True,
                                           "IS-IS logical-interface index {index} exist on port {port}.",
                                           "IS-IS logical-interface index {index} does NOT exist on port {port}!",
                                           **kwargs)

    def isis_verify_logical_interface_does_not_exist_on_port(self, device_name, index='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [port]        - The ISIS logical-interface port to verify.

        Verifies an ISIS logical-interface index does not exist on a port.
        """
        args = {"index": index,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_PORT, False,
                                           "IS-IS logical-interface index {index} does not exist on port {port}.",
                                           "IS-IS logical-interface index {index} exists on port {port}!",
                                           **kwargs)

    def isis_verify_logical_interface_exists_on_mlt(self, device_name, index='', mlt='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [mlt_index]   - The ISIS logical-interface mlt to verify.

        Verifies an ISIS logical-interface index exists on a mlt.
        """
        args = {"index": index,
                "mlt": mlt,
                "mlt_index": mlt}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_MLT, True,
                                           "IS-IS logical-interface index {index} exist on mlt {mlt}.",
                                           "IS-IS logical-interface index {index} does NOT exist on mlt {mlt}!",
                                           **kwargs)

    def isis_verify_logical_interface_does_not_exist_on_mlt(self, device_name, index='', mlt='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [port]        - The ISIS logical-interface port to verify.

        Verifies an ISIS logical-interface index does not exist on a mlt.
        """
        args = {"index": index,
                "mlt": mlt,
                "mlt_index": mlt}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_MLT, False,
                                           "IS-IS logical-interface index {index} does not exist on mlt {mlt}.",
                                           "IS-IS logical-interface index {index} exists on mlt {mlt}!",
                                           **kwargs)

    def isis_verify_logical_interface_ipv4_destination_exists(self, device_name, index='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [ip]          - The logical interface Destination IP IPv4 address.

        Verifies an ISIS logical-interface index exists for a destination IPv4 address.
        """
        args = {"index": index,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_IPV4, True,
                                           "IS-IS logical-interface index {index} exists for IP address {ip}.",
                                           "IS-IS logical-interface index {index} does NOT exist for IP address {ip}!",
                                           **kwargs)

    def isis_verify_logical_interface_ipv4_destination_does_not_exist(self, device_name, index='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index to verify.
        [ip]          - The logical interface Destination IP IPv4 address.

        Verifies an ISIS logical-interface index does not exist for a destination IPv4 address.
        """
        args = {"index": index,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_IPV4, False,
                                           "IS-IS logical-interface index {index} does not exist for IP address {ip}.",
                                           "IS-IS logical-interface index {index} exists for IP address {ip}!",
                                           **kwargs)

    def isis_verify_logical_interface_name(self, device_name, index='', name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index ID to verify.
        [name]        - The ISIS logical-interface name to verify.

        Verifies an ISIS logical-interface name exists for an index.
        """
        args = {"index": index,
                "name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE_NAME,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_NAME, True,
                                           "IS-IS logical-interface name {name} exists on index {index}.",
                                           "IS-IS logical-interface name {name} does NOT exist on index {index}!",
                                           **kwargs)

    def isis_verify_logical_interface_name_is_not(self, device_name, index='', name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [index]       - The ISIS logical-interface index ID to verify.
        [name]        - The ISIS logical-interface name to verify.

        Verifies an ISIS logical-interface name does not exist for an index.
        """
        args = {"index": index,
                "name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_INTERFACE_NAME,
                                           self.parse_const.VERIFY_ISIS_LOGICAL_INTERFACE_NAME, False,
                                           "IS-IS logical-interface name {name} does not exists on index {index}.",
                                           "IS-IS logical-interface name {name} exists on index {index}!",
                                           **kwargs)

    def isis_verify_port_auth_fails(self, device_name, port='', count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with the correct auth type has failed to pass authentication
        validation.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_AUTHENTICATION_FAILS, True,
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_adjacency_changes(self, device_name, port='', count='', count_operator="=", level="1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency state change has occurred on this circuit.

        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_ADJACENCY_CHANGES, True,
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_init_fails(self, device_name, port='', count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times initialization of this circuit has failed.
        This counts events such as PPP NCP failures. Failures to form an adjacency are counted by isisCircRejAdjs.

        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_INITIALIZATION_FAILS, True,
                                           "The number of times initialization of this circuit has failed"
                                           " is {count_operator} {count}.",
                                           "The number of times initialization of this circuit has failed"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_rejected_adjancencies(self, device_name, port='', count='', count_operator="=", level="1",
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency has been rejected on this circuit.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_REJECTED_ADJANCENCIES, True,
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_id_field_length_mismatches(self, device_name, port='', count='', count_operator="=", level="1",
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with an ID field length different to that for this system has
        been received.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_ID_FIELD_LENGTH_MISMATCHES, True,
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_max_area_address_mismatches(self, device_name, port='', count='', count_operator="=",
                                                     level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with a max area address field different to that for this
        system has been received been received.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_MAX_AREA_ADDRESS_MISMATCHES, True,
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_port_designated_is_changes(self, device_name, port='', count='', count_operator="=", level="1",
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies number of times the Designated IS has changed on this circuit at this level.  If the circuit is
        point to point, this count is zero.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_PORT_DESIGNATED_IS_CHANGES, True,
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_hellos_transmitted(self, device_name, port='', count='', count_operator="=", level="1",
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the transmitted direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_HELLOS_TRANSMITTED, True,
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_hellos_received(self, device_name, port='', count='', count_operator="=", level="1",
                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the received direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_HELLOS_RECEIVED, True,
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_lsps_transmitted(self, device_name, port='', count='', count_operator="=", level="1",
                                             **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the transmitted direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_LSPS_TRANSMITTED, True,
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_lsps_received(self, device_name, port='', count='', count_operator="=", level="1",
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the received direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_LSPS_RECEIVED, True,
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_csnps_transmitted(self, device_name, port='', count='', count_operator="=", level="1",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the transmitted direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_CSNPS_TRANSMITTED, True,
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_csnps_received(self, device_name, port='', count='', count_operator="=", level="1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the received direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_CSNPS_RECEIVED, True,
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_psnps_transmitted(self, device_name, port='', count='', count_operator="=", level="1",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the transmitted direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_PSNPS_TRANSMITTED, True,
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_port_psnps_received(self, device_name, port='', count='', count_operator="=", level="1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [port]            - The port on which to verify.  e.g. gigabitEthernet 1/8
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the received direction at this level.
        """
        args = {"port": port,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_PORT_IS_IS_PSNPS_RECEIVED, True,
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_auth_fails(self, device_name, mlt_id='', count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with the correct auth type has failed to pass authentication
        validation.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_AUTHENTICATION_FAILS, True,
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_adjacency_changes(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency state change has occurred on this circuit.

        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_ADJACENCY_CHANGES, True,
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_init_fails(self, device_name, mlt_id='', count='', count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times initialization of this circuit has failed.
        This counts events such as PPP NCP failures. Failures to form an adjacency are counted by isisCircRejAdjs.

        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_INITIALIZATION_FAILS, True,
                                           "The number of times initialization of this circuit has failed"
                                           " is {count_operator} {count}.",
                                           "The number of times initialization of this circuit has failed"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_rejected_adjancencies(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency has been rejected on this circuit.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_REJECTED_ADJANCENCIES, True,
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_id_field_length_mismatches(self, device_name, mlt_id='', count='', count_operator="=",
                                                   level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with an ID field length different to that for this system has
        been received.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_ID_FIELD_LENGTH_MISMATCHES, True,
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_max_area_address_mismatches(self, device_name, mlt_id='', count='', count_operator="=",
                                                    level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with a max area address field different to that for this
        system has been received been received.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_MAX_AREA_ADDRESS_MISMATCHES, True,
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_mlt_designated_is_changes(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies number of times the Designated IS has changed on this circuit at this level.  If the circuit is
        point to point, this count is zero.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_MLT_DESIGNATED_IS_CHANGES, True,
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_hellos_transmitted(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the transmitted direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_HELLOS_TRANSMITTED, True,
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_hellos_received(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the received direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_HELLOS_RECEIVED, True,
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_lsps_transmitted(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the transmitted direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_LSPS_TRANSMITTED, True,
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_lsps_received(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                         **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the received direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_LSPS_RECEIVED, True,
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_csnps_transmitted(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                             **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the transmitted direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_CSNPS_TRANSMITTED, True,
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_csnps_received(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the received direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_CSNPS_RECEIVED, True,
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_psnps_transmitted(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                             **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the transmitted direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_PSNPS_TRANSMITTED, True,
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_mlt_psnps_received(self, device_name, mlt_id='', count='', count_operator="=", level="1",
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [mlt_id]          - The MLT ID index on which to verify.  e.g. 1 for "MLT 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the received direction at this level.
        """
        args = {"mlt_id": mlt_id,
                "count": count,
                "level": level,
                "count_operator": count_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_MLT_IS_IS_PSNPS_RECEIVED, True,
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_auth_fails(self, device_name, isis_id='', count='', count_operator="=", level="1",
                                                 **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with the correct auth type has failed to pass authentication
        validation.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_AUTHENTICATION_FAILS, True,
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with the correct auth type has"
                                           " failed to pass authentication is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_adjacency_changes(self, device_name, isis_id='', count='', count_operator="=",
                                                        level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency state change has occurred on this circuit.

        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_ADJACENCY_CHANGES, True,
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency state change has occurred on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_init_fails(self, device_name, isis_id='', count='', count_operator="=",
                                                 level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times initialization of this circuit has failed.
        This counts events such as PPP NCP failures. Failures to form an adjacency are counted by isisCircRejAdjs.

        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_INITIALIZATION_FAILS, True,
                                           "The number of times initialization of this circuit has failed"
                                           " is {count_operator} {count}.",
                                           "The number of times initialization of this circuit has failed"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_rejected_adjancencies(self, device_name, isis_id='', count='', count_operator="=",
                                                            level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an adjacency has been rejected on this circuit.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_REJECTED_ADJANCENCIES, True,
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is {count_operator} {count}.",
                                           "The number of times an adjacency has been rejected on this circuit"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_id_field_length_mismatches(self, device_name, isis_id='', count='',
                                                                 count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with an ID field length different to that for this system has
        been received.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_ID_FIELD_LENGTH_MISMATCHES,
                                           True,
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with an ID field length"
                                           " different to that for this system has been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_max_area_address_mismatches(self, device_name, isis_id='', count='',
                                                                  count_operator="=", level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies the number of times an IS-IS control PDU with a max area address field different to that for this
        system has been received been received.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_MAX_AREA_ADDRESS_MISMATCHES,
                                           True,
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is {count_operator} {count}.",
                                           "The number of times an IS-IS control PDU with a max area address field"
                                           " different to that for this system has been received been received"
                                           " is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_logical_interface_designated_is_changes(self, device_name, isis_id='', count='', count_operator="=",
                                                            level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies number of times the Designated IS has changed on this circuit at this level.  If the circuit is
        point to point, this count is zero.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_STATS,
                                           self.parse_const.CHECK_ISIS_LOGICAL_INTERFACE_DESIGNATED_IS_CHANGES, True,
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of times the Designated IS has changed on this circuit at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_hellos_transmitted(self, device_name, isis_id='', count='', count_operator="=",
                                                            level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the transmitted direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_HELLOS_TRANSMITTED,
                                           True,
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_hellos_received(self, device_name, isis_id='', count='', count_operator="=",
                                                         level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS Hellos frames seen in the received direction at this level.
        Point-to-Point IIH PDUs are counted at the lowest enabled level: at L1 on L1 or L1L2 circuits,
        and at L2 otherwise.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_HELLOS_RECEIVED, True,
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS Hello PDUs seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_lsps_transmitted(self, device_name, isis_id='', count='', count_operator="=",
                                                          level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the transmitted direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_LSPS_TRANSMITTED,
                                           True,
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_lsps_received(self, device_name, isis_id='', count='', count_operator="=",
                                                       level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS LSP frames seen in the received direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_LSPS_RECEIVED, True,
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS LSP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_csnps_transmitted(self, device_name, isis_id='', count='', count_operator="=",
                                                           level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the transmitted direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_CSNPS_TRANSMITTED,
                                           True,
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_csnps_received(self, device_name, isis_id='', count='', count_operator="=",
                                                        level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS CSNP frames seen in the received direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_CSNPS_RECEIVED, True,
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS CSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_psnps_transmitted(self, device_name, isis_id='', count='', count_operator="=",
                                                           level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the transmitted direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_PSNPS_TRANSMITTED,
                                           True,
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the transmit direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_l1_logical_interface_psnps_received(self, device_name, isis_id='', count='', count_operator="=",
                                                        level="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [isis_id]         - The IS-IS logical interface index on which to verify.  e.g. 1 for "Logical Interface 1"
        [count]           - The number of counts to verify.
        [count_operator]  - Used in conjunction with verifying the count value.  Can be ">", "<", or "=". Default is "="
        [level]           - The IS-IS level that this entry describes.

        Verifies Number of IS-IS PSNP frames seen in the received direction at this level.
        """
        args = {"isis_id": isis_id,
                "count": count,
                "count_operator": count_operator,
                "level": level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_L1_PACKET_STATS,
                                           self.parse_const.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_PSNPS_RECEIVED, True,
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is {count_operator} {count}.",
                                           "The number of IS-IS PSNP frames seen in the receive direction at"
                                           " level {level} is NOT {count_operator} {count}!",
                                           **kwargs)

    def isis_verify_ipv4_source_address(self, device_name, ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ip]             - The ISIS source IPv4 address to verify.

        Verifies the ISIS PLSB IPv4 address that defines an existing router interface for management (ping/traceroute).
        """
        args = {"ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV4_SOURCE_ADDRESS, True,
                                           "IS-IS source IPv4 address {ip} exists on {device_name}.",
                                           "IS-IS source IPv4 address {ip} does NOT exist on {device_name}!",
                                           **kwargs)

    def isis_verify_ipv4_source_address_does_not_exist(self, device_name, ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ip]             - The ISIS source IPv4 address to verify.

        Verifies the ISIS PLSB IPv4 address that defines an existing router interface for management (ping/traceroute)
        does not exist.
        """
        args = {"ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV4_SOURCE_ADDRESS, False,
                                           "IS-IS source IPv4 address {ip} does not exist on {device_name}!",
                                           "IS-IS source IPv4 address {ip} EXISTS on {device_name}!",
                                           **kwargs)

    def isis_verify_ipv6_source_address(self, device_name, ipv6_addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ipv6_addr]      - The ISIS source IPv4 address to verify.

        Verifies the ISIS IPv6 address that defines an existing router interface for management (ping/traceroute).
        """
        args = {"ipv6_addr": ipv6_addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV6_SOURCE_ADDRESS, True,
                                           "IS-IS source IPv6 address {ipv6_addr} exists on {device_name}.",
                                           "IS-IS source IPv6 address {ipv6_addr} does NOT exist on {device_name}!",
                                           **kwargs)

    def isis_verify_ipv6_source_address_does_not_exist(self, device_name, ipv6_addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ipv6_addr]      - The ISIS source IPv6 address to verify.

        Verifies the ISIS IPv6 address that defines an existing router interface for management (ping/traceroute)
        does not exist.
        """
        args = {"ipv6_addr": ipv6_addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV6_SOURCE_ADDRESS, False,
                                           "IS-IS source IPv6 address {ipv6_addr} does not exist on {device_name}!",
                                           "IS-IS source IPv6 address {ipv6_addr} EXISTS on {device_name}!",
                                           **kwargs)

    def isis_verify_ipv4_tunnel_source_address(self, device_name, ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ip]             - The ISIS tunnel source IPv4 address to verify.

        Verifies the ISIS IPv4 tunnel source address.
        """
        args = {"ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV4_TUNNEL_SOURCE_ADDRESS, True,
                                           "IS-IS IPv4 tunnel source address {ip} exists on {device_name}.",
                                           "IS-IS IPv4 tunnel source address {ip} does NOT exist on {device_name}!",
                                           **kwargs)

    def isis_verify_ipv4_tunnel_source_address_does_not_exist(self, device_name, ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ip]             - The ISIS tunnel source IPv4 address to verify.

        Verifies the ISIS IPv4 tunnel source address does not exist.
        """
        args = {"ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_ISIS_IPV4_TUNNEL_SOURCE_ADDRESS, False,
                                           "IS-IS IPv4 tunnel source address {ip} does not exist on {device_name}.",
                                           "IS-IS IPv4 tunnel source address {ip} exists on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.

        Verifies ISIS redistribute direct is set.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT, True,
                                           "IS-IS Redistribute Direct is configured on {device_name}.",
                                           "IS-IS Redistribute Direct is NOT configured on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_not_set(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.

        Verifies ISIS redistribute direct is not set on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT, False,
                                           "IS-IS Redistribute Direct is not configured on {device_name}.",
                                           "IS-IS Redistribute Direct IS configured on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS redistribute direct is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ENABLED, True,
                                           "IS-IS redistribute direct is enabled on {device_name}.",
                                           "IS-IS redistribute direct is NOT enabled on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS redistribute direct is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_DISABLED, True,
                                           "IS-IS redistribute direct is disabled on {device_name}.",
                                           "IS-IS redistribute direct is NOT disabled on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_ipv6_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS redistribute direct IPv6 is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_IPV6_ENABLED, True,
                                           "IS-IS redistribute direct IPv6 is enabled on {device_name}.",
                                           "IS-IS redistribute direct IPv6 is NOT enabled on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_ipv6_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that IS-IS redistribute direct IPv6 is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_IPV6_DISABLED, True,
                                           "IS-IS redistribute direct IPv6 is disabled on {device_name}.",
                                           "IS-IS redistribute direct IPv6 is NOT disabled on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_route_map_policy(self, device_name, policy_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [policy_name]    - Route map name

        Verifies IS-IS route policy to achieve the final granularity in filtering to determine whether
        or not a specific route should be advertised to the given protocol.

        """
        args = {"policy_name": policy_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY, True,
                                           "IS-IS Redistribute Direct route map policy {policy_name}"
                                           " is configured on {device_name}.",
                                           "IS-IS Redistribute Direct route map policy {policy_name}"
                                           " is NOT configured on {device_name}!",
                                           **kwargs)

    def isis_verify_redistribute_direct_route_map_policy_does_not_exist(self, device_name, policy_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [policy_name]    - Route map name

        Verifies IS-IS route policy to achieve the final granularity in filtering to determine whether
        or not a specific route should be advertised to the given protocol is not configured.

        """
        args = {"policy_name": policy_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_REDISTRIBUTE,
                                           self.parse_const.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY_CLEAR,
                                           True,
                                           "IS-IS Redistribute Direct route map policy {policy_name}"
                                           " is not configured on {device_name}.",
                                           "IS-IS Redistribute Direct route map policy {policy_name}"
                                           " is configured on {device_name}!",
                                           **kwargs)
