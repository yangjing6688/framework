from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AaaConstants import AaaConstants


class UiAaaKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAaaKeywords, self).__init__()
        self.api_const = self.constants.API_AAA
        self.command_const = AaaConstants()

    def access_control_aaa_confirm_radius_server_exists(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_address]    - The IP Address of the RADIUS Server

        Verifies the specified RADIUS Server is configured.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.AAA_CONFIRM_RADIUS_SERVER_EXISTS, **kwargs)

    def access_control_aaa_confirm_ldap_configuration_exists(self, element_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name]   - The configuration filename

        Verifies the specified LDAP configuration exists.
        """
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_CONFIRM_LDAP_CONFIGURATION_EXISTS,
                                    **kwargs)

    def access_control_aaa_radius_server_click_add_radius_server_button(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the button to add a new RADIUS Server.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_CLICK_ADD_RADIUS_SERVER_BUTTON, **kwargs)

    def access_control_aaa_radius_server_click_edit_radius_server_button(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the button to edit an existing RADIUS Server.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_CLICK_EDIT_RADIUS_SERVER_BUTTON, **kwargs)

    def access_control_aaa_radius_server_click_delete_radius_server_button(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the button to delete the current RADIUS Server.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_CLICK_DELETE_RADIUS_SERVER_BUTTON, **kwargs)

    def access_control_aaa_radius_server_delete_radius_server(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name]   - The configuration filename

        Deletes the specified RADIUS Server, by IP address.
        """
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.AAA_RADIUS_SERVER_DELETE_RADIUS_SERVER,
                                    **kwargs)

    def access_control_aaa_radius_server_dialog_set_ip_and_response_window(self, element_name, ip_address,
                                                                           response_window, **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_set_ip_and_response_window."""
        args = {"ip_address": ip_address,
                "response_window": response_window}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_DIALOG_SET_IP_AND_RESPONSE_WINDOW, **kwargs)

    def access_control_aaa_radius_server_dialog_set_authentication_via_emc(self, element_name, timeout, retries,
                                                                           **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_set_authentication_via_emc."""
        args = {"timeout": timeout,
                "retries": retries}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_DIALOG_SET_AUTHENTICATION_VIA_EMC, **kwargs)

    def access_control_aaa_radius_server_dialog_set_configuration(self, element_name, auth_port, acct_port,
                                                                  proxy_accounting, **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_set_configuration."""
        args = {"auth_port": auth_port,
                "acct_port": acct_port,
                "proxy_accounting": proxy_accounting}

        return self.execute_keyword(element_name, args, self.command_const.AAA_RADIUS_SERVER_DIALOG_SET_CONFIGURATION,
                                    **kwargs)

    def access_control_aaa_radius_server_dialog_change_server_shared_secret(self, element_name, shared_secret,
                                                                            **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_change_server_shared_secret."""
        args = {"shared_secret": shared_secret}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_DIALOG_CHANGE_SERVER_SHARED_SECRET, **kwargs)

    def access_control_aaa_radius_server_dialog_open_advanced_config(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_open_advanced_config."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_DIALOG_OPEN_ADVANCED_CONFIG, **kwargs)

    def access_control_aaa_radius_server_dialog_save_configuration(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_save_configuration."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_RADIUS_SERVER_DIALOG_SAVE_CONFIGURATION,
                                    **kwargs)

    def access_control_aaa_radius_server_dialog_cancel_configuration(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_radius_server_dialog_cancel_configuration."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_SERVER_DIALOG_CANCEL_CONFIGURATION, **kwargs)

    def access_control_aaa_radius_advanced_config_dialog_username_setting(self, element_name, username_format,
                                                                          require_msg_auth, **kwargs):
        """Returns the result of access_control_aaa_radius_advanced_config_dialog_username_setting."""
        args = {"username_format": username_format,
                "require_msg_auth": require_msg_auth}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_USERNAME_SETTING, **kwargs)

    def access_control_aaa_radius_advanced_config_dialog_health_check_use_access_request(self, element_name,
                                                                                         use_access_request,
                                                                                         access_request_username,
                                                                                         access_request_password,
                                                                                         **kwargs):
        """Returns the result of access_control_aaa_radius_advanced_config_dialog_health_check_use_access_request."""
        args = {"use_access_request": use_access_request,
                "access_request_username": access_request_username,
                "access_request_password": access_request_password}

        return self.execute_keyword(element_name, args, self.command_const.
                                    AAA_RADIUS_ADVANCED_CONFIG_DIALOG_HEALTH_CHECK_USE_ACCESS_REQUEST, **kwargs)

    def access_control_aaa_radius_advanced_config_dialog_health_check_other_settings(self, element_name,
                                                                                     use_server_status_request,
                                                                                     check_interval, answers_number,
                                                                                     revive_interval, **kwargs):
        """Returns the result of access_control_aaa_radius_advanced_config_dialog_health_check_other_settings."""
        args = {"use_server_status_request": use_server_status_request,
                "check_interval": check_interval,
                "answers_number": answers_number,
                "revive_interval": revive_interval}

        return self.execute_keyword(element_name, args, self.command_const.
                                    AAA_RADIUS_ADVANCED_CONFIG_DIALOG_HEALTH_CHECK_OTHER_SETTINGS, **kwargs)

    def access_control_aaa_radius_advanced_config_dialog_save_advanced_setting(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_radius_advanced_config_dialog_save_advanced_setting."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_SAVE_ADVANCED_SETTING,
                                    **kwargs)

    def access_control_aaa_radius_advanced_config_dialog_cancel_advanced_setting(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_radius_advanced_config_dialog_cancel_advanced_setting."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_CANCEL_ADVANCED_SETTING,
                                    **kwargs)

    def access_control_aaa_default_check_auth_request_for(self, element_name, status, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"status": status}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_CHECK_AUTH_REQUEST_FOR, **kwargs)

    def access_control_aaa_default_select_auth_methods(self, element_name, auth_methods, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"auth_methods": auth_methods}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SELECT_AUTH_METHODS, **kwargs)

    def access_control_aaa_default_select_primary_radius_server(self, element_name, ip_address, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SELECT_PRIMARY_RADIUS_SERVER,
                                    **kwargs)

    def access_control_aaa_default_select_backup_radius_server(self, element_name, ip_address, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SELECT_BACKUP_RADIUS_SERVER,
                                    **kwargs)

    def access_control_aaa_default_select_ldap_configuration(self, element_name, config_name, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SELECT_LDAP_CONFIGURATION,
                                    **kwargs)

    def access_control_aaa_default_select_local_password_repository(self, element_name, repo_name, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {"repo_name": repo_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SELECT_LOCAL_PASSWORD_REPOSITORY,
                                    **kwargs)

    def access_control_aaa_default_save_default_aaa_settings(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_SAVE_DEFAULT_AAA_SETTINGS,
                                    **kwargs)

    def access_control_aaa_default_cancel_default_aaa_settings(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DEFAULT_CANCEL_DEFAULT_AAA_SETTINGS,
                                    **kwargs)

    def access_control_aaa_click_add_aaa_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_click_add_aaa_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_CLICK_ADD_AAA_CONFIGURATION_BUTTON,
                                    **kwargs)

    def access_control_aaa_click_edit_aaa_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_click_edit_aaa_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_CLICK_ADD_EDIT_CONFIGURATION_BUTTON,
                                    **kwargs)

    def access_control_aaa_click_delete_aaa_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_click_delete_aaa_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_CLICK_ADD_AAA_CONFIGURATION_BUTTON,
                                    **kwargs)

    def access_control_aaa_select_aaa_configuration(self, element_name, aaa_config_name, **kwargs):
        """Returns the result of access_control_aaa_select_aaa_configuration."""
        args = {"aaa_config_name": aaa_config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_SELECT_AAA_CONFIGURATION, **kwargs)

    def access_control_aaa_add_aaa_configuration(self, element_name, aaa_config_name, aaa_config_type, **kwargs):
        """Returns the result of access_control_aaa_add_aaa_configuration."""
        args = {"aaa_config_name": aaa_config_name,
                "aaa_config_type": aaa_config_type}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADD_AAA_CONFIGURATION, **kwargs)

    def access_control_aaa_delete_aaa_configuration(self, element_name, aaa_config_name, **kwargs):
        """Returns the result of access_control_aaa_delete_aaa_configuration."""
        args = {"aaa_config_name": aaa_config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DELETE_AAA_CONFIGURATION, **kwargs)

    def access_control_aaa_advanced_click_add_authentication_rule(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_advanced_click_add_authentication_rule."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_CLICK_ADD_AUTHENTICATION_RULE,
                                    **kwargs)

    def access_control_aaa_advanced_click_edit_authentication_rule(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_advanced_click_edit_authentication_rule."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_CLICK_EDIT_AUTHENTICATION_RULE,
                                    **kwargs)

    def access_control_aaa_advanced_click_delete_authentication_rule(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_advanced_click_delete_authentication_rule."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_CLICK_DELETE_AUTHENTICATION_RULE, **kwargs)

    def access_control_aaa_advanced_select_authentication_rule(self, element_name, rule_id, **kwargs):
        """Returns the result of access_control_aaa_advanced_select_authentication_rule."""
        args = {"rule_id": rule_id}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_SELECT_AUTHENTICATION_RULE,
                                    **kwargs)

    def access_control_aaa_advanced_delete_authentication_rule(self, element_name, rule_id, **kwargs):
        """Returns the result of access_control_aaa_advanced_delete_authentication_rule."""
        args = {"rule_id": rule_id}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_DELETE_AUTHENTICATION_RULE,
                                    **kwargs)

    def access_control_aaa_advanced_authentication_rule_open_edit_dialog(self, element_name, rule_id, **kwargs):
        """Returns the result of access_control_aaa_advanced_authentication_rule_open_edit_dialog."""
        args = {"rule_id": rule_id}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_AUTHENTICATION_RULE_OPEN_EDIT_DIALOG, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_authentication_type(self, element_name, auth_type, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_authentication_type."""
        args = {"auth_type": auth_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_AUTHENTICATION_TYPE, **kwargs)

    def access_control_aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button(self, element_name,
                                                                                            mac_type, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button."""
        args = {"type": mac_type}

        return self.execute_keyword(element_name, args, self.command_const.
                                    AAA_ADVANCED_RULE_DIALOG_CLICK_USER_MAC_HOST_PATTERN_OR_GROUP_BUTTON, **kwargs)

    def access_control_aaa_advanced_rule_dialog_set_pattern_or_group(self, element_name, mac_type, pattern_or_group,
                                                                     **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_set_pattern_or_group."""
        args = {"type": mac_type,
                "pattern_or_group": pattern_or_group}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SET_PATTERN_OR_GROUP, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_location(self, element_name, location, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_location."""
        args = {"location": location}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_LOCATION,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_authentication_method(self, element_name, auth_method, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_authentication_method."""
        args = {"auth_method": auth_method}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_AUTHENTICATION_METHOD, **kwargs)

    def access_control_aaa_advanced_rule_dialog_check_password_for_all_authentications(self, element_name, status,
                                                                                       **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_check_password_for_all_authentications."""
        args = {"status": status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_CHECK_PASSWORD_FOR_ALL_AUTHENTICATIONS,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_set_password(self, element_name, password, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_set_password."""
        args = {"password": password}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_RULE_DIALOG_SET_PASSWORD,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_set_ldap_authentication_type(self, element_name, ldap_auth_type,
                                                                             **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_set_ldap_authentication_type."""
        args = {"ldap_auth_type": ldap_auth_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SET_LDAP_AUTHENTICATION_TYPE, **kwargs)

    def access_control_aaa_advanced_rule_dialog_set_supported_radius_type(self, element_name, supported_radius_type,
                                                                          **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_set_supported_radius_type."""
        args = {"supported_radius_type": supported_radius_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SET_SUPPORTED_RADIUS_TYPE, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_ldap_configuration(self, element_name, ldap_config, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_ldap_configuration."""
        args = {"ldap_config": ldap_config}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_LDAP_CONFIGURATION, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_ldap_policy_mapping(self, element_name, ldap_policy_mapping,
                                                                           **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_ldap_policy_mapping."""
        args = {"ldap_policy_mapping": ldap_policy_mapping}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_LDAP_POLICY_MAPPING, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_primary_radius_server(self, element_name, radius_ip, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_primary_radius_server."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_PRIMARY_RADIUS_SERVER, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_backup_radius_server(self, element_name, radius_ip, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_backup_radius_server."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_BACKUP_RADIUS_SERVER, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_tertiary_radius_server(self, element_name, radius_ip, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_tertiary_radius_server."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_TERTIARY_RADIUS_SERVER, **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_quaternary_radius_server(self, element_name, radius_ip,
                                                                                **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_quaternary_radius_server."""
        args = {"radius_ip": radius_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_QUATERNARY_RADIUS_SERVER,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_inject_authentication_attributes(self, element_name,
                                                                                        auth_attributes, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_inject_authentication_attributes."""
        args = {"auth_attributes": auth_attributes}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_INJECT_AUTHENTICATION_ATTRIBUTES,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_select_inject_accounting_attributes(self, element_name, acct_attributes,
                                                                                    **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_select_inject_accounting_attributes."""
        args = {"acct_attributes": acct_attributes}

        return self.execute_keyword(element_name, args,
                                    self.command_const.AAA_ADVANCED_RULE_DIALOG_SELECT_INJECT_ACCOUNTING_ATTRIBUTES,
                                    **kwargs)

    def access_control_aaa_advanced_rule_dialog_save_configuration(self, element_name, **kwargs):
        """Returns the result of access_control_aaa_advanced_rule_dialog_save_configuration."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_RULE_DIALOG_SAVE_CONFIGURATION,
                                    **kwargs)

    def access_control_aaa_dialog_add_ldap_configuration(self, element_name, config_name, url, admin_user, admin_pw,
                                                         timeout, user_search_root, host_search_root, ou_search_root,
                                                         user_object_class, user_search_attr, keep_domain_user_lookup,
                                                         user_auth_type, host_object_class, host_search_attr,
                                                         use_fully_qualified_domain_name, ou_object_class, **kwargs):
        """Returns the result of aaa_dialog_add_ldap_configuration."""
        args = {"config_name": config_name,
                "url": url,
                "admin_user": admin_user,
                "admin_pw": admin_pw,
                "timeout": timeout,
                "user_search_root": user_search_root,
                "host_search_root": host_search_root,
                "ou_search_root": ou_search_root,
                "user_object_class": user_object_class,
                "user_search_attr": user_search_attr,
                "keep_domain_user_lookup": keep_domain_user_lookup,
                "user_auth_type": user_auth_type,
                "host_object_class": host_object_class,
                "host_search_attr": host_search_attr,
                "use_fully_qualified_domain_name": use_fully_qualified_domain_name,
                "ou_object_class": ou_object_class}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DIALOG_ADD_LDAP_CONFIGURATION, **kwargs)

    def access_control_aaa_dialog_select_ldap_configuration(self, element_name, config_name, **kwargs):
        """Returns the result of aaa_dialog_select_ldap_configuration."""
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DIALOG_SELECT_LDAP_CONFIGURATION,
                                    **kwargs)

    def access_control_aaa_dialog_test_ldap_configuration(self, element_name, config_name, **kwargs):
        """Returns the result of aaa_dialog_test_ldap_configuration."""
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DIALOG_TEST_LDAP_CONFIGURATION, **kwargs)

    def access_control_aaa_dialog_delete_ldap_configuration(self, element_name, config_name, **kwargs):
        """Returns the result of aaa_dialog_delete_ldap_configuration."""
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.command_const.AAA_DIALOG_DELETE_LDAP_CONFIGURATION,
                                    **kwargs)

    def aaa_advanced_rule_dialog_save_configuration(self, element_name, **kwargs):
        """Returns the result of aaa_advanced_rule_dialog_save_configuration."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.AAA_ADVANCED_RULE_DIALOG_SAVE_CONFIGURATION,
                                    **kwargs)

    # Old methods for 8.1.x.
    def aaa_edit_basic_aaa_configuration(self, element_name, local_mac_auth, mac_all, mac_pap, mac_chap, mac_mschap,
                                         mac_eap_md5, radius_1_ip, radius_2_ip, ldap, local_domain, **kwargs):
        """Returns the result of aaa_edit_basic_aaa_configuration."""
        args = {"local_mac_auth": local_mac_auth,
                "mac_all": mac_all,
                "mac_pap": mac_pap,
                "mac_chap": mac_chap,
                "mac_mschap": mac_mschap,
                "mac_eap_md5": mac_eap_md5,
                "radius_1_ip": radius_1_ip,
                "radius_2_ip": radius_2_ip,
                "ldap": ldap,
                "local_domain": local_domain}

        return self.execute_keyword(element_name, args, self.command_const.AAA_EDIT_BASIC_AAA_CONFIGURATION, **kwargs)
