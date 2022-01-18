"""
This class outlines all the constants for the policydevice API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicydeviceConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicydeviceConstants(ApiConstants):
    def __init__(self):
        super(PolicydeviceConstants, self).__init__()
        self.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_CLICK_OK = {"constant": "policy_device_add_radius_accounting_dialog_click_ok",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.policy_device_add_radius_accounting_dialog_click_ok}
        self.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_ACCESS = {"constant": "policy_device_add_radius_accounting_dialog_edit_access",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.policy_device_add_radius_accounting_dialog_edit_access}
        self.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_IP = {"constant": "policy_device_add_radius_accounting_dialog_edit_ip",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.policy_device_add_radius_accounting_dialog_edit_ip}
        self.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_SECRET = {"constant": "policy_device_add_radius_accounting_dialog_edit_secret",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.policy_device_add_radius_accounting_dialog_edit_secret}
        self.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_SERVER = {"constant": "policy_device_add_radius_accounting_server",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_device_add_radius_accounting_server}
        self.POLICY_DEVICE_ADD_RADIUS_DIALOG_CLICK_OK = {"constant": "policy_device_add_radius_dialog_click_ok",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_device_add_radius_dialog_click_ok}
        self.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_ACCESS = {"constant": "policy_device_add_radius_dialog_edit_access",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.policy_device_add_radius_dialog_edit_access}
        self.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_IP = {"constant": "policy_device_add_radius_dialog_edit_ip",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.policy_device_add_radius_dialog_edit_ip}
        self.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_SECRET = {"constant": "policy_device_add_radius_dialog_edit_secret",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.policy_device_add_radius_dialog_edit_secret}
        self.POLICY_DEVICE_ADD_RADIUS_SERVER = {"constant": "policy_device_add_radius_server",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.policy_device_add_radius_server}
        self.POLICY_DEVICE_APPLY_DEVICE_AUTHENTICATION = {"constant": "policy_device_apply_device_authentication",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.policy_device_apply_device_authentication}
        self.POLICY_DEVICE_APPLY_DEVICE_RADIUS_ACCOUNTING_SETTINGS = {"constant": "policy_device_apply_device_radius_accounting_settings",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.policy_device_apply_device_radius_accounting_settings}
        self.POLICY_DEVICE_APPLY_DEVICE_RADIUS_SETTINGS = {"constant": "policy_device_apply_device_radius_settings",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_device_apply_device_radius_settings}
        self.POLICY_DEVICE_APPLY_RADIUS_ACCOUNTING_CLIENT_SETTINGS = {"constant": "policy_device_apply_radius_accounting_client_settings",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.policy_device_apply_radius_accounting_client_settings}
        self.POLICY_DEVICE_APPLY_RADIUS_AUTHENTICATION_CLIENT_SETTINGS = {"constant": "policy_device_apply_radius_authentication_client_settings",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.policy_device_apply_radius_authentication_client_settings}
        self.POLICY_DEVICE_CLICK_AUTHENTICATION_DEVICE_TREE_PANEL = {"constant": "policy_device_click_authentication_device_tree_panel",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.policy_device_click_authentication_device_tree_panel}
        self.POLICY_DEVICE_CLICK_AUTHENTICATION_PORTS_TREE_PANEL = {"constant": "policy_device_click_authentication_ports_tree_panel",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.policy_device_click_authentication_ports_tree_panel}
        self.POLICY_DEVICE_CLICK_AUTHENTICATION_TREE_PANEL = {"constant": "policy_device_click_authentication_tree_panel",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.policy_device_click_authentication_tree_panel}
        self.POLICY_DEVICE_CLICK_PORT_AUTHENTICATION_APPLY = {"constant": "policy_device_click_port_authentication_apply",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.policy_device_click_port_authentication_apply}
        self.POLICY_DEVICE_CLICK_PORT_AUTHENTICATION_REFRESH = {"constant": "policy_device_click_port_authentication_refresh",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.policy_device_click_port_authentication_refresh}
        self.POLICY_DEVICE_CLICK_RADIUS_ACCOUNTING_TREE_PANEL = {"constant": "policy_device_click_radius_accounting_tree_panel",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.policy_device_click_radius_accounting_tree_panel}
        self.POLICY_DEVICE_CLICK_RADIUS_AUTHENTICATION_TREE_PANEL = {"constant": "policy_device_click_radius_authentication_tree_panel",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.policy_device_click_radius_authentication_tree_panel}
        self.POLICY_DEVICE_COLLAPSE_DEVICE_PORT = {"constant": "policy_device_collapse_device_port",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.policy_device_collapse_device_port}
        self.POLICY_DEVICE_DELETE_DEVICE_RADIUS_ACCOUNTING_SERVER = {"constant": "policy_device_delete_device_radius_accounting_server",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.policy_device_delete_device_radius_accounting_server}
        self.POLICY_DEVICE_DELETE_DEVICE_RADIUS_SERVER = {"constant": "policy_device_delete_device_radius_server",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.policy_device_delete_device_radius_server}
        self.POLICY_DEVICE_EXPAND_DEVICE_PORT = {"constant": "policy_device_expand_device_port",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_device_expand_device_port}
        self.POLICY_DEVICE_EXPAND_DEVICE_TREE = {"constant": "policy_device_expand_device_tree",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_device_expand_device_tree}
        self.POLICY_DEVICE_SELECT_AUTHENTICATION_TAB = {"constant": "policy_device_select_authentication_tab",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.policy_device_select_authentication_tab}
        self.POLICY_DEVICE_SELECT_DEVICE_AUTHENTICATION_TAB = {"constant": "policy_device_select_device_authentication_tab",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.policy_device_select_device_authentication_tab}
        self.POLICY_DEVICE_SELECT_DEVICE_DOT1X_STATUS = {"constant": "policy_device_select_device_dot1x_status",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_device_select_device_dot1x_status}
        self.POLICY_DEVICE_SELECT_DEVICE_MACAUTH_STATUS = {"constant": "policy_device_select_device_macauth_status",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_device_select_device_macauth_status}
        self.POLICY_DEVICE_SELECT_DEVICE_NODE = {"constant": "policy_device_select_device_node",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_device_select_device_node}
        self.POLICY_DEVICE_SELECT_DEVICE_PORT = {"constant": "policy_device_select_device_port",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_device_select_device_port}
        self.POLICY_DEVICE_SELECT_DEVICE_RADIUS_ACCOUNTING_SERVER = {"constant": "policy_device_select_device_radius_accounting_server",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.policy_device_select_device_radius_accounting_server}
        self.POLICY_DEVICE_SELECT_DEVICE_RADIUS_SERVER = {"constant": "policy_device_select_device_radius_server",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.policy_device_select_device_radius_server}
        self.POLICY_DEVICE_SELECT_DEVICE_RFC3580_VLAN_AUTHORIZATION_STATUS = {"constant": "policy_device_select_device_rfc3580_vlan_authorization_status",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.policy_device_select_device_rfc3580_vlan_authorization_status}
        self.POLICY_DEVICE_SELECT_MAC_AUTH_ADDRESS_DELIMITER = {"constant": "policy_device_select_mac_auth_address_delimiter",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.policy_device_select_mac_auth_address_delimiter}
        self.POLICY_DEVICE_SELECT_MAC_AUTH_MASK = {"constant": "policy_device_select_mac_auth_mask",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.policy_device_select_mac_auth_mask}
        self.POLICY_DEVICE_SELECT_MAC_AUTH_SET_PASSWORD_AND_MASK = {"constant": "policy_device_select_mac_auth_set_password_and_mask",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.policy_device_select_mac_auth_set_password_and_mask}
        self.POLICY_DEVICE_SELECT_PORTS_TAB = {"constant": "policy_device_select_ports_tab",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_device_select_ports_tab}
        self.POLICY_DEVICE_SELECT_PORT_AUTHENTICATION_MODE = {"constant": "policy_device_select_port_authentication_mode",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.policy_device_select_port_authentication_mode}
        self.POLICY_DEVICE_SELECT_PORT_AUTHENTICATION_TAB = {"constant": "policy_device_select_port_authentication_tab",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.policy_device_select_port_authentication_tab}
        self.POLICY_DEVICE_SELECT_PORT_DOT1X_STATUS = {"constant": "policy_device_select_port_dot1x_status",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.policy_device_select_port_dot1x_status}
        self.POLICY_DEVICE_SELECT_PORT_MACAUTH_STATUS = {"constant": "policy_device_select_port_macauth_status",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_device_select_port_macauth_status}
        self.POLICY_DEVICE_SELECT_RADIUS_ACCOUNTING_TAB = {"constant": "policy_device_select_radius_accounting_tab",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_device_select_radius_accounting_tab}
        self.POLICY_DEVICE_SELECT_RADIUS_AUTHENTICATION_RESPONSE_MODE = {"constant": "policy_device_select_radius_authentication_response_mode",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.policy_device_select_radius_authentication_response_mode}
        self.POLICY_DEVICE_SELECT_RADIUS_AUTHENTICATION_TAB = {"constant": "policy_device_select_radius_authentication_tab",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.policy_device_select_radius_authentication_tab}
        self.POLICY_DEVICE_SELECT_RADIUS_TAB = {"constant": "policy_device_select_radius_tab",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.policy_device_select_radius_tab}
        self.POLICY_DEVICE_SET_MAC_AUTH_USER_PASSWORD = {"constant": "policy_device_set_mac_auth_user_password",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_device_set_mac_auth_user_password}
