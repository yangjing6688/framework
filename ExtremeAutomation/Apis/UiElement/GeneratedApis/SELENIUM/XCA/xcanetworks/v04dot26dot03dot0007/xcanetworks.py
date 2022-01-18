from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcanetworksBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcanetworks(XcanetworksBase):
    def click_add_to_create_new_network(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.onCreate()']")

        return ui_cmd_obj

    def click_network_name_to_open_network_settings(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).click_network_name_to_open_network_settings(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_network_name_ssid_and_status(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["network_name"], "//input[@id='name']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["ssid"], "//input[@id='ssid']")
        if arg_dict["status"] and ("enable" in str(arg_dict["status"]).lower()):
            self.builder.click(ui_cmd_obj, "//select[@ng-model='wlan.status']/option[.='Enabled']")
        else:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='wlan.status']/option[.='Disabled']")

        return ui_cmd_obj

    def select_network_auth_type(self, ui_cmd_obj, arg_dict):
        if "RADIUS" in str(arg_dict["auth_type"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@name='authType']/option[@value='string:WpaEnterpriseElement']")
        elif "PSK" in str(arg_dict["auth_type"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@name='authType']/option[@value='string:WpaPskElement']")
        elif "OPEN" in str(arg_dict["auth_type"]).upper():
            self.builder.click(ui_cmd_obj, "//select[@name='authType']/option[@value='string:None']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def edit_network_auth_type_privacy_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@ng-click='openPrivacy()']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], "//*[@id='psk']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//md-checkbox[@id='sharedSecretMask']",
                                                            "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict['is_masked']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@id='sharedSecretMask']")
        ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//*[@ng-click='$close(result)']")

        return ui_cmd_obj

    def config_mac_based_authentication(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//*[@id='mba']", "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict["use_mba"]) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//*[@id='mba']")
        ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def select_mba_timeout_role(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj,
                           "//select[@ng-model='wlan.mbatimeoutRoleId']/option[.='" + arg_dict["mba_role"] + "']")

        return ui_cmd_obj

    def select_auth_method(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj,
                           "//select[@ng-model='wlanModel.aaaConf.selectedAuthMethod']/option[.='" +
                           arg_dict["auth_method"] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def config_default_aaa(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).config_default_aaa(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_auth_method_radius(self, ui_cmd_obj, arg_dict):
        if arg_dict["primary_radius"]:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='wlanModel.aaaConf.priRadius']/option[@label='" +
                               arg_dict["primary_radius"] + "']")
        if arg_dict["backup_radius"]:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='wlanModel.aaaConf.secRadius']/option[@label='" +
                               arg_dict["backup_radius"] + "']")

        return ui_cmd_obj

    def add_new_radius_server(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).add_new_radius_server(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_new_radius_server_advanced_settings(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).config_new_radius_server_advanced_settings(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_new_radius_server(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).save_new_radius_server(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_auth_method_local_and_dhcp(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).config_auth_method_local_and_dhcp(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def add_new_dhcp_config(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).add_new_dhcp_config(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_dhcp_schema_definition(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).edit_dhcp_schema_definition(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def test_new_dhcp_config(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).test_new_dhcp_config(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_new_dhcp_config(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).save_new_dhcp_config(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_network_default_unauth_role(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@ng-model='wlan.unAuthenticatedUserDefaultRoleID']/option[.='" +
                           arg_dict["unauth_role"] + "']")

        return ui_cmd_obj

    def select_network_default_auth_role_and_vlan(self, ui_cmd_obj, arg_dict):
        if arg_dict["auth_role"]:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='wlan.authenticatedUserDefaultRoleID']/option[@label='" +
                               arg_dict["auth_role"] + "']")
        if arg_dict["vlan_name"]:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='wlan.defaultTopology']/option[contains(@label, '" +
                               arg_dict["vlan_name"] + "')]")

        return ui_cmd_obj

    def config_network_advanced_settings(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).config_network_advanced_settings(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_settings_and_back_to_networks_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.click(ui_cmd_obj, "//button[@ng-click='setBack()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='networksBack()']")

        return ui_cmd_obj

    def delete_network(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['network_name']) + "']")
        self.builder.click(ui_cmd_obj, "//button[contains(text(), 'CONFIGURE NETWORK')]")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.showDelete()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='delete(this)']")

        return ui_cmd_obj

    def verify_network_exists(self, ui_cmd_obj, arg_dict):
        xpath = "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" + \
                arg_dict['network_name'] + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network " + str(arg_dict["network_name"]) + " doesn't exist.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/../following-sibling::div[1]//div", arg_dict['ssid'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network ssid doesn't match expectation.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/../following-sibling::div[2]//div", arg_dict['status'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network status doesn't match expectation.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/../following-sibling::div[3]//div", arg_dict['auth_role'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network authentication role doesn't match expectation.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/../following-sibling::div[4]//div", arg_dict['auth_type'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network authentication type doesn't match expectation.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/../following-sibling::div[5]//div", arg_dict['vlan_name'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network vlan name doesn't match expectation.")

            return ui_cmd_obj

        return ui_cmd_obj

    def verify_network_does_not_exist(self, ui_cmd_obj, arg_dict):
        xpath = "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" + \
                arg_dict['network_name'] + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Network " + str(arg_dict["network_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Network " + str(arg_dict["network_name"]) + " still exist.")

        return ui_cmd_obj

    def select_whether_enable_captive_portal(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).select_whether_enable_captive_portal(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_captive_portal_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).select_captive_portal_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_whether_use_fqdn_for_connection(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).select_whether_use_fqdn_for_connection(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_whether_use_https_connection(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).select_whether_use_https_connection(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_ecp_url(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).edit_ecp_url(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_identity_and_shared_secret(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).edit_identity_and_shared_secret(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_send_successful_login(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcanetworks, self).select_send_successful_login(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
