"""
This class outlines all the constants for the snmp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SnmpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SnmpConstants(ApiConstants):
    def __init__(self):
        super(SnmpConstants, self).__init__()
        self.CLEAR_NOTIFY = {"constant": "clear_notify",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.clear_notify}
        self.CLEAR_NOTIFY_FILTER = {"constant": "clear_notify_filter",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_notify_filter}
        self.CLEAR_TRAP_PARAM = {"constant": "clear_trap_param",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_trap_param}
        self.CREATE_ALL_TRAP_SERVER = {"constant": "create_all_trap_server",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_all_trap_server}
        self.CREATE_GROUP_AND_ACCESS = {"constant": "create_group_and_access",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.create_group_and_access}
        self.CREATE_READONLY_COMMUNITY = {"constant": "create_readonly_community",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.create_readonly_community}
        self.CREATE_READWRITE_COMMUNITY = {"constant": "create_readwrite_community",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.create_readwrite_community}
        self.CREATE_V1_TRAP_SERVER = {"constant": "create_v1_trap_server",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.create_v1_trap_server}
        self.CREATE_V2C_INFORM_SERVER = {"constant": "create_v2c_inform_server",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.create_v2c_inform_server}
        self.CREATE_V2C_TRAP_SERVER = {"constant": "create_v2c_trap_server",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_v2c_trap_server}
        self.CREATE_V3_INFORM_SERVER = {"constant": "create_v3_inform_server",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.create_v3_inform_server}
        self.CREATE_V3_TRAP_SERVER = {"constant": "create_v3_trap_server",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.create_v3_trap_server}
        self.CREATE_VIEW = {"constant": "create_view",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.create_view}
        self.DELETE_COMMUNITY = {"constant": "delete_community",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.delete_community}
        self.DELETE_GROUP_AND_ACCESS = {"constant": "delete_group_and_access",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.delete_group_and_access}
        self.DELETE_TRAP_SERVERS = {"constant": "delete_trap_servers",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.delete_trap_servers}
        self.DELETE_USER = {"constant": "delete_user",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.delete_user}
        self.DELETE_USER_ENGINE_ID = {"constant": "delete_user_engine_id",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.delete_user_engine_id}
        self.DELETE_V1_TRAP_SERVER = {"constant": "delete_v1_trap_server",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.delete_v1_trap_server}
        self.DELETE_V2C_INFORM_SERVER = {"constant": "delete_v2c_inform_server",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.delete_v2c_inform_server}
        self.DELETE_V2C_TRAP_SERVER = {"constant": "delete_v2c_trap_server",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.delete_v2c_trap_server}
        self.DELETE_V3_INFORM_SERVER = {"constant": "delete_v3_inform_server",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.delete_v3_inform_server}
        self.DELETE_V3_TRAP_SERVER = {"constant": "delete_v3_trap_server",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.delete_v3_trap_server}
        self.DELETE_VIEW = {"constant": "delete_view",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.delete_view}
        self.DISABLE_ACCESS_GLOBAL = {"constant": "disable_access_global",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_access_global}
        self.DISABLE_AUTHENTICATION_TRAP = {"constant": "disable_authentication_trap",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_authentication_trap}
        self.DISABLE_SAME_SNMP_AND_IP_SENDER_FLAG = {"constant": "disable_same_snmp_and_ip_sender_flag",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.disable_same_snmp_and_ip_sender_flag}
        self.DISABLE_SAME_SNMP_TRAP_SENDER_IP = {"constant": "disable_same_snmp_trap_sender_ip",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.disable_same_snmp_trap_sender_ip}
        self.ENABLE_ACCESS_GLOBAL = {"constant": "enable_access_global",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_access_global}
        self.ENABLE_AUTHENTICATION_TRAP = {"constant": "enable_authentication_trap",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_authentication_trap}
        self.ENABLE_SAME_SNMP_AND_IP_SENDER_FLAG = {"constant": "enable_same_snmp_and_ip_sender_flag",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.enable_same_snmp_and_ip_sender_flag}
        self.ENABLE_SAME_SNMP_TRAP_SENDER_IP = {"constant": "enable_same_snmp_trap_sender_ip",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.enable_same_snmp_trap_sender_ip}
        self.SET_NOTIFY = {"constant": "set_notify",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.set_notify}
        self.SET_NOTIFY_FILTER = {"constant": "set_notify_filter",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_notify_filter}
        self.SET_TRAP_PARAM = {"constant": "set_trap_param",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_trap_param}
        self.SET_USER_AUTHENTICATION = {"constant": "set_user_authentication",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_user_authentication}
        self.SET_USER_AUTHENTICATION_ENGINE_ID = {"constant": "set_user_authentication_engine_id",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.set_user_authentication_engine_id}
        self.SET_USER_NO_AUTHENTICATION = {"constant": "set_user_no_authentication",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_user_no_authentication}
        self.SET_USER_NO_AUTHENTICATION_ENGINE_ID = {"constant": "set_user_no_authentication_engine_id",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_user_no_authentication_engine_id}
        self.SET_USER_PRIVACY = {"constant": "set_user_privacy",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_user_privacy}
        self.SET_USER_PRIVACY_ENGINE_ID = {"constant": "set_user_privacy_engine_id",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_user_privacy_engine_id}
        self.SHOW_ACCESS = {"constant": "show_access",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_access}
        self.SHOW_COMMUNITY = {"constant": "show_community",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_community}
        self.SHOW_CONTEXT = {"constant": "show_context",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_context}
        self.SHOW_GLOBALS = {"constant": "show_globals",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_globals}
        self.SHOW_GROUP = {"constant": "show_group",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_group}
        self.SHOW_HOST = {"constant": "show_host",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_host}
        self.SHOW_NOTIFY_FILTER = {"constant": "show_notify_filter",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_notify_filter}
        self.SHOW_USER = {"constant": "show_user",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_user}
        self.SHOW_VIEW = {"constant": "show_view",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_view}
        self.SHOW_VR = {"constant": "show_vr",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.show_vr}
