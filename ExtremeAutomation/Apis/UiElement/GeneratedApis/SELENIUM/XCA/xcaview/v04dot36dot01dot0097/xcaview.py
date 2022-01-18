from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcaview.v04dot26dot03dot0007.xcaview import Xcaview \
    as XcaviewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaview(XcaviewBase):
    def open_page_in_left_view_menu(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@uib-tooltip='" + arg_dict['main_section_name'] + "']",
                                                            "aria-expanded", "true")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[@uib-tooltip='" + arg_dict['main_section_name'] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_page_in_left_view_expanded_menu(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@uib-tooltip='" + arg_dict['main_section_name'] + "']",
                                                            "aria-expanded", "true")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[@uib-tooltip='" + arg_dict['main_section_name'] + "']")
        if arg_dict['main_section_name'].lower() == 'configure':
            self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//*[@uib-tooltip='" + arg_dict['page_name'] +
                               "']")
        elif arg_dict['main_section_name'].lower() == 'monitor':
            self.builder.click(ui_cmd_obj, "//*[@id='side-menu-monitor']//*[@uib-tooltip='" + arg_dict['page_name'] +
                               "']")
        elif arg_dict['main_section_name'].lower() == 'onboard':
            self.builder.click(ui_cmd_obj, "//*[@id='side-menu-onboard']//a[contains(text(),'" + arg_dict['page_name'] +
                               "')]")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_page_in_left_view_submenu(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//button[@uib-tooltip='" +
                           arg_dict['sub_section_name'] + "']")
        self.builder.click(ui_cmd_obj,
                           "//div[contains(@class, 'md-clickable')]//a/div[normalize-space(.)='" +
                           arg_dict['page_name'] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_sites_page_in_expanded_menu(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['page_name'] = 'Sites'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_networks_page_in_expanded_menu(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['page_name'] = 'Networks'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_clients_page_in_expanded_menu(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Monitor'
        arg_dict['page_name'] = 'Clients'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_access_point_page_in_devices_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Devices'
        arg_dict['page_name'] = 'Access Points'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_switches_page_in_devices_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Devices'
        arg_dict['page_name'] = 'Switches'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_aaa_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'AAA'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_portal_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Portal'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_groups_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Groups'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_rules_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Rules'
        self.open_page_in_left_view_expanded_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_roles_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Policy'
        arg_dict['page_name'] = 'Roles'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_class_of_service_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Policy'
        arg_dict['page_name'] = 'Class of Service'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_vlans_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Policy'
        arg_dict['page_name'] = 'VLANs'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_vlan_groups_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Policy'
        arg_dict['page_name'] = 'VLAN Groups'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_rates_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['main_section_name'] = 'Configure'
        arg_dict['sub_section_name'] = 'Policy'
        arg_dict['page_name'] = 'Rates'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj
