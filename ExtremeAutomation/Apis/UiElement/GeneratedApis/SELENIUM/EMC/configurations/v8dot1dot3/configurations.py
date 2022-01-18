from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ConfigurationsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Configurations(ConfigurationsBase):
    def configs_aaa_default_check_authenticate_for(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:]",
                                         r"[0].checked")
        if "enable" in str(arg_dict["status"]) and not bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:] => "
                                   r".x-form-cb-input")
        elif "disable" in str(arg_dict["status"]) and bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj,
                                   r"#localMacAuthField checkbox[boxLabel=Authenticate Requests Locally for\:] => "
                                   r".x-form-cb-input")

        return ui_cmd_obj

    def configs_aaa_default_select_auth_methods(self, ui_cmd_obj, arg_dict):
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
                                             r"[0].checked")
            if not ui_cmd_obj.return_data and auth_method in common_methods_list:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#localMacAuthField checkbox[boxLabel=MAC \(" + str(auth_method) + r"\)] => "
                                       r".x-form-cb-label")
            elif ui_cmd_obj.return_data and auth_method not in common_methods_list:
                self.ext_builder.click(ui_cmd_obj,
                                       r"#localMacAuthField checkbox[boxLabel=MAC \(" + str(auth_method) + r"\)] => "
                                       r".x-form-cb-label")

        return ui_cmd_obj

    def configs_aaa_default_select_primary_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Primary RADIUS Server] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Primary RADIUS Server] boundlist => "
                               "div:textEquals(" + str(arg_dict["ip_address"]) + ")")

        return ui_cmd_obj

    def configs_aaa_default_select_backup_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS Server] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel radiusCombobox[fieldLabel=Backup RADIUS Server] boundlist => "
                               "div:textEquals(" + str(arg_dict["ip_address"]) + ")")

        return ui_cmd_obj

    def configs_aaa_default_select_ldap_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel ldapCombobox[fieldLabel=LDAP Configuration] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel ldapCombobox[fieldLabel=LDAP Configuration] boundlist => "
                               "div:textEquals(" + str(arg_dict["config_name"]) + ")")

        return ui_cmd_obj

    def configs_aaa_default_select_local_password_repository(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel localPasswordRepoCombo[fieldLabel=Local Password Repository] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "#nwcAAABasicInfoPanel localPasswordRepoCombo[fieldLabel=Local Password Repository] "
                               "boundlist=> div:textEquals(" + str(arg_dict["repo_name"]) + ")")

        return ui_cmd_obj

    def configs_aaa_default_save_aaa_default(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#aaaConfigBorderPanel button[text=Save] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def configs_aaa_default_cancel_aaa_default(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#aaaConfigBorderPanel button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def configs_click_add_access_control_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"#nacConfigGridWrapper_configs button[text=Add\.\.\.] => "
                               r".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def configs_click_delete_access_control_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_configs button[iconCls=deleteCell] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def configs_click_edit_access_control_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_configs button[iconCls=edit] => "
                               ".x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def configs_click_select_aaa_configuration_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "//span[contains(@class, 'x-btn-inner-gray-small') "
                                           "and .='Select AAA Configuration']",
                               strategy=self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def configs_select_aaa_configuration_dialog_select_aaa_configuration(self, ui_cmd_obj, arg_dict):
        self.configs_click_select_aaa_configuration_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "//input[@role='combobox' and @name='name']/../following-sibling::div[1]",
                               strategy=self.builder.constants.STRATEGY_XPATH)
        self.ext_builder.click(ui_cmd_obj, "//li[.='" + str(arg_dict["aaa_configuration"]) + "' and @role='option']",
                               strategy=self.builder.constants.STRATEGY_XPATH)
        self.ext_builder.click(ui_cmd_obj, "//div[@role='dialog'and @aria-hidden='false']"
                                           "//span[.='OK' and @class='x-btn-inner x-btn-inner-blue-small']",
                               strategy=self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def configs_select_access_control_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigGridWrapper_configs gridview => .x-grid-cell-inner:textEquals(" +
                               str(arg_dict["access_control_configuration"]) + ")")

        return ui_cmd_obj

    def configs_add_access_control_configuration(self, ui_cmd_obj, arg_dict):
        self.configs_click_add_access_control_configuration_button(ui_cmd_obj, arg_dict)
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["access_control_configuration"]),
                                    "textfield[fieldLabel=Name] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj, "button[text=Create] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def configs_delete_access_control_configuration(self, ui_cmd_obj, arg_dict):
        self.configs_select_access_control_configuration(ui_cmd_obj, arg_dict)
        self.configs_click_delete_access_control_configuration_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj
