from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqviewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqview(EciqviewBase):
    def view_select_tab(self, ui_cmd_obj, arg_dict):
        tab_dict = {}
        if arg_dict['tab_name'].lower() == 'manage':
            tab_dict['tab_name'] = "monitorTab"
        elif arg_dict['tab_name'].lower() == 'ml insights':
            tab_dict['tab_name'] = "insightsTab"
        elif arg_dict['tab_name'].lower() == 'cloud view':
            tab_dict['tab_name'] = "communityTab"
        else:
            tab_dict['tab_name'] = (arg_dict['tab_name'].lower() + 'Tab')

        self.builder.click(ui_cmd_obj, "//li[@data-dojo-attach-point='" + tab_dict['tab_name'] + "']")

        return ui_cmd_obj

    def view_select_sub_tab(self, ui_cmd_obj, arg_dict):
        tab_dict = {}
        subtab_dict = {}
        if arg_dict['tab_name'].lower() == 'manage':
            tab_dict['tab_name'] = "monitor"
        elif arg_dict['tab_name'].lower() == 'ml insights':
            tab_dict['tab_name'] = "insights"
        else:
            tab_dict['tab_name'] = arg_dict['tab_name'].lower()

        subtab_dict['subtab_name'] = arg_dict['subtab_name'].upper()
        self.builder.click(ui_cmd_obj, "//li[@data-dojo-attach-point='" + tab_dict['tab_name'] + "Tab']")
        if arg_dict['tab_name'].lower() == 'a3':
            self.builder.click(ui_cmd_obj, "//li[contains(@data-dojo-attach-point, '" + tab_dict['tab_name'] +
                               "')]/ul/li/a[.='" + subtab_dict['subtab_name'] + "']")
        else:
            self.builder.click(ui_cmd_obj, "//li[contains(@data-dojo-attach-point, '" + tab_dict['tab_name'] +
                               "')]/a[.='" + subtab_dict['subtab_name'] + "']")

        return ui_cmd_obj
