from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcanetworksConstants import XcanetworksConstants


class UiXcaNetworksKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaNetworksKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_NETWORKS
        self.command_const = XcanetworksConstants()

    def networks_click_add_to_create_new_network(self, element_names, **kwargs):
        """Returns the result of networks_click_add_to_create_new_network."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADD_TO_CREATE_NEW_NETWORK, **kwargs)

    def networks_click_network_name_to_open_network_settings(self, element_names, **kwargs):
        """Returns the result of networks_click_network_name_to_open_network_settings."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_NETWORK_NAME_TO_OPEN_NETWORK_SETTINGS, **kwargs)

    def networks_edit_network_name_ssid_and_status(self, element_names, network_name, ssid, status, **kwargs):
        """
        :param element_names:
        :param network_name:
        :param ssid:
        :param status: The status of a network. 2 key values are accepted as 'Enabled' and 'Disabled' in the data type
                       of string.
        :return:
        """
        args = {"network_name": network_name,
                "ssid": ssid,
                "status": status}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_NETWORK_NAME_SSID_AND_STATUS, **kwargs)

    def networks_select_network_auth_type(self, element_names, auth_type, **kwargs):
        """
        :param element_names:
        :param auth_type: The Auth Type of a network. 3 key values are accepted as 'RADIUS', 'PSK' and 'OPEN' in the
                          data type of string.
        :return:
        """
        args = {"auth_type": auth_type}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_NETWORK_AUTH_TYPE, **kwargs)

    def networks_edit_network_auth_type_privacy_settings(self, element_names, password, is_masked, **kwargs):
        """Returns the result of networks_edit_network_auth_type_privacy_settings."""
        args = {"password": password,
                "is_masked": is_masked}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_NETWORK_AUTH_TYPE_PRIVACY_SETTINGS,
                                    **kwargs)

    def networks_config_mac_based_authentication(self, element_names, use_mba, **kwargs):
        """Returns the result of networks_config_mac_based_authentication."""
        args = {"use_mba": use_mba}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_MAC_BASED_AUTHENTICATION, **kwargs)

    def networks_select_mba_timeout_role(self, element_names, mba_role, **kwargs):
        """Returns the result of networks_select_mba_timeout_role."""
        args = {"mba_role": mba_role}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_MBA_TIMEOUT_ROLE, **kwargs)

    def networks_select_whether_enable_captive_portal(self, element_names, **kwargs):
        """Returns the result of networks_select_whether_enable_captive_portal."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_WHETHER_ENABLE_CAPTIVE_PORTAL,
                                    **kwargs)

    def networks_select_captive_portal_type(self, element_names, **kwargs):
        """Returns the result of networks_select_captive_portal_type."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_CAPTIVE_PORTAL_TYPE, **kwargs)

    def networks_select_whether_use_fqdn_for_connection(self, element_names, **kwargs):
        """Returns the result of networks_select_whether_use_fqdn_for_connection."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_WHETHER_USE_FQDN_FOR_CONNECTION,
                                    **kwargs)

    def networks_select_whether_use_https_connection(self, element_names, **kwargs):
        """Returns the result of networks_select_whether_use_https_connection."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_WHETHER_USE_HTTPS_CONNECTION,
                                    **kwargs)

    def networks_edit_ecp_url(self, element_names, **kwargs):
        """Returns the result of networks_edit_ecp_url."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_ECP_URL, **kwargs)

    def networks_edit_identity_and_shared_secret(self, element_names, **kwargs):
        """Returns the result of networks_edit_identity_and_shared_secret."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_IDENTITY_AND_SHARED_SECRET, **kwargs)

    def networks_select_send_successful_login(self, element_names, **kwargs):
        """Returns the result of networks_select_send_successful_login."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_SEND_SUCCESSFUL_LOGIN, **kwargs)

    def networks_select_auth_method(self, element_names, auth_method, **kwargs):
        """
        :param element_names:
        :param auth_method: The Authentication Method of a network. 4 key values are accepted as 'DEFAULT', 'RADIUS' ,
                            'LOCAL' and 'LDAP' in the data type of string.
        :return:
        """
        args = {"auth_method": auth_method}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_AUTH_METHOD, **kwargs)

    def networks_config_default_aaa(self, element_names, **kwargs):
        """Returns the result of networks_config_."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEFAULT_AAA, **kwargs)

    def networks_add_new_radius_server(self, element_names, **kwargs):
        """Returns the result of networks_add_new_radius_server."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.ADD_NEW_RADIUS_SERVER, **kwargs)

    def networks_config_new_radius_server_advanced_settings(self, element_names, **kwargs):
        """Returns the result of networks_config_new_radius_server_advanced_settings."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CONFIG_NEW_RADIUS_SERVER_ADVANCED_SETTINGS, **kwargs)

    def networks_save_new_radius_server(self, element_names, **kwargs):
        """Returns the result of networks_save_new_radius_server."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_NEW_RADIUS_SERVER, **kwargs)

    def networks_config_auth_method_local_and_dhcp(self, element_names, **kwargs):
        """Returns the result of networks_config_auth_method_local_and_dhcp."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_AUTH_METHOD_LOCAL_AND_DHCP, **kwargs)

    def networks_add_new_dhcp_config(self, element_names, **kwargs):
        """Returns the result of networks_add_new_dhcp_config."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.ADD_NEW_DHCP_CONFIG, **kwargs)

    def networks_edit_dhcp_schema_definition(self, element_names, **kwargs):
        """Returns the result of networks_edit_dhcp_schema_."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_DHCP_SCHEMA_DEFINITION, **kwargs)

    def networks_test_new_dhcp_config(self, element_names, **kwargs):
        """Returns the result of networks_test_new_dhcp_config."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.TEST_NEW_DHCP_CONFIG, **kwargs)

    def networks_save_new_dhcp_config(self, element_names, **kwargs):
        """Returns the result of networks_save_new_dhcp_config."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_NEW_DHCP_CONFIG, **kwargs)

    def networks_select_network_default_unauth_role(self, element_names, unauth_role, **kwargs):
        """Returns the result of networks_select_network_."""
        args = {"unauth_role": unauth_role}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_NETWORK_DEFAULT_UNAUTH_ROLE,
                                    **kwargs)

    def networks_select_network_default_auth_role_and_vlan(self, element_names, auth_role, vlan_name, **kwargs):
        """Returns the result of networks_select_network_."""
        args = {"auth_role": auth_role,
                "vlan_name": vlan_name}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_NETWORK_DEFAULT_AUTH_ROLE_AND_VLAN,
                                    **kwargs)

    def networks_config_network_advanced_settings(self, element_names, **kwargs):
        """Returns the result of networks_config_network_advanced_settings."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_NETWORK_ADVANCED_SETTINGS, **kwargs)

    def networks_config_auth_method_radius(self, element_names, primary_radius, backup_radius, **kwargs):
        """Returns the result of networks_config_auth_method_radius."""
        args = {"primary_radius": primary_radius,
                "backup_radius": backup_radius}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_AUTH_METHOD_RADIUS,
                                    **kwargs)

    def networks_save_settings_and_back_to_networks_page(self, element_names, **kwargs):
        """Returns the result of networks_save_settings_and_back_to_networks_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_SETTINGS_AND_BACK_TO_NETWORKS_PAGE,
                                    **kwargs)

    def networks_delete_network(self, element_names, network_name, **kwargs):
        """Returns the result of networks_delete_network."""
        args = {"network_name": network_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_NETWORK, **kwargs)

    def networks_verify_network_exists(self, element_names, network_name, ssid, status, auth_type,
                                       auth_role, vlan_name, **kwargs):
        """Returns the result of networks_verify_network_exists."""
        args = {"network_name": network_name,
                "ssid": ssid,
                "status": status,
                "auth_type": auth_type,
                "auth_role": auth_role,
                "vlan_name": vlan_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_NETWORK_EXISTS, **kwargs)

    def networks_verify_network_does_not_exist(self, element_names, network_name, **kwargs):
        """Returns the result of networks_verify_network_does_not_exist."""
        args = {"network_name": network_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_NETWORK_DOES_NOT_EXIST, **kwargs)
