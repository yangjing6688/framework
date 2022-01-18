from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.accesscontrol.v8dot1dot3.accesscontrol import \
    Accesscontrol as AccesscontrolBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Accesscontrol(AccesscontrolBase):
    def access_control_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab nacConfigNavPanel[title=Configuration] button[text=Refresh] '
                                           '=> .x-btn-inner-default-small', wait_for_load_mask=False)
        self.ext_builder.delay(ui_cmd_obj, '1000', wait_for_load_mask=False)

        return ui_cmd_obj
