from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcleftnavipanelBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcleftnavipanel(EwcleftnavipanelBase):
    def left_navi_panel_select_section_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') "
                                       "and .='" + arg_dict['section_name'] + "']")
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj

    def left_navi_panel_select_link_in_section(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['link_name'] + "']")
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj

    def left_navi_panel_expand_tree_node_in_section(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//li[contains(@class, 'expandable')]/a[contains(@class, 'cnSiteLink') and .='" +
                           arg_dict['link_name'] + "']/../div[1]")
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj

    def left_navi_panel_collapse_tree_node_in_section(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//li[contains(@class, 'collapsable')]/a[contains(@class, 'cnSiteLink') "
                                       "and .='" + arg_dict['link_name'] + "']/../div[1]")
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj
