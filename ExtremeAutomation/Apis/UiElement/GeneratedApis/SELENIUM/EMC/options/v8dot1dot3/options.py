from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.options.v8dot1dot1.options import Options as \
    OptionsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Options(OptionsBase):
    def options_set_site_show_vlan_untagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'checkbox[name=showVlanUntagged]', '[0].value')
        if not ui_cmd_obj.return_data and StringUtils.string_to_boolean(arg_dict['option_value']):
            self.ext_builder.click(ui_cmd_obj, 'checkbox[name=showVlanUntagged] => .x-form-cb-input')
        elif ui_cmd_obj.return_data and not StringUtils.string_to_boolean(arg_dict['option_value']):
            self.ext_builder.click(ui_cmd_obj, 'checkbox[name=showVlanUntagged] => .x-form-cb-input')
        return ui_cmd_obj
