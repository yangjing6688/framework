from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.policymappings.v8dot1dot3.policymappings import \
    Policymappings as PolicymappingsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policymappings(PolicymappingsBase):
    def policy_mappings_dialog_edit_mapping_set_vlan_name(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj,
                           "//label[.='VLAN [ID] Name:']/following-sibling::div//div[contains(@id, 'trigger-')]")
        if arg_dict['vlan_name'] == "None":
            self.builder.click(ui_cmd_obj, "//li[contains(@class, 'x-boundlist-item') and .='None']")
        else:
            self.ext_builder.click(ui_cmd_obj, 'nacVlanCombobox[name=pmVlanName] boundlist => :textEquals(New...)')
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_id'],
                                        '#nacConfigAddVlanWindow numberfield[inputType=text] => .x-form-text')
            self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_name'],
                                        '#nacConfigAddVlanWindow textfield[fieldLabel=Name] => .x-form-text')
            self.ext_builder.click(ui_cmd_obj, '>>#nacConfigAddVlanWindow button[text=OK]')

        return ui_cmd_obj
