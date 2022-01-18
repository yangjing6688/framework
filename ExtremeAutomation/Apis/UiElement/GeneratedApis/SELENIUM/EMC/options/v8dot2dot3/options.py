from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.options.v8dot1dot3.options import Options as \
    OptionsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Options(OptionsBase):
    def options_set_trap_engine_delay_start(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['delay_time']),
                                    'numberfield[name=TrapEngineDelayStart] => .x-form-text')
        return ui_cmd_obj

    def options_set_syslog_engine_delay_start(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['delay_time']),
                                    'numberfield[name=SyslogEngineDelayStart] => .x-form-text')
        return ui_cmd_obj
