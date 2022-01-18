from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcasitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcasites(XcasitesBase):
    def select_site_and_config(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[.='" + str(arg_dict['site_name']) + "']")
        self.builder.click(ui_cmd_obj, "//button[.='CONFIGURE SITE']")

        return ui_cmd_obj

    def open_site_device_groups_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[.='DEVICE GROUPS']")

        return ui_cmd_obj

    def click_site_open_detail_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).click_site_open_detail_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def open_site_floor_plans_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).open_site_floor_plans_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def open_site_location_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).open_site_location_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def open_site_switches_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).open_site_switches_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def open_site_snmp_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).open_site_snmp_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def click_name_to_open_device_group_edit_window(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).click_name_to_open_device_group_edit_window(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def close_device_group_edit_window(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).close_device_group_edit_window(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def open_device_group_profile_edit_window(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).open_device_group_profile_edit_window(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_radios_for_device_group_profile(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).config_radios_for_device_group_profile(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def select_roles_for_device_group_profile(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).select_roles_for_device_group_profile(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def deselect_roles_for_device_group_profile(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).deselect_roles_for_device_group_profile(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_device_group_profile_config(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).save_device_group_profile_config(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_site_config_and_back_to_site_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcasites, self).save_site_config_and_back_to_site_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
