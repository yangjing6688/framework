from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcaviewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaview(XcaviewBase):
    def open_page_in_left_view_menu(self, ui_cmd_obj, arg_dict):
        page_name = str(arg_dict['page_name']).lower().capitalize()
        self.builder.click(ui_cmd_obj, "//*[contains(@uib-tooltip, '" + page_name + "')]")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_page_in_left_view_submenu(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[contains(@uib-tooltip, '" + arg_dict['section_name'] + "')]")
        self.builder.click(ui_cmd_obj,
                           "//div[contains(@class, 'md-clickable')]//span[normalize-space(.)='" +
                           arg_dict['page_name'] + "']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_overview_page(self, ui_cmd_obj, arg_dict):
        arg_dict['page_name'] = 'Overview'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_sites_page(self, ui_cmd_obj, arg_dict):
        arg_dict['page_name'] = 'Sites'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_networks_page(self, ui_cmd_obj, arg_dict):
        arg_dict['page_name'] = 'Networks'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_clients_page(self, ui_cmd_obj, arg_dict):
        arg_dict['page_name'] = 'Clients'
        self.open_page_in_left_view_menu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_adoption_page_in_devices_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Devices'
        arg_dict['page_name'] = 'Adoption'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_access_point_page_in_devices_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Devices'
        arg_dict['page_name'] = 'Access Points'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_switches_page_in_devices_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Devices'
        arg_dict['page_name'] = 'Switches'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_aaa_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'AAA'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_portal_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Portal'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_groups_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Groups'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_rules_page_in_onboard_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'OnBoard'
        arg_dict['page_name'] = 'Rules'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_roles_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Policy'
        arg_dict['page_name'] = 'Roles'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_class_of_service_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Policy'
        arg_dict['page_name'] = 'Class of Service'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_vlans_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Policy'
        arg_dict['page_name'] = 'VLANs'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_rates_page_in_policy_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Policy'
        arg_dict['page_name'] = 'Rates'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_system_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'System'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_utilities_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'Utilities'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_license_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'License'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_logs_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'Logs'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_accounts_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'Accounts'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def open_applications_page_in_admin_section(self, ui_cmd_obj, arg_dict):
        arg_dict['section_name'] = 'Admin'
        arg_dict['page_name'] = 'Applications'
        self.open_page_in_left_view_submenu(ui_cmd_obj, arg_dict)

        return ui_cmd_obj
