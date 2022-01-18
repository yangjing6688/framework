from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcadevicegroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcadevicegroups(XcadevicegroupsBase):
    def click_add_to_create_new_group(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='ctrl.onCreate()']")

        return ui_cmd_obj

    def select_device_group(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@role='row']/div[.='" + str(arg_dict["device_group_name"]) + "']")

        return ui_cmd_obj

    def select_device_group_edit_config(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@role='row']/div[.='" + str(arg_dict["device_group_name"]) + "']")

        return ui_cmd_obj

    def click_device_group_edit_profile_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@ng-click='ctrl.editProfile(ctrl.deviceGroup.profileId)']")

        return ui_cmd_obj

    def config_device_group_name_and_country(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).config_device_group_name_and_country(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_device_group_networks(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/span[.='Networks']")
        for radio_port in str(arg_dict["radio_ports"]).split(","):
            self.builder.click(ui_cmd_obj, "//label[@class='form-control-static ng-scope']/span[contains(text(),'" +
                               str(arg_dict["network_name"]) + "')]/../../following-sibling::td/div/md-checkbox[@id='" +
                               str(radio_port) + "']")

        return ui_cmd_obj

    def config_device_group_devices(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).config_device_group_devices(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_device_group_roles(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/span[.='Roles']")
        roles = str(arg_dict["roles"]).split(",")
        for role in roles:
            self.builder.click(ui_cmd_obj, "//label[@class='form-control-static']/a[.='" + str(role).strip() +
                               "']/../../following-sibling::td/md-checkbox")

        return ui_cmd_obj

    def config_device_group_advanced_settings(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).config_device_group_advanced_settings(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_config_and_back_to_groups_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='ctrl.addEditProfile()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='ctrl.closeDgModal()']")

        return ui_cmd_obj

    def delete_existing_device_group(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).delete_existing_device_group(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def clone_device_group(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).clone_device_group(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def verify_device_group_exists(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcadevicegroups, self).verify_device_group_exists(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
