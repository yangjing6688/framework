from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ViewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class View(ViewBase):
    def view_select_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, '//span[contains(@class,"x-btn-inner x-btn-inner-extr-nav-toolbar-button-small")'
                           ' and contains(.,' + arg_dict['tab_name'] + ')]')

        return ui_cmd_obj
