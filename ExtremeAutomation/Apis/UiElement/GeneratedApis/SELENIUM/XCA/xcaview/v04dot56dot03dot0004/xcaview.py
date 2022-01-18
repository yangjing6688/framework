from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcaview.v04dot36dot01dot0097.xcaview import Xcaview \
    as XcaviewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaview(XcaviewBase):
    def open_wlans_page_in_networks_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Networks'
        arg_dict['page_name'] = 'WLANs'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//button[@uib-tooltip='" +
                           arg_dict['sub_section_name'] + "']")
        self.builder.click(ui_cmd_obj,
                           "//*[@href='#/networks/configure' and @uib-tooltip='" + arg_dict['page_name'] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_meshpoints_page_in_networks_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Networks'
        arg_dict['page_name'] = 'Meshpoints'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//button[@uib-tooltip='" +
                           arg_dict['sub_section_name'] + "']")
        self.builder.click(ui_cmd_obj,
                           "//*[@href='#/meshpoints/configure' and @uib-tooltip='" + arg_dict['page_name'] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj
