from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcaaaaBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcaaaa(XcaaaaBase):
    def click_configure_default_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='setDefaultAAAConfig()']")

        return ui_cmd_obj

    def click_manage_certificates(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='manageNacCertificates()']")

        return ui_cmd_obj

    def click_radius_servers_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='RADIUS SERVERS']")

        return ui_cmd_obj

    def click_ldap_configurations_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='LDAP CONFIGURATIONS']")

        return ui_cmd_obj

    def click_local_password_repository_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='LOCAL PASSWORD REPOSITORY']")

        return ui_cmd_obj

    def click_add_to_create_a_new_radius_server(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='addRadiusServer()']")

        return ui_cmd_obj

    def click_add_to_create_a_new_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='addLdapConfig()']")

        return ui_cmd_obj

    def click_add_to_create_a_new_local_password_repository_user(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='addLocalPassUser()']")

        return ui_cmd_obj

    def select_aaa_authentication_method(self, ui_cmd_obj, arg_dict):
        if "RADIUS" in str(arg_dict["authentication_method"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@ng-model='authMethod']/option[@value='string:Proxy RADIUS']")
        elif "LOCAL" in str(arg_dict["authentication_method"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@ng-model='authMethod']/option[@value='string:Local']")
        elif "LDAP" in str(arg_dict["authentication_method"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@ng-model='authMethod']/option[@value='string:LDAP']")

        return ui_cmd_obj

    def select_aaa_primary_and_backup_radius(self, ui_cmd_obj, arg_dict):
        if arg_dict['primary_radius_server']:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='primaryRadiusServerIP']/option[@label='" +
                               str(arg_dict['primary_radius_server']) + "']")
        if arg_dict['backup_radius_server']:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='backupRadiusServerIP']/option[@label='" +
                               str(arg_dict['backup_radius_server']) + "']")

        return ui_cmd_obj

    def select_aaa_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@id='ldapConfiguration']/option[@label='" +
                           str(arg_dict['ldap_configuration']) + "']")

        return ui_cmd_obj

    def check_authenticate_locally_for_mac(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@id='authMacLocal']", "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict["auth_locally"]) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//*[@id='authMacLocal']")
        ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def save_config_and_back_to_aaa_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-disabled='false']")

        return ui_cmd_obj

    def click_radius_server_to_open_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['radius_server_ip']) + "']")

        return ui_cmd_obj

    def click_ldap_configuration_to_open_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['ldap_name']) + "']")

        return ui_cmd_obj

    def click_local_password_repository_user_to_open_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-row ng-scope']//div[2]/div[.='" +
                           str(arg_dict['username']) + "']")

        return ui_cmd_obj

    def edit_radius_server_settings(self, ui_cmd_obj, arg_dict):
        if arg_dict['radius_server_ip']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['radius_server_ip'], "//*[@id='radiusIPAddress']")
        if arg_dict['response_window']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['response_window'], "//*[@id='responseWindow']")
        if arg_dict['auth_timeout']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['auth_timeout'], "//*[@id='authTimeoutRadius']")
        if arg_dict['auth_retry_count']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['auth_retry_count'], "//*[@id='authRetryCountRadius']")
        if arg_dict['auth_client_udp_port']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['auth_client_udp_port'], "//*[@id='authRadiusUDPPort']")
        if arg_dict['acct_client_udp_port']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['acct_client_udp_port'], "//*[@id='radiusAcctClientUdpPort']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@id='proxyRadiusAcctReq']", "aria-checked", "true")
        if ("enable" in arg_dict['proxy_radius_acct_requests']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//*[@id='proxyRadiusAcctReq']")
        ui_cmd_obj.error_state = False
        if arg_dict['shared_secret']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['shared_secret'], "//*[@id='radiusSharedSecret']")
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//*[@ng-click='hideShowSharedSecret()']",
                                                                "aria-checked", "true")
            if StringUtils.string_to_boolean(arg_dict["is_masked"]) is ui_cmd_obj.error_state:
                self.builder.click(ui_cmd_obj, "//*[@ng-click='hideShowSharedSecret()']")
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def edit_radius_server_advanced_settings_and_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcaaaa, self).edit_radius_server_advanced_settings_and_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_ldap_connection_url(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['ldap_connection_url'],
                                "//*[@ng-model='newLDAPConfig.ldap_configuration_urls[key]']")

        return ui_cmd_obj

    def add_ldap_connection_url(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['ldap_connection_url'], "//*[@ng-model='ldapConnectionUrl']")
        self.builder.click(ui_cmd_obj, "//*[@ng-click='addLdapConnectionUrl()']")

        return ui_cmd_obj

    def edit_ldap_configuration_settings(self, ui_cmd_obj, arg_dict):
        if arg_dict['ldap_name']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['ldap_name'], "//*[@id='ldapConfigName']")
        if arg_dict['admin_username']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['admin_username'], "//*[@id='adminUsername']")
        if arg_dict['admin_password']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['admin_password'], "//*[@id='adminPassword']")
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//*[@ng-click='hideShowSharedSecret()']",
                                                                "aria-checked", "true")
            if StringUtils.string_to_boolean(arg_dict["is_masked"]) is ui_cmd_obj.error_state:
                self.builder.click(ui_cmd_obj, "//*[@ng-click='hideShowSharedSecret()']")
            ui_cmd_obj.error_state = False
        if arg_dict['user_search_root']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['user_search_root'], "//*[@id='userSearchRootLdap']")
        if arg_dict['host_search_root']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['host_search_root'], "//*[@id='hostSearchRootLdap']")
        if arg_dict['ou_search_root']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['ou_search_root'], "//*[@id='ouSearchRootLdap']")

        return ui_cmd_obj

    def edit_ldap_schema_definition_and_close(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcaaaa, self).edit_ldap_schema_definition_and_close(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_local_password_repository_user_settings(self, ui_cmd_obj, arg_dict):
        if arg_dict['status']:
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                                "//*[@id='userEnabled']", "aria-checked", "true")
            if ("enable" in arg_dict['status']) is ui_cmd_obj.error_state:
                self.builder.click(ui_cmd_obj, "//*[@id='userEnabled']")
            ui_cmd_obj.error_state = False
        if arg_dict['username']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['username'], "//*[@id='userUserName']")
        if arg_dict['display_name']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['display_name'], "//*[@id='userDisplayName']")
        if arg_dict['first_name']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['first_name'], "//*[@id='userFirstName']")
        if arg_dict['last_name']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['last_name'], "//*[@id='userLastName']")
        if arg_dict['hash_type']:
            if "PKCS5" in str(arg_dict["hash_type"]).upper():
                self.builder.click(ui_cmd_obj, "//select[@id='userPassHashType']/option[.='PKCS5 Reversible Hash']")
            if "SHA1" in str(arg_dict["hash_type"]).upper():
                self.builder.click(ui_cmd_obj, "//select[@id='userPassHashType']/option[.='SHA1 Non-Reversible Hash']")
        if arg_dict['password']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['password'], "//*[@id='userPassword']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['password'], "//*[@id='userPasswordConfirm']")
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                                "//*[@ng-model='passMask']", "aria-checked", "true")
            if StringUtils.string_to_boolean(arg_dict["is_masked"]) is ui_cmd_obj.error_state:
                self.builder.click(ui_cmd_obj, "//*[@ng-model='passMask']")
            ui_cmd_obj.error_state = False
        if arg_dict['description']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['description'], "//*[@id='userDescription']")

        return ui_cmd_obj

    def delete_radius_server(self, ui_cmd_obj, arg_dict):
        self.click_radius_server_to_open_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canDelete' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='deleteRadius(this)']")

        return ui_cmd_obj

    def delete_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.click_ldap_configuration_to_open_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canDelete' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='delete(this)']")

        return ui_cmd_obj

    def delete_local_password_repository_user(self, ui_cmd_obj, arg_dict):
        self.click_local_password_repository_user_to_open_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canDelete' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='delete(this)']")

        return ui_cmd_obj
