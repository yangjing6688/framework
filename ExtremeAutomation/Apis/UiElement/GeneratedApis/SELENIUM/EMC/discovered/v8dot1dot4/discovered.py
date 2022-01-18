from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.discovered.v8dot1dot3.discovered import Discovered as \
    DiscoveredBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Discovered(DiscoveredBase):
    def discovered_select_device_in_table(self, ui_cmd_obj, arg_dict):
        # Look for the specified device
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           '#networkTabPanel #networkDiscoveredTab '
                                                           '#DiscoveredDevicesGrid', '[0]', 'ipAddress',
                                                           arg_dict['device_ip'])
        if ui_cmd_obj.return_data is True:
            # The ipAddress was found
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview => '
                                   '.x-grid-cell-inner:textEquals(' + arg_dict['device_ip'] + ')')
        else:
            # If the device wasn't found by the ipAddress attribute, check the connectedIpAddress attribute
            ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                               '#networkTabPanel #networkDiscoveredTab '
                                                               '#DiscoveredDevicesGrid', '[0]', 'connectedIpAddress',
                                                               arg_dict['device_ip'])
            if ui_cmd_obj.return_data is True:
                self.ext_builder.click(ui_cmd_obj,
                                       '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview => '
                                       '.x-grid-cell-inner:textEquals(' + arg_dict['device_ip'] + ')')
            else:
                self.logger.log_info("\nCould not find a device with IP '" + arg_dict['device_ip'] + "'\n")

        return ui_cmd_obj
