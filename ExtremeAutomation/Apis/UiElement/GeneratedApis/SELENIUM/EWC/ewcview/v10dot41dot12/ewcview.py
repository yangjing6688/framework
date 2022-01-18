from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcviewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcview(EwcviewBase):
    def view_select_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@title='" + arg_dict['tab_name'] + "']")
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj
