from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.options.v8dot2dot3.options import Options as \
    OptionsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Options(OptionsBase):
    def options_site_set_length_of_snmp_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['snmp_timeout'],
                                    'numberfield[name=initialTimeout] => .x-form-text')
        return ui_cmd_obj

    def options_site_set_number_of_snmp_retries(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['snmp_retries'],
                                    'numberfield[name=initialTimeout] => .x-form-text')
        return ui_cmd_obj
