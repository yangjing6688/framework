from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcasites.v04dot26dot03dot0007.xcasites import \
    Xcasites as XcasitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcasites(XcasitesBase):
    def open_site_device_groups_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item/strong[.='DEVICE GROUPS']")

        return ui_cmd_obj

    def select_site_and_config(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['site_name']) + "']")

        return ui_cmd_obj
