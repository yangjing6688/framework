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
        self.CHECK_ISIS_SPBM_ADJACENCIES_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_adjacencies_on_logical_interface",
                                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                 "link": self.link.check_isis_spbm_adjacencies_on_logical_interface}
        self.CHECK_ISIS_SPBM_ADJACENCIES_ON_MLT = {"constant": "check_isis_spbm_adjacencies_on_mlt",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_spbm_adjacencies_on_mlt}
        self.CHECK_ISIS_SPBM_ADJACENCIES_ON_PORT = {"constant": "check_isis_spbm_adjacencies_on_port",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_spbm_adjacencies_on_port}
        self.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_admin_status_on_logical_interface",
                                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                  "link": self.link.check_isis_spbm_admin_status_on_logical_interface}
        self.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_MLT = {"constant": "check_isis_spbm_admin_status_on_mlt",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_spbm_admin_status_on_mlt}
        self.CHECK_ISIS_SPBM_ADMIN_STATUS_ON_PORT = {"constant": "check_isis_spbm_admin_status_on_port",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_spbm_admin_status_on_port}
        self.CHECK_ISIS_SPBM_INSTANCE_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_instance_on_logical_interface",
                                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                              "link": self.link.check_isis_spbm_instance_on_logical_interface}
        self.CHECK_ISIS_SPBM_INSTANCE_ON_MLT = {"constant": "check_isis_spbm_instance_on_mlt",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_isis_spbm_instance_on_mlt}
        self.CHECK_ISIS_SPBM_INSTANCE_ON_PORT = {"constant": "check_isis_spbm_instance_on_port",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_isis_spbm_instance_on_port}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_DEST_NETWORK = {"constant": "check_isis_spbm_ipv6_unicast_fib_dest_network",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_isis_spbm_ipv6_unicast_fib_dest_network}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_BVLAN = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_bvlan",
                                                            "tags": ["PARSE_CLI"],
                                                            "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_bvlan}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_DEST_NETWORK = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_dest_network",
                                                                   "tags": ["PARSE_CLI"],
                                                                   "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_dest_network}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_NH_BEB = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_nh_beb",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_nh_beb}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_OUT_INT_PORT = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_out_int_port",
                                                                   "tags": ["PARSE_CLI"],
                                                                   "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_out_int_port}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_PREFIX_COST = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_prefix_cost",
                                                                  "tags": ["PARSE_CLI"],
                                                                  "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_prefix_cost}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_SPBM_COST = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_spbm_cost",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_spbm_cost}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_ISID_VRF_NAME = {"constant": "check_isis_spbm_ipv6_unicast_fib_isid_vrf_name",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_isis_spbm_ipv6_unicast_fib_isid_vrf_name}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_OUT_PORT = {"constant": "check_isis_spbm_ipv6_unicast_fib_out_port",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_isis_spbm_ipv6_unicast_fib_out_port}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_PREFIX_COST = {"constant": "check_isis_spbm_ipv6_unicast_fib_prefix_cost",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_isis_spbm_ipv6_unicast_fib_prefix_cost}
        self.CHECK_ISIS_SPBM_IPV6_UNICAST_FIB_SPBM_COST = {"constant": "check_isis_spbm_ipv6_unicast_fib_spbm_cost",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_isis_spbm_ipv6_unicast_fib_spbm_cost}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_BVLAN = {"constant": "check_isis_spbm_ip_unicast_fib_bvlan",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_spbm_ip_unicast_fib_bvlan}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_DESTINATION_ISID = {"constant": "check_isis_spbm_ip_unicast_fib_destination_isid",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_isis_spbm_ip_unicast_fib_destination_isid}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_DEST_NETWORK = {"constant": "check_isis_spbm_ip_unicast_fib_dest_network",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_spbm_ip_unicast_fib_dest_network}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ENTRY_EXISTS = {"constant": "check_isis_spbm_ip_unicast_fib_entry_exists",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_spbm_ip_unicast_fib_entry_exists}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_IP_ROUTE_PREFERENCE = {"constant": "check_isis_spbm_ip_unicast_fib_ip_route_preference",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_spbm_ip_unicast_fib_ip_route_preference}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_BVLAN = {"constant": "check_isis_spbm_ip_unicast_fib_isid_bvlan",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_isis_spbm_ip_unicast_fib_isid_bvlan}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK = {"constant": "check_isis_spbm_ip_unicast_fib_isid_dest_network",
                                                                 "tags": ["PARSE_CLI"],
                                                                 "link": self.link.check_isis_spbm_ip_unicast_fib_isid_dest_network}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_DEST_NETWORK_ISID = {"constant": "check_isis_spbm_ip_unicast_fib_isid_dest_network_isid",
                                                                      "tags": ["PARSE_CLI"],
                                                                      "link": self.link.check_isis_spbm_ip_unicast_fib_isid_dest_network_isid}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_IP_ROUTE_PREF = {"constant": "check_isis_spbm_ip_unicast_fib_isid_ip_route_pref",
                                                                  "tags": ["PARSE_CLI"],
                                                                  "link": self.link.check_isis_spbm_ip_unicast_fib_isid_ip_route_pref}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_NH_BEB = {"constant": "check_isis_spbm_ip_unicast_fib_isid_nh_beb",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_isis_spbm_ip_unicast_fib_isid_nh_beb}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_OUT_INT_PORT = {"constant": "check_isis_spbm_ip_unicast_fib_isid_out_int_port",
                                                                 "tags": ["PARSE_CLI"],
                                                                 "link": self.link.check_isis_spbm_ip_unicast_fib_isid_out_int_port}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_PREFIX_COST = {"constant": "check_isis_spbm_ip_unicast_fib_isid_prefix_cost",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.check_isis_spbm_ip_unicast_fib_isid_prefix_cost}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_PREFIX_TYPE = {"constant": "check_isis_spbm_ip_unicast_fib_isid_prefix_type",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.check_isis_spbm_ip_unicast_fib_isid_prefix_type}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_SPBM_COST = {"constant": "check_isis_spbm_ip_unicast_fib_isid_spbm_cost",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_isis_spbm_ip_unicast_fib_isid_spbm_cost}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_VRF_ISID = {"constant": "check_isis_spbm_ip_unicast_fib_isid_vrf_isid",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_isis_spbm_ip_unicast_fib_isid_vrf_isid}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_ISID_VRF_NAME = {"constant": "check_isis_spbm_ip_unicast_fib_isid_vrf_name",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_isis_spbm_ip_unicast_fib_isid_vrf_name}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_NH_MAC = {"constant": "check_isis_spbm_ip_unicast_fib_nh_mac",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_spbm_ip_unicast_fib_nh_mac}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_OUT_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_ip_unicast_fib_out_logical_interface",
                                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                     "link": self.link.check_isis_spbm_ip_unicast_fib_out_logical_interface}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_OUT_PORT = {"constant": "check_isis_spbm_ip_unicast_fib_out_port",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_spbm_ip_unicast_fib_out_port}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_COST = {"constant": "check_isis_spbm_ip_unicast_fib_prefix_cost",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_spbm_ip_unicast_fib_prefix_cost}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE = {"constant": "check_isis_spbm_ip_unicast_fib_prefix_type",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_spbm_ip_unicast_fib_prefix_type}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE_EXTERNAL = {"constant": "check_isis_spbm_ip_unicast_fib_prefix_type_external",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_spbm_ip_unicast_fib_prefix_type_external}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_PREFIX_TYPE_INTERNAL = {"constant": "check_isis_spbm_ip_unicast_fib_prefix_type_internal",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_spbm_ip_unicast_fib_prefix_type_internal}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_SPBM_COST = {"constant": "check_isis_spbm_ip_unicast_fib_spbm_cost",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_isis_spbm_ip_unicast_fib_spbm_cost}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_ISID = {"constant": "check_isis_spbm_ip_unicast_fib_vrf_isid",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_spbm_ip_unicast_fib_vrf_isid}
        self.CHECK_ISIS_SPBM_IP_UNICAST_FIB_VRF_NAME = {"constant": "check_isis_spbm_ip_unicast_fib_vrf_name",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_isis_spbm_ip_unicast_fib_vrf_name}
        self.CHECK_ISIS_SPBM_L1_METRIC_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_l1_metric_on_logical_interface",
                                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                               "link": self.link.check_isis_spbm_l1_metric_on_logical_interface}
        self.CHECK_ISIS_SPBM_L1_METRIC_ON_MLT = {"constant": "check_isis_spbm_l1_metric_on_mlt",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_isis_spbm_l1_metric_on_mlt}
        self.CHECK_ISIS_SPBM_L1_METRIC_ON_PORT = {"constant": "check_isis_spbm_l1_metric_on_port",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_spbm_l1_metric_on_port}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_CVLAN = {"constant": "check_isis_spbm_multicast_fib_cvlan",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_isis_spbm_multicast_fib_cvlan}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_HOST_NAME = {"constant": "check_isis_spbm_multicast_fib_host_name",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_spbm_multicast_fib_host_name}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_IN_MLTS = {"constant": "check_isis_spbm_multicast_fib_in_mlts",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_spbm_multicast_fib_in_mlts}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_IN_PORTS = {"constant": "check_isis_spbm_multicast_fib_in_ports",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_spbm_multicast_fib_in_ports}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_ISID = {"constant": "check_isis_spbm_multicast_fib_isid",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_spbm_multicast_fib_isid}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_OUT_MLTS = {"constant": "check_isis_spbm_multicast_fib_out_mlts",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_spbm_multicast_fib_out_mlts}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_OUT_PORTS = {"constant": "check_isis_spbm_multicast_fib_out_ports",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_spbm_multicast_fib_out_ports}
        self.CHECK_ISIS_SPBM_MULTICAST_FIB_TYPE = {"constant": "check_isis_spbm_multicast_fib_type",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_spbm_multicast_fib_type}
        self.CHECK_ISIS_SPBM_MULTICAST_FWD_CACHE_TIMEOUT = {"constant": "check_isis_spbm_multicast_fwd_cache_timeout",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_spbm_multicast_fwd_cache_timeout}
        self.CHECK_ISIS_SPBM_OPER_STATUS_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_oper_status_on_logical_interface",
                                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                 "link": self.link.check_isis_spbm_oper_status_on_logical_interface}
        self.CHECK_ISIS_SPBM_OPER_STATUS_ON_MLT = {"constant": "check_isis_spbm_oper_status_on_mlt",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_spbm_oper_status_on_mlt}
        self.CHECK_ISIS_SPBM_OPER_STATUS_ON_PORT = {"constant": "check_isis_spbm_oper_status_on_port",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_spbm_oper_status_on_port}
        self.CHECK_ISIS_SPBM_SMLT_SPLIT_BEB_PRIMARY = {"constant": "check_isis_spbm_smlt_split_beb_primary",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_spbm_smlt_split_beb_primary}
        self.CHECK_ISIS_SPBM_SMLT_SPLIT_BEB_SECONDARY = {"constant": "check_isis_spbm_smlt_split_beb_secondary",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_isis_spbm_smlt_split_beb_secondary}
        self.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_type_broadcast_on_logical_interface",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_spbm_type_broadcast_on_logical_interface}
        self.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_MLT = {"constant": "check_isis_spbm_type_broadcast_on_mlt",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_spbm_type_broadcast_on_mlt}
        self.CHECK_ISIS_SPBM_TYPE_BROADCAST_ON_PORT = {"constant": "check_isis_spbm_type_broadcast_on_port",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_spbm_type_broadcast_on_port}
        self.CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_type_point_to_point_on_logical_interface",
                                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                         "link": self.link.check_isis_spbm_type_point_to_point_on_logical_interface}
        self.CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_MLT = {"constant": "check_isis_spbm_type_point_to_point_on_mlt",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_spbm_type_point_to_point_on_mlt}
        self.CHECK_ISIS_SPBM_TYPE_POINT_TO_POINT_ON_PORT = {"constant": "check_isis_spbm_type_point_to_point_on_port",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_spbm_type_point_to_point_on_port}
        self.CHECK_ISIS_SPBM_UNICAST_FIB_COST = {"constant": "check_isis_spbm_unicast_fib_cost",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_isis_spbm_unicast_fib_cost}
        self.CHECK_ISIS_SPBM_UNICAST_FIB_HOST_NAME = {"constant": "check_isis_spbm_unicast_fib_host_name",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_spbm_unicast_fib_host_name}
        self.CHECK_ISIS_SPBM_UNICAST_FIB_OUTGOING_INTERFACE = {"constant": "check_isis_spbm_unicast_fib_outgoing_interface",
                                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                               "link": self.link.check_isis_spbm_unicast_fib_outgoing_interface}
        self.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_LOGICAL_INTERFACE = {"constant": "check_isis_spbm_up_adjacencies_on_logical_interface",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_spbm_up_adjacencies_on_logical_interface}
        self.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_MLT = {"constant": "check_isis_spbm_up_adjacencies_on_mlt",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_spbm_up_adjacencies_on_mlt}
        self.CHECK_ISIS_SPBM_UP_ADJACENCIES_ON_PORT = {"constant": "check_isis_spbm_up_adjacencies_on_port",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_spbm_up_adjacencies_on_port}
        self.CHECK_SPBM_ETHERTYPE = {"constant": "check_spbm_ethertype",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_spbm_ethertype}
        self.VERIFY_ISIS_SPBM_BVID = {"constant": "verify_isis_spbm_bvid",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.verify_isis_spbm_bvid}
        self.VERIFY_ISIS_SPBM_INSTANCE_ID = {"constant": "verify_isis_spbm_instance_id",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_isis_spbm_instance_id}
        self.VERIFY_ISIS_SPBM_MULTICAST_ENABLED = {"constant": "verify_isis_spbm_multicast_enabled",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.verify_isis_spbm_multicast_enabled}
        self.VERIFY_ISIS_SPBM_NICK_NAME = {"constant": "verify_isis_spbm_nick_name",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.verify_isis_spbm_nick_name}
        self.VERIFY_ISIS_SPBM_SMLT_PEER_SYSTEM_ID = {"constant": "verify_isis_spbm_smlt_peer_system_id",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.verify_isis_spbm_smlt_peer_system_id}
        self.VERIFY_ISIS_SPBM_SMLT_VIRTUAL_BMAC = {"constant": "verify_isis_spbm_smlt_virtual_bmac",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.verify_isis_spbm_smlt_virtual_bmac}
        self.VERIFY_SPBM_ENABLED = {"constant": "verify_spbm_enabled",
                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                    "link": self.link.verify_spbm_enabled}
        self.VERIFY_SPBM_IPV6_ENABLED = {"constant": "verify_spbm_ipv6_enabled",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.verify_spbm_ipv6_enabled}
        self.VERIFY_SPBM_IP_ENABLED = {"constant": "verify_spbm_ip_enabled",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.verify_spbm_ip_enabled}
        self.VERIFY_SPBM_LSDB_TRAP_ENABLED = {"constant": "verify_spbm_lsdb_trap_enabled",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.verify_spbm_lsdb_trap_enabled}
        self.VERIFY_VIRTUAL_IST_PEER_IP = {"constant": "verify_virtual_ist_peer_ip",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_virtual_ist_peer_ip}
