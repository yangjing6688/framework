from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcadevicegroups.v04dot26dot03dot0007.xcadevicegroups \
    import Xcadevicegroups as XcadevicegroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcadevicegroups(XcadevicegroupsBase):
    def click_device_group_edit_profile_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@ng-click='ctrl.editProfile(ctrl.deviceGroup.profileId , ctrl.site)']")

        return ui_cmd_obj

    def config_device_group_networks(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab' and .='Networks']")
        for radio_port in str(arg_dict["radio_ports"]).split(","):
            self.builder.click(ui_cmd_obj, "//label[@class='form-control-static ng-scope']/span[contains(text(),'" +
                               str(arg_dict["network_name"]) + "')]/../../following-sibling::td/div/md-checkbox[@id='" +
                               str(radio_port) + "']")

        return ui_cmd_obj

    def config_device_group_roles(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab' and .='Roles']")
        roles = str(arg_dict["roles"]).split(",")
        for role in roles:
            self.builder.click(ui_cmd_obj, "//label[@class='form-control-static']/a[.='" + str(role).strip() +
                               "']/../../following-sibling::td/md-checkbox")

        return ui_cmd_obj
