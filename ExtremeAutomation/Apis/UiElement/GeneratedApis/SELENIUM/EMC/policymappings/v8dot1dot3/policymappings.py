from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as PolicymappingsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policymappings(PolicymappingsBase):
    def policy_mappings_dialog_add_policy_mapping(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'#nacConfigTab #nacConfigCenterPanel '
                                           r'panel[title=Default]#configContentPanel button[text=Add\.\.\.] => '
                                           r'.x-btn-inner-default-toolbar-small')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['mapping_name'], 'textfield[name=pmName] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, 'nacPolicyRoleCombobox[name=pmPolicyRole] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'nacPolicyRoleCombobox[name=pmPolicyRole] boundlist => '
                                           'div:textEquals(' + arg_dict['policy_role'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmAccess] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmAccess] boundlist => '
                                           ':textEquals(' + arg_dict['mgmt_access'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'nacConfigPolicyMappingWindow[title=Create Policy Mapping] '
                                           'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_mappings_dialog_delete_policy_mapping(self, ui_cmd_obj, arg_dict):
        self.policy_mappings_select_mapping(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nacConfigCenterPanel '
                                           'panel[title=Default]#configContentPanel button[text=Delete] => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_mappings_navigate_to_edit_policy_mapping(self, ui_cmd_obj, arg_dict):
        self.policy_mappings_select_mapping(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, r'#nacConfigTab #nacConfigCenterPanel '
                                           r'panel[title=Default]#configContentPanel button[text=Edit\.\.\.] => '
                                           r'.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def policy_mappings_click_switch_to_basic(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#nacConfigTab #nacConfigCenterPanel '
                                         'panel[title=Default]#configContentPanel button', '[3].text')
        if ui_cmd_obj.return_data == "Switch to Basic":
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel panel[title=Default]#configContentPanel '
                                   'button[text=Switch to Basic] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def policy_mappings_click_switch_to_advanced(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#nacConfigTab #nacConfigCenterPanel '
                                         'panel[title=Default]#configContentPanel button', '[3].text')
        if ui_cmd_obj.return_data == "Switch to Advanced":
            self.ext_builder.click(ui_cmd_obj,
                                   '#nacConfigTab #nacConfigCenterPanel panel[title=Default]#configContentPanel '
                                   'button[text=Switch to Advanced] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_custom_fields(self, ui_cmd_obj, arg_dict):
        if arg_dict['custom1'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['custom1'], 'textfield[name=pmCustom1] => .x-form-text')
        if arg_dict['custom2'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['custom2'], 'textfield[name=pmCustom2] => .x-form-text')
        if arg_dict['custom3'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['custom3'], 'textfield[name=pmCustom3] => .x-form-text')
        if arg_dict['custom4'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['custom4'], 'textfield[name=pmCustom4] => .x-form-text')
        if arg_dict['custom5'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['custom5'], 'textfield[name=pmCustom5] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_filter(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['filter'], 'textfield[name=pmFilter] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_location(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=pmLocation] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=pmLocation] boundlist => '
                                           'div:textEquals(' + arg_dict['location'] + ')')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_login_lat_group_and_port(self, ui_cmd_obj, arg_dict):
        if arg_dict['lat_group'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['lat_group'],
                                        'textfield[name=pmLoginLatGroup] => .x-form-text')
        if arg_dict['lat_port'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['lat_port'],
                                        'textfield[name=pmLoginLatPort] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_management_access(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmAccess] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmAccess] boundlist => '
                                           ':textEquals(' + arg_dict['mgmt_access'] + ')')
        if arg_dict['mgmt_access'] == "User Defined":
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['management'],
                                        'textfield[name=pmManagement] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['mgmt_service_type'],
                                        'textfield[name=pmMgmtServiceType] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['cli_access'],
                                        'textfield[name=pmCliAccess] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['mapping_name'], 'textfield[name=pmName] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_policy_role(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'nacPolicyRoleCombobox[name=pmPolicyRole] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'nacPolicyRoleCombobox[name=pmPolicyRole] boundlist => '
                                           'div:textEquals(' + arg_dict['policy_role'] + ')')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_port_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['port_profile'],
                                    'textfield[name=pmPortProfile] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_radius_attribute_lists(self, ui_cmd_obj, arg_dict):
        if arg_dict['org1'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['org1'],
                                        'textarea[name=pmOrg1RadiusAttrsList] => .x-form-text')
        if arg_dict['org2'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['org2'],
                                        'textarea[name=pmOrg2RadiusAttrsList] => .x-form-text')
        if arg_dict['org3'] is not None:
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['org3'],
                                        'textarea[name=pmOrg3RadiusAttrsList] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_virtual_router(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['virtual_router'],
                                    'textfield[name=pmVirtualRouter] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_vlan_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmVlanName] => .x-form-trigger')
        self.ext_builder.component_query(ui_cmd_obj, 'combo[name=pmVlanName]', '[0].config.store.data.items.length')
        end_index = ui_cmd_obj.return_data
        self.logger.log_debug("End index is " + str(end_index))
        if not end_index:
            ui_cmd_obj.error_state = True
            return ui_cmd_obj
        index = 0
        vlan_id_name = "[" + arg_dict['vlan_id'] + "] " + arg_dict['vlan_name']
        if arg_dict['vlan_name'] == "None":
            vlan_id_name = arg_dict['vlan_name']
        while index < end_index:
            self.ext_builder.component_query(ui_cmd_obj, 'combo[name=pmVlanName] ',
                                             '[0].config.store.data.items[' + str(index) + '].data.name')
            if vlan_id_name in ui_cmd_obj.return_data:
                index += 1
                self.ext_builder.click(ui_cmd_obj, 'combo[name=pmVlanName] boundlist => '
                                                   '.x-boundlist-item:contains(' + arg_dict['vlan_name'] + ')')
                return ui_cmd_obj
            elif ui_cmd_obj.return_data != u'':
                index += 1
        self.ext_builder.click(ui_cmd_obj, r'combo[name=pmVlanName] boundlist => :textEquals(New\.\.\.)')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_id'],
                                    '#nacConfigAddVlanWindow numberfield[inputType=text] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_name'],
                                    '#nacConfigAddVlanWindow textfield[fieldLabel=Name] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '>>#nacConfigAddVlanWindow button[text=OK]')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_set_vlan_egress(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmVlanEgress] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=pmVlanEgress] boundlist => '
                                           ':textEquals(' + arg_dict['vlan_egress'] + ')')
        if arg_dict['vlan_egress'] == "User Defined":
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_egress_field'],
                                        'textfield[name=pmVlanEgressField] => .x-form-text')

        return ui_cmd_obj

    def policy_mappings_dialog_edit_mapping_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'nacConfigPolicyMappingWindow[title=Edit Policy Mapping] '
                                           'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_mappings_select_mapping(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_table_row_by_attr(ui_cmd_obj,
                                                  '#nacConfigTab #nacConfigCenterPanel '
                                                  'panel[title=Default]#configContentPanel gridview', '[0]',
                                                  'nameCol', arg_dict['mapping_name'])

        return ui_cmd_obj
