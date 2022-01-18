from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.view.v8dot1dot1.view import View as ViewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class View(ViewBase):
    def view_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#leftNavToolbar button[text=' + str(arg_dict['tab_name']) + '] => '
                                           '.x-btn-inner-extr-nav-toolbar-button-small')

        return ui_cmd_obj
