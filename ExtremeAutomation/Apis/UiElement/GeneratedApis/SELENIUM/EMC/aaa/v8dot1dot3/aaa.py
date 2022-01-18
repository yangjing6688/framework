from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as AaaBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Aaa(AaaBase):
    def aaa_confirm_radius_server_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(
            ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                        "#authManageRadiusServersGrid gridview", '[0].store.data.items.length')
        max_index = max(range(int(ui_cmd_obj.return_data)))
        for index in range(int(ui_cmd_obj.return_data)):
            self.ext_builder.component_query(
                ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel #authManageRadiusServersGrid "
                            "gridview", '[0].store.data.items[' + str(index) + '].data.ipAddressCol')
            if arg_dict['ip_address'] == str(ui_cmd_obj.return_data):
                self.logger.log_debug("RADIUS server with IP address: " + str(arg_dict["ip_address"]) +
                                      " is displayed in the grid.")
                break
            elif index is max_index:
                self.logger.log_debug("RADIUS server with IP address: " + str(arg_dict["ip_address"]) +
                                      " is NOT displayed in the grid.")
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def aaa_confirm_ldap_configuration_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(
            ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel #authManageLdapConfigGrid gridview",
            '[0].store.data.items.length')
        max_index = max(range(int(ui_cmd_obj.return_data)))
        for index in range(int(ui_cmd_obj.return_data)):
            self.ext_builder.component_query(
                ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel #authManageLdapConfigGrid "
                            "gridview", '[0].store.data.items[' + str(index) + '].data.nameCol')
            if arg_dict['config_name'] == str(ui_cmd_obj.return_data):
                self.logger.log_debug("LDAP configuration with name: " + str(arg_dict["config_name"]) +
                                      " is displayed in the grid.")
                break
            elif index is max_index:
                self.logger.log_debug("LDAP configuration with name: " + str(arg_dict["config_name"]) +
                                      " is NOT displayed in the grid.")
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def aaa_radius_server_click_add_radius_server_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                           "#authManageRadiusServersGrid button[iconCls=tableAddIcon] => "
                                           ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_radius_server_click_edit_radius_server_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                           "#authManageRadiusServersGrid button[iconCls=edit] => "
                                           ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_radius_server_click_delete_radius_server_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                           "#authManageRadiusServersGrid button[iconCls=deleteCell] => "
                                           ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_radius_server_delete_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                           "#authManageRadiusServersGrid gridview => .x-grid-cell-inner:textEquals(" +
                               str(arg_dict["ip_address"]) + ")")
        self.aaa_radius_server_click_delete_radius_server_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_radius_server_dialog_set_ip_and_response_window(self, ui_cmd_obj, arg_dict):
        if arg_dict["ip_address"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ip_address']),
                                        "#authManageRadiusAddEditWindow textfield[name=ipAddress] => .x-form-text")
        if arg_dict["response_window"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['response_window']),
                                        "#authManageRadiusAddEditWindow numberfield[name=responseWindow] => "
                                        ".x-form-text")

        return ui_cmd_obj

    def aaa_radius_server_dialog_set_authentication_via_emc(self, ui_cmd_obj, arg_dict):
        if arg_dict["timeout"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['timeout']),
                                        "#authManageRadiusAddEditWindow numberfield[name=timeout] => .x-form-text")
        if arg_dict["retries"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['retries']),
                                        "#authManageRadiusAddEditWindow numberfield[name=retries] => .x-form-text")

        return ui_cmd_obj

    def aaa_radius_server_dialog_set_configuration(self, ui_cmd_obj, arg_dict):
        if arg_dict["auth_port"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['auth_port']),
                                        "#authManageRadiusAddEditWindow numberfield[name=authPort] => .x-form-text")

        if arg_dict["proxy_accounting"] is not None:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#authManageRadiusAddEditWindow checkbox[name=radiusAccountingEnabled]",
                                             "[0].checked")
            if "enable" in str(arg_dict["proxy_accounting"]).lower() and not ui_cmd_obj.return_data:
                self.ext_builder.click(ui_cmd_obj,
                                       "#authManageRadiusAddEditWindow checkbox[name=radiusAccountingEnabled] => "
                                       ".x-form-cb-input")
            elif "disable" in str(arg_dict["proxy_accounting"]).lower() and ui_cmd_obj.return_data:
                self.ext_builder.click(ui_cmd_obj,
                                       "#authManageRadiusAddEditWindow checkbox[name=radiusAccountingEnabled] => "
                                       ".x-form-cb-input")

        if arg_dict["acct_port"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['acct_port']),
                                        "#authManageRadiusAddEditWindow numberfield[name=acctPort] => .x-form-text")

        return ui_cmd_obj

    def aaa_radius_server_dialog_change_server_shared_secret(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['shared_secret']),
                                    "#authManageRadiusAddEditWindow passwordfield[name=sharedSecret] => .x-form-text")

        return ui_cmd_obj

    def aaa_radius_server_dialog_open_advanced_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"#authManageRadiusAddEditWindow button[text=Advanced\.\.\.] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_radius_advanced_config_dialog_username_setting(self, ui_cmd_obj, arg_dict):
        if arg_dict['username_format'] is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   "#authManageRadiusAddEditAdvancedPanel combobox[fieldLabel=Username Format] => "
                                   ".x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "#authManageRadiusAddEditAdvancedPanel combobox[fieldLabel=Username Format] "
                                   "boundlist => li:textEquals(" + str(arg_dict['username_format']) + ")")

        if arg_dict["require_msg_auth"] is not None:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#authManageRadiusAddEditAdvancedPanel "
                                             "checkboxfield[name=requireMessageAuthenticator]", "[0].checked")
            if "enable" in str(arg_dict["require_msg_auth"]).lower() and not ui_cmd_obj.return_data:
                self.ext_builder.click(ui_cmd_obj,
                                       "#authManageRadiusAddEditAdvancedPanel "
                                       "checkboxfield[name=requireMessageAuthenticator] => .x-form-checkbox")
            elif "disable" in str(arg_dict["require_msg_auth"]).lower() and ui_cmd_obj.return_data:
                self.ext_builder.click(ui_cmd_obj,
                                       "#authManageRadiusAddEditAdvancedPanel "
                                       "checkboxfield[name=requireMessageAuthenticator] => .x-form-checkbox")

        return ui_cmd_obj

    def aaa_radius_advanced_config_dialog_health_check_use_access_request(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#authManageRadiusAddEditAdvancedPanel "
                                         "checkboxfield[name=disableAccessRequest]", "[0].checked")
        if "enable" in str(arg_dict["use_access_request"]).lower():
            if not ui_cmd_obj.return_data:
                self.ext_builder.click(ui_cmd_obj,
                                       "#authManageRadiusAddEditAdvancedPanel "
                                       "checkboxfield[name=disableAccessRequest] => .x-form-checkbox")
            if arg_dict["access_request_username"] is not None:
                self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["access_request_username"]),
                                            "#authManageRadiusAddEditAdvancedPanel "
                                            "#accessRequestFields textfield[fieldLabel=Username] => .x-form-text")
            if arg_dict["access_request_password"] is not None:
                self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["access_request_password"]),
                                            "#authManageRadiusAddEditAdvancedPanel #accessRequestFields "
                                            "passwordfield[fieldLabel=Password] => .x-form-text")
        elif "disable" in str(arg_dict["use_access_request"]).lower() and ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj,
                                   "#authManageRadiusAddEditAdvancedPanel checkboxfield[name=disableAccessRequest] => "
                                   ".x-form-checkbox")

        return ui_cmd_obj

    def aaa_radius_advanced_config_dialog_health_check_other_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#authManageRadiusAddEditAdvancedPanel "
                                         "checkboxfield[name=disableServerStatus]", "[0].checked")
        if "enable" in str(arg_dict["use_server_status_request"]).lower() and not ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj,
                                   "#authManageRadiusAddEditAdvancedPanel checkboxfield[name=disableServerStatus] => "
                                   ".x-form-cb-input")
        elif "disable" in str(arg_dict["use_server_status_request"]).lower() and ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj,
                                   "#authManageRadiusAddEditAdvancedPanel checkboxfield[name=disableServerStatus] => "
                                   ".x-form-cb-input")

        if arg_dict["check_interval"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["check_interval"]),
                                        "#authManageRadiusAddEditAdvancedPanel numberfield[name=checkInterval] => "
                                        ".x-form-field")
        if arg_dict["answers_number"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["answers_number"]),
                                        "#authManageRadiusAddEditAdvancedPanel "
                                        "numberfield[name=numberOfAnswersUntilAlive] => .x-form-field")
        if arg_dict["revive_interval"] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["revive_interval"]),
                                        "#authManageRadiusAddEditAdvancedPanel numberfield[name=reviveInterval] => "
                                        ".x-form-field")

        return ui_cmd_obj

    def aaa_radius_advanced_config_dialog_save_advanced_setting(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageRadiusAddEditAdvancedWindow button[text=OK] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_radius_advanced_config_dialog_cancel_advanced_setting(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageRadiusAddEditAdvancedWindow button[text=Cancel] => "
                               ".x-btn-inner-default-small")

        return ui_cmd_obj

    def aaa_radius_server_dialog_save_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageRadiusAddEditWindow button[text=Save] => .x-btn-inner-blue-small")
        self.ext_builder.component_query(ui_cmd_obj, 'title[text=Warning]', '[0].config.text')
        if ui_cmd_obj.return_data == 'Warning':
            self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
        elif ui_cmd_obj.return_data != u'':
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def aaa_radius_server_dialog_cancel_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageRadiusAddEditWindow button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def aaa_default_check_auth_request_for(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:]",
                                         "[0].checked")
        if "enable" in str(arg_dict["status"]) and not bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:] => "
                                   ".x-form-cb-input")
        elif "disable" in str(arg_dict["status"]) and bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:] => "
                                   ".x-form-cb-input")

        return ui_cmd_obj

    def aaa_default_select_auth_methods(self, ui_cmd_obj, arg_dict):
        methods_list = sorted(["All", "PAP", "CHAP", "MsCHAP", "EAP-MD5"])
        selected_methods_list = sorted(["EAP-MD5" if "EAP" in method else method for method in
                                        str(arg_dict["auth_methods"]).replace(" ", "").split(",")])
        if "All" in selected_methods_list:
            common_methods_list = methods_list = ["All"]
        else:
            common_methods_list = list(set(methods_list).intersection(selected_methods_list))

        for auth_method in methods_list:
            self.ext_builder.component_query(ui_cmd_obj,
                                             r"#localMacAuthField checkbox[boxLabel=MAC \(" + str(auth_method) + r"\)]",
                                             "[0].checked")
            if not ui_cmd_obj.return_data and auth_method in common_methods_list:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#localMacAuthField checkbox[boxLabel=MAC \(" + str(auth_method) +
                                       r"\)] => .x-form-cb-label")
            elif ui_cmd_obj.return_data and auth_method not in common_methods_list:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#localMacAuthField checkbox[boxLabel=MAC \(" + str(auth_method) +
                                       r"\)] => .x-form-cb-label")

        return ui_cmd_obj

    def aaa_default_select_primary_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Primary RADIUS Server] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Primary RADIUS Server] boundlist => "
                               "div:textEquals(" + str(arg_dict["ip_address"]) + ")")

        return ui_cmd_obj

    def aaa_default_select_backup_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS Server] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS Server] boundlist => "
                               "div:textEquals(" + str(arg_dict["ip_address"]) + ")")

        return ui_cmd_obj

    def aaa_default_select_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel ldapCombobox[fieldLabel=LDAP Configuration] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel ldapCombobox[fieldLabel=LDAP Configuration] boundlist => "
                               "div:textEquals(" + str(arg_dict["config_name"]) + ")")

        return ui_cmd_obj

    def aaa_default_select_local_password_repository(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel localPasswordRepoCombo[fieldLabel=Local Password Repository] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel localPasswordRepoCombo[fieldLabel=Local Password Repository] "
                               "boundlist=> div:textEquals(" + str(arg_dict["repo_name"]) + ")")

        return ui_cmd_obj

    def aaa_default_save_default_aaa_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#aaaConfigBorderPanel button[text=Save] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_default_cancel_default_aaa_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#aaaConfigBorderPanel button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def aaa_click_add_aaa_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfigList button[iconCls=addCell] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_click_edit_aaa_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfigList button[iconCls=edit] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_click_delete_aaa_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfigList button[iconCls=deleteCell] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_select_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj,
                                                  '#nacConfigGridWrapper_aaaConfigList gridview', '[0]', 'nameCol',
                                                  arg_dict['aaa_config_name'])

        return ui_cmd_obj

    def aaa_add_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.aaa_click_add_aaa_configuration_button(ui_cmd_obj, arg_dict)
        if "advanced" in str(arg_dict["aaa_config_type"]).lower():
            self.ext_builder.click(ui_cmd_obj, "checkbox[boxLabel=Advanced Configuration] => .x-form-cb-input")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["aaa_config_name"]),
                                    "textfield[fieldLabel=Name] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj, "button[text=Add] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_delete_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.aaa_select_aaa_configuration(ui_cmd_obj, arg_dict)
        self.aaa_click_delete_aaa_configuration_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_advanced_click_add_authentication_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfig button[iconCls=addCell] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_advanced_click_edit_authentication_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfig button[iconCls=edit] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_advanced_click_delete_authentication_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfig button[iconCls=deleteCell] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def aaa_advanced_select_authentication_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_aaaConfig gridview => .x-grid-item:nth-of-type(" +
                               str(arg_dict["rule_id"]) + ") :nth-of-type(2) .x-grid-cell-inner")

        return ui_cmd_obj

    def aaa_advanced_delete_authentication_rule(self, ui_cmd_obj, arg_dict):
        self.aaa_advanced_select_authentication_rule(ui_cmd_obj, arg_dict)
        self.aaa_click_delete_aaa_configuration_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def aaa_advanced_authentication_rule_open_edit_dialog(self, ui_cmd_obj, arg_dict):
        self.aaa_advanced_select_authentication_rule(ui_cmd_obj, arg_dict)
        self.aaa_advanced_click_edit_authentication_rule(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_authentication_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=authType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=authType] boundlist => :textEquals(" +
                               str(arg_dict["auth_type"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button(self, ui_cmd_obj, arg_dict):
        if "pattern" in str(arg_dict["type"]).lower():
            self.ext_builder.click(ui_cmd_obj, "radio[boxLabel=Pattern] => .x-form-cb-input")
        elif "group" in str(arg_dict["type"]).lower():
            self.ext_builder.click(ui_cmd_obj, "radio[boxLabel=Group] => .x-form-cb-input")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_set_pattern_or_group(self, ui_cmd_obj, arg_dict):
        self.aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button(ui_cmd_obj, arg_dict)
        if "pattern" in str(arg_dict["type"]).lower():
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["pattern_or_group"]),
                                        "textfield[name=patternOrGroup_pattern] => .x-form-text")
        elif "group" in str(arg_dict["type"]).lower():
            self.ext_builder.click(ui_cmd_obj, "combo[name=patternOrGroup_group] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj, "combo[name=patternOrGroup_group] boundlist => :textEquals(" +
                                   str(arg_dict["pattern_or_group"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_location(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=location] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=location] boundlist => :textEquals(" +
                               str(arg_dict["location"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_authentication_method(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#authMethodValueCombo => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#authMethodValueCombo boundlist => :textEquals(" +
                               str(arg_dict["auth_method"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_check_password_for_all_authentications(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "checkbox[boxLabel=Password for all Authentications]",
                                         "[0].checked")
        if "enable" in str(arg_dict["status"]) and not bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[boxLabel=Password for all Authentications] => .x-form-cb-input")
        elif "disable" in str(arg_dict["status"]) and bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[boxLabel=Password for all Authentications] => .x-form-cb-input")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_set_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["password"]),
                                    "passwordfield[name=password] => .x-form-text")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_set_ldap_authentication_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["ldap_auth_type"]),
                                    "textfield[name=ldapAuthType] => .x-form-text")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_set_supported_radius_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["supported_radius_type"]),
                                    "textfield[name=supportedRadiusType] => .x-form-text")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "ldapCombobox[name=ldapConfig] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "ldapCombobox[name=ldapConfig] boundlist => div:textEquals(" +
                               str(arg_dict["ldap_config"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_ldap_policy_mapping(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=ldapPolicyMapping] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=ldapPolicyMapping] boundlist => :textEquals(" +
                               str(arg_dict["ldap_policy_mapping"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_primary_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius1] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius1] boundlist => div:textEquals(" +
                               str(arg_dict["radius_ip"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_backup_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius2] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius2] boundlist => div:textEquals(" +
                               str(arg_dict["radius_ip"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_tertiary_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius3] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius3] boundlist => div:textEquals(" +
                               str(arg_dict["radius_ip"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_quaternary_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius4] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusCombobox[name=radius4] boundlist => div:textEquals(" +
                               str(arg_dict["radius_ip"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_inject_authentication_attributes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusAttrCombobox[name=radProxyAuth] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusAttrCombobox[name=radProxyAuth] boundlist => div:textEquals(" +
                               str(arg_dict["auth_attributes"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_select_inject_accounting_attributes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "radiusAttrCombobox[name=radProxyAcct] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "radiusAttrCombobox[name=radProxyAcct] boundlist => div:textEquals(" +
                               str(arg_dict["acct_attributes"]) + ")")

        return ui_cmd_obj

    def aaa_advanced_rule_dialog_save_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcAddEditAAAEntryWindow button[text=OK] => .x-btn-inner-blue-small")
        self.ext_builder.click(ui_cmd_obj, "#aaaConfigBorderPanel button[text=Save] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def aaa_dialog_add_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab panel #nacConfigCenterPanel #configContentPanel "
                               "authManageRadiusServersPanel #authManageRadiusServersGrid button[text=Add...] => "
                               ".x-btn-button")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ip_address']),
                                    "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                    "textfield[name=ipAddress] => .x-form-text")
        if str(arg_dict['response_window']) != '20':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['response_window']),
                                        "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                        "numberfield[name=responseWindow] => .x-form-text")
        if str(arg_dict['timeout']) != '2':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['timeout']),
                                        "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                        "panel[title=Authentication via Extreme Management Center or Captive Portal] "
                                        "numberfield[name=timeout] => .x-form-text")
        if str(arg_dict['retries']) != '1':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['retries']),
                                        "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                        "panel[title=Authentication via Extreme Management Center or Captive Portal] "
                                        "numberfield[name=retries] => .x-form-text")
        if str(arg_dict['auth_port']) != '1812':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['auth_port']),
                                        "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                        "panel[title=Configuration] numberfield[name=authPort] => .x-form-text")
        if str(arg_dict['acct_port']) != '1813':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['acct_port']),
                                        "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                        "panel[title=Configuration] numberfield[name=acctPort] => .x-form-text")
        if StringUtils.string_to_boolean(arg_dict['radius_accounting']) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   ">>#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                   "panel[title=Configuration] checkboxfield[name=radiusAccountingEnabled]")

        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['shared_secret']),
                                    "#authManageRadiusAddEditWindow authManageRadiusAddEditPanel "
                                    "panel[title=Change Server Shared Secret] passwordfield[name=sharedSecret] => "
                                    ".x-form-text")
        self.ext_builder.click(ui_cmd_obj, "#authManageRadiusAddEditWindow button[text=Save] => .x-btn-button")
        self.ext_builder.click(ui_cmd_obj, "#ok => .x-btn-button")

        return ui_cmd_obj

    def aaa_dialog_delete_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab treeview => .x-tree-node-text:contains(AAA)")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                               "#nacConfigGridWrapper_aaaConfigList tableview => .x-grid-cell-first .x-grid-cell-inner")
        self.ext_builder.click(ui_cmd_obj,
                               r"#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                               r"#nacConfigGridWrapper_aaaConfigList button[text=Edit\.\.\.] => "
                               r".x-btn-inner-default-toolbar-small")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel "
                               "#nwcAAAConfigPanel #nwcAAABasicInfoPanel "
                               "radiusCombobox[fieldLabel=Primary RADIUS Server] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel "
                               "#nwcAAABasicInfoPanel radiusCombobox[name=radius1] boundlist => div:textEquals(None)")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel button[text=Save] => "
                               ".x-btn-inner-blue-small")

        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab treeview => .x-tree-node-text:contains(RADIUS Servers)")
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab #nacConfigCenterPanel #configContentPanel #authManageRadiusServersGrid '
                               'tableview => .x-grid-cell-inner:contains(' + arg_dict['ip_address'] + ')')
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                               '#authManageRadiusServersGrid button[iconCls=deleteCell] => '
                               '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def aaa_edit_basic_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nacConfigTab treeview => .x-tree-node-text:contains(AAA)")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                               "#nacConfigGridWrapper_aaaConfigList tableview => .x-grid-cell-first .x-grid-cell-inner")
        self.ext_builder.click(ui_cmd_obj,
                               r"#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                               r"#nacConfigGridWrapper_aaaConfigList button[text=Edit\.\.\.] => "
                               r".x-btn-inner-default-toolbar-small")

        if StringUtils.string_to_boolean(arg_dict['local_mac_auth']) is True:
            local_mac_auth = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj,
                                                                          'Authenticate Requests Locally for:')
            if StringUtils.string_to_boolean(arg_dict['local_mac_auth']) is True and \
                    StringUtils.string_to_boolean(local_mac_auth) is False:
                self.ext_builder.click(ui_cmd_obj,
                                       r'#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                       r'#nwcAAAConfigPanel #localMacAuthField checkbox[boxLabel=Authenticate Requests '
                                       r'Locally for\:] => .x-form-cb-input')

            mac_all = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (All)')
            if StringUtils.string_to_boolean(arg_dict['mac_all']) is True and \
                    StringUtils.string_to_boolean(mac_all) is False:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel "
                                       r"#localMacAuthField checkboxfield[name=MAC \(All\)] => [data-ref='displayEl']")
            elif StringUtils.string_to_boolean(arg_dict['mac_all']) is False and \
                    StringUtils.string_to_boolean(mac_all) is True:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel "
                                       r"#localMacAuthField checkboxfield[name=MAC \(All\)] => [data-ref='displayEl']")

            mac_all = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (All)')
            if StringUtils.string_to_boolean(mac_all) is False:
                mac_pap = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (PAP)')
                if StringUtils.string_to_boolean(arg_dict['mac_pap']) is True and \
                        StringUtils.string_to_boolean(mac_pap) is False:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(PAP\)] => "
                                           r"[data-ref='displayEl']")
                elif StringUtils.string_to_boolean(arg_dict['mac_pap']) is False and \
                        StringUtils.string_to_boolean(mac_pap) is True:
                    self.ext_builder.click(ui_cmd_obj, r"#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                                       r"#nwcAAAConfigPanel #localMacAuthField "
                                                       r"checkboxfield[name=MAC \(PAP\)] => [data-ref='displayEl']")

                mac_chap = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (CHAP)')
                if StringUtils.string_to_boolean(arg_dict['mac_chap']) is True and \
                        StringUtils.string_to_boolean(mac_chap) is False:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel "
                                           r"#nwcAAAConfigPanel #localMacAuthField checkboxfield[name=MAC \(CHAP\)] => "
                                           r"[data-ref='displayEl']")
                elif StringUtils.string_to_boolean(arg_dict['mac_chap']) is False and \
                        StringUtils.string_to_boolean(mac_chap) is True:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(CHAP\)] => "
                                           r"[data-ref='displayEl']")

                mac_mschap = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (MsCHAP)')
                if StringUtils.string_to_boolean(arg_dict['mac_mschap']) is True and \
                        StringUtils.string_to_boolean(mac_mschap) is False:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(MsCHAP\)] => "
                                           r"[data-ref='displayEl']")
                elif StringUtils.string_to_boolean(arg_dict['mac_machap']) is False and \
                        StringUtils.string_to_boolean(mac_mschap) is True:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(MsCHAP\)] => "
                                           r"[data-ref='displayEl']")

                mac_eap_md5 = self.is_basic_aaa_config_default_box_checked(ui_cmd_obj, 'MAC (EAP-MD5)')
                if StringUtils.string_to_boolean(arg_dict['mac_eap_md5']) is True and \
                        StringUtils.string_to_boolean(mac_eap_md5) is False:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(EAP-MD5\)] => "
                                           r"[data-ref='displayEl']")
                elif StringUtils.string_to_boolean(arg_dict['mac_eap_md5']) is False and \
                        StringUtils.string_to_boolean(mac_eap_md5) is True:
                    self.ext_builder.click(ui_cmd_obj,
                                           r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel"
                                           r" #localMacAuthField checkboxfield[name=MAC \(EAP-MD5\)] => "
                                           r"[data-ref='displayEl']")

        if str(arg_dict['radius_1_ip']) is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   "#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel "
                                   "#nwcAAAConfigPanel #nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Primary RADIUS "
                                   "Server] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "#nacConfigTab #nacConfigCenterPanel #configContentPanel #nwcAAAConfigPanel "
                                   "#nwcAAABasicInfoPanel radiusCombobox[name=radius1] boundlist => div:textEquals(" +
                                   str(arg_dict['radius_1_ip']) + ")")
        if str(arg_dict['radius_2_ip']) is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS '
                                   'Server] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS '
                                   'Server] boundlist => div:textEquals(' + arg_dict['radius_2_ip'] + ')')
        if str(arg_dict['ldap']) is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel ldapCombobox => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel ldapCombobox boundlist => '
                                   'div:textEquals(' + arg_dict['ldap'] + ')')
        if str(arg_dict['local_domain']) is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel localPasswordRepoCombo => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel #configContentPanel #aaaConfigBorderPanel '
                                   '#nwcAAAConfigPanel #nwcAAABasicInfoPanel localPasswordRepoCombo boundlist => '
                                   'div:textEquals(' + arg_dict['local_domain'] + ')')
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel #configContentPanel button[text=Save] => "
                               ".x-btn-inner-blue-small")
        self.ext_builder.delay(ui_cmd_obj, "5000")

        return ui_cmd_obj

    def aaa_dialog_add_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab treeview => .x-tree-node-text:textEquals(LDAP Configurations)")
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab panel #nacConfigCenterPanel #configContentPanel "
                               "authManageLdapConfigPanel #authManageLdapConfigGrid button[text=Add...] => "
                               ".x-btn-button")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['config_name']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "textfield[name=configName] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=LDAP Connection "
                               "URLs] gridpanel button[text=Add...] => .x-btn-button")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['url']),
                                    "window[title=LDAP Connection URL] textfield[inputType=text] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj, "window[title=LDAP Connection URL] button[text=OK] => .x-btn-button")

        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['admin_user']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Authentication Settings] textfield[name=adminUsername] => "
                                    ".x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['admin_pw']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Authentication Settings] passwordfield[name=adminPassword] => "
                                    ".x-form-text")
        if str(arg_dict['timeout']) != '4':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['timeout']),
                                        "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                        "panel[title=Authentication Settings] numberfield[name=timeout] => "
                                        ".x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_search_root']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Search Settings] textfield[name=userSearchRoot] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['host_search_root']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Search Settings] textfield[name=hostSearchRoot] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ou_search_root']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Search Settings] textfield[name=ouSearchRoot] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_object_class']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Schema Definition] textfield[name=userObjectClass] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_search_attr']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Schema Definition] textfield[name=userSearchAttribute] => "
                                    ".x-form-text")
        if StringUtils.string_to_boolean(arg_dict['keep_domain_user_lookup']) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   ">>#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=Schema "
                                   "Definition] checkboxfield[name=keepDomainForUserLookup]")
        self.ext_builder.click(ui_cmd_obj,
                               "#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=Schema Definition] "
                               "combobox[name=userAuthenticationType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=userAuthenticationType].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['user_auth_type']) + ")")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['host_object_class']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=Schema "
                                    "Definition] textfield[name=hostObjectClass] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['host_search_attr']),
                                    "#authManageLdapAddEditWindow authManageLdapAddEditPanel "
                                    "panel[title=Schema Definition] textfield[name=hostSearchAttribute] => "
                                    ".x-form-text")
        if StringUtils.string_to_boolean(arg_dict['use_fully_qualified_domain_name']) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   ">>#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=Schema "
                                   "Definition] checkboxfield[name=keepDomainForHostLookup]")

        if str(arg_dict['ou_object_class']) != 'organizationalUnit':
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ou_object_class']),
                                        "#authManageLdapAddEditWindow authManageLdapAddEditPanel panel[title=Schema "
                                        "Definition] textfield[name=ouObjectClass] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj, ">>#authManageLdapAddEditWindow button[text=Save]")

        return ui_cmd_obj

    def aaa_dialog_delete_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.aaa_dialog_select_ldap_configuration(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab panel #nacConfigCenterPanel #configContentPanel "
                               "authManageLdapConfigPanel #authManageLdapConfigGrid button[text=Delete] => "
                               ".x-btn-button")
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-button")

        return ui_cmd_obj

    def aaa_dialog_select_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab treeview => .x-tree-node-text:textEquals(LDAP Configurations)")
        self.builder.click(ui_cmd_obj, "//*[@class='x-grid-cell-inner ' and .='" + str(arg_dict["config_name"]) + "']")

        return ui_cmd_obj

    def aaa_dialog_test_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.aaa_dialog_select_ldap_configuration(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj,
                               r"#nacConfigTab #nacConfigCenterPanel #configContentPanel #authManageLdapConfigGrid "
                               r"button[text=Test\.\.\.] => .x-btn-inner-default-toolbar-small")
        self.ext_builder.delay(ui_cmd_obj, "2000")
        self.ext_builder.click(ui_cmd_obj, "#ldapConfigTestWindow button[text=Close] => .x-btn-inner-default-small")

        return ui_cmd_obj
