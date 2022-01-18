"""
Keyword class for all spbm cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SpbmConstants import \
    SpbmConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SpbmConstants import \
    SpbmConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NetworkElementSpbmGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSpbmGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "spbm"

    def spbm_set_ethertype(self, device_name, ethertype='', **kwargs):
        """
        Description: Configures the SPBM ethertype.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ethertype": ethertype
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ETHERTYPE,
                                    **kwargs)

    def spbm_clear_ethertype(self, device_name, **kwargs):
        """
        Description: Configures the SPBM ethertype to the default value of 0x8100.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ETHERTYPE,
                                    **kwargs)

    def spbm_enable_global(self, device_name, **kwargs):
        """
        Description: Enables the PLSB global flag.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def spbm_disable_global(self, device_name, **kwargs):
        """
        Description: Disables the PLSB global flag.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def spbm_enable_ip_shortcut(self, device_name, spbm_id='', **kwargs):
        """
        Description: Enables ISIS PLSB IP shortcut.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IP_SHORTCUT,
                                    **kwargs)

    def spbm_disable_ip_shortcut(self, device_name, spbm_id='', **kwargs):
        """
        Description: Disables ISIS PLSB IP shortcut.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IP_SHORTCUT,
                                    **kwargs)

    def spbm_enable_ipv6_shortcut(self, device_name, spbm_id='', **kwargs):
        """
        Description: Enables ISIS PLSB IPv6 shortcut.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPV6_SHORTCUT,
                                    **kwargs)

    def spbm_disable_ipv6_shortcut(self, device_name, spbm_id='', **kwargs):
        """
        Description: Disables ISIS PLSB IPv6 shortcut.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPV6_SHORTCUT,
                                    **kwargs)

    def spbm_enable_lsdb_trap(self, device_name, spbm_id='', **kwargs):
        """
        Description: Enables the ISIS PLSB LSDB update trap on the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LSDB_TRAP,
                                    **kwargs)

    def spbm_disable_lsdb_trap(self, device_name, spbm_id='', **kwargs):
        """
        Description: Disables the ISIS PLSB LSDB update trap on the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LSDB_TRAP,
                                    **kwargs)

    def spbm_set_isis_instance_id(self, device_name, spbm_id='', **kwargs):
        """
        Description: Configures a PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_clear_isis_instance_id(self, device_name, spbm_id='', **kwargs):
        """
        Description: Removes a PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_set_isis_nickname(self, device_name, spbm_id='', nickname='', **kwargs):
        """
        Description: Configures a PLSB instance nickname.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "nickname": nickname,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_NICKNAME,
                                    **kwargs)

    def spbm_clear_isis_nickname(self, device_name, nickname='', spbm_id='', **kwargs):
        """
        Description: Sets the nickname which is an octet string consisting 3 octets to all zeros.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "nickname": nickname,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_NICKNAME,
                                    **kwargs)

    def spbm_set_isis_bvid(self, device_name, spbm_id='', pri_vlan='', sec_vlan='', **kwargs):
        """
        Description: Configures the PLSB ISIS vlans for the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "pri_vlan": pri_vlan,
            "sec_vlan": sec_vlan,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_BVID,
                                    **kwargs)

    def spbm_clear_isis_bvid(self, device_name, spbm_id='', pri_vlan='', sec_vlan='', **kwargs):
        """
        Description: Configures the PLSB ISIS vlans for the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "pri_vlan": pri_vlan,
            "sec_vlan": sec_vlan,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_BVID,
                                    **kwargs)

    def spbm_enable_isis_multicast(self, device_name, spbm_id='', **kwargs):
        """
        Description: Sets ISIS PLSB Multicast to enable.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ISIS_MULTICAST,
                                    **kwargs)

    def spbm_disable_isis_multicast(self, device_name, spbm_id='', **kwargs):
        """
        Description: Sets ISIS PLSB Multicast to disable.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ISIS_MULTICAST,
                                    **kwargs)

    def spbm_set_isis_multicast_fwd_cache_timeout(self, device_name, spbm_id='', timeout='', **kwargs):
        """
        Description: Configures the multicast forward cache timeout.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_MULTICAST_FWD_CACHE_TIMEOUT,
                                    **kwargs)

    def spbm_clear_isis_multicast_fwd_cache_timeout(self, device_name, spbm_id='', **kwargs):
        """
        Description: Configures the multicast forward cache timeout to the default value.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_MULTICAST_FWD_CACHE_TIMEOUT,
                                    **kwargs)

    def spbm_set_isis_smlt_virtual_bmac(self, device_name, spbm_id='', bmac='', **kwargs):
        """
        Description: Configures the ISIS PLSB SMLT virtual MAC for the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "bmac": bmac,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_SMLT_VIRTUAL_BMAC,
                                    **kwargs)

    def spbm_clear_isis_smlt_virtual_bmac(self, device_name, bmac='', spbm_id='', **kwargs):
        """
        Description: Removes the ISIS PLSB SMLT virtual MAC for the PLSB instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "bmac": bmac,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_SMLT_VIRTUAL_BMAC,
                                    **kwargs)

    def spbm_set_isis_smlt_peer_system_id(self, device_name, spbm_id='', peer_id='', **kwargs):
        """
        Description: Configures the ISIS PLSB SMLT Peer's system-id for the SPBM instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "peer_id": peer_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_SMLT_PEER_SYSTEM_ID,
                                    **kwargs)

    def spbm_clear_isis_smlt_peer_system_id(self, device_name, peer_id='', spbm_id='', **kwargs):
        """
        Description: Removes the ISIS PLSB SMLT Peer's system-id for the SPBM instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "peer_id": peer_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_SMLT_PEER_SYSTEM_ID,
                                    **kwargs)

    def spbm_set_port_isis_instance_id(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Creates an ISIS SPBM instance on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_clear_port_isis_instance_id(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Removes an ISIS SPBM instance from a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_set_mlt_isis_instance_id(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Creates an ISIS SPBM instance on an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_clear_mlt_isis_instance_id(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Removes an ISIS SPBM instance on an MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MLT_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_set_port_isis_interface_type_broadcast(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a port to a broadcast interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ISIS_INTERFACE_TYPE_BROADCAST,
                                    **kwargs)

    def spbm_set_port_isis_interface_type_p2p(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a port to a point to point interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ISIS_INTERFACE_TYPE_P2P,
                                    **kwargs)

    def spbm_clear_port_isis_interface_type(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a port to default - point to point interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_ISIS_INTERFACE_TYPE,
                                    **kwargs)

    def spbm_set_mlt_isis_interface_type_broadcast(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on an MLT to a broadcast interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ISIS_INTERFACE_TYPE_BROADCAST,
                                    **kwargs)

    def spbm_set_mlt_isis_interface_type_p2p(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on an MLT to a point to point interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ISIS_INTERFACE_TYPE_P2P,
                                    **kwargs)

    def spbm_clear_mlt_isis_interface_type(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on an MLT to interface type to the default value of point to
                     point.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MLT_ISIS_INTERFACE_TYPE,
                                    **kwargs)

    def spbm_set_port_isis_l1_metric(self, device_name, port='', spbm_id='', metric='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a port to a desired L1 metric value.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "metric": metric,
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_clear_port_isis_l1_metric(self, device_name, port='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a port to the default L1 metric value of 10.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_set_mlt_isis_l1_metric(self, device_name, mlt_id='', spbm_id='', metric='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on an MLT to the desired L1 metric value.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "metric": metric,
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_clear_mlt_isis_l1_metric(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on an MLT to the default metric value of 10.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MLT_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_set_logical_interface_isis_instance_id(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Creates an ISIS SPBM instance on a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_clear_logical_interface_isis_instance_id(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Removes an ISIS SPBM instance from a logical interface.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOGICAL_INTERFACE_ISIS_INSTANCE_ID,
                                    **kwargs)

    def spbm_set_logical_interface_isis_interface_type_broadcast(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a logical interface to a broadcast interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE_BROADCAST,
                                    **kwargs)

    def spbm_set_logical_interface_isis_interface_type_p2p(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a logical interface to a point to point interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE_P2P,
                                    **kwargs)

    def spbm_clear_logical_interface_isis_interface_type(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a logical interface to default - point to point interface type.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE,
                                    **kwargs)

    def spbm_set_logical_interface_isis_l1_metric(self, device_name, isis_id='', spbm_id='', metric='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a logical interface to a desired L1 metric value.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "metric": metric,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LOGICAL_INTERFACE_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_clear_logical_interface_isis_l1_metric(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Description: Configures an ISIS SPBM instance on a logical interface to the default L1 metric value of 1000.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "isis_id": isis_id,
            "spbm_id": spbm_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOGICAL_INTERFACE_ISIS_L1_METRIC,
                                    **kwargs)

    def spbm_set_virtual_ist_peer_ip(self, device_name, ip='', vlan='', **kwargs):
        """
        Description: Configures a virtual-ist peer ip address on a vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VIRTUAL_IST_PEER_IP,
                                    **kwargs)

    def spbm_clear_virtual_ist_peer_ip(self, device_name, **kwargs):
        """
        Description: Removes a virtual-ist peer ip address.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_VIRTUAL_IST_PEER_IP,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def spbm_verify_ethertype(self, device_name, ethertype='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ethertype]   - The ethertype to be used for SPBM (Acceptable values: 0x8100  0x88a8)

        Verifies the SPBM ethertype.
        """
        args = {"ethertype": ethertype,
                "integer_ethertype": StringUtils().hex_str_to_int(ethertype)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_SPBM_ETHERTYPE, True,
                                           "SPBM ethertype is {ethertype}.",
                                           "SPBM ethertype is NOT {ethertype}!",
                                           **kwargs)

    def spbm_verify_globally_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies SPBM is globally enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_SPBM_ENABLED, True,
                                           "SPBM is globally enabled.",
                                           "SPBM is not globally enabled!",
                                           **kwargs)

    def spbm_verify_globally_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies SPBM is globally disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_SPBM_ENABLED, False,
                                           "SPBM is globally disabled.",
                                           "SPBM is not globally disabled!",
                                           **kwargs)

    def spbm_verify_ip_shortcut_enabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM IP shortcut is enabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_IP_ENABLED, True,
                                           "SPBM {spbm_id} IP shortcut is enabled.",
                                           "SPBM {spbm_id} IP shortcut is NOT enabled!",
                                           **kwargs)

    def spbm_verify_ip_shortcut_disabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM IP shortcut is disabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_IP_ENABLED, False,
                                           "SPBM {spbm_id} IP shortcut is disabled.",
                                           "SPBM {spbm_id} IP shortcut is NOT disabled!",
                                           **kwargs)

    def spbm_verify_ipv6_shortcut_enabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM IP V6 shortcut is enabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_IPV6_ENABLED, True,
                                           "SPBM {spbm_id} IPV6 shortcut is enabled.",
                                           "SPBM {spbm_id} IPV6 shortcut is NOT enabled!",
                                           **kwargs)

    def spbm_verify_ipv6_shortcut_disabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM IP V6 shortcut is disabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_IPV6_ENABLED, False,
                                           "SPBM {spbm_id} IPV6 shortcut is disabled.",
                                           "SPBM {spbm_id} IPV6 shortcut is NOT disabled!",
                                           **kwargs)

    def spbm_verify_instance_exists(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM Id exists.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_INSTANCE_ID, True,
                                           "SPBM {spbm_id} exists.",
                                           "SPBM {spbm_id} does NOT exist!",
                                           **kwargs)

    def spbm_verify_instance_does_not_exist(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies the SPBM Id does not exist.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_INSTANCE_ID, False,
                                           "SPBM {spbm_id} does not exist.",
                                           "SPBM {spbm_id} exists!",
                                           **kwargs)

    def spbm_verify_nickname(self, device_name, spbm_id='', nickname='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.
        [nickname]    - Configures the PLSB node's nickname which is used to calculate ISID multicast mac address.
                        The nickname is an octet string consisting 3 octets.  Example: 0.00.42
        Verifies a PLSB instance nickname.
        """
        args = {"spbm_id": spbm_id,
                "nickname": nickname}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_NICK_NAME, True,
                                           "SPBM {spbm_id} nickname is {nickname}.",
                                           "SPBM {spbm_id} nickname is NOT {nickname}!",
                                           **kwargs)

    def spbm_verify_vlan_exists(self, device_name, spbm_id='', bvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.
        [bvid]        - PLSB ISIS vlan

        Verifies a PLSB instance VLAN ID.
        """
        args = {"spbm_id": spbm_id,
                "bvid": bvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_BVID, True,
                                           "SPBM {spbm_id} b-vid is {bvid}.",
                                           "SPBM {spbm_id} b-vid is NOT {bvid}!",
                                           **kwargs)

    def spbm_verify_vlan_does_not_exist(self, device_name, spbm_id='', bvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.
        [bvid]        - PLSB ISIS vlan

        Verifies a PLSB instance VLAN ID does not exist.
        """
        args = {"spbm_id": spbm_id,
                "bvid": bvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_BVID, False,
                                           "SPBM {spbm_id} b-vid is NOT {bvid}.",
                                           "SPBM {spbm_id} b-vid IS {bvid}!",
                                           **kwargs)

    def spbm_verify_multicast_enabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies SPBM multicast is enabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_MULTICAST_ENABLED, True,
                                           "SPBM {spbm_id} multicast is enabled.",
                                           "SPBM {spbm_id} multicast is NOT enabled!",
                                           **kwargs)

    def spbm_verify_multicast_disabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies SPBM multicast is disabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_MULTICAST_ENABLED, False,
                                           "SPBM {spbm_id} multicast is disabled.",
                                           "SPBM {spbm_id} multicast is NOT disabled!",
                                           **kwargs)

    def spbm_verify_lsdb_trap_enabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies SPBM LSDB trap is enabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_LSDB_TRAP_ENABLED, True,
                                           "SPBM {spbm_id} trap is enabled.",
                                           "SPBM {spbm_id} trap is NOT enabled!",
                                           **kwargs)

    def spbm_verify_lsdb_trap_disabled(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.

        Verifies SPBM LSDB trap is disabled.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_SPBM_LSDB_TRAP_ENABLED, False,
                                           "SPBM {spbm_id} trap is disabled.",
                                           "SPBM {spbm_id} trap is enabled!",
                                           **kwargs)

    def spbm_verify_smlt_bmac(self, device_name, spbm_id='', bmac='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The PLSB instance ID.
        [bmac]        - The ISIS PLSB SMLT virtual MAC for the SPBM instance in the form of xx:xx:xx:xx:xx:xx

        Verifies the ISIS PLSB SMLT virtual MAC for the PLSB instance.
        """
        args = {"spbm_id": spbm_id,
                "bmac": bmac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_SMLT_VIRTUAL_BMAC, True,
                                           "SPBM {spbm_id} virtual BMAC is {bmac}.",
                                           "SPBM {spbm_id} virtual BMAC NOT {bmac}!",
                                           **kwargs)

    def spbm_verify_smlt_peer_system_id(self, device_name, spbm_id='', peer_sys_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [spbm_id]       - The PLSB instance ID.
        [peer_sys_id]   - The ISIS Peer SMLT system Id for the SPBM instance in the form of xx:xx:xx:xx:xx:xx

        Verifies the ISIS Peer SMLT system Id for the PLSB instance.
        """
        args = {"spbm_id": spbm_id,
                "peer_sys_id": peer_sys_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.VERIFY_ISIS_SPBM_SMLT_PEER_SYSTEM_ID, True,
                                           "SPBM {spbm_id} SMLT Peer system ID is {peer_sys_id}.",
                                           "SPBM {spbm_id} virtual BMAC NOT {peer_sys_id}!",
                                           **kwargs)

    def spbm_verify_split_beb_primary(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [spbm_id]       - The PLSB instance ID.

        Verifies the ISIS SPBM Peer SMLT split BEB as primary for the PLSB instance.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.CHECK_ISIS_SPBM_SMLT_SPLIT_BEB_PRIMARY, True,
                                           "SPBM {spbm_id} SMLT split BEB is primary.",
                                           "SPBM {spbm_id} SMLT split BEB is NOT primary!",
                                           **kwargs)

    def spbm_verify_split_beb_secondary(self, device_name, spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [spbm_id]       - The PLSB instance ID.

        Verifies the ISIS SPBM Peer SMLT split BEB as secondary for the PLSB instance.
        """
        args = {"spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INFO,
                                           self.parse_const.CHECK_ISIS_SPBM_SMLT_SPLIT_BEB_SECONDARY, True,
                                           "SPBM {spbm_id} SMLT split BEB is secondary.",
                                           "SPBM {spbm_id} SMLT split BEB is NOT secondary!",
                                           **kwargs)

    def spbm_verify_isis_instance_exists_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance exists on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_PORT, True,
                                           "SPBM {spbm_id} instance exists on port {port}.",
                                           "SPBM {spbm_id} instance does not exist on port {port}!",
                                           **kwargs)

    def spbm_verify_isis_instance_does_not_exist_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance does not exist on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_PORT, False,
                                           "SPBM {spbm_id} instance does not exist on port {port}.",
                                           "SPBM {spbm_id} instance exists on port {port}!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_enabled_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively up on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_PORT, True,
                                           "SPBM {spbm_id} instance on port {port} is administratively UP.",
                                           "SPBM {spbm_id} instance on port {port} is administratively DOWN!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_disabled_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively down on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_PORT, False,
                                           "SPBM {spbm_id} instance on port {port} is administratively DOWN.",
                                           "SPBM {spbm_id} instance on port {port} is administratively UP!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_enabled_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally up on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_PORT, True,
                                           "SPBM {spbm_id} instance on port {port} is operationally UP.",
                                           "SPBM {spbm_id} instance on port {port} is operationally DOWN!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_disabled_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port on which to create an ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally down on a port.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_PORT, False,
                                           "SPBM {spbm_id} instance on port {port} is operationally DOWN.",
                                           "SPBM {spbm_id} instance on port {port} is operationally UP!",
                                           **kwargs)

    def spbm_verify_isis_total_adjacencies_on_port(self, device_name, port='', spbm_id='', total_adj='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [total_adj]   - The total number of IS-IS adjacencies on the port.

        Verifies the total number of ISIS SPBM  adjacencies on the port.
        """
        args = {"port": port,
                "spbm_id": spbm_id,
                "total_adj": total_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADJACENCIES_ON_PORT, True,
                                           "SPBM {spbm_id} total adjancencies on port {port} is {total_adj}.",
                                           "SPBM {spbm_id} total adjancencies on port {port} is NOT {total_adj}!",
                                           **kwargs)

    def spbm_verify_isis_up_adjacencies_on_port(self, device_name, port='', spbm_id='', up_adj='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [up_adj]      - The number of IS-IS adjacencies on the port that are up.

        Verifies the number of ISIS SPBM  adjacencies on the port that are up.
        """
        args = {"port": port,
                "spbm_id": spbm_id,
                "up_adj": up_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_PORT, True,
                                           "SPBM {spbm_id} adjacencies that are up on port {port} is {up_adj}.",
                                           "SPBM {spbm_id} adjacencies that are up on port {port} is "
                                           "NOT {up_adj}!",
                                           **kwargs)

    def spbm_verify_isis_l1_metric_on_port(self, device_name, port='', spbm_id='', l1_metric='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [l1_metric]   - The metric value of the circuit at L1.

        Verifies the metric value of the circuit at L1.
        """
        args = {"port": port,
                "spbm_id": spbm_id,
                "l1_metric": l1_metric}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_L1_METRIC_ON_PORT, True,
                                           "SPBM {spbm_id} L1 metric on port {port} is {l1_metric}.",
                                           "SPBM {spbm_id} L1 metric on port {port} is NOT {l1_metric}!",
                                           **kwargs)

    def spbm_verify_isis_type_broadcast_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is broadcast.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_PORT, True,
                                           "SPBM {spbm_id} circuit type is broadcast on port {port}.",
                                           "SPBM {spbm_id} circuit type is not broadcast on port {port}!",
                                           **kwargs)

    def spbm_verify_isis_type_point_to_point_on_port(self, device_name, port='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is point to point.
        """
        args = {"port": port,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_PORT, True,
                                           "SPBM {spbm_id} circuit type is point to point on port {port}.",
                                           "SPBM {spbm_id} circuit type is not point to point on port {port}!",
                                           **kwargs)

    def spbm_verify_isis_instance_exists_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance exists on an MLT.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_MLT, True,
                                           "SPBM {spbm_id} instance exists on MLT {mlt_id}.",
                                           "SPBM {spbm_id} instance does not exist on MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_instance_does_not_exist_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance does not exist on an MLT.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_MLT, False,
                                           "SPBM {spbm_id} instance does not exist on MLT {mlt_id}.",
                                           "SPBM {spbm_id} instance exists on MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_enabled_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively up on a port.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_MLT, True,
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is administratively UP.",
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is administratively DOWN!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_disabled_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively down on a port.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_MLT, False,
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is administratively DOWN.",
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is administratively UP!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_enabled_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally up on a port.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_MLT, True,
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is operationally UP.",
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is operationally DOWN!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_disabled_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally down on a port.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_MLT, False,
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is operationally DOWN.",
                                           "SPBM {spbm_id} instance on MLT {mlt_id} is operationally UP!",
                                           **kwargs)

    def spbm_verify_isis_total_adjacencies_on_mlt(self, device_name, mlt_id='', spbm_id='', total_adj='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [total_adj]   - The total number of IS-IS adjacencies on the port.

        Verifies the total number of ISIS SPBM  adjacencies on the port.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id,
                "total_adj": total_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADJACENCIES_ON_MLT, True,
                                           "SPBM {spbm_id} total adjancencies on MLT {mlt_id} is {total_adj}.",
                                           "SPBM {spbm_id} total adjancencies on MLT"
                                           " {mlt_id} is NOT {total_adj}!",
                                           **kwargs)

    def spbm_verify_isis_up_adjacencies_on_mlt(self, device_name, mlt_id='', spbm_id='', up_adj='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [up_adj]      - The number of IS-IS adjacencies on the port that are up.

        Verifies the number of ISIS SPBM  adjacencies on the port that are up.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id,
                "up_adj": up_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_MLT, True,
                                           "SPBM {spbm_id} adjacencies that are up on MLT {mlt_id} is {up_adj}.",
                                           "SPBM {spbm_id} adjacencies that are up on MLT"
                                           " {mlt_id} is NOT {up_adj}!",
                                           **kwargs)

    def spbm_verify_isis_l1_metric_on_mlt(self, device_name, mlt_id='', spbm_id='', l1_metric='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [l1_metric]   - The metric value of the circuit at L1.

        Verifies the metric value of the circuit at L1.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id,
                "l1_metric": l1_metric}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_L1_METRIC_ON_MLT, True,
                                           "SPBM {spbm_id} L1 metric on MLT {mlt_id} is {l1_metric}.",
                                           "SPBM {spbm_id} L1 metric on MLT {mlt_id} is NOT {l1_metric}!",
                                           **kwargs)

    def spbm_verify_isis_type_broadcast_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is broadcast.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_MLT, True,
                                           "SPBM {spbm_id} circuit type is broadcast on MLT {mlt_id}.",
                                           "SPBM {spbm_id} circuit type is not broadcast on MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_type_point_to_point_on_mlt(self, device_name, mlt_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The MLT ID of the ISIS SPBM instance.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is point to point.
        """
        args = {"mlt_id": mlt_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_MLT, True,
                                           "SPBM {spbm_id} circuit type is point to point on MLT {mlt_id}.",
                                           "SPBM {spbm_id} circuit type is not point to point on MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_instance_exists_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance exists on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_LOGICAL_INTERFACE, True,
                                           "SPBM {spbm_id} instance exists on logical interface {isis_id}.",
                                           "SPBM {spbm_id} instance does not exist on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def spbm_verify_isis_instance_does_not_exist_on_logical_interface(self, device_name, isis_id='', spbm_id='',
                                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance does not exist on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_INSTANCE_ON_LOGICAL_INTERFACE, False,
                                           "SPBM {spbm_id} instance exists on logical interface {isis_id}.",
                                           "SPBM {spbm_id} instance does not exist on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_enabled_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively up on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_LOGICAL_INTERFACE,
                                           True,
                                           "SPBM {spbm_id} instance on"
                                           " logical interface {isis_id} is administratively UP.",
                                           "SPBM {spbm_id} instance on"
                                           " logical interface {isis_id} is administratively DOWN!",
                                           **kwargs)

    def spbm_verify_isis_admin_status_disabled_on_logical_interface(self, device_name, isis_id='', spbm_id='',
                                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is administratively down on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_LOGICAL_INTERFACE,
                                           False,
                                           "SPBM {spbm_id} instance on logical interface"
                                           " (isis_id} is administratively DOWN.",
                                           "SPBM {spbm_id} instance on port logical interface"
                                           " {isis_id} is administratively UP!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_enabled_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally up on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_LOGICAL_INTERFACE,
                                           True,
                                           "SPBM {spbm_id} instance on logical interface"
                                           " (isis_id} is operationally UP.",
                                           "SPBM {spbm_id} instance on logical interface"
                                           " (isis_id} is operationally DOWN!",
                                           **kwargs)

    def spbm_verify_isis_oper_status_disabled_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies an ISIS SPBM instance is operationally down on a logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_OPER_STATUS_ON_LOGICAL_INTERFACE,
                                           False,
                                           "SPBM {spbm_id} instance on logical interface"
                                           " {isis_id} is operationally DOWN.",
                                           "SPBM {spbm_id} instance on logical interface"
                                           " {isis_id} is operationally UP!",
                                           **kwargs)

    def spbm_verify_isis_total_adjacencies_on_logical_interface(self, device_name, isis_id='', spbm_id='', total_adj='',
                                                                **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [total_adj]   - The total number of IS-IS adjacencies on the logical interface.

        Verifies the total number of ISIS SPBM  adjacencies on the logical interface.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id,
                "total_adj": total_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_ADJACENCIES_ON_LOGICAL_INTERFACE,
                                           True,
                                           "SPBM {spbm_id} total adjancencies on logical interface {isis_id}"
                                           " is {total_adj}.",
                                           "SPBM {spbm_id} total adjancencies on logical interface {isis_id}"
                                           " is NOT {total_adj}!",
                                           **kwargs)

    def spbm_verify_isis_up_adjacencies_on_logical_interface(self, device_name, isis_id='', spbm_id='', up_adj='',
                                                             **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [up_adj]      - The number of IS-IS adjacencies on the logical interface that are up.

        Verifies the number of ISIS SPBM  adjacencies on the logical interface that are up.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id,
                "up_adj": up_adj}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_LOGICAL_INTERFACE,
                                           True,
                                           "SPBM {spbm_id} adjacencies that are up on logical interface"
                                           " {isis_id} is {up_adj}.",
                                           "SPBM {spbm_id} adjacencies that are up on logical interface"
                                           " {isis_id} is NOT {up_adj}!",
                                           **kwargs)

    def spbm_verify_isis_l1_metric_on_logical_interface(self, device_name, isis_id='', spbm_id='', l1_metric='',
                                                        **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.
        [l1_metric]   - The metric value of the circuit at L1.

        Verifies the metric value of the circuit at L1.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id,
                "l1_metric": l1_metric}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_L1_METRIC_ON_LOGICAL_INTERFACE, True,
                                           "SPBM {spbm_id} L1 metric on logical interface"
                                           " {isis_id} is {l1_metric}.",
                                           "SPBM {spbm_id} L1 metric on logical interface"
                                           " {isis_id} is NOT {l1_metric}!",
                                           **kwargs)

    def spbm_verify_isis_type_broadcast_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is broadcast.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_LOGICAL_INTERFACE,
                                           True,
                                           "SPBM {spbm_id} circuit type is broadcast on"
                                           " logical interface {isis_id}.",
                                           "SPBM {spbm_id} circuit type is not broadcast on"
                                           " logical interface {isis_id}!",
                                           **kwargs)

    def spbm_verify_isis_type_point_to_point_on_logical_interface(self, device_name, isis_id='', spbm_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [isis_id]     - The IS-IS logical interface identifier index.
        [spbm_id]     - The numeric instance identifier of the SPBM.

        Verifies the ISIS circuit type is point to point.
        """
        args = {"isis_id": isis_id,
                "spbm_id": spbm_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_INTERFACE,
                                           self.parse_const.
                                           CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_LOGICAL_INTERFACE, True,
                                           "SPBM {spbm_id} circuit type is point to point"
                                           " on logical interface {isis_id}.",
                                           "SPBM {spbm_id} circuit type is not point to point"
                                           " on logical interface {isis_id}!",
                                           **kwargs)

    def spbm_verify_isis_unicast_fib_host_name(self, device_name, sysid='', bvlan='', dmac='', hostname='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [hostname]    - The Host Name of the node where unicast FIB entry comes from.

        Verifies the Host Name of the node where unicast FIB entry comes from.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "hostname": hostname}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_UNICAST_FIB_HOST_NAME, True,
                                           "SPBM host name {hostname} exists on the System ID {sysid},"
                                           " BVLAN {bvlan}, Destination Address {da} entry.",
                                           "SPBM host name {hostname} does NOT exist on the System ID {sysid},"
                                           " BVLAN {bvlan}, Destination Address {da} entry!",
                                           **kwargs)

    def spbm_verify_isis_unicast_fib_cost(self, device_name, sysid='', bvlan='', dmac='', cost='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [cost]        - The unicast FIB cost.

        Verifies the unicast FIB cost to the node of the unicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "cost": cost}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_UNICAST_FIB_COST, True,
                                           "SPBM cost to System ID {sysid}, via BVLAN {bvlan},"
                                           " Destination Address {da} entry is {cost}.",
                                           "SPBM cost to System ID {sysid}, via BVLAN {bvlan},"
                                           " Destination Address {da} entry is NOT {cost}!",
                                           **kwargs)

    def spbm_verify_isis_unicast_fib_outgoing_port(self, device_name, sysid='', bvlan='', dmac='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [port]        - The outgoing interface to the Destination Mac Address of the unicast FIB entry.

        Verifies the outgoing interface to the node of the unicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_UNICAST_FIB_OUTGOING_INTERFACE, True,
                                           "SPBM outgoing interface to System ID {sysid}, via BVLAN {bvlan},"
                                           " Destination Address {da} entry is port {port}.",
                                           "SPBM outgoing interface to System ID {sysid}, via BVLAN {bvlan},"
                                           " Destination Address {da} entry is NOT port {port}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fwd_cache_timeout(self, device_name, spbm_id='', timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_id]     - The SPBM instance ID.
        [timeout]     - The Multicast Fwd Cache Timeout in seconds. Values: 10..86400  Default: 210

        Verifies the the multicast forward cache timeout.
        """
        args = {"spbm_id": spbm_id,
                "timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FWD_CACHE_TIMEOUT, True,
                                           "ISIS SPBM multicast forward cache timeout is {timeout}.",
                                           "ISIS SPBM multicast forward cache timeout is NOT {timeout}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_isid(self, device_name, sysid='', bvlan='', dmac='', isid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.

        Verifies the ISIS of the multicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_ISID, True,
                                           "SPBM multicast FIB I-SID to Destination Address {da}"
                                           " via System ID {sysid}, BVLAN {bvlan} is I-SID {isid}.",
                                           "SPBM multicast FIB I-SID to Destination Address {da}"
                                           " via System ID {sysid}, BVLAN {bvlan} is NOT I-SID {isid}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_host_name(self, device_name, sysid='', bvlan='', dmac='', isid='', hostname='',
                                                 **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [hostname]    - The host name of the node where multicast FIB entry comes from.

        Verifies the host name of the node where multicast FIB entry comes from.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "hostname": hostname}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_HOST_NAME, True,
                                           "SPBM multicast FIB Host-Name to Destination Address {da} via System "
                                           "ID {sysid}, I-SID {isid}, and BVLAN {bvlan} is {hostname}.",
                                           "SPBM multicast FIB Host-Name to Destination Address {da} via System "
                                           "ID {sysid}, I-SID {isid}, and BVLAN {bvlan} is NOT {hostname}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_outbound_port(self, device_name, sysid='', bvlan='', dmac='', isid='', port='',
                                                     **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [port]        - The outgoing port interface.

        Verifies the outgoing port interface to the node of the multicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_OUT_PORTS, True,
                                           "SPBM multicast FIB Outgoing Interface(s) to Destination Address {da} "
                                           "via System ID {sysid}, I-SID {isid} and BVLAN {bvlan} is port(s) "
                                           "{port}.",
                                           "SPBM multicast FIB Outgoing Interface(s) to Destination Address {da} "
                                           "via System ID {sysid}, I-SID {isid} and BVLAN {bvlan} is NOT port(s) "
                                           "{port}!", **kwargs)

    def spbm_verify_isis_multicast_fib_outbound_mlt(self, device_name, sysid='', bvlan='', dmac='', isid='', mlt_id='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [mlt_id]      - The outgoing MLT ID interface.

        Verifies the outgoing MLT interface to the node of the multicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "mlt_id": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_OUT_MLTS, True,
                                           "SPBM multicast FIB MLT to Destination Address {da} via System ID"
                                           " {sysid}, BVLAN {bvlan} is MLT {mlt_id}.",
                                           "SPBM multicast FIB MLT to Destination Address {da} via System ID"
                                           " {sysid}, BVLAN {bvlan} is NOT MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_inbound_port(self, device_name, sysid='', bvlan='', dmac='', isid='', port='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [port]        - The incoming port interface of the multicast FIB entry.

        Verifies the incoming port interface of the multicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_IN_PORTS, True,
                                           "SPBM multicast FIB Incoming Interface port to Destination Address "
                                           "{da} via System ID {sysid}, I-SID {isid} and BVLAN {bvlan} is port "
                                           "{port}.",
                                           "SPBM multicast FIB Incoming Interface port to Destination Address "
                                           "{da} via System ID {sysid}, I-SID {isid} and BVLAN {bvlan} is NOT "
                                           "port {port}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_inbound_mlt(self, device_name, sysid='', bvlan='', dmac='', isid='', mlt_id='',
                                                   **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [mlt_id]      - The incoming MLT ID interface of the multicast FIB entry.

        Verifies the incoming port interface of the multicast FIB entry.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "mlt_id": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_IN_MLTS, True,
                                           "SPBM multicast FIB inbound MLT to Destination Address {da} via"
                                           " System ID {sysid}, BVLAN {bvlan} entry is MLT {mlt_id}.",
                                           "SPBM multicast FIB inbound MLT to Destination Address {da} via"
                                           " System ID {sysid}, BVLAN {bvlan} entry is NOT MLT {mlt_id}!",
                                           **kwargs)

    def spbm_verify_isis_multicast_fib_cvlan(self, device_name, sysid='', bvlan='', dmac='', isid='', cvlan='',
                                             **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [sysid]       - The System ID of the node where unicast FIB entry comes from in the form of xxxx.xxxx.xxxx
        [bvlan]       - The VLAN of the unicast FIB entry.
        [da]          - The Destination Mac Address of the unicast FIB entry in the form of: xx:xx:xx:xx:xx:xx
        [isid]        - The Isid ID of the multicast FIB entry.
        [cvlan]       - The CVLAN to verify.

        Verifies the host name of the node where multicast FIB entry comes from.
        """
        args = {"sysid": sysid,
                "bvlan": bvlan,
                "da": dmac,
                "isid": isid,
                "cvlan": cvlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_MULTICAST_FIB_DETAIL,
                                           self.parse_const.CHECK_ISIS_SPBM_MULTICAST_FIB_CVLAN, True,
                                           "SPBM multicast FIB CVLAN to Multicast Destination Address {da} via "
                                           "System ID {sysid}, I-SID {isid}, and BVLAN {bvlan} is {cvlan}.",
                                           "SPBM multicast FIB CVLAN to Multicast Destination Address {da} via "
                                           "System ID {sysid}, I-SID {isid}, and BVLAN {bvlan} is NOT {cvlan}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_destination_network(self, device_name, dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified nh_beb and bvlan.  (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Destination Network entry.  (Example format: 4051)

        Verifies that a Destination Network entry is present in the ip-unicast-fib table for the specified NH BEB and
        BVLAN entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_DEST_NETWORK, True,
                                           "Destination Network entry {dest} is present for NH BEB {nh_beb} and"
                                           " BVLAN {bvlan} on {device_name}.",
                                           "Destination Network entry {dest} is NOT present for NH BEB {nh_beb}"
                                           " and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_destination_network(self, device_name, dest='', nh_beb='', bvlan='',
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network entry that should be present in the ipv6 unicast fib table, which
                        is associated with the specified nh_beb and bvlan.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ipv6 unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Destination Network entry.  (Example format: 4051)

        Verifies an IPv6 Destination Network entry is present in the ipv6-unicast-fib table for the specified NH BEB and
        BVLAN.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_DEST_NETWORK, True,
                                           "IPv6 Destination Network entry {dest} is present for NH BEB {nh_beb}"
                                           " and BVLAN {bvlan} on {device_name}.",
                                           "IPv6 Destination Network entry {dest} is NOT present for NH BEB"
                                           " {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_nh_beb(self, device_name, dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the nh_beb entry.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the nh_beb entry.  (Example format: 4051)

        Verifies that a NH BEB entry is present in the ip-unicast-fib table for the specified Destination Network and
        BVLAN entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ENTRY_EXISTS, True,
                                           "NH BEB {nh_beb} is present for Destination Network {dest} and"
                                           " BVLAN {bvlan} on {device_name}.",
                                           "NH BEB {nh_beb} is NOT present for Destination Network {dest} and"
                                           " BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_nh_beb(self, device_name, dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network entry that is associated with the nh_beb entry.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ipv6 unicast fib table, which is associated with
                        the specified destination network and bvlan.         (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the nh_beb entry.  (Example format: 4051)

        Verifies that a NH BEB entry is present in the ipv6-unicast-fib table for the specified Destination Network and
        BVLAN entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_DEST_NETWORK, True,
                                           "NH BEB {nh_beb} is present for IPv6 Destination Network {dest} and"
                                           " BVLAN {bvlan} on {device_name}.",
                                           "NH BEB {nh_beb} is NOT present for IPv6 Destination Network {dest}"
                                           " and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_bvlan(self, device_name, dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the bvlan entry.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table and associated with the
                        specified destination network and nh_beb.  (Example format: 4051)

        Verifies that a BVLAN entry is present in the ip-unicast-fib table for the specified Destination Network and
        NH_BEB entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_BVLAN, True,
                                           "BVLAN {bvlan} is present for Destination Network entry {dest} and"
                                           " NH BEB {nh_beb} on {device_name}.",
                                           "BVLAN {bvlan} is NOT present for Destination Network entry {dest}"
                                           " and NH BEB {nh_beb} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_bvlan(self, device_name, dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network entry that is associated with the bvlan entry.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table and associated with the
                        specified destination network and nh_beb.  (Example format: 4051)

        Verifies that a BVLAN entry is present in the ipv6-unicast-fib table for the specified Destination Network and
        NH_BEB entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_DEST_NETWORK, True,
                                           "BVLAN {bvlan} is present for IPv6 Destination Network entry {dest}"
                                           " and NH BEB {nh_beb} on {device_name}.",
                                           "BVLAN {bvlan} is NOT present for IPv6 Destination Network entry"
                                           " {dest} and NH BEB {nh_beb} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_outgoing_port(self, device_name, dest='', nh_beb='', bvlan='', out_int='',
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Outgoing Interface.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Outgoing Interface.  (Example format: 4051)
        [out_int]     - The Outgoing Interface port entry that should be present in the ip unicast fib table and
                        associated with the specified destination network, nh_beb and bvlan.
                        (Example format: gigabitEthernet 1/12)

        Verifies that the Outgoing Interface entry is present in the ip-unicast-fib table for the specified
        destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "out_int": out_int}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_OUT_PORT, True,
                                           "Outgoing Interface {out_int} is present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Outgoing Interface {out_int} is NOT present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_outgoing_port(self, device_name, dest='', nh_beb='', bvlan='', out_int='',
                                                        **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network entry that is associated with the Outgoing Interface.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ipv6-unicast-fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Outgoing Interface.  (Example format: 4051)
        [out_int]     - The Outgoing Interface port entry that should be present in the ipv6-unicast-fib table and
                        associated with the specified destination network, nh_beb and bvlan.
                        (Example format: gigabitEthernet 1/12)

        Verifies that the Outgoing Interface entry is present in the ipv6-unicast-fib table for the specified
        destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "out_int": out_int}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_OUT_PORT, True,
                                           "Outgoing Interface {out_int} is present for IPv6 Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Outgoing Interface {out_int} is NOT present for IPv6 Destination"
                                           " Network {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_spbm_cost(self, device_name, dest='', nh_beb='', bvlan='', spbm_cost='',
                                                  **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Spbm Cost.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [spbm_cost]   - The Spbm Cost entry that should be present in the ip unicast fib table and associated
                        with the specified destination network, nh_beb and bvlan.  (Example format: 3000)

        Verifies that the Spbm Cost entry is present in the ip-unicast-fib table for the specified destination network,
        nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "spbm_cost": spbm_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_SPBM_COST, True,
                                           "Spbm Cost {spbm_cost} is present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Spbm Cost {spbm_cost} is NOT present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_spbm_cost(self, device_name, dest='', nh_beb='', bvlan='', spbm_cost='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network and mask that is associated with the Spbm Cost.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ipv6-unicast-fib table, which is associated with
                        the specified ipv6-destination-network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [spbm_cost]   - The Spbm Cost entry that should be present in the ipv6-unicast-fib table and associated
                        with the specified IPv6 destination network, nh_beb and bvlan.  (Example format: 3000)

        Verifies that the Spbm Cost entry is present in the ipv6-unicast-fib table for the specified destination
        network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "spbm_cost": spbm_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_SPBM_COST, True,
                                           "Spbm Cost {spbm_cost} is present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Spbm Cost {spbm_cost} is NOT present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_prefix_cost(self, device_name, dest='', nh_beb='', bvlan='', prefix_cost='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Prefix Cost.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [prefix_cost] - The Prefix Cost entry that should be present in the ip unicast fib table and associated
                        with the specified destination network, nh_beb and bvlan.  (Example format: 3000)

        Verifies that the Spbm Prefix Cost entry is present in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_cost": prefix_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_COST, True,
                                           "Prefix Cost {prefix_cost} is present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Prefix Cost {prefix_cost} is NOT present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_prefix_cost(self, device_name, dest='', nh_beb='', bvlan='', prefix_cost='',
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The IPv6 Destination Network and mask that is associated with the Prefix Cost.
                        (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ipv6-unicast-fib table, which is associated with
                        the specified IPv6 destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.   (Example format: 4051)
        [prefix_cost] - The Prefix Cost entry that should be present in the ipv6-unicast-fib table and associated
                        with the specified IPv6 destination network, nh_beb and bvlan.  (Example format: 3000)

        Verifies that the Spbm Prefix Cost entry is present in the ipv6-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_cost": prefix_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_PREFIX_COST, True,
                                           "Prefix Cost {prefix_cost} is present for IPv6 Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Prefix Cost {prefix_cost} is NOT present for IPv6 Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_prefix_type(self, device_name, dest='', nh_beb='', bvlan='', prefix_type='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Prefix Cost.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [prefix_type] - The Prefix Type entry that should be present in the ip unicast fib table and associated
                        with the specified destination network, nh_beb and bvlan.  (Example format: Internal)

        Verifies that the Spbm Prefix Type entry is present in the ip-unicast-fib table for the specified destination
        network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_type": prefix_type}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE, True,
                                           "Prefix Type {prefix_type} is present for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Prefix Type {prefix_type} is NOT present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_metric_prefix_type_internal(self, device_name, dest='', nh_beb='', bvlan='',
                                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Prefix Cost.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)

        Verifies that IP Metric Prefix Type of the IP unicast FIB entry is internal in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE_INTERNAL,
                                           True,
                                           "Metric Prefix Type is internal for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Metric Prefix Type is NOT internal for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_metric_prefix_type_external(self, device_name, dest='', nh_beb='', bvlan='',
                                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [dest]        - The Destination Network and mask that is associated with the Prefix Cost.
                        (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                        the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]       - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)

        Verifies that IP Metric Prefix Type of the IP unicast FIB entry is external in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE_EXTERNAL,
                                           True,
                                           "Metric Prefix Type is external for Destination Network {dest},"
                                           " NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Metric Prefix Type is NOT external for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_ip_route_preference(self, device_name, dest='', nh_beb='', bvlan='',
                                                            ip_route_pref='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [dest]          - The Destination Network and mask that is associated with the Prefix Cost.
                          (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                          the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]         - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [ip_route_pref] - The IP Route preference entry that should be present in the ip unicast fib table
                          and associated with the specified destination network, nh_beb and bvlan.  (Example format: 7)

        Verifies that the IP Route preference entry is present in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "ip_route_pref": ip_route_pref}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_IP_ROUTE_PREFERENCE,
                                           True,
                                           "IP Route preference {ip_route_pref} is present for Destination"
                                           " Network {dest}, NH BEB {nh_beb} and BVLAN {bvlan}"
                                           " on {device_name}.",
                                           "IP Route preference {ip_route_pref} is NOT present for Destination"
                                           " Network {dest}, NH BEB {nh_beb} and BVLAN {bvlan}"
                                           " on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_name(self, device_name, dest='', nh_beb='', bvlan='', vrf_name='',
                                                 **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [dest]          - The Destination Network and mask that is associated with the Prefix Cost.
                          (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                          the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]         - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [vrf_name]      - The VRF Name that should be present in the ip unicast fib table.  (Example format: green)

        Verifies that the VRF Name is present in the ip-unicast-fib table for the specified destination network, nh beb,
        and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_NAME,
                                           True,
                                           "The VRF Name {vrf_name} is present for Destination Network {dest}, "
                                           "NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "The VRF Name {vrf_name} is NOT present for Destination Network "
                                           "{dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_nh_bmac(self, device_name, dest='', nh_bmac='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [dest]         - The Destination Network and mask that is associated with the Prefix Cost.
                         (Example format: 151.1.10.0/24)
        [nh_bmac]      - The BEB IS-IS System ID MAC that is associated with the Destination Network entry.
                         (Example format: 00:bb:00:00:40:00)
        [bvlan]        - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [nh_mac]       - The next hop BMAC of the IP unicast FIB entry that should be present in the ip unicast
                         fib table and associated with the specified destination network, nh_beb and bvlan.
                         (Example format: 00:bb:00:00:01:10)

        Verifies that next hop BMAC of the IP unicast FIB entry is present in the ip-unicast-fib table for the
        specified destination network, and bvlan entries.
        """
        args = {"dest": dest,
                "bvlan": bvlan,
                "nh_bmac": nh_bmac}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_SPBM_NH_AS_MAC,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_NH_MAC,
                                           True,
                                           "Next hop BMAC {nh_bmac} is present for Destination"
                                           " Network {dest}, and BVLAN {bvlan} on {device_name}.",
                                           "Next hop BMAC {nh_bmac} is NOT present for Destination"
                                           " Network {dest}, and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid(self, device_name, dest='', nh_beb='', bvlan='', isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [dest]          - The Destination Network and mask that is associated with the Prefix Cost.
                          (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                          the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]         - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [isid]          - The ISID of the IP unicast FIB entry that should be present in the ip unicast fib table
                          and associated with the specified destination network, nh_beb and bvlan.
                          (Example format: 10) Note: Default is 0 for no ISID - This is shown as a dash in the CLI.

        Verifies that ISID of the IP unicast FIB entry is present in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "isid": isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_ISID,
                                           True,
                                           "VRF ISID {isid} is present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "VRF ISID {isid} is NOT present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_destination_network_isid(self, device_name, dest='', nh_beb='', bvlan='',
                                                                 dest_isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [dest]          - The Destination Network and mask that is associated with the Prefix Cost.
                          (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                          the specified destination network and bvlan.  (Example format: VSP4002)
        [bvlan]         - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [dest_isid]     - The Destination ISID of the IP unicast FIB entry that should be present in the ip unicast
                          fib table and associated with the specified destination network, nh_beb and bvlan.
                          (Example format: 10) Note: Default is 0 for no ISID - This is shown as a dash in the CLI.

        Verifies that Destination ISID of the IP unicast FIB entry is present in the ip-unicast-fib table for the
        specified destination network, nh beb and bvlan entries.
        """
        args = {"dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "dest_isid": dest_isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_DESTINATION_ISID,
                                           True,
                                           "Destination ISID {dest_isid} is present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Destination ISID {dest_isid} is NOT present for Destination Network"
                                           " {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_name(self, device_name, vrf_name='', isid='', dest_isid='', dest='',
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf for which to verify the VRF ID.
        [isid]        - The VRF I-sid for which to verify the VRF name is present.
        [dest_isid]   - The Destination Isid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)

        Verifies that the VRF Name exists in the ip unicast table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_DESTINATION_ISID, True,
                                           "The VRF Name {vrf_name} for VRF ISID {isid} is present "
                                           "on {device_name}.",
                                           "The VRF Name {vrf_name} for VRF ISID {isid} is NOT present "
                                           "on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_id(self, device_name, vrf_name='', isid='', dest_isid='', dest='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf for which to verify the VRF ID.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination Isid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)

        Verifies that the specified VRF ISID exists in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_ISID, True,
                                           "VRF ISID {isid} is present on {device_name}.",
                                           "VRF ISID {isid} is NOT present on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_isid(self, device_name, vrf_name='', isid='', dest_isid='',
                                                           dest='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)

        Verifies that the Destination I-sid is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_ISID,
                                           True,
                                           "The Destination i-sid {dest_isid} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The Destination i-sid {dest_isid} is NOT present for VRF "
                                           "ISID {isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_network(self, device_name, vrf_name='', isid='', dest_isid='',
                                                              dest='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)

        Verifies that the Destination Network is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK_ISID,
                                           True,
                                           "The Destination network {dest} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The Destination network {dest} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_nh_beb(self, device_name, vrf_name='', isid='', dest_isid='', dest='',
                                                        nh_beb='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table, which is associated with
                          the specified VRF ISID.  (Example format: VSP4002)

        Verifies that the NH BEB is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "nh_beb": nh_beb}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_NH_BEB, True,
                                           "The NH BEB {nh_beb} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The NH BEB {nh_beb} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_bvlan(self, device_name, vrf_name='', isid='', dest_isid='', dest='',
                                                       bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table, which is associated with
                          the specified VRF ISID.  (Example format: 4002)

        Verifies that the BVLAN is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_BVLAN, True,
                                           "The BVLAN {bvlan} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The BVLAN {bvlan} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_out_port(self, device_name, vrf_name='', isid='', dest_isid='',
                                                          dest='', out_int='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [out_int]     - The Outgoing Interface entry that should be present in the ip unicast fib table, which is
                        associated with the specified VRF ISID.  (Example format: GigabitEthernet 1/12)

        Verifies that the Outgoing Interface is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "out_int": out_int}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_OUT_INT_PORT,
                                           True,
                                           "The Outgoing Interface {out_int} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The Outgoing Interface {out_int} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_spbm_cost(self, device_name, vrf_name='', isid='', dest_isid='',
                                                           dest='', spbm_cost='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [spbm_cost]   - The SPBM Cost entry that should be present in the ip unicast fib table, which is
                        associated with the specified VRF ISID.  (Example format: 3000)

        Verifies that the SPBM Cost is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "spbm_cost": spbm_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_SPBM_COST,
                                           True,
                                           "The SPBM Cost {spbm_cost} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The SPBM Cost {spbm_cost} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_prefix_cost(self, device_name, vrf_name='', isid='', dest_isid='',
                                                             dest='', prefix_cost='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the Vrf to verify.
        [isid]        - The VRF I-sid to verify.
        [dest_isid]   - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]        - The Destination Network and mask entry that should be present in the ip unicast fib table,
                        which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [prefix_cost] - The Prefix Cost entry that should be present in the ip unicast fib table, which is
                        associated with the specified VRF ISID.  (Example format: 1)

        Verifies that the PREFIX Cost is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "prefix_cost": prefix_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_PREFIX_COST,
                                           True,
                                           "The PREFIX Cost {prefix_cost} is present for VRF ISID {isid} "
                                           "on {device_name}.",
                                           "The PREFIX Cost {prefix_cost} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_ip_route_pref(self, device_name, vrf_name='', isid='', dest_isid='',
                                                               dest='', ip_route_pref='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the Vrf to verify.
        [isid]          - The VRF I-sid to verify.
        [dest_isid]     - The Destination I-sid that should be present in the ip unicast fib table.
        [dest]          - The Destination Network and mask entry that should be present in the ip unicast fib table,
                          which is associated with the specified VRF ISID.  (Example format: 151.1.10.0/24)
        [ip_route_pref] - The IP ROUTE PREFERENCE entry that should be present in the ip unicast fib table, which is
                          associated with the specified VRF ISID.  (Example format: 7)

        Verifies that the IP ROUTE PREFERENCE entry is present in the ip unicast fib table for the specified VRF ISID.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest_isid": dest_isid,
                "dest": dest,
                "ip_route_pref": ip_route_pref}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_IP_ROUTE_PREF,
                                           True,
                                           "The IP ROUTE PREFERENCE {ip_route_pref} is present for VRF ISID "
                                           "{isid} on {device_name}.",
                                           "The IP ROUTE PREFERENCE {ip_route_pref} is NOT present for VRF ISID "
                                           "{isid} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_dest_network_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                        dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the destination network entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK,
                                           True,
                                           "Destination Network {dest} is correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "Destination Network {dest} is NOT correctly mapped to VRF {vrf_name}"
                                           "and i-sid {isid} for NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_dest_network_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                          dest='', nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the IPv6 destination network entry exists in the IPv6 unicast fib table for the specified vrf name
        and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_DEST_NETWORK,
                                           True,
                                           "Destination Network {dest} is correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "Destination Network {dest} is NOT correctly mapped to VRF {vrf_name}"
                                           "and i-sid {isid} for NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_nh_beb_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                  nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the NH BEB entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_NH_BEB, True,
                                           "NH BEB {nh_beb} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "NH BEB {nh_beb} is NOT correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and BVLAN {bvlan} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_nh_beb_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                    nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the NH BEB entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_NH_BEB, True,
                                           "NH BEB {nh_beb} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "NH BEB {nh_beb} is NOT correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and BVLAN {bvlan} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_bvlan_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                 nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the BVLAN entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_BVLAN, True,
                                           "BVLAN {bvlan} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and NH BEB {nh_beb} on "
                                           "{device_name}.",
                                           "BVLAN {bvlan} is NOT correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and NH BEB {nh_beb} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_bvlan_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                   nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)

        Verifies the BVLAN entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_BVLAN, True,
                                           "BVLAN {bvlan} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and NH BEB {nh_beb} on "
                                           "{device_name}.",
                                           "BVLAN {bvlan} is NOT correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest} and NH BEB {nh_beb} on "
                                           "{device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_out_int_port_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                        dest='', nh_beb='', bvlan='', out_int='',
                                                                        **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [out_int]     - The output interface entry that should be present in the ip unicast fib table for the specified
                        vrf name and i-sid.             (Example format: 1/12)

        Verifies the OUTPUT INTERFACE entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "out_int": out_int}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_OUT_INT_PORT,
                                           True,
                                           "Outgoing Interface {out_int} is correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} "
                                           "and BVLAN {bvlan} on {device_name}.",
                                           "Outgoing Interface {out_int} is NOT correctly mapped to VRF "
                                           "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_out_int_port_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                          dest='', nh_beb='', bvlan='', out_int='',
                                                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [out_int]     - The output interface entry that should be present in the ip unicast fib table for the specified
                        vrf name and i-sid.             (Example format: 1/12)

        Verifies the OUTPUT INTERFACE entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "out_int": out_int}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_OUT_INT_PORT,
                                           True,
                                           "Outgoing Interface {out_int} is correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} "
                                           "and BVLAN {bvlan} on {device_name}.",
                                           "Outgoing Interface {out_int} is NOT correctly mapped to VRF "
                                           "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}.!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_spbm_cost_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                     nh_beb='', bvlan='', spbm_cost='', **kwargs):
        """
        Keyword Arguments:
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [spbm_cost]   - The SPBM COST entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 3000)

        Verifies the SPBM COST entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "spbm_cost": spbm_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_SPBM_COST, True,
                                           "SPBM COST {spbm_cost} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "SPBM COST {spbm_cost} is NOT correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_spbm_cost_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                       nh_beb='', bvlan='', spbm_cost='', **kwargs):
        """
        Keyword Arguments:
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [spbm_cost]   - The SPBM COST entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 3000)

        Verifies the SPBM COST entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "spbm_cost": spbm_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_SPBM_COST, True,
                                           "SPBM COST {spbm_cost} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "SPBM COST {spbm_cost} is NOT correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_prefix_cost_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                       nh_beb='', bvlan='', prefix_cost='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [prefix_cost] - The PREFIX COST entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 1)

        Verifies the PREFIX COST entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_cost": prefix_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_PREFIX_COST, True,
                                           "Prefix Cost {prefix_cost} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "Prefix Cost {prefix_cost} is NOT correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} "
                                           "and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_prefix_cost_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                         dest='', nh_beb='', bvlan='', prefix_cost='',
                                                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network entry that should be present in the ipv6 unicast fib table for
                        the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [prefix_cost] - The PREFIX COST entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 1)

        Verifies the PREFIX COST entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_cost": prefix_cost}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_PREFIX_COST,
                                           True,
                                           "Prefix Cost {prefix_cost} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "Prefix Cost {prefix_cost} is NOT correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} "
                                           "and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_prefix_type_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                       nh_beb='', bvlan='', prefix_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [prefix_type] - The PREFIX TYPE entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: Internal)

        Verifies the Prefix Type entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_type": prefix_type}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_PREFIX_TYPE, True,
                                           "Prefix Type {prefix_type} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "Prefix Type {prefix_type} is NOT correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_prefix_type_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                         dest='', nh_beb='', bvlan='', prefix_type='',
                                                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [vrf_name]    - The name of the VRF to verify.  (Example format: GRT)
        [isid]        - The i-sid to verify.            (Example format: 30001)
        [dest]        - The Destination Network and mask that should be present in the ip unicast fib table for the
                        specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]      - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: VSP4002)
        [bvlan]       - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: 4051)
        [prefix_type] - The PREFIX TYPE entry that should be present in the ip unicast fib table for the specified vrf
                        name and i-sid.                 (Example format: Internal)

        Verifies the Prefix Type entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "prefix_type": prefix_type}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_PREFIX_TYPE,
                                           True,
                                           "Prefix Type {prefix_type} is correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}.",
                                           "Prefix Type {prefix_type} is NOT correctly mapped to VRF {vrf_name} "
                                           "and i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_ip_route_pref_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                         dest='', nh_beb='', bvlan='', ip_route_pref='',
                                                                         **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [ip_route_pref] - The IP Route preference entry that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 7)

        Verifies the IP Route Preference entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "ip_route_pref": ip_route_pref}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_IP_ROUTE_PREF,
                                           True,
                                           "IP Route preference {ip_route_pref} is correctly mapped to VRF "
                                           "{vrf_name} i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "IP Route preference {ip_route_pref} is NOT correctly mapped to VRF "
                                           "{vrf_name} i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_ip_route_pref_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                           dest='', nh_beb='', bvlan='',
                                                                           ip_route_pref='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [ip_route_pref] - The IP Route preference entry that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 7)

        Verifies the IP Route Preference entry exists in the IPv6 unicast fib table for the specified vrf name and
        i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "ip_route_pref": ip_route_pref}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_IP_ROUTE_PREF,
                                           True,
                                           "IP Route preference {ip_route_pref} is correctly mapped to VRF "
                                           "{vrf_name} i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "IP Route preference {ip_route_pref} is NOT correctly mapped to VRF "
                                           "{vrf_name} i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_name_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                    nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)

        Verifies the vrf name entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_VRF_NAME,
                                           True,
                                           "The VRF name {vrf_name} and i-sid {isid} is correctly mapped to "
                                           "Destination Address {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "The VRF name {vrf_name} and i-sid {isid} is NOT correctly mapped to "
                                           "Destination Address {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_vrf_name_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                      nh_beb='', bvlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network entry that should be present in the ipv6 unicast fib table for
                          the specified vrf name and i-sid.   (Example format: 3000:11:0:0:0:0:0:0/64)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)

        Verifies the vrf name entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_VRF_NAME,
                                           True,
                                           "The VRF name {vrf_name} and i-sid {isid} is correctly mapped to "
                                           "Destination {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}.",
                                           "The VRF name {vrf_name} and i-sid {isid} is NOT correctly mapped to "
                                           "Destination {dest}, NH BEB {nh_beb} and BVLAN {bvlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_vrf_isid_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                    nh_beb='', bvlan='', vrf_isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [vrf_isid]      - The VRF i-sid that should be present in the ip unicast fib table for the specified vrf name
                          and i-sid.                      (Example format: 30001)

        Verifies the VRF i-sid entry exists in the ip unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "vrf_isid": vrf_isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_VRF_ISID,
                                           True,
                                           "VRF ISID {vrf_isid} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest}, NH BEB {nh_beb} and BVLAN "
                                           "{bvlan} on {device_name}.",
                                           "VRF ISID {vrf_isid} is NOT correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_vrf_isid_by_vrf_name_and_id(self, device_name, vrf_name='', isid='', dest='',
                                                                      nh_beb='', bvlan='', vrf_isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [vrf_isid]      - The VRF i-sid that should be present in the ip unicast fib table for the specified vrf name
                          and i-sid.                      (Example format: 30001)

        Verifies the VRF i-sid entry exists in the IPv6 unicast fib table for the specified vrf name and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "vrf_isid": vrf_isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_VRF_ISID,
                                           True,
                                           "VRF ISID {vrf_isid} is correctly mapped to VRF {vrf_name} and i-sid "
                                           "{isid} for Destination Network {dest}, NH BEB {nh_beb} and BVLAN "
                                           "{bvlan} on {device_name}.",
                                           "VRF ISID {vrf_isid} is NOT correctly mapped to VRF {vrf_name} and "
                                           "i-sid {isid} for Destination Network {dest}, NH BEB {nh_beb} and "
                                           "BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_unicast_fib_dest_network_isid_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                             dest='', nh_beb='', bvlan='',
                                                                             dest_isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [dest_isid]     - The Destination Network ISID entry that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 10) Note: Default is 0 for no ISID
                                                     - This is shown as a dash in the CLI.

        Verifies the Destination Network ISID entry exists in the ip unicast fib table for the specified vrf name
        and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "dest_isid": dest_isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_ID,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK_ISID,
                                           True,
                                           "Destination Network ISID {dest_isid} is correctly mapped to VRF "
                                           "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}.",
                                           "Destination Network ISID {dest_isid} is NOT correctly mapped to VRF "
                                           "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
                                           "{nh_beb} and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ipv6_unicast_fib_dest_network_isid_by_vrf_name_and_id(self, device_name, vrf_name='', isid='',
                                                                               dest='', nh_beb='', bvlan='',
                                                                               dest_isid="0", **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [vrf_name]      - The name of the VRF to verify.  (Example format: GRT)
        [isid]          - The i-sid to verify.            (Example format: 30001)
        [dest]          - The Destination Network and mask that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 151.1.10.0/24)
        [nh_beb]        - The NH BEB entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: VSP4002)
        [bvlan]         - The BVLAN entry that should be present in the ip unicast fib table for the specified vrf
                          name and i-sid.                 (Example format: 4051)
        [dest_isid]     - The Destination Network ISID entry that should be present in the ip unicast fib table for the
                          specified vrf name and i-sid.   (Example format: 10) Note: Default is 0 for no ISID
                                                     - This is shown as a dash in the CLI.

        Verifies the Destination Network ISID entry exists in the IPv6 unicast fib table for the specified vrf name
        and i-sid.
        """
        args = {"vrf_name": vrf_name,
                "isid": isid,
                "dest": dest,
                "nh_beb": nh_beb,
                "bvlan": bvlan,
                "dest_isid": dest_isid}

        return self.execute_verify_keyword(
            device_name, args, self.cmd_const.SHOW_ISIS_IPV6_UNICAST_FIB_ID,
            self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK_ISID, True,
            "Destination Network ISID {dest_isid} is correctly mapped to VRF "
            "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
            "{nh_beb} and BVLAN {bvlan} on {device_name}.",
            "Destination Network ISID {dest_isid} is NOT correctly mapped to VRF "
            "{vrf_name} and i-sid {isid} for Destination Network {dest}, NH BEB "
            "{nh_beb} and BVLAN {bvlan} on {device_name}!", **kwargs)

    def spbm_verify_isis_ip_unicast_fib_nh_bmac_by_id(self, device_name, dest='', nh_bmac='', bvlan='', vrf_isid="0",
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [dest]         - The Destination Network and mask that is associated with the Prefix Cost.
                         (Example format: 151.1.10.0/24)
        [nh_bmac]      - The BEB IS-IS System ID MAC that is associated with the Destination Network entry.
                         (Example format: 00:bb:00:00:40:00)
        [bvlan]        - The BVLAN that is associated with the Spbm Cost.  (Example format: 4051)
        [nh_mac]       - The next hop BMAC of the IP unicast FIB entry that should be present in the ip unicast
                         fib table and associated with the specified destination network, nh_beb and bvlan.
                         (Example format: 00:bb:00:00:01:10)
        [vrf_isid]     - The VRF ISID to verify.

        Verifies that next hop BMAC of the IP unicast FIB entry is present in the ip-unicast-fib table for the
        specified destination network, and bvlan entries.
        """
        args = {"dest": dest,
                "bvlan": bvlan,
                "nh_bmac": nh_bmac,
                "vrf_isid": vrf_isid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_UNICAST_FIB_SPBM_NH_AS_MAC,
                                           self.parse_const.CHECK_ISIS_SPBM_IP_UNICAST_FIB_NH_MAC,
                                           True,
                                           "Next hop BMAC {nh_bmac} is present for Destination"
                                           " Network {dest}, and BVLAN {bvlan} on {device_name}.",
                                           "Next hop BMAC {nh_bmac} is NOT present for Destination"
                                           " Network {dest}, and BVLAN {bvlan} on {device_name}!",
                                           **kwargs)

    def spbm_verify_isis_ip_multicast_route_vrf_entries_exist(self, device_name, vrf_name='', mcast_source='',
                                                              mcast_group='', data_isid='', bvlan='', source_beb='',
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [vrf_name]     - The name of the VRF to verify.  (Example format: surveillance)
        [mcast_source] - The Multicast Source IP Address entry to verify. (Example format: 172.16.10.52)
        [mcast_group]  - The Multicast Group entry to verify.  (Example format: 226.1.1.2)
        [data_isid]    - The Data ISID entry to verify.  (Example format: 16300727)
        [bvlan]        - The BVLAN entry to verify.  (Example format: 4052)
        [source_beb]   - The Source-BEB entry to verify. (Example format: BEB-8284-110)

        Verifies that the specified entries exist in the ip multicast route table for a given VRF.
        """
        args = {"vrf_name": vrf_name,
                "mcast_source": mcast_source,
                "mcast_group": mcast_group,
                "data_isid": data_isid,
                "bvlan": bvlan,
                "source_beb": source_beb}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ISIS_IP_MULTICAST_ROUTE_VRF,
                                           self.parse_const.VERIFY_ISIS_SPBM_MULTICAST_ENABLED,
                                           True,
                                           "The ISIS SPBM IP Multicast Route Entry for VRF {vrf_name} is present "
                                           "on {device_name}",
                                           "The ISIS SPBM IP Multicast Route Entry for VRF {vrf_name} is NOT "
                                           "present on {device_name}!",
                                           **kwargs)

    def spbm_verify_virtual_ist_peer_ip(self, device_name, ip='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ip]          - The ip address to verify
        [vlan]        - The VLAN to verify.

        Verifies a virtual-ist peer ip address is set for a given vlan.
        """
        args = {"ip": ip,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VIRTUAL_IST,
                                           self.parse_const.VERIFY_VIRTUAL_IST_PEER_IP, True,
                                           "Virtual-ist peer ip {ip} on vlan {vlan} exists on {device_name}.",
                                           "Virtual-ist peer ip {ip} on vlan {vlan} does NOT exist on {device_name}!",
                                           **kwargs)

    def spbm_verify_virtual_ist_peer_ip_is_not(self, device_name, ip='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ip]          - The ip address to verify
        [vlan]        - The VLAN to verify.

        Verifies a virtual-ist peer ip address is not set for a given vlan.
        """
        args = {"ip": ip,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VIRTUAL_IST,
                                           self.parse_const.VERIFY_VIRTUAL_IST_PEER_IP, False,
                                           "Virtual-ist peer ip {ip} on vlan {vlan} is not present on {device_name}.",
                                           "Virtual-ist peer ip {ip} on vlan {vlan} IS present on {device_name}!",
                                           **kwargs)
