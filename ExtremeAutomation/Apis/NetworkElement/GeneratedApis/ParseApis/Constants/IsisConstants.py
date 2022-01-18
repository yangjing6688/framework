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
        self.CHECK_ENABLE_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "check_enable_isis_circuit_on_logical_interface",
                                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                               "link": self.link.check_enable_isis_circuit_on_logical_interface}
        self.CHECK_ENABLE_ISIS_CIRCUIT_ON_MLT = {"constant": "check_enable_isis_circuit_on_mlt",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_enable_isis_circuit_on_mlt}
        self.CHECK_ENABLE_ISIS_CIRCUIT_ON_PORT = {"constant": "check_enable_isis_circuit_on_port",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_enable_isis_circuit_on_port}
        self.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_holdtime_on_logical_interface",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_adjacency_holdtime_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_MLT = {"constant": "check_isis_adjacency_holdtime_on_mlt",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_adjacency_holdtime_on_mlt}
        self.CHECK_ISIS_ADJACENCY_HOLDTIME_ON_PORT = {"constant": "check_isis_adjacency_holdtime_on_port",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_adjacency_holdtime_on_port}
        self.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_hostname_on_logical_interface",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_adjacency_hostname_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_MLT = {"constant": "check_isis_adjacency_hostname_on_mlt",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_adjacency_hostname_on_mlt}
        self.CHECK_ISIS_ADJACENCY_HOSTNAME_ON_PORT = {"constant": "check_isis_adjacency_hostname_on_port",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_adjacency_hostname_on_port}
        self.CHECK_ISIS_ADJACENCY_LEVEL_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_level_on_logical_interface",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_isis_adjacency_level_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_LEVEL_ON_MLT = {"constant": "check_isis_adjacency_level_on_mlt",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_adjacency_level_on_mlt}
        self.CHECK_ISIS_ADJACENCY_LEVEL_ON_PORT = {"constant": "check_isis_adjacency_level_on_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_adjacency_level_on_port}
        self.CHECK_ISIS_ADJACENCY_PRIORITY_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_priority_on_logical_interface",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_adjacency_priority_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_PRIORITY_ON_MLT = {"constant": "check_isis_adjacency_priority_on_mlt",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_adjacency_priority_on_mlt}
        self.CHECK_ISIS_ADJACENCY_PRIORITY_ON_PORT = {"constant": "check_isis_adjacency_priority_on_port",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_adjacency_priority_on_port}
        self.CHECK_ISIS_ADJACENCY_STATE_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_state_on_logical_interface",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_isis_adjacency_state_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_STATE_ON_MLT = {"constant": "check_isis_adjacency_state_on_mlt",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_adjacency_state_on_mlt}
        self.CHECK_ISIS_ADJACENCY_STATE_ON_PORT = {"constant": "check_isis_adjacency_state_on_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_adjacency_state_on_port}
        self.CHECK_ISIS_ADJACENCY_STATUS_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_status_on_logical_interface",
                                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                 "link": self.link.check_isis_adjacency_status_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_STATUS_ON_MLT = {"constant": "check_isis_adjacency_status_on_mlt",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_adjacency_status_on_mlt}
        self.CHECK_ISIS_ADJACENCY_STATUS_ON_PORT = {"constant": "check_isis_adjacency_status_on_port",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_adjacency_status_on_port}
        self.CHECK_ISIS_ADJACENCY_SYSID_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_sysid_on_logical_interface",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_isis_adjacency_sysid_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_SYSID_ON_MLT = {"constant": "check_isis_adjacency_sysid_on_mlt",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_adjacency_sysid_on_mlt}
        self.CHECK_ISIS_ADJACENCY_SYSID_ON_PORT = {"constant": "check_isis_adjacency_sysid_on_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_adjacency_sysid_on_port}
        self.CHECK_ISIS_ADJACENCY_UPTIME_ON_LOGICAL_INTERFACE = {"constant": "check_isis_adjacency_uptime_on_logical_interface",
                                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                 "link": self.link.check_isis_adjacency_uptime_on_logical_interface}
        self.CHECK_ISIS_ADJACENCY_UPTIME_ON_MLT = {"constant": "check_isis_adjacency_uptime_on_mlt",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_isis_adjacency_uptime_on_mlt}
        self.CHECK_ISIS_ADJACENCY_UPTIME_ON_PORT = {"constant": "check_isis_adjacency_uptime_on_port",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_adjacency_uptime_on_port}
        self.CHECK_ISIS_AUTHENTICATION_KEY_FAILS = {"constant": "check_isis_authentication_key_fails",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_authentication_key_fails}
        self.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_LOGICAL_INTERFACE = {"constant": "check_isis_circuit_auth_key_id_on_logical_interface",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_circuit_auth_key_id_on_logical_interface}
        self.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_MLT = {"constant": "check_isis_circuit_auth_key_id_on_mlt",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_circuit_auth_key_id_on_mlt}
        self.CHECK_ISIS_CIRCUIT_AUTH_KEY_ID_ON_PORT = {"constant": "check_isis_circuit_auth_key_id_on_port",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_circuit_auth_key_id_on_port}
        self.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_LOGICAL_INTERFACE = {"constant": "check_isis_circuit_auth_type_on_logical_interface",
                                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                  "link": self.link.check_isis_circuit_auth_type_on_logical_interface}
        self.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_MLT = {"constant": "check_isis_circuit_auth_type_on_mlt",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_circuit_auth_type_on_mlt}
        self.CHECK_ISIS_CIRCUIT_AUTH_TYPE_ON_PORT = {"constant": "check_isis_circuit_auth_type_on_port",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_circuit_auth_type_on_port}
        self.CHECK_ISIS_CIRCUIT_ON_LOGICAL_INTERFACE = {"constant": "check_isis_circuit_on_logical_interface",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_circuit_on_logical_interface}
        self.CHECK_ISIS_CIRCUIT_ON_MLT = {"constant": "check_isis_circuit_on_mlt",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_isis_circuit_on_mlt}
        self.CHECK_ISIS_CIRCUIT_ON_PORT = {"constant": "check_isis_circuit_on_port",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_isis_circuit_on_port}
        self.CHECK_ISIS_CORRUPTED_LSPS = {"constant": "check_isis_corrupted_lsps",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_isis_corrupted_lsps}
        self.CHECK_ISIS_ID_LENGTH_MISMATCHES = {"constant": "check_isis_id_length_mismatches",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_isis_id_length_mismatches}
        self.CHECK_ISIS_IPV4_SOURCE_ADDRESS = {"constant": "check_isis_ipv4_source_address",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_isis_ipv4_source_address}
        self.CHECK_ISIS_IPV4_TUNNEL_SOURCE_ADDRESS = {"constant": "check_isis_ipv4_tunnel_source_address",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_ipv4_tunnel_source_address}
        self.CHECK_ISIS_IPV6_SOURCE_ADDRESS = {"constant": "check_isis_ipv6_source_address",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_isis_ipv6_source_address}
        self.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_LOGICAL_INTERFACE = {"constant": "check_isis_l1_dr_hello_interval_on_logical_interface",
                                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                     "link": self.link.check_isis_l1_dr_hello_interval_on_logical_interface}
        self.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_MLT = {"constant": "check_isis_l1_dr_hello_interval_on_mlt",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_l1_dr_hello_interval_on_mlt}
        self.CHECK_ISIS_L1_DR_HELLO_INTERVAL_ON_PORT = {"constant": "check_isis_l1_dr_hello_interval_on_port",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_l1_dr_hello_interval_on_port}
        self.CHECK_ISIS_L1_HELLO_INTERVAL_ON_LOGICAL_INTERFACE = {"constant": "check_isis_l1_hello_interval_on_logical_interface",
                                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                  "link": self.link.check_isis_l1_hello_interval_on_logical_interface}
        self.CHECK_ISIS_L1_HELLO_INTERVAL_ON_MLT = {"constant": "check_isis_l1_hello_interval_on_mlt",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_l1_hello_interval_on_mlt}
        self.CHECK_ISIS_L1_HELLO_INTERVAL_ON_PORT = {"constant": "check_isis_l1_hello_interval_on_port",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_l1_hello_interval_on_port}
        self.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_LOGICAL_INTERFACE = {"constant": "check_isis_l1_hello_multiplier_on_logical_interface",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_l1_hello_multiplier_on_logical_interface}
        self.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_MLT = {"constant": "check_isis_l1_hello_multiplier_on_mlt",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_l1_hello_multiplier_on_mlt}
        self.CHECK_ISIS_L1_HELLO_MULTIPLIER_ON_PORT = {"constant": "check_isis_l1_hello_multiplier_on_port",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_l1_hello_multiplier_on_port}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_CSNPS_RECEIVED = {"constant": "check_isis_l1_logical_interface_is_is_csnps_received",
                                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                     "link": self.link.check_isis_l1_logical_interface_is_is_csnps_received}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_CSNPS_TRANSMITTED = {"constant": "check_isis_l1_logical_interface_is_is_csnps_transmitted",
                                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                        "link": self.link.check_isis_l1_logical_interface_is_is_csnps_transmitted}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_HELLOS_RECEIVED = {"constant": "check_isis_l1_logical_interface_is_is_hellos_received",
                                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                      "link": self.link.check_isis_l1_logical_interface_is_is_hellos_received}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_HELLOS_TRANSMITTED = {"constant": "check_isis_l1_logical_interface_is_is_hellos_transmitted",
                                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                         "link": self.link.check_isis_l1_logical_interface_is_is_hellos_transmitted}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_LSPS_RECEIVED = {"constant": "check_isis_l1_logical_interface_is_is_lsps_received",
                                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                    "link": self.link.check_isis_l1_logical_interface_is_is_lsps_received}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_LSPS_TRANSMITTED = {"constant": "check_isis_l1_logical_interface_is_is_lsps_transmitted",
                                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                       "link": self.link.check_isis_l1_logical_interface_is_is_lsps_transmitted}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_PSNPS_RECEIVED = {"constant": "check_isis_l1_logical_interface_is_is_psnps_received",
                                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                     "link": self.link.check_isis_l1_logical_interface_is_is_psnps_received}
        self.CHECK_ISIS_L1_LOGICAL_INTERFACE_IS_IS_PSNPS_TRANSMITTED = {"constant": "check_isis_l1_logical_interface_is_is_psnps_transmitted",
                                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                        "link": self.link.check_isis_l1_logical_interface_is_is_psnps_transmitted}
        self.CHECK_ISIS_L1_MLT_IS_IS_CSNPS_RECEIVED = {"constant": "check_isis_l1_mlt_is_is_csnps_received",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_l1_mlt_is_is_csnps_received}
        self.CHECK_ISIS_L1_MLT_IS_IS_CSNPS_TRANSMITTED = {"constant": "check_isis_l1_mlt_is_is_csnps_transmitted",
                                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                          "link": self.link.check_isis_l1_mlt_is_is_csnps_transmitted}
        self.CHECK_ISIS_L1_MLT_IS_IS_HELLOS_RECEIVED = {"constant": "check_isis_l1_mlt_is_is_hellos_received",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_l1_mlt_is_is_hellos_received}
        self.CHECK_ISIS_L1_MLT_IS_IS_HELLOS_TRANSMITTED = {"constant": "check_isis_l1_mlt_is_is_hellos_transmitted",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_l1_mlt_is_is_hellos_transmitted}
        self.CHECK_ISIS_L1_MLT_IS_IS_LSPS_RECEIVED = {"constant": "check_isis_l1_mlt_is_is_lsps_received",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_l1_mlt_is_is_lsps_received}
        self.CHECK_ISIS_L1_MLT_IS_IS_LSPS_TRANSMITTED = {"constant": "check_isis_l1_mlt_is_is_lsps_transmitted",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_isis_l1_mlt_is_is_lsps_transmitted}
        self.CHECK_ISIS_L1_MLT_IS_IS_PSNPS_RECEIVED = {"constant": "check_isis_l1_mlt_is_is_psnps_received",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_l1_mlt_is_is_psnps_received}
        self.CHECK_ISIS_L1_MLT_IS_IS_PSNPS_TRANSMITTED = {"constant": "check_isis_l1_mlt_is_is_psnps_transmitted",
                                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                          "link": self.link.check_isis_l1_mlt_is_is_psnps_transmitted}
        self.CHECK_ISIS_L1_PORT_IS_IS_CSNPS_RECEIVED = {"constant": "check_isis_l1_port_is_is_csnps_received",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_l1_port_is_is_csnps_received}
        self.CHECK_ISIS_L1_PORT_IS_IS_CSNPS_TRANSMITTED = {"constant": "check_isis_l1_port_is_is_csnps_transmitted",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_l1_port_is_is_csnps_transmitted}
        self.CHECK_ISIS_L1_PORT_IS_IS_HELLOS_RECEIVED = {"constant": "check_isis_l1_port_is_is_hellos_received",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_isis_l1_port_is_is_hellos_received}
        self.CHECK_ISIS_L1_PORT_IS_IS_HELLOS_TRANSMITTED = {"constant": "check_isis_l1_port_is_is_hellos_transmitted",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_l1_port_is_is_hellos_transmitted}
        self.CHECK_ISIS_L1_PORT_IS_IS_LSPS_RECEIVED = {"constant": "check_isis_l1_port_is_is_lsps_received",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_isis_l1_port_is_is_lsps_received}
        self.CHECK_ISIS_L1_PORT_IS_IS_LSPS_TRANSMITTED = {"constant": "check_isis_l1_port_is_is_lsps_transmitted",
                                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                          "link": self.link.check_isis_l1_port_is_is_lsps_transmitted}
        self.CHECK_ISIS_L1_PORT_IS_IS_PSNPS_RECEIVED = {"constant": "check_isis_l1_port_is_is_psnps_received",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_isis_l1_port_is_is_psnps_received}
        self.CHECK_ISIS_L1_PORT_IS_IS_PSNPS_TRANSMITTED = {"constant": "check_isis_l1_port_is_is_psnps_transmitted",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_l1_port_is_is_psnps_transmitted}
        self.CHECK_ISIS_LOGICAL_INTERFACE_ADJACENCY_CHANGES = {"constant": "check_isis_logical_interface_adjacency_changes",
                                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                               "link": self.link.check_isis_logical_interface_adjacency_changes}
        self.CHECK_ISIS_LOGICAL_INTERFACE_AUTHENTICATION_FAILS = {"constant": "check_isis_logical_interface_authentication_fails",
                                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                  "link": self.link.check_isis_logical_interface_authentication_fails}
        self.CHECK_ISIS_LOGICAL_INTERFACE_DESIGNATED_IS_CHANGES = {"constant": "check_isis_logical_interface_designated_is_changes",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_logical_interface_designated_is_changes}
        self.CHECK_ISIS_LOGICAL_INTERFACE_ID_FIELD_LENGTH_MISMATCHES = {"constant": "check_isis_logical_interface_id_field_length_mismatches",
                                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                        "link": self.link.check_isis_logical_interface_id_field_length_mismatches}
        self.CHECK_ISIS_LOGICAL_INTERFACE_INITIALIZATION_FAILS = {"constant": "check_isis_logical_interface_initialization_fails",
                                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                  "link": self.link.check_isis_logical_interface_initialization_fails}
        self.CHECK_ISIS_LOGICAL_INTERFACE_MAX_AREA_ADDRESS_MISMATCHES = {"constant": "check_isis_logical_interface_max_area_address_mismatches",
                                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                         "link": self.link.check_isis_logical_interface_max_area_address_mismatches}
        self.CHECK_ISIS_LOGICAL_INTERFACE_REJECTED_ADJANCENCIES = {"constant": "check_isis_logical_interface_rejected_adjancencies",
                                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                   "link": self.link.check_isis_logical_interface_rejected_adjancencies}
        self.CHECK_ISIS_LSDB_IP_AND_HOSTNAME = {"constant": "check_isis_lsdb_ip_and_hostname",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_isis_lsdb_ip_and_hostname}
        self.CHECK_ISIS_LSP_DATABASE_OVERLOADS = {"constant": "check_isis_lsp_database_overloads",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_lsp_database_overloads}
        self.CHECK_ISIS_MANUAL_ADDRESSES_DROPPED_FROM_AREA = {"constant": "check_isis_manual_addresses_dropped_from_area",
                                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                              "link": self.link.check_isis_manual_addresses_dropped_from_area}
        self.CHECK_ISIS_MAXIMUM_SEQUENCE_NUMBER_EXCEEDED_ATTEMPTS = {"constant": "check_isis_maximum_sequence_number_exceeded_attempts",
                                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                     "link": self.link.check_isis_maximum_sequence_number_exceeded_attempts}
        self.CHECK_ISIS_MLT_ADJACENCY_CHANGES = {"constant": "check_isis_mlt_adjacency_changes",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_isis_mlt_adjacency_changes}
        self.CHECK_ISIS_MLT_AUTHENTICATION_FAILS = {"constant": "check_isis_mlt_authentication_fails",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_mlt_authentication_fails}
        self.CHECK_ISIS_MLT_DESIGNATED_IS_CHANGES = {"constant": "check_isis_mlt_designated_is_changes",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_mlt_designated_is_changes}
        self.CHECK_ISIS_MLT_ID_FIELD_LENGTH_MISMATCHES = {"constant": "check_isis_mlt_id_field_length_mismatches",
                                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                          "link": self.link.check_isis_mlt_id_field_length_mismatches}
        self.CHECK_ISIS_MLT_INITIALIZATION_FAILS = {"constant": "check_isis_mlt_initialization_fails",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_isis_mlt_initialization_fails}
        self.CHECK_ISIS_MLT_MAX_AREA_ADDRESS_MISMATCHES = {"constant": "check_isis_mlt_max_area_address_mismatches",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_mlt_max_area_address_mismatches}
        self.CHECK_ISIS_MLT_REJECTED_ADJANCENCIES = {"constant": "check_isis_mlt_rejected_adjancencies",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_mlt_rejected_adjancencies}
        self.CHECK_ISIS_OWN_LSP_PURGES = {"constant": "check_isis_own_lsp_purges",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_isis_own_lsp_purges}
        self.CHECK_ISIS_PARTITION_CHANGES = {"constant": "check_isis_partition_changes",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_isis_partition_changes}
        self.CHECK_ISIS_PORT_ADJACENCY_CHANGES = {"constant": "check_isis_port_adjacency_changes",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_isis_port_adjacency_changes}
        self.CHECK_ISIS_PORT_AUTHENTICATION_FAILS = {"constant": "check_isis_port_authentication_fails",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_port_authentication_fails}
        self.CHECK_ISIS_PORT_DESIGNATED_IS_CHANGES = {"constant": "check_isis_port_designated_is_changes",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_port_designated_is_changes}
        self.CHECK_ISIS_PORT_ID_FIELD_LENGTH_MISMATCHES = {"constant": "check_isis_port_id_field_length_mismatches",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_isis_port_id_field_length_mismatches}
        self.CHECK_ISIS_PORT_INITIALIZATION_FAILS = {"constant": "check_isis_port_initialization_fails",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_isis_port_initialization_fails}
        self.CHECK_ISIS_PORT_MAX_AREA_ADDRESS_MISMATCHES = {"constant": "check_isis_port_max_area_address_mismatches",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_isis_port_max_area_address_mismatches}
        self.CHECK_ISIS_PORT_REJECTED_ADJANCENCIES = {"constant": "check_isis_port_rejected_adjancencies",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_isis_port_rejected_adjancencies}
        self.CHECK_ISIS_SEQUENCE_NUMBER_SKIPS = {"constant": "check_isis_sequence_number_skips",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_isis_sequence_number_skips}
        self.VERIFY_ISIS_GLOBALLY_DISABLED = {"constant": "verify_isis_globally_disabled",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.verify_isis_globally_disabled}
        self.VERIFY_ISIS_GLOBALLY_ENABLED = {"constant": "verify_isis_globally_enabled",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_isis_globally_enabled}
        self.VERIFY_ISIS_INBAND_MGMT_IP = {"constant": "verify_isis_inband_mgmt_ip",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.verify_isis_inband_mgmt_ip}
        self.VERIFY_ISIS_IP_SOURCE_ADDRESS = {"constant": "verify_isis_ip_source_address",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.verify_isis_ip_source_address}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_IPV4 = {"constant": "verify_isis_logical_interface_ipv4",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.verify_isis_logical_interface_ipv4}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_MLT = {"constant": "verify_isis_logical_interface_mlt",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.verify_isis_logical_interface_mlt}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_MLT_NAME = {"constant": "verify_isis_logical_interface_mlt_name",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.verify_isis_logical_interface_mlt_name}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_NAME = {"constant": "verify_isis_logical_interface_name",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.verify_isis_logical_interface_name}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_PORT = {"constant": "verify_isis_logical_interface_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.verify_isis_logical_interface_port}
        self.VERIFY_ISIS_LOGICAL_INTERFACE_PORT_NAME = {"constant": "verify_isis_logical_interface_port_name",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.verify_isis_logical_interface_port_name}
        self.VERIFY_ISIS_MANUAL_AREA = {"constant": "verify_isis_manual_area",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.verify_isis_manual_area}
        self.VERIFY_ISIS_METRIC_NARROW = {"constant": "verify_isis_metric_narrow",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.verify_isis_metric_narrow}
        self.VERIFY_ISIS_METRIC_WIDE = {"constant": "verify_isis_metric_wide",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.verify_isis_metric_wide}
        self.VERIFY_ISIS_OVERLOAD = {"constant": "verify_isis_overload",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.verify_isis_overload}
        self.VERIFY_ISIS_REDISTRIBUTE_BGP = {"constant": "verify_isis_redistribute_bgp",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_isis_redistribute_bgp}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT = {"constant": "verify_isis_redistribute_direct",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.verify_isis_redistribute_direct}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_DISABLED = {"constant": "verify_isis_redistribute_direct_disabled",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.verify_isis_redistribute_direct_disabled}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ENABLED = {"constant": "verify_isis_redistribute_direct_enabled",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.verify_isis_redistribute_direct_enabled}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_IPV6_DISABLED = {"constant": "verify_isis_redistribute_direct_ipv6_disabled",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.verify_isis_redistribute_direct_ipv6_disabled}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_IPV6_ENABLED = {"constant": "verify_isis_redistribute_direct_ipv6_enabled",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.verify_isis_redistribute_direct_ipv6_enabled}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY = {"constant": "verify_isis_redistribute_direct_route_map_policy",
                                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                 "link": self.link.verify_isis_redistribute_direct_route_map_policy}
        self.VERIFY_ISIS_REDISTRIBUTE_DIRECT_ROUTE_MAP_POLICY_CLEAR = {"constant": "verify_isis_redistribute_direct_route_map_policy_clear",
                                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                       "link": self.link.verify_isis_redistribute_direct_route_map_policy_clear}
        self.VERIFY_ISIS_REDISTRIBUTE_OSPF = {"constant": "verify_isis_redistribute_ospf",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.verify_isis_redistribute_ospf}
        self.VERIFY_ISIS_REDISTRIBUTE_RIP = {"constant": "verify_isis_redistribute_rip",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_isis_redistribute_rip}
        self.VERIFY_ISIS_REDISTRIBUTE_STATIC = {"constant": "verify_isis_redistribute_static",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.verify_isis_redistribute_static}
        self.VERIFY_ISIS_SPF_DELAY = {"constant": "verify_isis_spf_delay",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.verify_isis_spf_delay}
        self.VERIFY_ISIS_SYS_ID = {"constant": "verify_isis_sys_id",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.verify_isis_sys_id}
        self.VERIFY_ISIS_SYS_NAME = {"constant": "verify_isis_sys_name",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.verify_isis_sys_name}
