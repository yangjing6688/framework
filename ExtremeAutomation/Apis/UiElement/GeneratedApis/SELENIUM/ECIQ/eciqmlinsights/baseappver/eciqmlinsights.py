from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqmlinsightsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqmlinsights(EciqmlinsightsBase):
    def ml_insights_comparative_analytics_popup_click_done_button(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='dijitDialogTitle' and .='Comparative Analytics']")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
        else:
            self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='closeDialog' and .='DONE']")

        return ui_cmd_obj
