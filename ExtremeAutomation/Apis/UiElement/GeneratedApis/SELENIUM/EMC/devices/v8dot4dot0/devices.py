from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot3dot0.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devices(DevicesBase):
    def devices_edit_device_ports_edit_row_port_template(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=deviceDetailsRoleEditor] => .x-form-trigger')
        if arg_dict['port_template'] == 'Use Local Settings':
            self.ext_builder.click(ui_cmd_obj,
                                   "combo[name=deviceDetailsRoleEditor] boundlist => "
                                   ":textEquals( < Use Local Settings > )")
        else:
            self.ext_builder.click(ui_cmd_obj, 'combo[name=deviceDetailsRoleEditor] boundlist => ' +
                                   ':textEquals(' + arg_dict['port_template'] + ')')
            self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def devices_edit_device_enforce_preview(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Enforce Preview...] => .x-btn-inner-default-small')
        self.ext_builder.wait_for_attribute(ui_cmd_obj, "button[text=Enforce]", '[0].ariaEl.dom.attributes[6].value',
                                            "false")
        self.ext_builder.delay(ui_cmd_obj, 2000)
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Enforce] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Enforce] boundlist => :textEquals(Custom)')
        self.ext_builder.delay(ui_cmd_obj, 2000)

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceSystem]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_system"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceSystem] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce System check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceVlan]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_vlan"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceVlan] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce VLAN check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceVrf]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_vrf"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceVrf] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce Vrf check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceConsolidatedPort]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_port"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceConsolidatedPort] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce Port check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceIpClip]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_clip_address"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceIpClip] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce IpClip check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceTopologies]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_topologies"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceTopologies] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce topologies check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceServices]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_services"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceServices] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce Services check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceLAG]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_lag"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceLAG] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce LAG check button already at desired state.\n")

        self.ext_builder.click(ui_cmd_obj,
                               "button[text=Enforce] => .x-btn-inner-blue-small")
        self.ext_builder.click(ui_cmd_obj,
                               "button[itemId=yes] => .x-btn-inner-blue-small")
        self.ext_builder.delay(ui_cmd_obj, 5000)
        self.ext_builder.click(ui_cmd_obj,
                               "compareDeviceDataWindow[name=compareDeviceDataWindow] button[text=Cancel] => "
                               ".x-btn-inner-default-small")
        return ui_cmd_obj
