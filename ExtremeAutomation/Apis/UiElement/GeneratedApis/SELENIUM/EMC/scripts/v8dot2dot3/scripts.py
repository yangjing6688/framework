from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.scripts.v8dot1dot3.scripts import Scripts as \
    ScriptsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Scripts(ScriptsBase):
    def scripts_dialog_run_click_next(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptNext] => .x-btn-inner-blue-small')

        return ui_cmd_obj
