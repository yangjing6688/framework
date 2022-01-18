from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcaaaaConstants import XcaaaaConstants
from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass


class UiXcaAaaKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaAaaKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_AAA
        self.command_const = XcaaaaConstants()

    def aaa_click_configure_default_aaa_configuration(self, element_names, **kwargs):
        """Returns the result of aaa_click_configure_."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_CONFIGURE_DEFAULT_AAA_CONFIGURATION, **kwargs)

    def aaa_click_manage_certificates(self, element_names, **kwargs):
        """Returns the result of aaa_click_manage_certificates."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_MANAGE_CERTIFICATES, **kwargs)

    def aaa_click_radius_servers_tab(self, element_names, **kwargs):
        """Returns the result of aaa_click_radius_servers_tab."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_RADIUS_SERVERS_TAB, **kwargs)

    def aaa_click_ldap_configurations_tab(self, element_names, **kwargs):
        """Returns the result of aaa_click_ldap_configurations_tab."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_LDAP_CONFIGURATIONS_TAB, **kwargs)

    def aaa_click_local_password_repository_tab(self, element_names, **kwargs):
        """Returns the result of aaa_click_local_password_repository_tab."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_LOCAL_PASSWORD_REPOSITORY_TAB, **kwargs)

    def aaa_click_add_to_create_a_new_radius_server(self, element_names, **kwargs):
        """Returns the result of aaa_click_add_to_create_a_new_radius_server."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_ADD_TO_CREATE_A_NEW_RADIUS_SERVER, **kwargs)

    def aaa_click_add_to_create_a_new_ldap_configuration(self, element_names, **kwargs):
        """Returns the result of aaa_click_add_to_create_a_new_ldap_configuration."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_ADD_TO_CREATE_A_NEW_LDAP_CONFIGURATION, **kwargs)

    def aaa_click_add_to_create_a_new_local_password_repository_user(self, element_names, **kwargs):
        """Returns the result of aaa_click_add_to_create_a_new_local_password_repository_user."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_ADD_TO_CREATE_A_NEW_LOCAL_PASSWORD_REPOSITORY_USER,
                                    **kwargs)

    def aaa_select_aaa_authentication_method(self, element_names, authentication_method, **kwargs):
        """Returns the result of aaa_select_aaa_authentication_method."""
        args = {"authentication_method": authentication_method}

        return self.execute_keyword(element_names, args,
                                    self.command_const.SELECT_AAA_AUTHENTICATION_METHOD, **kwargs)

    def aaa_select_aaa_primary_and_backup_radius(self, element_names, primary_radius_server,
                                                 backup_radius_server=None, **kwargs):
        """Returns the result of aaa_select_aaa_primary_and_backup_radius."""
        args = {"primary_radius_server": primary_radius_server,
                "backup_radius_server": backup_radius_server}

        return self.execute_keyword(element_names, args,
                                    self.command_const.SELECT_AAA_PRIMARY_AND_BACKUP_RADIUS, **kwargs)

    def aaa_select_aaa_ldap_configuration(self, element_names, ldap_configuration, **kwargs):
        """Returns the result of aaa_select_aaa_ldap_configuration."""
        args = {"ldap_configuration": ldap_configuration}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_AAA_LDAP_CONFIGURATION, **kwargs)

    def aaa_check_authenticate_locally_for_mac(self, element_names, auth_locally, **kwargs):
        """Returns the result of aaa_check_authenticate_locally_for_mac."""
        args = {"auth_locally": auth_locally}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CHECK_AUTHENTICATE_LOCALLY_FOR_MAC, **kwargs)

    def aaa_save_config_and_back_to_aaa_page(self, element_names, **kwargs):
        """Returns the result of aaa_save_config_and_back_to_aaa_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_CONFIG_AND_BACK_TO_AAA_PAGE, **kwargs)

    def aaa_click_radius_server_to_open_settings(self, element_names, radius_server_ip, **kwargs):
        """Returns the result of aaa_click_radius_server_to_open_settings."""
        args = {"radius_server_ip": radius_server_ip}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_RADIUS_SERVER_TO_OPEN_SETTINGS, **kwargs)

    def aaa_click_ldap_configuration_to_open_settings(self, element_names, ldap_name, **kwargs):
        """Returns the result of aaa_click_ldap_configuration_to_open_settings."""
        args = {"ldap_name": ldap_name}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_LDAP_CONFIGURATION_TO_OPEN_SETTINGS, **kwargs)

    def aaa_click_local_password_repository_user_to_open_settings(self, element_names, username, **kwargs):
        """Returns the result of aaa_click_local_password_repository_user_to_open_settings."""
        args = {"username": username}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_LOCAL_PASSWORD_REPOSITORY_USER_TO_OPEN_SETTINGS, **kwargs)

    def aaa_edit_radius_server_settings(self, element_names, radius_server_ip, response_window, auth_timeout,
                                        auth_retry_count, auth_client_udp_port, acct_client_udp_port,
                                        proxy_radius_acct_requests, shared_secret, is_masked, **kwargs):
        """Returns the result of aaa_edit_radius_server_settings."""
        args = {"radius_server_ip": radius_server_ip,
                "response_window": response_window,
                "auth_timeout": auth_timeout,
                "auth_retry_count": auth_retry_count,
                "auth_client_udp_port": auth_client_udp_port,
                "acct_client_udp_port": acct_client_udp_port,
                "proxy_radius_acct_requests": proxy_radius_acct_requests,
                "shared_secret": shared_secret,
                "is_masked": is_masked}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_RADIUS_SERVER_SETTINGS, **kwargs)

    def aaa_edit_radius_server_advanced_settings_and_close(self, element_names, **kwargs):
        """Returns the result of aaa_edit_radius_server_advanced_settings_and_close."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.EDIT_RADIUS_SERVER_ADVANCED_SETTINGS_AND_CLOSE, **kwargs)

    def aaa_edit_ldap_connection_url(self, element_names, ldap_connection_url, **kwargs):
        """Returns the result of aaa_edit_ldap_connection_url."""
        args = {"ldap_connection_url": ldap_connection_url}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_LDAP_CONNECTION_URL, **kwargs)

    def aaa_add_ldap_connection_url(self, element_names, ldap_connection_url, **kwargs):
        """Returns the result of aaa_add_ldap_connection_url."""
        args = {"ldap_connection_url": ldap_connection_url}

        return self.execute_keyword(element_names, args, self.command_const.ADD_LDAP_CONNECTION_URL, **kwargs)

    def aaa_edit_ldap_configuration_settings(self, element_names, ldap_name, admin_username, admin_password,
                                             is_masked, user_search_root, host_search_root, ou_search_root, **kwargs):
        """Returns the result of aaa_edit_ldap_configuration_settings."""
        args = {"ldap_name": ldap_name,
                "admin_username": admin_username,
                "admin_password": admin_password,
                "is_masked": is_masked,
                "user_search_root": user_search_root,
                "host_search_root": host_search_root,
                "ou_search_root": ou_search_root}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_LDAP_CONFIGURATION_SETTINGS, **kwargs)

    def aaa_edit_ldap_schema_definition_and_close(self, element_names, **kwargs):
        """Returns the result of aaa_edit_ldap_schema_."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.EDIT_LDAP_SCHEMA_DEFINITION_AND_CLOSE, **kwargs)

    def aaa_edit_local_password_repository_user_settings(self, element_names, status, username, display_name,
                                                         first_name, last_name, hash_type, password, is_masked,
                                                         description, **kwargs):
        """Returns the result of aaa_edit_local_password_repository_user_settings."""
        args = {"status": status,
                "username": username,
                "display_name": display_name,
                "first_name": first_name,
                "last_name": last_name,
                "hash_type": hash_type,
                "password": password,
                "is_masked": is_masked,
                "description": description}

        return self.execute_keyword(element_names, args,
                                    self.command_const.EDIT_LOCAL_PASSWORD_REPOSITORY_USER_SETTINGS, **kwargs)

    def aaa_delete_radius_server(self, element_names, radius_server_ip, **kwargs):
        """Returns the result of aaa_delete_radius_server."""
        args = {"radius_server_ip": radius_server_ip}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_RADIUS_SERVER, **kwargs)

    def aaa_delete_ldap_configuration(self, element_names, ldap_name, **kwargs):
        """Returns the result of aaa_delete_ldap_configuration."""
        args = {"ldap_name": ldap_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_LDAP_CONFIGURATION, **kwargs)

    def aaa_delete_local_password_repository_user(self, element_names, username, **kwargs):
        """Returns the result of aaa_delete_local_password_repository_user."""
        args = {"username": username}

        return self.execute_keyword(element_names, args,
                                    self.command_const.DELETE_LOCAL_PASSWORD_REPOSITORY_USER, **kwargs)
