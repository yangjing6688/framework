from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.sites.v8dot1dot1.sites import Sites as SitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Sites(SitesBase):
    def sites_configure_ztp_set_subnet_address(self, ui_cmd_obj, arg_dict):
        # Enter the Subnet Address
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ztpSubnetAddress] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_starting_ip_address(self, ui_cmd_obj, arg_dict):
        # Enter the Starting IP
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ztpStartingIp] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_ending_ip_address(self, ui_cmd_obj, arg_dict):
        # Enter the Ending IP
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ztpEndingIp] => .x-form-text")

        return ui_cmd_obj
