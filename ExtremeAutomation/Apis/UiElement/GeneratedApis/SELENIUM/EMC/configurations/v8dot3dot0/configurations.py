from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.configurations.v8dot1dot3.configurations import \
    Configurations as ConfigurationsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Configurations(ConfigurationsBase):
    def configs_rules_click_add_rule_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=Rules]#configContentPanel button[text=Add...] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def configs_rules_click_delete_rule_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=Rules]#configContentPanel button[text=Delete] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def configs_rules_click_edit_rule_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=Rules]#configContentPanel button[text=Edit...] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def configs_rules_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=Rules]#configContentPanel button[text=Refresh] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def configs_rules_select_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'ruleEngineGrid gridview => .x-grid-cell-inner:textEquals(' +
                               arg_dict['rule_name'] + ')')

        return ui_cmd_obj

    def configs_rules_dialog_add_rule(self, ui_cmd_obj, arg_dict):
        self.configs_rules_click_add_rule_button(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict["rule_name"], "//*[@name='name']")
        if arg_dict["authentication_method"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'combo[name=authenticationMethod] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=authenticationMethod] boundlist => :textEquals(' +
                                   arg_dict['authentication_method'] + ')')
        if arg_dict["user_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=userGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=userGroup] boundlist => div:textEquals(' +
                                   arg_dict['user_group'] + ')')
        if arg_dict["endsystem_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=endSystemGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=endSystemGroup] boundlist => div:textEquals(' +
                                   arg_dict['endsystem_group'] + ')')
        if arg_dict["device_type_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=deviceTypeGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=deviceTypeGroup] boundlist => '
                                   'div:textEquals(' + arg_dict['device_type_group'] + ')')
        if arg_dict["location_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=locationGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=locationGroup] boundlist => div:textEquals(' +
                                   arg_dict['location_group'] + ')')
        if arg_dict["time_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=timeGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'groupEditorCombobox[name=timeGroup] boundlist => div:textEquals(' +
                                   arg_dict['time_group'] + ')')
        if arg_dict["nac_profile"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'nacProfileCombobox[name=profile] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'nacProfileCombobox[name=profile] boundlist => div:textEquals(' +
                                   arg_dict['nac_profile'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def configs_rules_dialog_delete_rule(self, ui_cmd_obj, arg_dict):
        self.configs_rules_select_rule(ui_cmd_obj, arg_dict)
        self.configs_rules_click_delete_rule_button(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//*[@class='x-btn-inner x-btn-inner-blue-small' and .='Yes']")

        return ui_cmd_obj

    def configs_rules_dialog_enable_rule(self, ui_cmd_obj, arg_dict):
        self.configs_rules_select_rule(ui_cmd_obj, arg_dict)
        self.configs_rules_click_edit_rule_button(ui_cmd_obj, arg_dict)
        self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=ruleEnabled]", "[0].checked")
        if "true" in str(arg_dict["rule_enabled"]).lower() and not bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=ruleEnabled] => .x-form-cb-input")
        elif "false" in str(arg_dict["rule_enabled"]).lower() and bool(ui_cmd_obj.return_data):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=ruleEnabled] => .x-form-cb-input")
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj
