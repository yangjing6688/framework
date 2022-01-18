from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot1dot4.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Devices(DevicesBase):
    def devices_edit_device_vlan_definition_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVlanNameEditor] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVlanNameEditor] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_set_vid(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVidEditor] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVidEditor] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_ports_select_row(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[title=Configure Device] "
                               "deviceDetailPortsPanel[name=deviceDetailPortsPanel] tableview => "
                               ".x-grid-cell-inner:contains(" + str(arg_dict['port_name']) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_select_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[title=Configure Device] "
                               "deviceDetailPortsPanel[name=deviceDetailPortsPanel] tableview => "
                               ".x-grid-cell-inner:contains(" + str(arg_dict['port_name']) + ")")
        return ui_cmd_obj
