from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.configurations.v8dot3dot0.configurations import \
    Configurations as ConfigurationsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Configurations(ConfigurationsBase):
    def configs_rules_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='x-btn-inner x-btn-inner-default-toolbar-small' and .='View...']")
        self.builder.click(ui_cmd_obj, "//a/span[@class='x-menu-item-text x-menu-item-text-default "
                                       "x-menu-item-indent' and .='Refresh']")

        return ui_cmd_obj

    def configs_rules_dialog_add_rule(self, ui_cmd_obj, arg_dict):
        self.configs_rules_click_add_rule_button(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict["rule_name"], "//*[@name='name']")
        if arg_dict["authentication_method"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'combo[name=authenticationMethod] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=authenticationMethod] boundlist => :textEquals(' +
                                   arg_dict['authentication_method'] + ')')
        if arg_dict["user_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=userGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=userGroup] boundlist => div:textEquals(' +
                                   arg_dict['user_group'] + ')')
        if arg_dict["endsystem_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=endSystemGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=endSystemGroup] boundlist => div:textEquals(' +
                                   arg_dict['endsystem_group'] + ')')
        if arg_dict["device_type_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=deviceTypeGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=deviceTypeGroup] boundlist => '
                                   'div:textEquals(' + arg_dict['device_type_group'] + ')')
        if arg_dict["location_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=locationGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=locationGroup] boundlist => div:textEquals(' +
                                   arg_dict['location_group'] + ')')
        if arg_dict["time_group"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=timeGroup] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'dgeCombo[name=timeGroup] boundlist => div:textEquals(' +
                                   arg_dict['time_group'] + ')')
        if arg_dict["nac_profile"] is not None:
            self.ext_builder.click(ui_cmd_obj, 'nacProfileCombobox[name=profile] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'nacProfileCombobox[name=profile] boundlist => div:textEquals(' +
                                   arg_dict['nac_profile'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj
