"""
This class outlines all the constants for the isis API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IsisConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IsisConstants(ApiConstants):
    def __init__(self):
        super(IsisConstants, self).__init__()
        self.CLEAR_AUTH_ON_LOGICAL_INTERFACE = {"constant": "clear_auth_on_logical_interface",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.clear_auth_on_logical_interface}
        self.CLEAR_AUTH_ON_MLT = {"constant": "clear_auth_on_mlt",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.clear_auth_on_mlt}
        self.CLEAR_AUTH_ON_PORT = {"constant": "clear_auth_on_port",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.clear_auth_on_port}
        self.CLEAR_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "clear_circuit_on_logical_interface",
                                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                   "link": self.link.clear_circuit_on_logical_interface}
        self.CLEAR_CIRCUIT_ON_MLT = {"constant": "clear_circuit_on_mlt",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.clear_circuit_on_mlt}
        self.CLEAR_CIRCUIT_ON_PORT = {"constant": "clear_circuit_on_port",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.clear_circuit_on_port}
        self.CLEAR_INBAND_MGMT_IP = {"constant": "clear_inband_mgmt_ip",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_inband_mgmt_ip}
        self.CLEAR_IPV4_SOURCE_ADDRESS = {"constant": "clear_ipv4_source_address",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_ipv4_source_address}
        self.CLEAR_IPV4_TUNNEL_SOURCE_ADDRESS = {"constant": "clear_ipv4_tunnel_source_address",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.clear_ipv4_tunnel_source_address}
        self.CLEAR_IPV6_SOURCE_ADDRESS = {"constant": "clear_ipv6_source_address",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_ipv6_source_address}
        self.CLEAR_LOGICAL_INTERFACE = {"constant": "clear_logical_interface",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.clear_logical_interface}
        self.CLEAR_MANUAL_AREA = {"constant": "clear_manual_area",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.clear_manual_area}
        self.CLEAR_METRIC_NARROW = {"constant": "clear_metric_narrow",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_metric_narrow}
        self.CLEAR_METRIC_WIDE = {"constant": "clear_metric_wide",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_metric_wide}
        self.CLEAR_OVERLOAD = {"constant": "clear_overload",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_overload}
        self.CLEAR_REDISTRIBUTE_BGP = {"constant": "clear_redistribute_bgp",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.clear_redistribute_bgp}
        self.CLEAR_REDISTRIBUTE_DIRECT = {"constant": "clear_redistribute_direct",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_redistribute_direct}
        self.CLEAR_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY = {"constant": "clear_redistribute_direct_route_map_policy",
                                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                           "link": self.link.clear_redistribute_direct_route_map_policy}
        self.CLEAR_REDISTRIBUTE_OSPF = {"constant": "clear_redistribute_ospf",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.clear_redistribute_ospf}
        self.CLEAR_REDISTRIBUTE_RIP = {"constant": "clear_redistribute_rip",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.clear_redistribute_rip}
        self.CLEAR_REDISTRIBUTE_STATIC = {"constant": "clear_redistribute_static",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_redistribute_static}
        self.CLEAR_SPF_DELAY = {"constant": "clear_spf_delay",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.clear_spf_delay}
        self.CLEAR_SYSTEM_ID = {"constant": "clear_system_id",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.clear_system_id}
        self.CLEAR_SYS_NAME = {"constant": "clear_sys_name",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.clear_sys_name}
        self.DISABLE_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "disable_circuit_on_logical_interface",
                                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                     "link": self.link.disable_circuit_on_logical_interface}
        self.DISABLE_CIRCUIT_ON_MLT = {"constant": "disable_circuit_on_mlt",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.disable_circuit_on_mlt}
        self.DISABLE_CIRCUIT_ON_PORT = {"constant": "disable_circuit_on_port",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.disable_circuit_on_port}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_global}
        self.DISABLE_REDISTRIBUTE_BGP = {"constant": "disable_redistribute_bgp",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.disable_redistribute_bgp}
        self.DISABLE_REDISTRIBUTE_DIRECT = {"constant": "disable_redistribute_direct",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.disable_redistribute_direct}
        self.DISABLE_REDISTRIBUTE_DIRECT_IPV6 = {"constant": "disable_redistribute_direct_ipv6",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.disable_redistribute_direct_ipv6}
        self.DISABLE_REDISTRIBUTE_OSPF = {"constant": "disable_redistribute_ospf",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.disable_redistribute_ospf}
        self.DISABLE_REDISTRIBUTE_RIP = {"constant": "disable_redistribute_rip",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.disable_redistribute_rip}
        self.DISABLE_REDISTRIBUTE_STATIC = {"constant": "disable_redistribute_static",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.disable_redistribute_static}
        self.ENABLE_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "enable_circuit_on_logical_interface",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.enable_circuit_on_logical_interface}
        self.ENABLE_CIRCUIT_ON_MLT = {"constant": "enable_circuit_on_mlt",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.enable_circuit_on_mlt}
        self.ENABLE_CIRCUIT_ON_PORT = {"constant": "enable_circuit_on_port",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.enable_circuit_on_port}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_global}
        self.ENABLE_REDISTRIBUTE_BGP = {"constant": "enable_redistribute_bgp",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.enable_redistribute_bgp}
        self.ENABLE_REDISTRIBUTE_DIRECT = {"constant": "enable_redistribute_direct",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.enable_redistribute_direct}
        self.ENABLE_REDISTRIBUTE_DIRECT_IPV6 = {"constant": "enable_redistribute_direct_ipv6",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.enable_redistribute_direct_ipv6}
        self.ENABLE_REDISTRIBUTE_OSPF = {"constant": "enable_redistribute_ospf",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.enable_redistribute_ospf}
        self.ENABLE_REDISTRIBUTE_RIP = {"constant": "enable_redistribute_rip",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.enable_redistribute_rip}
        self.ENABLE_REDISTRIBUTE_STATIC = {"constant": "enable_redistribute_static",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.enable_redistribute_static}
        self.SET_AUTH_ON_LOGICAL_INTERFACE = {"constant": "set_auth_on_logical_interface",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.set_auth_on_logical_interface}
        self.SET_AUTH_ON_MLT = {"constant": "set_auth_on_mlt",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_auth_on_mlt}
        self.SET_AUTH_ON_PORT = {"constant": "set_auth_on_port",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.set_auth_on_port}
        self.SET_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "set_circuit_on_logical_interface",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.set_circuit_on_logical_interface}
        self.SET_CIRCUIT_ON_MLT = {"constant": "set_circuit_on_mlt",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_circuit_on_mlt}
        self.SET_CIRCUIT_ON_PORT = {"constant": "set_circuit_on_port",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_circuit_on_port}
        self.SET_INBAND_MGMT_IP = {"constant": "set_inband_mgmt_ip",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_inband_mgmt_ip}
        self.SET_IPV4_SOURCE_ADDRESS = {"constant": "set_ipv4_source_address",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_ipv4_source_address}
        self.SET_IPV4_TUNNEL_SOURCE_ADDRESS = {"constant": "set_ipv4_tunnel_source_address",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.set_ipv4_tunnel_source_address}
        self.SET_IPV6_SOURCE_ADDRESS = {"constant": "set_ipv6_source_address",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_ipv6_source_address}
        self.SET_L1_DR_PRIORITY_ON_LOGICAL_INTERFACE = {"constant": "set_l1_dr_priority_on_logical_interface",
                                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                        "link": self.link.set_l1_dr_priority_on_logical_interface}
        self.SET_L1_DR_PRIORITY_ON_MLT = {"constant": "set_l1_dr_priority_on_mlt",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.set_l1_dr_priority_on_mlt}
        self.SET_L1_DR_PRIORITY_ON_PORT = {"constant": "set_l1_dr_priority_on_port",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_l1_dr_priority_on_port}
        self.SET_L1_HELLO_INTERVAL_ON_LOGICAL_INTERFACE = {"constant": "set_l1_hello_interval_on_logical_interface",
                                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                           "link": self.link.set_l1_hello_interval_on_logical_interface}
        self.SET_L1_HELLO_INTERVAL_ON_MLT = {"constant": "set_l1_hello_interval_on_mlt",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.set_l1_hello_interval_on_mlt}
        self.SET_L1_HELLO_INTERVAL_ON_PORT = {"constant": "set_l1_hello_interval_on_port",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.set_l1_hello_interval_on_port}
        self.SET_L1_HELLO_MULTIPLIER_ON_LOGICAL_INTERFACE = {"constant": "set_l1_hello_multiplier_on_logical_interface",
                                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                             "link": self.link.set_l1_hello_multiplier_on_logical_interface}
        self.SET_L1_HELLO_MULTIPLIER_ON_MLT = {"constant": "set_l1_hello_multiplier_on_mlt",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.set_l1_hello_multiplier_on_mlt}
        self.SET_L1_HELLO_MULTIPLIER_ON_PORT = {"constant": "set_l1_hello_multiplier_on_port",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.set_l1_hello_multiplier_on_port}
        self.SET_LOGICAL_INTERFACE_IPV4 = {"constant": "set_logical_interface_ipv4",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_logical_interface_ipv4}
        self.SET_LOGICAL_INTERFACE_IPV4_NAME = {"constant": "set_logical_interface_ipv4_name",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.set_logical_interface_ipv4_name}
        self.SET_LOGICAL_INTERFACE_MLT = {"constant": "set_logical_interface_mlt",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.set_logical_interface_mlt}
        self.SET_LOGICAL_INTERFACE_MLT_NAME = {"constant": "set_logical_interface_mlt_name",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.set_logical_interface_mlt_name}
        self.SET_LOGICAL_INTERFACE_PORT = {"constant": "set_logical_interface_port",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_logical_interface_port}
        self.SET_LOGICAL_INTERFACE_PORT_NAME = {"constant": "set_logical_interface_port_name",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.set_logical_interface_port_name}
        self.SET_MANUAL_AREA = {"constant": "set_manual_area",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_manual_area}
        self.SET_METRIC_NARROW = {"constant": "set_metric_narrow",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_metric_narrow}
        self.SET_METRIC_WIDE = {"constant": "set_metric_wide",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_metric_wide}
        self.SET_OVERLOAD = {"constant": "set_overload",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_overload}
        self.SET_REDISTRIBUTE_APPLY = {"constant": "set_redistribute_apply",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_redistribute_apply}
        self.SET_REDISTRIBUTE_BGP = {"constant": "set_redistribute_bgp",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_redistribute_bgp}
        self.SET_REDISTRIBUTE_DIRECT = {"constant": "set_redistribute_direct",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_redistribute_direct}
        self.SET_REDISTRIBUTE_DIRECT_APPLY = {"constant": "set_redistribute_direct_apply",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.set_redistribute_direct_apply}
        self.SET_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY = {"constant": "set_redistribute_direct_route_map_policy",
                                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                         "link": self.link.set_redistribute_direct_route_map_policy}
        self.SET_REDISTRIBUTE_OSPF = {"constant": "set_redistribute_ospf",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.set_redistribute_ospf}
        self.SET_REDISTRIBUTE_RIP = {"constant": "set_redistribute_rip",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_redistribute_rip}
        self.SET_REDISTRIBUTE_STATIC = {"constant": "set_redistribute_static",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_redistribute_static}
        self.SET_SPF_DELAY = {"constant": "set_spf_delay",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_spf_delay}
        self.SET_SYSTEM_ID = {"constant": "set_system_id",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_system_id}
        self.SET_SYS_NAME = {"constant": "set_sys_name",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.set_sys_name}
        self.SHOW_ADJACENCIES = {"constant": "show_adjacencies",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_adjacencies}
        self.SHOW_AREA = {"constant": "show_area",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_area}
        self.SHOW_CIRCUIT = {"constant": "show_circuit",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.show_circuit}
        self.SHOW_CIRCUIT_INTERFACES = {"constant": "show_circuit_interfaces",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.show_circuit_interfaces}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_info}
        self.SHOW_INTERFACE = {"constant": "show_interface",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_interface}
        self.SHOW_INTERFACE_AUTH = {"constant": "show_interface_auth",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_interface_auth}
        self.SHOW_INTERFACE_L1 = {"constant": "show_interface_l1",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_interface_l1}
        self.SHOW_INTERFACE_L12 = {"constant": "show_interface_l12",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_interface_l12}
        self.SHOW_INTERFACE_L1_PACKET_STATS = {"constant": "show_interface_l1_packet_stats",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.show_interface_l1_packet_stats}
        self.SHOW_INTERFACE_L2 = {"constant": "show_interface_l2",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_interface_l2}
        self.SHOW_INTERFACE_L2_PACKET_STATS = {"constant": "show_interface_l2_packet_stats",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.show_interface_l2_packet_stats}
        self.SHOW_INTERFACE_STATS = {"constant": "show_interface_stats",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_interface_stats}
        self.SHOW_INTERFACE_TIMERS = {"constant": "show_interface_timers",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_interface_timers}
        self.SHOW_IPV6_REDISTRIBUTE = {"constant": "show_ipv6_redistribute",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_ipv6_redistribute}
        self.SHOW_IP_REDISTRIBUTE = {"constant": "show_ip_redistribute",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_ip_redistribute}
        self.SHOW_LOGICAL_INTERFACE = {"constant": "show_logical_interface",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_logical_interface}
        self.SHOW_LOGICAL_INTERFACE_NAME = {"constant": "show_logical_interface_name",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.show_logical_interface_name}
        self.SHOW_LSDB = {"constant": "show_lsdb",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_lsdb}
        self.SHOW_LSDB_IP_UNICAST = {"constant": "show_lsdb_ip_unicast",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_lsdb_ip_unicast}
        self.SHOW_MANUAL_AREA = {"constant": "show_manual_area",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_manual_area}
        self.SHOW_NET = {"constant": "show_net",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_net}
        self.SHOW_SPB_MCAST_SUMMARY = {"constant": "show_spb_mcast_summary",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_spb_mcast_summary}
        self.SHOW_STATISTICS = {"constant": "show_statistics",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_statistics}
        self.SHOW_SYSTEM_STATS = {"constant": "show_system_stats",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_system_stats}
        self.SHOW_SYS_ID = {"constant": "show_sys_id",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.show_sys_id}
