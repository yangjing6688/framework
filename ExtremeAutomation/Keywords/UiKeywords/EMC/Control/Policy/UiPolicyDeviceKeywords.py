from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.PolicydeviceConstants import PolicydeviceConstants


class UiPolicyDeviceKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiPolicyDeviceKeywords, self).__init__()
        self.api_const = self.constants.API_POLICY_DEVICE
        self.command_const = PolicydeviceConstants()

    def policy_device_expand_device_tree(self, element_name, device_ip, **kwargs):
        """Returns the result of policy_device_expand_device_tree."""
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_EXPAND_DEVICE_TREE, **kwargs)

    def policy_device_select_device_node(self, element_name, device_name, **kwargs):
        """Returns the result of policy_device_select_device_node."""
        args = {"device_name": device_name}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_DEVICE_NODE, **kwargs)

    def policy_device_select_radius_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_radius_tab."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_RADIUS_TAB, **kwargs)

    def policy_device_select_device_radius_server(self, element_name, radius_ip, **kwargs):
        """Returns the result of policy_device_select_device_radius_server."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_DEVICE_RADIUS_SERVER,
                                    **kwargs)

    def policy_device_delete_device_radius_server(self, element_name, **kwargs):
        """Returns the result of policy_device_delete_device_radius_server."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_DELETE_DEVICE_RADIUS_SERVER,
                                    **kwargs)

    def policy_device_apply_device_radius_settings(self, element_name, **kwargs):
        """Returns the result of policy_device_apply_device_radius_settings."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_APPLY_DEVICE_RADIUS_SETTINGS,
                                    **kwargs)

    def policy_device_select_ports_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_ports_tab."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_PORTS_TAB, **kwargs)

    def policy_device_select_device_port(self, element_name, device_port, **kwargs):
        """Returns the result of policy_device_select_device_port."""
        args = {"device_port": device_port}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_DEVICE_PORT, **kwargs)

    def policy_device_expand_device_port(self, element_name, device_port, **kwargs):
        """Returns the result of policy_device_expand_device_port."""
        args = {"device_port": device_port}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_EXPAND_DEVICE_PORT, **kwargs)

    def policy_device_collapse_device_port(self, element_name, device_port, **kwargs):
        """Returns the result of policy_device_collapse_device_port."""
        args = {"device_port": device_port}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_COLLAPSE_DEVICE_PORT, **kwargs)

    def policy_device_select_authentication_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_authentication_tab."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_AUTHENTICATION_TAB,
                                    **kwargs)

    def policy_device_click_authentication_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_device_click_authentication_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_AUTHENTICATION_TREE_PANEL, **kwargs)

    def policy_device_click_authentication_device_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_device_click_authentication_device_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_AUTHENTICATION_DEVICE_TREE_PANEL, **kwargs)

    def policy_device_click_authentication_ports_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_device_click_authentication_ports_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_AUTHENTICATION_PORTS_TREE_PANEL, **kwargs)

    def policy_device_select_device_authentication_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_device_authentication_tab."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_DEVICE_AUTHENTICATION_TAB, **kwargs)

    def policy_device_select_port_authentication_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_port_authentication_tab."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_PORT_AUTHENTICATION_TAB, **kwargs)

    def policy_device_select_port_authentication_mode(self, element_name, port_mode, **kwargs):
        """Returns the result of policy_device_select_port_authentication_mode."""
        args = {"port_mode": port_mode}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_PORT_AUTHENTICATION_MODE, **kwargs)

    def policy_device_select_port_dot1x_status(self, element_name, dot1x_status, **kwargs):
        """Returns the result of policy_device_select_port_dot1x_status."""
        args = {"dot1x_status": dot1x_status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_PORT_DOT1X_STATUS, **kwargs)

    def policy_device_add_radius_server(self, element_name, **kwargs):
        """Returns the result of policy_device_add_radius_server."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_SERVER, **kwargs)

    def policy_device_click_port_authentication_apply(self, element_name, **kwargs):
        """Returns the result of policy_device_click_port_authentication_apply."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_PORT_AUTHENTICATION_APPLY, **kwargs)

    def policy_device_click_port_authentication_refresh(self, element_name, **kwargs):
        """Returns the result of policy_device_click_port_authentication_refresh."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_PORT_AUTHENTICATION_REFRESH, **kwargs)

    def policy_device_add_radius_dialog_edit_ip(self, element_name, radius_ip, **kwargs):
        """Returns the result of policy_device_add_radius_dialog_edit_ip."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_IP,
                                    **kwargs)

    def policy_device_add_radius_dialog_edit_secret(self, element_name, radius_secret, **kwargs):
        """Returns the result of policy_device_add_radius_dialog_edit_secret."""
        args = {"radius_secret": radius_secret}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_SECRET,
                                    **kwargs)

    def policy_device_add_radius_dialog_edit_access(self, element_name, radius_access, **kwargs):
        """Returns the result of policy_device_add_radius_dialog_edit_access."""
        args = {"radius_access": radius_access}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_DIALOG_EDIT_ACCESS,
                                    **kwargs)

    def policy_device_add_radius_dialog_click_ok(self, element_name, **kwargs):
        """Returns the result of policy_device_add_radius_dialog_click_ok."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_DIALOG_CLICK_OK,
                                    **kwargs)

    def policy_device_select_port_macauth_status(self, element_name, macauth_status, **kwargs):
        """Returns the result of policy_device_select_port_macauth_status."""
        args = {"macauth_status": macauth_status}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_PORT_MACAUTH_STATUS,
                                    **kwargs)

    def policy_device_select_radius_accounting_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_radius_accounting_tab."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_RADIUS_ACCOUNTING_TAB,
                                    **kwargs)

    def policy_device_select_device_radius_accounting_server(self, element_name, acct_server, **kwargs):
        """Returns the result of policy_device_select_device_radius_accounting_server."""
        args = {"acct_server": acct_server}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_DEVICE_RADIUS_ACCOUNTING_SERVER, **kwargs)

    def policy_device_delete_device_radius_accounting_server(self, element_name, **kwargs):
        """Returns the result of policy_device_delete_device_radius_accounting_server."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_DELETE_DEVICE_RADIUS_ACCOUNTING_SERVER, **kwargs)

    def policy_device_apply_device_radius_accounting_settings(self, element_name, **kwargs):
        """Returns the result of policy_device_apply_device_radius_accounting_settings."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_APPLY_DEVICE_RADIUS_ACCOUNTING_SETTINGS, **kwargs)

    def policy_device_add_radius_accounting_server(self, element_name, **kwargs):
        """Returns the result of policy_device_add_radius_accounting_server."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_SERVER,
                                    **kwargs)

    def policy_device_add_radius_accounting_dialog_edit_ip(self, element_name, radius_acct_ip, **kwargs):
        """Returns the result of policy_device_add_radius_accounting_dialog_edit_ip."""
        args = {"radius_acct_ip": radius_acct_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_IP, **kwargs)

    def policy_device_add_radius_accounting_dialog_edit_secret(self, element_name, radius_acct_secret, **kwargs):
        """Returns the result of policy_device_add_radius_accounting_dialog_edit_secret."""
        args = {"radius_acct_secret": radius_acct_secret}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_SECRET, **kwargs)

    def policy_device_add_radius_accounting_dialog_edit_access(self, element_name, radius_acct_access, **kwargs):
        """Returns the result of policy_device_add_radius_accounting_dialog_edit_access."""
        args = {"radius_acct_access": radius_acct_access}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_EDIT_ACCESS, **kwargs)

    def policy_device_add_radius_accounting_dialog_click_ok(self, element_name, **kwargs):
        """Returns the result of policy_device_add_radius_accounting_dialog_click_ok."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_ADD_RADIUS_ACCOUNTING_DIALOG_CLICK_OK, **kwargs)

    def policy_device_select_device_macauth_status(self, element_name, macauth_status, **kwargs):
        """Returns the result of policy_device_select_device_macauth_status."""
        args = {"macauth_status": macauth_status}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_DEVICE_MACAUTH_STATUS,
                                    **kwargs)

    def policy_device_select_device_dot1x_status(self, element_name, dot1x_status, **kwargs):
        """Returns the result of policy_device_select_device_dot1x_status."""
        args = {"dot1x_status": dot1x_status}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_DEVICE_DOT1X_STATUS,
                                    **kwargs)

    def policy_device_select_device_rfc3580_vlan_authorization_status(self, element_name, rfc3580_vlan_auth_status,
                                                                      **kwargs):
        """Returns the result of policy_device_select_device_rfc3580_vlan_authorization_status."""
        args = {"rfc3580_vlan_auth_status": rfc3580_vlan_auth_status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_DEVICE_RFC3580_VLAN_AUTHORIZATION_STATUS,
                                    **kwargs)

    def policy_device_apply_device_authentication(self, element_name, **kwargs):
        """Returns the result of policy_device_apply_device_authentication."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_APPLY_DEVICE_AUTHENTICATION,
                                    **kwargs)

    def policy_device_select_mac_auth_set_password_and_mask(self, element_name, status, **kwargs):
        """Returns the result of policy_device_select_mac_auth_set_password_and_mask."""
        args = {"status": status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_MAC_AUTH_SET_PASSWORD_AND_MASK, **kwargs)

    def policy_device_set_mac_auth_user_password(self, element_name, password, **kwargs):
        """Returns the result of policy_device_set_mac_auth_user_password."""
        args = {"password": password}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SET_MAC_AUTH_USER_PASSWORD,
                                    **kwargs)

    def policy_device_select_mac_auth_mask(self, element_name, mask, **kwargs):
        """Returns the result of policy_device_select_mac_auth_mask."""
        args = {"mask": mask}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_DEVICE_SELECT_MAC_AUTH_MASK, **kwargs)

    def policy_device_select_mac_auth_address_delimiter(self, element_name, delimiter, **kwargs):
        """Returns the result of policy_device_select_mac_auth_address_delimiter."""
        args = {"delimiter": delimiter}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_MAC_AUTH_ADDRESS_DELIMITER, **kwargs)

    def policy_device_click_radius_authentication_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_device_click_radius_authentication_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_RADIUS_AUTHENTICATION_TREE_PANEL, **kwargs)

    def policy_device_click_radius_accounting_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_device_click_radius_accounting_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_CLICK_RADIUS_ACCOUNTING_TREE_PANEL, **kwargs)

    def policy_device_select_radius_authentication_tab(self, element_name, **kwargs):
        """Returns the result of policy_device_select_radius_authentication_tab."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_RADIUS_AUTHENTICATION_TAB, **kwargs)

    def policy_device_select_radius_authentication_response_mode(self, element_name, radius_auth_response_mode,
                                                                 **kwargs):
        """Returns the result of policy_device_select_radius_authentication_response_mode."""
        args = {"radius_auth_response_mode": radius_auth_response_mode}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_SELECT_RADIUS_AUTHENTICATION_RESPONSE_MODE,
                                    **kwargs)

    def policy_device_apply_radius_authentication_client_settings(self, element_name, **kwargs):
        """Returns the result of policy_device_apply_radius_authentication_client_settings."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_APPLY_RADIUS_AUTHENTICATION_CLIENT_SETTINGS,
                                    **kwargs)

    def policy_device_apply_radius_accounting_client_settings(self, element_name, **kwargs):
        """Returns the result of policy_device_apply_radius_accounting_client_settings."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_DEVICE_APPLY_RADIUS_ACCOUNTING_CLIENT_SETTINGS, **kwargs)
