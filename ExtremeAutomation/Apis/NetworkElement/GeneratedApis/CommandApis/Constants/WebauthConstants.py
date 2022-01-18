"""
This class outlines all the constants for the webauth API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(WebauthConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class WebauthConstants(ApiConstants):
    def __init__(self):
        super(WebauthConstants, self).__init__()
        self.CLEAR_ALLOWED_REFRESH_FAILURES = {"constant": "clear_allowed_refresh_failures",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_allowed_refresh_failures}
        self.CLEAR_DB_ORDER = {"constant": "clear_db_order",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_db_order}
        self.CLEAR_HOSTNAME = {"constant": "clear_hostname",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_hostname}
        self.CLEAR_IDLE_TIMEOUT = {"constant": "clear_idle_timeout",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_idle_timeout}
        self.CLEAR_LEASE_TIME = {"constant": "clear_lease_time",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_lease_time}
        self.CLEAR_PROTOCOL_ORDER = {"constant": "clear_protocol_order",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_protocol_order}
        self.CLEAR_REDIRECT_PAGE = {"constant": "clear_redirect_page",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_redirect_page}
        self.CLEAR_SESSION_REFRESH = {"constant": "clear_session_refresh",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_session_refresh}
        self.CLEAR_SESSION_TIMEOUT = {"constant": "clear_session_timeout",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_session_timeout}
        self.DISABLE_CONTROL_PORT = {"constant": "disable_control_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_control_port}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_LOGOUT_PAGE = {"constant": "disable_logout_page",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_logout_page}
        self.DISABLE_REAUTHENTICATION_ON_REFRESH = {"constant": "disable_reauthentication_on_refresh",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.disable_reauthentication_on_refresh}
        self.DISABLE_REDIRECT_PAGE = {"constant": "disable_redirect_page",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_redirect_page}
        self.DISABLE_SESSION_REFRESH = {"constant": "disable_session_refresh",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.disable_session_refresh}
        self.ENABLE_CONTROL_PORT = {"constant": "enable_control_port",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_control_port}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_LOGOUT_PAGE = {"constant": "enable_logout_page",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_logout_page}
        self.ENABLE_REAUTHENTICATION_ON_REFRESH = {"constant": "enable_reauthentication_on_refresh",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.enable_reauthentication_on_refresh}
        self.ENABLE_REDIRECT_PAGE = {"constant": "enable_redirect_page",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_redirect_page}
        self.ENABLE_SESSION_REFRESH = {"constant": "enable_session_refresh",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.enable_session_refresh}
        self.SET_ALLOWED_REFRESH_FAILURES = {"constant": "set_allowed_refresh_failures",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_allowed_refresh_failures}
        self.SET_DB_ORDER_LOCAL = {"constant": "set_db_order_local",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_db_order_local}
        self.SET_DB_ORDER_LOCAL_RADIUS = {"constant": "set_db_order_local_radius",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_db_order_local_radius}
        self.SET_DB_ORDER_RADIUS = {"constant": "set_db_order_radius",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_db_order_radius}
        self.SET_DB_ORDER_RADIUS_LOCAL = {"constant": "set_db_order_radius_local",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_db_order_radius_local}
        self.SET_HOSTNAME = {"constant": "set_hostname",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_hostname}
        self.SET_IDLE_TIMEOUT = {"constant": "set_idle_timeout",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_idle_timeout}
        self.SET_INIT_ALL = {"constant": "set_init_all",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_init_all}
        self.SET_INIT_MAC = {"constant": "set_init_mac",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_init_mac}
        self.SET_INIT_MAC_PORT = {"constant": "set_init_mac_port",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_init_mac_port}
        self.SET_INIT_PORT = {"constant": "set_init_port",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_init_port}
        self.SET_LEASE_TIME = {"constant": "set_lease_time",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_lease_time}
        self.SET_PROTOCOL_ORDER = {"constant": "set_protocol_order",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_protocol_order}
        self.SET_PROTOCOL_ORDER_WEB_DOT1X_MAC = {"constant": "set_protocol_order_web_dot1x_mac",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_protocol_order_web_dot1x_mac}
        self.SET_PROTOCOL_ORDER_WEB_MAC_DOT1X = {"constant": "set_protocol_order_web_mac_dot1x",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_protocol_order_web_mac_dot1x}
        self.SET_REDIRECT_PAGE = {"constant": "set_redirect_page",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_redirect_page}
        self.SET_SESSION_REFRESH = {"constant": "set_session_refresh",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_session_refresh}
        self.SET_SESSION_TIMEOUT = {"constant": "set_session_timeout",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_session_timeout}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_port}
        self.SHOW_SUMMARY_SNAPSHOT = {"constant": "show_summary_snapshot",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_summary_snapshot}
        self.SHOW_TIMEOUT_VALUES = {"constant": "show_timeout_values",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_timeout_values}
        self.SHOW_VLAN_DHCP_NETLOGIN_LEASE_TIME = {"constant": "show_vlan_dhcp_netlogin_lease_time",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.show_vlan_dhcp_netlogin_lease_time}
