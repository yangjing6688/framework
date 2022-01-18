from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.endsystems.v8dot1dot4.endsystems import Endsystems as \
    EndsystemsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Endsystems(EndsystemsBase):
    def endsystems_click_force_reauthentication_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab button[text=Force Reauthentication] => "
                                           ".x-btn-inner-default-toolbar-small")
        self.ext_builder.click(ui_cmd_obj, "#ok => .x-btn-inner-blue-small")

        return ui_cmd_obj
