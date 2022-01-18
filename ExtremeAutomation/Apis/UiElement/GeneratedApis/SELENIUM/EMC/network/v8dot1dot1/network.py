from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as NetworkBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Network(NetworkBase):
    def network_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel tab[text=' + str(arg_dict['tab_name']) +
                               '] => .x-tab-inner-extr-main-tab-panel')

        return ui_cmd_obj
