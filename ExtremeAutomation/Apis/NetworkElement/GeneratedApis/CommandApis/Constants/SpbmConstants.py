"""
This class outlines all the constants for the spbm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SpbmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SpbmConstants(ApiConstants):
    def __init__(self):
        super(SpbmConstants, self).__init__()
        self.CLEAR_ETHERTYPE = {"constant": "clear_ethertype",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.clear_ethertype}
        self.CLEAR_ISIS_BVID = {"constant": "clear_isis_bvid",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.clear_isis_bvid}
        self.CLEAR_ISIS_INSTANCE_ID = {"constant": "clear_isis_instance_id",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.clear_isis_instance_id}
        self.CLEAR_ISIS_MULTICAST_FWD_CACHE_TIMEOUT = {"constant": "clear_isis_multicast_fwd_cache_timeout",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.clear_isis_multicast_fwd_cache_timeout}
        self.CLEAR_ISIS_NICKNAME = {"constant": "clear_isis_nickname",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.clear_isis_nickname}
        self.CLEAR_ISIS_SMLT_PEER_SYSTEM_ID = {"constant": "clear_isis_smlt_peer_system_id",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.clear_isis_smlt_peer_system_id}
        self.CLEAR_ISIS_SMLT_VIRTUAL_BMAC = {"constant": "clear_isis_smlt_virtual_bmac",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.clear_isis_smlt_virtual_bmac}
        self.CLEAR_LOGICAL_INTERFACE_ISIS_INSTANCE_ID = {"constant": "clear_logical_interface_isis_instance_id",
                                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                         "link": self.link.clear_logical_interface_isis_instance_id}
        self.CLEAR_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE = {"constant": "clear_logical_interface_isis_interface_type",
                                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                            "link": self.link.clear_logical_interface_isis_interface_type}
        self.CLEAR_LOGICAL_INTERFACE_ISIS_L1_METRIC = {"constant": "clear_logical_interface_isis_l1_metric",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.clear_logical_interface_isis_l1_metric}
        self.CLEAR_MLT_ISIS_INSTANCE_ID = {"constant": "clear_mlt_isis_instance_id",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.clear_mlt_isis_instance_id}
        self.CLEAR_MLT_ISIS_INTERFACE_TYPE = {"constant": "clear_mlt_isis_interface_type",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.clear_mlt_isis_interface_type}
        self.CLEAR_MLT_ISIS_L1_METRIC = {"constant": "clear_mlt_isis_l1_metric",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.clear_mlt_isis_l1_metric}
        self.CLEAR_PORT_ISIS_INSTANCE_ID = {"constant": "clear_port_isis_instance_id",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.clear_port_isis_instance_id}
        self.CLEAR_PORT_ISIS_INTERFACE_TYPE = {"constant": "clear_port_isis_interface_type",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.clear_port_isis_interface_type}
        self.CLEAR_PORT_ISIS_L1_METRIC = {"constant": "clear_port_isis_l1_metric",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_port_isis_l1_metric}
        self.CLEAR_VIRTUAL_IST_PEER_IP = {"constant": "clear_virtual_ist_peer_ip",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_virtual_ist_peer_ip}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_global}
        self.DISABLE_IPV6_SHORTCUT = {"constant": "disable_ipv6_shortcut",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.disable_ipv6_shortcut}
        self.DISABLE_IP_SHORTCUT = {"constant": "disable_ip_shortcut",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_ip_shortcut}
        self.DISABLE_ISIS_MULTICAST = {"constant": "disable_isis_multicast",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.disable_isis_multicast}
        self.DISABLE_LSDB_TRAP = {"constant": "disable_lsdb_trap",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.disable_lsdb_trap}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_global}
        self.ENABLE_IPV6_SHORTCUT = {"constant": "enable_ipv6_shortcut",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.enable_ipv6_shortcut}
        self.ENABLE_IP_SHORTCUT = {"constant": "enable_ip_shortcut",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_ip_shortcut}
        self.ENABLE_ISIS_MULTICAST = {"constant": "enable_isis_multicast",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.enable_isis_multicast}
        self.ENABLE_LSDB_TRAP = {"constant": "enable_lsdb_trap",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.enable_lsdb_trap}
        self.SET_ETHERTYPE = {"constant": "set_ethertype",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_ethertype}
        self.SET_ISIS_BVID = {"constant": "set_isis_bvid",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_isis_bvid}
        self.SET_ISIS_INSTANCE_ID = {"constant": "set_isis_instance_id",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_isis_instance_id}
        self.SET_ISIS_MULTICAST_FWD_CACHE_TIMEOUT = {"constant": "set_isis_multicast_fwd_cache_timeout",
                                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                     "link": self.link.set_isis_multicast_fwd_cache_timeout}
        self.SET_ISIS_NICKNAME = {"constant": "set_isis_nickname",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_isis_nickname}
        self.SET_ISIS_SMLT_PEER_SYSTEM_ID = {"constant": "set_isis_smlt_peer_system_id",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.set_isis_smlt_peer_system_id}
        self.SET_ISIS_SMLT_VIRTUAL_BMAC = {"constant": "set_isis_smlt_virtual_bmac",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_isis_smlt_virtual_bmac}
        self.SET_LOGICAL_INTERFACE_ISIS_INSTANCE_ID = {"constant": "set_logical_interface_isis_instance_id",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.set_logical_interface_isis_instance_id}
        self.SET_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE_BROADCAST = {"constant": "set_logical_interface_isis_interface_type_broadcast",
                                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                                    "link": self.link.set_logical_interface_isis_interface_type_broadcast}
        self.SET_LOGICAL_INTERFACE_ISIS_INTERFACE_TYPE_P2P = {"constant": "set_logical_interface_isis_interface_type_p2p",
                                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                              "link": self.link.set_logical_interface_isis_interface_type_p2p}
        self.SET_LOGICAL_INTERFACE_ISIS_L1_METRIC = {"constant": "set_logical_interface_isis_l1_metric",
                                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                     "link": self.link.set_logical_interface_isis_l1_metric}
        self.SET_MLT_ISIS_INSTANCE_ID = {"constant": "set_mlt_isis_instance_id",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.set_mlt_isis_instance_id}
        self.SET_MLT_ISIS_INTERFACE_TYPE_BROADCAST = {"constant": "set_mlt_isis_interface_type_broadcast",
                                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                      "link": self.link.set_mlt_isis_interface_type_broadcast}
        self.SET_MLT_ISIS_INTERFACE_TYPE_P2P = {"constant": "set_mlt_isis_interface_type_p2p",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.set_mlt_isis_interface_type_p2p}
        self.SET_MLT_ISIS_L1_METRIC = {"constant": "set_mlt_isis_l1_metric",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_mlt_isis_l1_metric}
        self.SET_PORT_ISIS_INSTANCE_ID = {"constant": "set_port_isis_instance_id",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.set_port_isis_instance_id}
        self.SET_PORT_ISIS_INTERFACE_TYPE_BROADCAST = {"constant": "set_port_isis_interface_type_broadcast",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.set_port_isis_interface_type_broadcast}
        self.SET_PORT_ISIS_INTERFACE_TYPE_P2P = {"constant": "set_port_isis_interface_type_p2p",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.set_port_isis_interface_type_p2p}
        self.SET_PORT_ISIS_L1_METRIC = {"constant": "set_port_isis_l1_metric",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_port_isis_l1_metric}
        self.SET_VIRTUAL_IST_PEER_IP = {"constant": "set_virtual_ist_peer_ip",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_virtual_ist_peer_ip}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_info}
        self.SHOW_ISID = {"constant": "show_isid",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_isid}
        self.SHOW_ISID_ALL = {"constant": "show_isid_all",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_isid_all}
        self.SHOW_ISID_ELAN = {"constant": "show_isid_elan",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_isid_elan}
        self.SHOW_ISID_ELAN_TRANSPARENT = {"constant": "show_isid_elan_transparent",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isid_elan_transparent}
        self.SHOW_ISID_MAC_ADDRESS_ENTRY = {"constant": "show_isid_mac_address_entry",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_isid_mac_address_entry}
        self.SHOW_ISID_MAC_ADDRESS_ENTRY_ALL = {"constant": "show_isid_mac_address_entry_all",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_isid_mac_address_entry_all}
        self.SHOW_ISID_MAC_ADDRESS_ENTRY_MAC = {"constant": "show_isid_mac_address_entry_mac",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_isid_mac_address_entry_mac}
        self.SHOW_ISID_MAC_ADDRESS_ENTRY_PORT = {"constant": "show_isid_mac_address_entry_port",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_isid_mac_address_entry_port}
        self.SHOW_ISID_MAC_ADDRESS_ENTRY_REMOTE = {"constant": "show_isid_mac_address_entry_remote",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.show_isid_mac_address_entry_remote}
        self.SHOW_ISIS_INFO = {"constant": "show_isis_info",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_isis_info}
        self.SHOW_ISIS_INTERFACE = {"constant": "show_isis_interface",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_isis_interface}
        self.SHOW_ISIS_IPV6_UNICAST_FIB = {"constant": "show_isis_ipv6_unicast_fib",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isis_ipv6_unicast_fib}
        self.SHOW_ISIS_IPV6_UNICAST_FIB_ID = {"constant": "show_isis_ipv6_unicast_fib_id",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_isis_ipv6_unicast_fib_id}
        self.SHOW_ISIS_IP_MULTICAST_FIB = {"constant": "show_isis_ip_multicast_fib",
                                           "tags": ["COMMAND_SNMP"],
                                           "link": self.link.show_isis_ip_multicast_fib}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE = {"constant": "show_isis_ip_multicast_route",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.show_isis_ip_multicast_route}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_ALL = {"constant": "show_isis_ip_multicast_route_all",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.show_isis_ip_multicast_route_all}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_DETAIL = {"constant": "show_isis_ip_multicast_route_detail",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.show_isis_ip_multicast_route_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_GROUP = {"constant": "show_isis_ip_multicast_route_group",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.show_isis_ip_multicast_route_group}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_GROUP_DETAIL = {"constant": "show_isis_ip_multicast_route_group_detail",
                                                          "tags": ["COMMAND_CLI"],
                                                          "link": self.link.show_isis_ip_multicast_route_group_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_GROUP_SOURCE = {"constant": "show_isis_ip_multicast_route_group_source",
                                                          "tags": ["COMMAND_CLI"],
                                                          "link": self.link.show_isis_ip_multicast_route_group_source}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_GROUP_SOURCE_BEB = {"constant": "show_isis_ip_multicast_route_group_source_beb",
                                                              "tags": ["COMMAND_CLI"],
                                                              "link": self.link.show_isis_ip_multicast_route_group_source_beb}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_GROUP_SOURCE_DETAIL = {"constant": "show_isis_ip_multicast_route_group_source_detail",
                                                                 "tags": ["COMMAND_CLI"],
                                                                 "link": self.link.show_isis_ip_multicast_route_group_source_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN = {"constant": "show_isis_ip_multicast_route_vlan",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.show_isis_ip_multicast_route_vlan}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_DETAIL = {"constant": "show_isis_ip_multicast_route_vlan_detail",
                                                         "tags": ["COMMAND_CLI"],
                                                         "link": self.link.show_isis_ip_multicast_route_vlan_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_GROUP = {"constant": "show_isis_ip_multicast_route_vlan_group",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.show_isis_ip_multicast_route_vlan_group}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_GROUP_DETAIL = {"constant": "show_isis_ip_multicast_route_vlan_group_detail",
                                                               "tags": ["COMMAND_CLI"],
                                                               "link": self.link.show_isis_ip_multicast_route_vlan_group_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_GROUP_SOURCE = {"constant": "show_isis_ip_multicast_route_vlan_group_source",
                                                               "tags": ["COMMAND_CLI"],
                                                               "link": self.link.show_isis_ip_multicast_route_vlan_group_source}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_GROUP_SOURCE_BEB = {"constant": "show_isis_ip_multicast_route_vlan_group_source_beb",
                                                                   "tags": ["COMMAND_CLI"],
                                                                   "link": self.link.show_isis_ip_multicast_route_vlan_group_source_beb}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VLAN_GROUP_SOURCE_DETAIL = {"constant": "show_isis_ip_multicast_route_vlan_group_source_detail",
                                                                      "tags": ["COMMAND_CLI"],
                                                                      "link": self.link.show_isis_ip_multicast_route_vlan_group_source_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VRF = {"constant": "show_isis_ip_multicast_route_vrf",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_isis_ip_multicast_route_vrf}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VRF_DETAIL = {"constant": "show_isis_ip_multicast_route_vrf_detail",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.show_isis_ip_multicast_route_vrf_detail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VRF_GROUP = {"constant": "show_isis_ip_multicast_route_vrf_group",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.show_isis_ip_multicast_route_vrf_group}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VSN_ISID = {"constant": "show_isis_ip_multicast_route_vsn_isid",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.show_isis_ip_multicast_route_vsn_isid}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VSN_ISID_ETAIL = {"constant": "show_isis_ip_multicast_route_vsn_isid_etail",
                                                            "tags": ["COMMAND_CLI"],
                                                            "link": self.link.show_isis_ip_multicast_route_vsn_isid_etail}
        self.SHOW_ISIS_IP_MULTICAST_ROUTE_VSN_ISID_GROUP = {"constant": "show_isis_ip_multicast_route_vsn_isid_group",
                                                            "tags": ["COMMAND_CLI"],
                                                            "link": self.link.show_isis_ip_multicast_route_vsn_isid_group}
        self.SHOW_ISIS_IP_UNICAST_FIB = {"constant": "show_isis_ip_unicast_fib",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.show_isis_ip_unicast_fib}
        self.SHOW_ISIS_IP_UNICAST_FIB_ID = {"constant": "show_isis_ip_unicast_fib_id",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_isis_ip_unicast_fib_id}
        self.SHOW_ISIS_IP_UNICAST_FIB_SPBM_NH_AS_MAC = {"constant": "show_isis_ip_unicast_fib_spbm_nh_as_mac",
                                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                        "link": self.link.show_isis_ip_unicast_fib_spbm_nh_as_mac}
        self.SHOW_ISIS_ISID_ALL = {"constant": "show_isis_isid_all",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_isis_isid_all}
        self.SHOW_ISIS_ISID_ALL_ID = {"constant": "show_isis_isid_all_id",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_isis_isid_all_id}
        self.SHOW_ISIS_ISID_ALL_NICKNAME = {"constant": "show_isis_isid_all_nickname",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_isis_isid_all_nickname}
        self.SHOW_ISIS_ISID_ALL_VLAN = {"constant": "show_isis_isid_all_vlan",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_isis_isid_all_vlan}
        self.SHOW_ISIS_ISID_CONFIG = {"constant": "show_isis_isid_config",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_isis_isid_config}
        self.SHOW_ISIS_ISID_CONFIG_ID = {"constant": "show_isis_isid_config_id",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_isis_isid_config_id}
        self.SHOW_ISIS_ISID_CONFIG_NICKNAME = {"constant": "show_isis_isid_config_nickname",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.show_isis_isid_config_nickname}
        self.SHOW_ISIS_ISID_CONFIG_VLAN = {"constant": "show_isis_isid_config_vlan",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isis_isid_config_vlan}
        self.SHOW_ISIS_ISID_DISCOVER = {"constant": "show_isis_isid_discover",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_isis_isid_discover}
        self.SHOW_ISIS_ISID_DISCOVER_ID = {"constant": "show_isis_isid_discover_id",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isis_isid_discover_id}
        self.SHOW_ISIS_ISID_DISCOVER_NICKNAME = {"constant": "show_isis_isid_discover_nickname",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_isis_isid_discover_nickname}
        self.SHOW_ISIS_ISID_DISCOVER_VLAN = {"constant": "show_isis_isid_discover_vlan",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_isis_isid_discover_vlan}
        self.SHOW_ISIS_MULTICAST = {"constant": "show_isis_multicast",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_isis_multicast}
        self.SHOW_ISIS_MULTICAST_FIB = {"constant": "show_isis_multicast_fib",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.show_isis_multicast_fib}
        self.SHOW_ISIS_MULTICAST_FIB_DETAIL = {"constant": "show_isis_multicast_fib_detail",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.show_isis_multicast_fib_detail}
        self.SHOW_ISIS_MULTICAST_FIB_ISID = {"constant": "show_isis_multicast_fib_isid",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_isis_multicast_fib_isid}
        self.SHOW_ISIS_MULTICAST_FIB_NICKNAME = {"constant": "show_isis_multicast_fib_nickname",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_isis_multicast_fib_nickname}
        self.SHOW_ISIS_MULTICAST_FIB_SUMMARY = {"constant": "show_isis_multicast_fib_summary",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_isis_multicast_fib_summary}
        self.SHOW_ISIS_MULTICAST_FIB_VLAN = {"constant": "show_isis_multicast_fib_vlan",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_isis_multicast_fib_vlan}
        self.SHOW_ISIS_NICKNAME = {"constant": "show_isis_nickname",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_isis_nickname}
        self.SHOW_ISIS_NICKNAME_SMLT_VIRTUAL_BMAC = {"constant": "show_isis_nickname_smlt_virtual_bmac",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.show_isis_nickname_smlt_virtual_bmac}
        self.SHOW_ISIS_NICKNAME_SYSID = {"constant": "show_isis_nickname_sysid",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_isis_nickname_sysid}
        self.SHOW_ISIS_UNICAST_FIB = {"constant": "show_isis_unicast_fib",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_isis_unicast_fib}
        self.SHOW_ISIS_UNICAST_FIB_BMAC = {"constant": "show_isis_unicast_fib_bmac",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isis_unicast_fib_bmac}
        self.SHOW_ISIS_UNICAST_FIB_SUMMARY = {"constant": "show_isis_unicast_fib_summary",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_isis_unicast_fib_summary}
        self.SHOW_ISIS_UNICAST_FIB_VLAN = {"constant": "show_isis_unicast_fib_vlan",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_isis_unicast_fib_vlan}
        self.SHOW_ISIS_UNICAST_TREE = {"constant": "show_isis_unicast_tree",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_isis_unicast_tree}
        self.SHOW_ISIS_UNICAST_TREE_DESTINATION = {"constant": "show_isis_unicast_tree_destination",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.show_isis_unicast_tree_destination}
        self.SHOW_VIRTUAL_IST = {"constant": "show_virtual_ist",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_virtual_ist}
        self.SHOW_VIRTUAL_IST_STAT = {"constant": "show_virtual_ist_stat",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_virtual_ist_stat}
