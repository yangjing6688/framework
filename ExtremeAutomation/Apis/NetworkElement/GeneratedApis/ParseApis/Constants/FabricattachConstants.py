"""
This class outlines all the constants for the fabricattach API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(FabricattachConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class FabricattachConstants(ApiConstants):
    def __init__(self):
        super(FabricattachConstants, self).__init__()
        self.CHECK_FA_AGENT_TIMEOUT = {"constant": "check_fa_agent_timeout",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_fa_agent_timeout}
        self.CHECK_FA_ASSIGNMENT_TIMEOUT = {"constant": "check_fa_assignment_timeout",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_fa_assignment_timeout}
        self.CHECK_FA_ASSIGN_ISID_TO_VLAN = {"constant": "check_fa_assign_isid_to_vlan",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_fa_assign_isid_to_vlan}
        self.CHECK_FA_ASSIGN_ISID_TO_VLAN_ORIGIN = {"constant": "check_fa_assign_isid_to_vlan_origin",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_fa_assign_isid_to_vlan_origin}
        self.CHECK_FA_ASSIGN_ISID_TO_VLAN_STATE = {"constant": "check_fa_assign_isid_to_vlan_state",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_fa_assign_isid_to_vlan_state}
        self.CHECK_FA_AUTO_PROVISION_SETTING = {"constant": "check_fa_auto_provision_setting",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_fa_auto_provision_setting}
        self.CHECK_FA_CLIENT_PROXY_STATUS = {"constant": "check_fa_client_proxy_status",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_fa_client_proxy_status}
        self.CHECK_FA_DISCOVERY_TIMEOUT = {"constant": "check_fa_discovery_timeout",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_fa_discovery_timeout}
        self.CHECK_FA_DISC_ELEMENT_ASSIGNED_OPER_AUTH = {"constant": "check_fa_disc_element_assigned_oper_auth",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_fa_disc_element_assigned_oper_auth}
        self.CHECK_FA_DISC_ELEMENT_ASSIGN_AUTH = {"constant": "check_fa_disc_element_assign_auth",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_fa_disc_element_assign_auth}
        self.CHECK_FA_DISC_ELEMENT_AUTH = {"constant": "check_fa_disc_element_auth",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_fa_disc_element_auth}
        self.CHECK_FA_DISC_ELEMENT_OPER_AUTH = {"constant": "check_fa_disc_element_oper_auth",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_fa_disc_element_oper_auth}
        self.CHECK_FA_DISC_ELEMENT_STATE = {"constant": "check_fa_disc_element_state",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_fa_disc_element_state}
        self.CHECK_FA_DISC_ELEMENT_SYSTEM_ID = {"constant": "check_fa_disc_element_system_id",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_fa_disc_element_system_id}
        self.CHECK_FA_DISC_ELEMENT_TYPE = {"constant": "check_fa_disc_element_type",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_fa_disc_element_type}
        self.CHECK_FA_DISC_ELEMENT_VLAN = {"constant": "check_fa_disc_element_vlan",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_fa_disc_element_vlan}
        self.CHECK_FA_ELEMENTS_AUTO_PROVISION = {"constant": "check_fa_elements_auto_provision",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fa_elements_auto_provision}
        self.CHECK_FA_ELEMENTS_MGMT_VLAN = {"constant": "check_fa_elements_mgmt_vlan",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_fa_elements_mgmt_vlan}
        self.CHECK_FA_ELEMENTS_PORT = {"constant": "check_fa_elements_port",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_fa_elements_port}
        self.CHECK_FA_ELEMENTS_SYSTEM_ID = {"constant": "check_fa_elements_system_id",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_fa_elements_system_id}
        self.CHECK_FA_ELEMENTS_TAG = {"constant": "check_fa_elements_tag",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_fa_elements_tag}
        self.CHECK_FA_ELEMENTS_TYPE = {"constant": "check_fa_elements_type",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_fa_elements_type}
        self.CHECK_FA_ELEMENT_TYPE = {"constant": "check_fa_element_type",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.check_fa_element_type}
        self.CHECK_FA_EXTENDED_LOGGING_STATUS = {"constant": "check_fa_extended_logging_status",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fa_extended_logging_status}
        self.CHECK_FA_GLOBAL_STATS_ASGN_ACCEPTED = {"constant": "check_fa_global_stats_asgn_accepted",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_fa_global_stats_asgn_accepted}
        self.CHECK_FA_GLOBAL_STATS_ASGN_AUTH_FAILED = {"constant": "check_fa_global_stats_asgn_auth_failed",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_fa_global_stats_asgn_auth_failed}
        self.CHECK_FA_GLOBAL_STATS_ASGN_DELETED = {"constant": "check_fa_global_stats_asgn_deleted",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_fa_global_stats_asgn_deleted}
        self.CHECK_FA_GLOBAL_STATS_ASGN_EXPIRED = {"constant": "check_fa_global_stats_asgn_expired",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_fa_global_stats_asgn_expired}
        self.CHECK_FA_GLOBAL_STATS_ASGN_RECEIVED = {"constant": "check_fa_global_stats_asgn_received",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_fa_global_stats_asgn_received}
        self.CHECK_FA_GLOBAL_STATS_ASGN_REJECTED = {"constant": "check_fa_global_stats_asgn_rejected",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_fa_global_stats_asgn_rejected}
        self.CHECK_FA_GLOBAL_STATS_DISC_AUTH_FAILED = {"constant": "check_fa_global_stats_disc_auth_failed",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_fa_global_stats_disc_auth_failed}
        self.CHECK_FA_GLOBAL_STATS_DISC_ELEM_DELETED = {"constant": "check_fa_global_stats_disc_elem_deleted",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_fa_global_stats_disc_elem_deleted}
        self.CHECK_FA_GLOBAL_STATS_DISC_ELEM_EXPIRED = {"constant": "check_fa_global_stats_disc_elem_expired",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_fa_global_stats_disc_elem_expired}
        self.CHECK_FA_GLOBAL_STATS_DISC_ELEM_RECEIVED = {"constant": "check_fa_global_stats_disc_elem_received",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_fa_global_stats_disc_elem_received}
        self.CHECK_FA_ISID_MLT_CVID = {"constant": "check_fa_isid_mlt_cvid",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.check_fa_isid_mlt_cvid}
        self.CHECK_FA_ISID_MLT_ISID_TYPE = {"constant": "check_fa_isid_mlt_isid_type",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_fa_isid_mlt_isid_type}
        self.CHECK_FA_ISID_MLT_ORIGIN = {"constant": "check_fa_isid_mlt_origin",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_fa_isid_mlt_origin}
        self.CHECK_FA_ISID_MLT_PLAT_VLAN = {"constant": "check_fa_isid_mlt_plat_vlan",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_fa_isid_mlt_plat_vlan}
        self.CHECK_FA_ISID_PORT_CVID = {"constant": "check_fa_isid_port_cvid",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_fa_isid_port_cvid}
        self.CHECK_FA_ISID_PORT_ISID_TYPE = {"constant": "check_fa_isid_port_isid_type",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_fa_isid_port_isid_type}
        self.CHECK_FA_ISID_PORT_ORIGIN = {"constant": "check_fa_isid_port_origin",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_fa_isid_port_origin}
        self.CHECK_FA_ISID_PORT_PLAT_VLAN = {"constant": "check_fa_isid_port_plat_vlan",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_fa_isid_port_plat_vlan}
        self.CHECK_FA_MANAGEMENT_ISID_AND_CVID_ON_MLT = {"constant": "check_fa_management_isid_and_cvid_on_mlt",
                                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                         "link": self.link.check_fa_management_isid_and_cvid_on_mlt}
        self.CHECK_FA_MANAGEMENT_ISID_AND_CVID_ON_PORT = {"constant": "check_fa_management_isid_and_cvid_on_port",
                                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                          "link": self.link.check_fa_management_isid_and_cvid_on_port}
        self.CHECK_FA_MANAGEMENT_ISID_ON_MLT = {"constant": "check_fa_management_isid_on_mlt",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_fa_management_isid_on_mlt}
        self.CHECK_FA_MANAGEMENT_ISID_ON_PORT = {"constant": "check_fa_management_isid_on_port",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_fa_management_isid_on_port}
        self.CHECK_FA_MLT_AUTHENTICATION_STATUS = {"constant": "check_fa_mlt_authentication_status",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_fa_mlt_authentication_status}
        self.CHECK_FA_MLT_EXISTS = {"constant": "check_fa_mlt_exists",
                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                    "link": self.link.check_fa_mlt_exists}
        self.CHECK_FA_MLT_SERVER_STATUS = {"constant": "check_fa_mlt_server_status",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_fa_mlt_server_status}
        self.CHECK_FA_NEIGHBORS = {"constant": "check_fa_neighbors",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_fa_neighbors}
        self.CHECK_FA_PORT_AUTHENTICATION_STATUS = {"constant": "check_fa_port_authentication_status",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_fa_port_authentication_status}
        self.CHECK_FA_PORT_EXISTS = {"constant": "check_fa_port_exists",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_fa_port_exists}
        self.CHECK_FA_PORT_SERVER_STATUS = {"constant": "check_fa_port_server_status",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_fa_port_server_status}
        self.CHECK_FA_PORT_STATS_ASGN_ACCEPTED = {"constant": "check_fa_port_stats_asgn_accepted",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_fa_port_stats_asgn_accepted}
        self.CHECK_FA_PORT_STATS_ASGN_AUTH_FAILED = {"constant": "check_fa_port_stats_asgn_auth_failed",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_fa_port_stats_asgn_auth_failed}
        self.CHECK_FA_PORT_STATS_ASGN_DELETED = {"constant": "check_fa_port_stats_asgn_deleted",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_fa_port_stats_asgn_deleted}
        self.CHECK_FA_PORT_STATS_ASGN_EXPIRED = {"constant": "check_fa_port_stats_asgn_expired",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_fa_port_stats_asgn_expired}
        self.CHECK_FA_PORT_STATS_ASGN_RECEIVED = {"constant": "check_fa_port_stats_asgn_received",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_fa_port_stats_asgn_received}
        self.CHECK_FA_PORT_STATS_ASGN_REJECTED = {"constant": "check_fa_port_stats_asgn_rejected",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_fa_port_stats_asgn_rejected}
        self.CHECK_FA_PORT_STATS_DISC_AUTH_FAILED = {"constant": "check_fa_port_stats_disc_auth_failed",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_fa_port_stats_disc_auth_failed}
        self.CHECK_FA_PORT_STATS_DISC_ELEM_DELETED = {"constant": "check_fa_port_stats_disc_elem_deleted",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_fa_port_stats_disc_elem_deleted}
        self.CHECK_FA_PORT_STATS_DISC_ELEM_EXPIRED = {"constant": "check_fa_port_stats_disc_elem_expired",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_fa_port_stats_disc_elem_expired}
        self.CHECK_FA_PORT_STATS_DISC_ELEM_RECEIVED = {"constant": "check_fa_port_stats_disc_elem_received",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_fa_port_stats_disc_elem_received}
        self.CHECK_FA_PORT_STATS_ELEM_DELETED = {"constant": "check_fa_port_stats_elem_deleted",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fa_port_stats_elem_deleted}
        self.CHECK_FA_PRIMARY_SERVER_ID = {"constant": "check_fa_primary_server_id",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_fa_primary_server_id}
        self.CHECK_FA_PROVISION_MODE = {"constant": "check_fa_provision_mode",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_fa_provision_mode}
        self.CHECK_FA_SERVER_DESCRIPTION = {"constant": "check_fa_server_description",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_fa_server_description}
        self.CHECK_FA_SERVICE_STATE = {"constant": "check_fa_service_state",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.check_fa_service_state}
        self.CHECK_FA_STANDALONE_PROXY_STATUS = {"constant": "check_fa_standalone_proxy_status",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fa_standalone_proxy_status}
        self.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_ISID = {"constant": "check_fa_zero_touch_client_auto_attach_isid",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_fa_zero_touch_client_auto_attach_isid}
        self.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_NAME = {"constant": "check_fa_zero_touch_client_auto_attach_name",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_fa_zero_touch_client_auto_attach_name}
        self.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_VLAN = {"constant": "check_fa_zero_touch_client_auto_attach_vlan",
                                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                            "link": self.link.check_fa_zero_touch_client_auto_attach_vlan}
        self.CHECK_FA_ZERO_TOUCH_STATUS = {"constant": "check_fa_zero_touch_status",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_fa_zero_touch_status}
