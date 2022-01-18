"""
Keyword class for all ospf cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.OspfConstants import \
    OspfConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.OspfConstants import \
    OspfConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class NetworkElementOspfGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementOspfGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "ospf"

    def ospf_enable_global(self, device_name, **kwargs):
        """
        Description: Globally enable the OSPF protocol.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: EXOS, VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def ospf_disable_global(self, device_name, **kwargs):
        """
        Description: Globally disables the OSPF protocol.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: EXOS, VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def ospf_set_router_id(self, device_name, router_id='', **kwargs):
        """
        Description: Configures the OSPF Router ID.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: EXOS, VOSS
        """
        args = {
            "router_id": router_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ROUTER_ID,
                                    **kwargs)

    def ospf_clear_router_id(self, device_name, **kwargs):
        """
        Description: Unconfigures the OSPF Router ID.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: EXOS, VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ROUTER_ID,
                                    **kwargs)

    def ospf_set_metric_table_100g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 100G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_100G,
                                    **kwargs)

    def ospf_set_metric_table_100m(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 100M field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_100M,
                                    **kwargs)

    def ospf_set_metric_table_10g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 10G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_10G,
                                    **kwargs)

    def ospf_set_metric_table_10m(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 10M field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_10M,
                                    **kwargs)

    def ospf_set_metric_table_1g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 1G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_1G,
                                    **kwargs)

    def ospf_set_metric_table_2dot5g(self, device_name, cost='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_2DOT5G,
                                    **kwargs)

    def ospf_set_metric_table_25g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 25G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_25G,
                                    **kwargs)

    def ospf_set_metric_table_40g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 40G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_40G,
                                    **kwargs)

    def ospf_set_metric_table_50g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 50G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_50G,
                                    **kwargs)

    def ospf_set_metric_table_5g(self, device_name, cost='', **kwargs):
        """
        Description: Assigns the given cost value to the 5G field in the ospf metric-table.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cost": cost
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_METRIC_TABLE_5G,
                                    **kwargs)

    def ospf_set_vlan_auth_md5(self, device_name, vlan='', key_id='', key='', **kwargs):
        """
        Description: Assigns md5 authentication to the given vlan, using the supplied key and key-id.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "key": key,
            "key_id": key_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_AUTH_MD5,
                                    **kwargs)

    def ospf_set_vlan_auth_none(self, device_name, vlan='', **kwargs):
        """
        Description: Assigns authentication none to the given vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_AUTH_NONE,
                                    **kwargs)

    def ospf_set_add_vlan(self, device_name, vlan='', area='', **kwargs):
        """
        Description: Adds the provided vlan to ospf.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "area": area,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ADD_VLAN,
                                    **kwargs)

    def ospf_set_del_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Deletes the provided vlan from ospf.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DEL_VLAN,
                                    **kwargs)

    def ospf_enable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Enables the OSPF protocol on an interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE,
                                    **kwargs)

    def ospf_disable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Disables the OSPF protocol on an interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE,
                                    **kwargs)

    def ospf_enable_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables the OSPF protocol on a VLAN.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN,
                                    **kwargs)

    def ospf_disable_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables the OSPF protocol on a VLAN.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def ospf_verify_router_id(self, device_name, router_id='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [router_id]   - The ospf router id (NOTE: This is usually the IP Address).

        Verifies the OSPF Router ID.
        """
        args = {"router_id": router_id,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_ROUTER_ID, True,
                                           "OSPF router id is correctly set to {router_id}.",
                                           "OSPF router id IS NOT set to {router_id}!",
                                           **kwargs)

    def ospf_verify_router_id_removed(self, device_name, router_id='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [router_id]   - The ospf router id (NOTE: This is usually the IP Address).

        Verifies the OSPF Router ID is removed.
        """
        args = {"router_id": router_id,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_ROUTER_ID_IS_REMOVED, True,
                                           "OSPF router id is correctly set to {router_id}.",
                                           "OSPF router id IS NOT set to {router_id}!",
                                           **kwargs)

    def ospf_verify_globally_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.

        Verifies that OSPF is globally enabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_GLOBALLY_ENABLED, True,
                                           "OSPF is globally enabled.",
                                           "OSPF is globally DISABLED!",
                                           **kwargs)

    def ospf_verify_globally_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.

        Verifies that OSPF is globally disabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_GLOBALLY_DISABLED, True,
                                           "OSPF is globally disabled.",
                                           "OSPF is globally ENABLED!",
                                           **kwargs)

    def ospf_verify_interface_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [interface]   - The port interface(s) that OSPF should be enabled on.

        Verifies that OSPF is enabled on the port interface(s).
        This keyword applies to VOSS.
        """
        args = {"interface": interface,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, interface)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_ENABLED_ON_INTERFACE, True,
                                           "OSPF is enabled on interface {interface}.",
                                           "OSPF is DISABLED on interface {interface}!",
                                           **kwargs)

    def ospf_verify_interface_disabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [interface]   - The port interface(s) that OSPF should be disabled on.

        Verifies that OSPF is disabled on the port interface(s).
        This keyword applies to VOSS.
        """
        args = {"interface": interface,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, interface)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_DISABLED_ON_INTERFACE, True,
                                           "OSPF is disabled on interface {interface}.",
                                           "OSPF is ENABLED on interface {interface}!",
                                           **kwargs)

    def ospf_verify_vlan_enabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that OSPF should be enabled on.

        Verifies that OSPF is enabled on a vlan.
        This keyword applies to VOSS.
        """
        args = {"vlan": vlan,
                "voss_oid_index": SnmpUtils().get_voss_vlan_if_index(vlan)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_ENABLED_ON_VLAN, True,
                                           "OSPF is enabled on vlan {vlan}.",
                                           "OSPF is DISABLED on vlan {vlan}!",
                                           **kwargs)

    def ospf_verify_vlan_disabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that OSPF should be disabled on.

        Verifies that OSPF is disabled on a vlan.
        This keyword applies to VOSS.
        """
        args = {"vlan": vlan,
                "voss_oid_index": SnmpUtils().get_voss_vlan_if_index(vlan)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_DISABLED_ON_VLAN, True,
                                           "OSPF is disabled on vlan {vlan}.",
                                           "OSPF is ENABLED on vlan {vlan}!",
                                           **kwargs)

    def ospf_verify_neighbor_exists(self, device_name, neighbor_id='', neighbor_ip='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor_id] - The Router ID of the OSPF neighbor.
        [neighbor_ip] - The IP Address of the OSPF Neighbor interface.

        Verifies that the given OSPF neighbor IP exists in the table.
        """
        args = {"neighbor_id": neighbor_id,
                "neighbor_ip": neighbor_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBOR,
                                           self.parse_const.VERIFY_OSPF_NEIGHBOR_EXISTS, True,
                                           "OSPF neighbor {neighbor_ip} is present.",
                                           "OSPF neighbor {neighbor_ip} is NOT present!",
                                           **kwargs)

    def ospf_verify_neighbor_does_not_exist(self, device_name, neighbor_id='', neighbor_ip='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor_id] - The Router ID of the OSPF neighbor.
        [neighbor_ip] - The IP Address of the OSPF Neighbor interface.

        Verifies that the given OSPF neighbor IP exists in the table.
        """
        args = {"neighbor_id": neighbor_id,
                "neighbor_ip": neighbor_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBOR,
                                           self.parse_const.VERIFY_OSPF_NEIGHBOR_EXISTS, False,
                                           "OSPF neighbor {neighbor_ip} is not present.",
                                           "OSPF neighbor {neighbor_ip} IS present!",
                                           **kwargs)

    def ospf_verify_neighbor_adjacency_full(self, device_name, neighbor_id='', neighbor_ip='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor_id] - The Router ID of the OSPF neighbor.
        [neighbor_ip] - The IP Address of the OSPF Neighbor interface.

        Verifies that the OSPF neighbor adjacency, for the given IP, is FULL.
        """
        args = {"neighbor_id": neighbor_id,
                "neighbor_ip": neighbor_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBOR,
                                           self.parse_const.VERIFY_OSPF_NEIGHBOR_ADJACENCY_FULL, True,
                                           "OSPF neighbor {neighbor_ip} adjacency is FULL.",
                                           "OSPF neighbor {neighbor_ip} adjacency is NOT FULL!",
                                           **kwargs)

    def ospf_verify_vlan_auth_md5(self, device_name, vlan='', keyid='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan interface to query.
        [keyid]       - The KeyID that exists on the vlan (ex. '60').

        Verifies the Authentication: MD5 and key id is present on the vlan interface.
        This keyword applies to EXOS.
        """
        args = {"vlan": vlan,
                "keyid": keyid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_INTERFACE_AUTHENTICATION, True,
                                           "OSPF interface {vlan} uses Authentication MD5 and Key Id {keyid}.",
                                           "OSPF interface {vlan} does NOT use Authentication MD5 and Key Id {keyid}!",
                                           **kwargs)

    def ospf_verify_vlan_auth_none(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan interface to query.

        Verifies Authentication: NONE is present on the vlan interface.
        This keyword applies to EXOS.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_INTERFACE_AUTHENTICATION_NONE, True,
                                           "OSPF interface {vlan} uses Authentication: NONE.",
                                           "OSPF interface {vlan} does NOT use Authentication: NONE!",
                                           **kwargs)

    def ospf_verify_metric_table_100g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 100G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_100G, True,
                                           "OSPF metric-table 100G cost is set to {cost}.",
                                           "OSPF metric-table 100G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_100m(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 100M field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_100M, True,
                                           "OSPF metric-table 100M cost is set to {cost}.",
                                           "OSPF metric-table 100M cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_10g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 10G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_10G, True,
                                           "OSPF metric-table 10G cost is set to {cost}.",
                                           "OSPF metric-table 10G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_10m(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 10M field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_10M, True,
                                           "OSPF metric-table 10M cost is set to {cost}.",
                                           "OSPF metric-table 10M cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_1g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 1G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_1G, True,
                                           "OSPF metric-table 1G cost is set to {cost}.",
                                           "OSPF metric-table 1G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_2dot5g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 2.5G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_2_5G, True,
                                           "OSPF metric-table 2.5G cost is set to {cost}.",
                                           "OSPF metric-table 2.5G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_25g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 25G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_25G, True,
                                           "OSPF metric-table 25G cost is set to {cost}.",
                                           "OSPF metric-table 25G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_40g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 40G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_40G, True,
                                           "OSPF metric-table 40G cost is set to {cost}.",
                                           "OSPF metric-table 40G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_50g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 50G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_50G, True,
                                           "OSPF metric-table 50G cost is set to {cost}.",
                                           "OSPF metric-table 50G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_metric_table_5g(self, device_name, cost='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [cost]        - The cost value that should be listed in the ospf metric-table.

        Verifies the 5G field in the ospf metric-table has the given cost value.
        This keyword applies to EXOS.
        """
        args = {"cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_OSPF_METRIC_TABLE_5G, True,
                                           "OSPF metric-table 5G cost is set to {cost}.",
                                           "OSPF metric-table 5G cost is NOT set to {cost}!",
                                           **kwargs)

    def ospf_verify_enabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan to ensure ospf is enabled on.

        Verifies ospf is enabled on the provided vlan.
        This keyword applies to EXOS.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_ENABLED_ON_VLAN, True,
                                           "OSPF is enabled on vlan {vlan}.",
                                           "OSPF is NOT enabled on vlan {vlan}.!",
                                           **kwargs)

    def ospf_verify_disabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan to ensure ospf is disabled on.

        Verifies ospf is disabled on the provided vlan.
        This keyword applies to EXOS.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_INTERFACE,
                                           self.parse_const.VERIFY_OSPF_DISABLED_ON_VLAN, True,
                                           "OSPF is disabled on vlan {vlan}.",
                                           "OSPF is NOT disabled on vlan {vlan}.!",
                                           **kwargs)
