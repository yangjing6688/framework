from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.discovered.v8dot1dot4.discovered import Discovered as \
    DiscoveredBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Discovered(DiscoveredBase):
    def discovered_edit_device_vlan_definition_update(self, ui_cmd_obj, arg_dict):
        type_string = "[RETURN]"
        self.ext_builder.enter_text(ui_cmd_obj, str(type_string),
                                    "textfield[name=deviceDetailsVlanNameEditor] => .x-form-text", clear_existing=False)
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVlanNameEditor] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVlanNameEditor] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_vid(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVidEditor] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVidEditor] => .x-form-text")
        return ui_cmd_obj
