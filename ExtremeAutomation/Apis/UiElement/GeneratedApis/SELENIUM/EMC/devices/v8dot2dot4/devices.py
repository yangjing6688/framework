from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot2dot1.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devices(DevicesBase):
    def devices_edit_device_ports_select_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                                     '.x-column-header-text')
        self.ext_builder.double_click(ui_cmd_obj, "grid[name=deviceDetailPortsGrid] gridview => "
                                                  ":nth-of-type(2) .x-grid-cell-inner:textEquals(" +
                                      str(arg_dict['port_name']) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_alias(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=portAlias] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=portAlias] => .x-form-text")
        return ui_cmd_obj

    def devices_confirm_device_port_alias(self, ui_cmd_obj, arg_dict):
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'deviceDetailPortsPanel[name=deviceDetailPortsPanel] '
                                                     'gridview{isVisible()}', "deviceDetailsPortNumber",
                                                     str(arg_dict["port_id"]))
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Confirmed Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
        else:
            port_alias = str(
                self.devices_get_table(ui_cmd_obj,
                                       'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                                       row_index, "portAlias"))

            if port_alias == str(arg_dict["port_alias"]):
                self.logger.log_info("Confirmed Port Alias: " + arg_dict['port_alias'] +
                                     " matches the Port Alias value: " + port_alias +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed Port Alias: " + arg_dict['port_alias'] +
                                     " does not match Port Alias: " + port_alias +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_edit_device_ports_show_columns(self, ui_cmd_obj, arg_dict):
        # Open the column menu
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                                     '.x-column-header-text')
        self.ext_builder.click(ui_cmd_obj,
                               'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                               '.x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem => '
                               '.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'grid[name=deviceDetailPortsGrid] menu  #columnItem menucheckitem[text=PVID] '
                                     '=> .x-menu-item-text')

        # Make sure the menu exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'editDeviceDataWindow grid[name=deviceDetailPortsGrid] '
                                                      'menu #columnItem', '[0].menu')

        if ui_cmd_obj.return_data is not None:
            # Make sure the menu contains items
            self.ext_builder.component_query(ui_cmd_obj,
                                             'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem',
                                             '[0].menu.items.length')
            menu_count = int(ui_cmd_obj.return_data)
            self.logger.log_info("\nMenu contains '" + str(menu_count) + "' items.\n")
            if menu_count != 0:
                # Loop through each of the column names in the comma-separated list and toggle each column
                # checkbox appropriately
                columns = arg_dict['col_list'].split(',')
                for col_name in columns:
                    self.logger.log_debug("\nAsking for index of '" + col_name + "'\n")
                    self.ext_builder.get_menu_index(ui_cmd_obj, 'editDeviceDataWindow grid[name=deviceDetailPortsGrid] '
                                                    'menu #columnItem', '[0]', col_name)
                    menu_index = ui_cmd_obj.return_data
                    self.logger.log_debug("\n   Found menu '" + col_name + "' at index '" + str(menu_index) + "'\n")
                    if menu_index != -1:
                        self.ext_builder.component_query(ui_cmd_obj,
                                                         'editDeviceDataWindow grid[name=deviceDetailPortsGrid] '
                                                         'menu #columnItem', '[0].menu.items.items[' +
                                                         str(menu_index) + '].checked')

                        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['show_col']):
                            self.ext_builder.click(ui_cmd_obj,
                                                   'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu '
                                                   '#columnItem menucheckitem[text=' + col_name + '] => '
                                                   '.x-menu-item-icon')
                        else:
                            self.logger.log_info("\nMenu '" + col_name + "' is already at desired selection state (" +
                                                 arg_dict['show_col'] + ").\n")
                    else:
                        self.logger.log_info("\nCould not find column menu '" + col_name + "'\n")
                        ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nColumn menu is empty.\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find column menu.\n")
            ui_cmd_obj.error_state = True

        # Type escape twice to close the column dropdown
        self.ext_builder.enter_text_no_target(ui_cmd_obj, '[ESCAPE]')
        self.ext_builder.enter_text_no_target(ui_cmd_obj, '[ESCAPE]')

        return ui_cmd_obj

    def devices_confirm_device_port_enabled(self, ui_cmd_obj, arg_dict):
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'deviceDetailPortsPanel[name=deviceDetailPortsPanel] '
                                                     'gridview{isVisible()}', "deviceDetailsPortNumber",
                                                     str(arg_dict["port_id"]))
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Confirmed Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
        else:
            column_value = str(
                self.devices_get_table(ui_cmd_obj,
                                       'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                                       row_index, "portEnabled"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Enabled: " + arg_dict['the_value'] + " matches the Enabled value: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed Enabled: " + arg_dict['the_value'] + " does not match Enabled: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_enabled(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "checkbox[name=portEnabled]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=portEnabled] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj
