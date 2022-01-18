from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqcommonobjectsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqcommonobjects(EciqcommonobjectsBase):
    def common_objects_expand_section(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@class,'ui-nav-sider-title qa-sider-title-" +
                                  arg_dict['section_name'].lower() +
                                  "')]/following-sibling::*[contains(@style,'display: none;')]")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
        else:
            self.builder.click(ui_cmd_obj, "//*[contains(@class,'ui-nav-sider-title qa-sider-title-" +
                               arg_dict['section_name'].lower() + "')]")

        return ui_cmd_obj

    def common_objects_collapse_section(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@class,'ui-nav-sider-title qa-sider-title-" +
                                  arg_dict['section_name'].lower() +
                                  "')]/following-sibling::*[contains(@style,'display: none;')]")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[contains(@class,'ui-nav-sider-title qa-sider-title-" +
                               arg_dict['section_name'].lower() + "')]")

        return ui_cmd_obj

    def common_objects_select_sub_section(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[contains(@class,'ui-nav-sider-title qa-sider-title-" +
                           arg_dict['section_name'].lower() + "')]/../ul/*[.='" + arg_dict['sub_section_name'] + "']")

        return ui_cmd_obj
