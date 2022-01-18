from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EnginesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Engines(EnginesBase):
    def engines_dialog_add_access_control_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab nacConfigApplianceTree[title=Engines] treeview => '
                               '.x-tree-node-text:textEquals(' + arg_dict['engine_group'] + ')')
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab #nacConfigCenterPanel panel[title=Engine Group - ' +
                               arg_dict['engine_group'] + ']#configContentPanel tab[text=Access Control Engines] => '
                               '.x-tab-inner')
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab #nacConfigCenterPanel #configContentPanel #allAppliancesNwcTab '
                               '#nacConfigGridWrapper_allappliances button[iconCls=addCell] => '
                               '.x-btn-inner-default-toolbar-small')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['ip_address'],
                                    'textfield[fieldLabel=IP Address] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['engine_name'], 'textfield[fieldLabel=Name] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, "combo[fieldLabel=SNMP Profile] => .x-form-text")
        self.ext_builder.click(ui_cmd_obj, "combo[fieldLabel=SNMP Profile].getPicker() => "
                                           ".x-boundlist-item:contains(" + str(arg_dict['profile']) + ")")
        self.ext_builder.click(ui_cmd_obj, "button[text=Add] => .x-btn-inner-blue-small")
        self.ext_builder.click(ui_cmd_obj, "#ok => .x-btn-inner-blue-small")
        self.ext_builder.delay(ui_cmd_obj, '15000')

        return ui_cmd_obj

    def engines_dialog_delete_access_control_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab nacConfigApplianceTree[title=Engines] treeview => '
                                           '.x-tree-node-text:textEquals(All Engines)')
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                                           '#allAppliancesNwcTab #nacConfigGridWrapper_allappliances gridview => '
                                           '.x-grid-cell-first .x-grid-cell-inner')

        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                                           '#allAppliancesNwcTab #nacConfigGridWrapper_allappliances '
                                           'button[iconCls=deleteCell] => .x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def engines_dialog_add_switch(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel panel[title=Engine Group - ' +
                               arg_dict['engine_group'] + ']#configContentPanel tab[text=Switches] => .x-tab-inner')
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                                           '#switchesNwcTab #nacConfigGridWrapper_switches button[iconCls=addCell]'
                                           ' => .x-btn-inner-default-toolbar-small')
        self.builder.double_click(ui_cmd_obj, "//span[contains(text (),'All Devices')]")
        self.ext_builder.component_query(ui_cmd_obj, '[itemId=nacAddSwitchDeviceSelectionTree]',
                                         '[0].items.items[0].body.dom.childElementCount')
        end_index = ui_cmd_obj.return_data
        self.logger.log_debug("End index is " + str(end_index))
        if not end_index:
            ui_cmd_obj.error_state = True
            return ui_cmd_obj
        index = 0
        while index < end_index:
            self.ext_builder.component_query(ui_cmd_obj, '[itemId=nacAddSwitchDeviceSelectionTree]',
                                             '[0].items.items[0].body.dom.childNodes[' + str(index) + '].innerText')
            if arg_dict['switch_ip'] in ui_cmd_obj.return_data:
                index += 1
                self.ext_builder.click(ui_cmd_obj, '#nwcAddSwitchesWindow #nacAddSwitchDeviceSelectionTree treeview => '
                                                   '.x-grid-item:nth-of-type(' + str(index) + ') .x-tree-checkbox')
                break
            elif ui_cmd_obj.return_data != u'':
                index += 1
            else:
                ui_cmd_obj.error_state = True
                break
        self.ext_builder.click(ui_cmd_obj, '#nwcAddSwitchesWindow combo[name=primaryGateway] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#nwcAddSwitchesWindow combo[name=primaryGateway] boundlist => '
                                           ':textEquals(' + str(arg_dict['primary_engine_name']) + '/' +
                                           str(arg_dict['primary_engine_ip']) + ')')
        self.ext_builder.click(ui_cmd_obj, '>>#nwcAddSwitchesWindow button[text=Save]')
        self.ext_builder.delay(ui_cmd_obj, '15000')
        if arg_dict['device_type'] == "exos" or arg_dict['device_type'] == "ewc" or arg_dict['device_type'] == "xca":
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Enforce Policy Domain]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Enforce Policy Domain':
                self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')
                self.ext_builder.delay(ui_cmd_obj, '10000')
            else:
                ui_cmd_obj.error_state = True
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Success]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Success':
                self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = False
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Save Successful]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Save Successful':
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = False
        if arg_dict['device_type'] != "exos" and arg_dict['device_type'] != "ewc" and arg_dict['device_type'] != "xca":
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Save Successful]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Save Successful':
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def engines_dialog_delete_switch(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel panel[title=Engine Group - ' +
                               arg_dict['engine_group'] + ']#configContentPanel tab[text=Switches] => .x-tab-inner')
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj,
                                                  '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                                                  '#switchesNwcTab #nacConfigGridWrapper_switches gridview',
                                                  '[0]', 'switchIpCol', arg_dict['switch_ip'])
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel #configContentPanel #switchesNwcTab '
                                           '#nacConfigGridWrapper_switches button[iconCls=deleteCell] => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_switch_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=switchType] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=switchType] boundlist => :textEquals(' +
                               arg_dict['switch_type'] + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_primary_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=primaryGateway] => .x-form-trigger')
        if arg_dict['primary_engine_name'] == 'None':
            self.ext_builder.click(ui_cmd_obj,
                                   '#nwcEditSwitchesWindow combo[name=primaryGateway] boundlist => '
                                   ':textEquals(' + arg_dict['primary_engine_name'] + ')')
        elif arg_dict['primary_engine_name'] != 'None':
            self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=primaryGateway] boundlist => '
                                   ':textEquals(' + str(arg_dict['primary_engine_name']) + '/' +
                                   str(arg_dict['primary_engine_ip']) + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_secondary_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=secondaryGateway] => .x-form-trigger')
        if arg_dict['secondary_engine_name'] == 'None':
            self.ext_builder.click(ui_cmd_obj,
                                   '#nwcEditSwitchesWindow combo[name=secondaryGateway] boundlist => '
                                   ':textEquals(' + arg_dict['secondary_engine_name'] + ')')
        elif arg_dict['secondary_engine_name'] != 'None':
            self.ext_builder.click(ui_cmd_obj,
                                   '#nwcEditSwitchesWindow combo[name=secondaryGateway] boundlist => '
                                   ':textEquals(' + str(arg_dict['secondary_engine_name']) + '/' +
                                   str(arg_dict['secondary_engine_ip']) + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_auth_access_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=authAccessType] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=authAccessType] boundlist => "
                                           ".x-boundlist-item:contains(" + str(arg_dict['access_type']) + ")")

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_virtual_router_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vr_name'], '#nwcEditSwitchesWindow textfield[name=vrName] => '
                                                                     '.x-form-text')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_radius_attr_to_send(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=attributesToSend] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=attributesToSend] boundlist => "
                                           ":textEquals(" + str(arg_dict['attributes_to_send']) + ")")

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_radius_accounting(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=radiusAccounting] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=radiusAccounting] boundlist => "
                                           ".x-boundlist-item:contains(" + str(arg_dict['radius_accounting']) + ")")

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_radius_mgmt_server_1(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow radiusCombobox[name=managementRadiusServer1] "
                                           "=> .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow radiusCombobox[name=managementRadiusServer1] '
                                           'boundlist => div:textEquals(' + arg_dict['mgmt_server'] + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_radius_mgmt_server_2(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow radiusCombobox[name=managementRadiusServer2] "
                                           "=> .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow radiusCombobox[name=managementRadiusServer2] '
                                           'boundlist => div:textEquals(' + arg_dict['mgmt_server'] + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_network_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow radiusCombobox[name=networkRadiusServer] => "
                                           ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow radiusCombobox[name=networkRadiusServer]'
                                           ' boundlist => div:textEquals(' + arg_dict['network_server'] + ')')

        return ui_cmd_obj

    def engines_dialog_edit_switch_set_policy_domain(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#nwcEditSwitchesWindow combo[name=policyDomain] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow combo[name=policyDomain] boundlist => '
                                           ':textEquals(' + arg_dict['domain_name'] + ')')
        return ui_cmd_obj

    def engines_dialog_edit_switch_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nwcEditSwitchesWindow button[text=Save] => .x-btn-inner-blue-small')
        if arg_dict['device_type'] == "exos" or arg_dict['device_type'] == "ewc" or arg_dict['device_type'] == "xca":
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Enforce Policy Domain]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Enforce Policy Domain':
                self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')
                self.ext_builder.delay(ui_cmd_obj, '10000')
            else:
                ui_cmd_obj.error_state = True
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Success]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Success':
                self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = False
            self.ext_builder.component_query(ui_cmd_obj, 'title[text=Save Successful]', '[0].config.text')
            if ui_cmd_obj.return_data == 'Save Successful':
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
            else:
                ui_cmd_obj.error_state = False
        if arg_dict['device_type'] != "exos" and arg_dict['device_type'] != "ewc" and arg_dict['device_type'] != "xca":
            self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def engines_navigate_to_edit_switch(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel panel[title=Engine Group - ' +
                               arg_dict['engine_group'] + ']#configContentPanel tab[text=Switches] => .x-tab-inner')
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj,
                                                  '#nacConfigTab #nacConfigCenterPanel #configContentPanel '
                                                  '#switchesNwcTab #nacConfigGridWrapper_switches gridview',
                                                  '[0]', 'switchIpCol', arg_dict['switch_ip'])
        self.ext_builder.click(ui_cmd_obj,
                               '#nacConfigTab #nacConfigCenterPanel #configContentPanel #switchesNwcTab '
                               '#nacConfigGridWrapper_switches button[iconCls=edit] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def engines_open_advanced_settings_dialog(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"nacConfigSwitchEditPanel button[text=Advanced Settings\.\.\.] => "
                               r".x-btn-inner-gray-small")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_select_ip_subnet(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combobox[name=ipSubnet] => .x-form-trigger-wrap-default")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=ipSubnet] boundlist => li:textEquals(" + str(arg_dict["ip_subnet"]) + ")")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_enter_shared_security(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["shared_secret"]),
                                    "passwordfield[name=sharedSecret] => .x-form-text")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_select_reauth_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combobox[name=switchReauthConfig] => .x-form-arrow-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=switchReauthConfig] boundlist => li:textEquals(" +
                               str(arg_dict["reauth_type"]) + ")")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_check_enable_port_link_control(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[name=togglePortLink]", "[0].checked")
        if "enable" in str(arg_dict["port_link"]).lower() and not ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, "checkboxfield[name=togglePortLink] => .x-form-cb-input")
        elif "disable" in str(arg_dict["port_link"]).lower() and ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, "checkboxfield[name=togglePortLink] => .x-form-cb-input")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_save_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "window[title=Advanced Switch Settings] button[text=OK] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def engines_advanced_switch_settings_dialog_cancel_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj
