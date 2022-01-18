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
        self.CLEAR_MLT_MGMT_ISID = {"constant": "clear_mlt_mgmt_isid",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.clear_mlt_mgmt_isid}
        self.CLEAR_PORT_MGMT_ISID = {"constant": "clear_port_mgmt_isid",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.clear_port_mgmt_isid}
        self.CLEAR_ZERO_TOUCH_CLIENT = {"constant": "clear_zero_touch_client",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.clear_zero_touch_client}
        self.DELETE_MLT = {"constant": "delete_mlt",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.delete_mlt}
        self.DELETE_PORT = {"constant": "delete_port",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.delete_port}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_global}
        self.DISABLE_MLT = {"constant": "disable_mlt",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.disable_mlt}
        self.DISABLE_MLT_AUTH = {"constant": "disable_mlt_auth",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.disable_mlt_auth}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_port}
        self.DISABLE_PORT_AUTH = {"constant": "disable_port_auth",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.disable_port_auth}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_global}
        self.ENABLE_MLT = {"constant": "enable_mlt",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.enable_mlt}
        self.ENABLE_MLT_AUTH = {"constant": "enable_mlt_auth",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.enable_mlt_auth}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_port}
        self.ENABLE_PORT_AUTH = {"constant": "enable_port_auth",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.enable_port_auth}
        self.SET_ASSIGNMENT_TIMEOUT = {"constant": "set_assignment_timeout",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_assignment_timeout}
        self.SET_DISCOVERY_TIMEOUT = {"constant": "set_discovery_timeout",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.set_discovery_timeout}
        self.SET_MLT_AUTH_KEY = {"constant": "set_mlt_auth_key",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.set_mlt_auth_key}
        self.SET_MLT_MGMT_ISID = {"constant": "set_mlt_mgmt_isid",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_mlt_mgmt_isid}
        self.SET_MLT_MGMT_ISID_AND_CVID = {"constant": "set_mlt_mgmt_isid_and_cvid",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_mlt_mgmt_isid_and_cvid}
        self.SET_PORT_AUTH_KEY = {"constant": "set_port_auth_key",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_port_auth_key}
        self.SET_PORT_MGMT_ISID = {"constant": "set_port_mgmt_isid",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_port_mgmt_isid}
        self.SET_PORT_MGMT_ISID_AND_CVID = {"constant": "set_port_mgmt_isid_and_cvid",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.set_port_mgmt_isid_and_cvid}
        self.SET_ZERO_TOUCH_CLIENT_ISID = {"constant": "set_zero_touch_client_isid",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_zero_touch_client_isid}
        self.SHOW_AGENT = {"constant": "show_agent",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_agent}
        self.SHOW_AGENT_TIMEOUT = {"constant": "show_agent_timeout",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_agent_timeout}
        self.SHOW_ASSIGNMENT_PORT = {"constant": "show_assignment_port",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_assignment_port}
        self.SHOW_AUTO_PROVISION_SETTING = {"constant": "show_auto_provision_setting",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_auto_provision_setting}
        self.SHOW_CLIENT_PROXY_STATUS = {"constant": "show_client_proxy_status",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_client_proxy_status}
        self.SHOW_ELEMENTS = {"constant": "show_elements",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_elements}
        self.SHOW_ELEMENTS_PORT = {"constant": "show_elements_port",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_elements_port}
        self.SHOW_ELEMENT_TYPE = {"constant": "show_element_type",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_element_type}
        self.SHOW_EXTENDED_LOGGING_STATUS = {"constant": "show_extended_logging_status",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_extended_logging_status}
        self.SHOW_GLOBAL_TIMEOUTS = {"constant": "show_global_timeouts",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_global_timeouts}
        self.SHOW_ISID = {"constant": "show_isid",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_isid}
        self.SHOW_MLT = {"constant": "show_mlt",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.show_mlt}
        self.SHOW_NEIGHBORS = {"constant": "show_neighbors",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_neighbors}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_port}
        self.SHOW_PRIMARY_SERVER_ID = {"constant": "show_primary_server_id",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_primary_server_id}
        self.SHOW_PROVISION_MODE = {"constant": "show_provision_mode",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_provision_mode}
        self.SHOW_SERVER_DESCRIPTION = {"constant": "show_server_description",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_server_description}
        self.SHOW_SERVICE_STATE = {"constant": "show_service_state",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_service_state}
        self.SHOW_STANDALONE_PROXY_STATUS = {"constant": "show_standalone_proxy_status",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_standalone_proxy_status}
        self.SHOW_STATS_GLOBAL = {"constant": "show_stats_global",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_stats_global}
        self.SHOW_STATS_PORT = {"constant": "show_stats_port",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_stats_port}
        self.SHOW_ZERO_TOUCH_CLIENT = {"constant": "show_zero_touch_client",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_zero_touch_client}
        self.SHOW_ZERO_TOUCH_STATUS = {"constant": "show_zero_touch_status",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_zero_touch_status}
