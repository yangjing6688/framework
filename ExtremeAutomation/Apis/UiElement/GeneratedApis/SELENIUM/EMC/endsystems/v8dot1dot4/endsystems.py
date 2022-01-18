from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.endsystems.v8dot1dot3.endsystems import Endsystems as \
    EndsystemsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Endsystems(EndsystemsBase):
    def endsystems_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab #refresh => .x-btn-icon-el")

        return ui_cmd_obj
