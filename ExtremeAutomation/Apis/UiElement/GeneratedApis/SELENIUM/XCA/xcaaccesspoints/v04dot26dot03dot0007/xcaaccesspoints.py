from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcaaccesspointsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaaccesspoints(XcaaccesspointsBase):
    def verify_access_point_is_associated_with_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj,
                           "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['access_point_name']) + "']")
        self.builder.click(ui_cmd_obj, "//md-tab-item/strong[.='SITES']")
        self.builder.find_element(ui_cmd_obj,
                                  "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                                  str(arg_dict['site_name']) + "']")
        if ui_cmd_obj.error_state:
            self.logger.log_debug("AP isn't associated with site " + str(arg_dict["site_name"]) + ".")
        else:
            self.logger.log_debug("AP is associated with site " + str(arg_dict["site_name"]) + ".")

        return ui_cmd_obj
