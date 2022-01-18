from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot1dot1.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devices(DevicesBase):
    def devices_open_device_view(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[title=Devices] tableview => .x-grid-cell:textEquals(' +
                               str(arg_dict['ip_address']) + ')')
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel deviceGrid[title=Devices] '
                                                          'tableview', '[0]', 'ip', str(arg_dict['ip_address']))
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            # query is 0-based, table is 1-based, so adjust the selection index accordingly
            row_index = ui_cmd_obj.return_data + 1
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid gridview => .x-grid-item:nth-of-type(' +
                                   str(row_index) + ') .summaryButton .x-grid-cell-inner')
        else:
            self.logger.log_info("\nCould not find '" + str(arg_dict['ip_address']) + "' in table.\n")

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
                                     'grid[name=deviceDetailPortsGrid] menu  '
                                     '#columnItem menucheckitem[text=Enabled] => .x-menu-item-text')

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
                                                         'menu #columnItem',
                                                         '[0].menu.items.items[' + str(menu_index) + '].checked')

                        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['show_col']):
                            self.ext_builder.click(ui_cmd_obj,
                                                   'editDeviceDataWindow grid[name=deviceDetailPortsGrid] '
                                                   'menu #columnItem menucheckitem[text=' + col_name + '] => '
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

        # Click the title of the dialog to close the column menu
        self.ext_builder.click(ui_cmd_obj,
                               'editDeviceDataWindow[name=editDeviceDataWindow] title[text=Configure Device] =>'
                               '.x-title-text')

        return ui_cmd_obj

    def devices_edit_device_vendor_profile_device_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel textfield[itemId=pluginEditorEnterpriseEditorAddPanelDisplayName] "
                               "=> .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel "
                                    "textfield[itemId=pluginEditorEnterpriseEditorAddPanelDisplayName] => .x-form-text")

        return ui_cmd_obj

    def devices_edit_device_vendor_profile_family(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelFamilyName] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelFamilyName] "
                               "boundlist => :textEquals(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def devices_edit_device_vendor_profile_sub_family(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelSubFamily] => "
                               ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelSubFamily] "
                               "boundlist => :textEquals(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def devices_confirm_device_vendor_profile_device_type(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(
            ui_cmd_obj, "deviceDetailsPanel textfield[itemId=pluginEditorEnterpriseEditorAddPanelDisplayName]",
            "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Vendor Profile Device Type value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Vendor Profile Device Type value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_vendor_profile_vendor(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(
            ui_cmd_obj,
            "deviceDetailsPanel textfield[itemId=pluginEditorEnterpriseEditorAddPanelVendor]", "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Vendor Profile Device Type value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Vendor Profile Device Type value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_vendor_profile_company(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(
            ui_cmd_obj,
            "deviceDetailsPanel textfield[itemId=pluginEditorEnterpriseEditorAddPanelCompanyName]", "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Vendor Profile Company value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Vendor Profile Company value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_vendor_profile_family(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(
            ui_cmd_obj,
            "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelFamilyName]", "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Vendor Profile Family value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Vendor Profile Family value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_vendor_profile_sub_family(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(
            ui_cmd_obj,
            "deviceDetailsPanel combo[itemId=pluginEditorEnterpriseEditorAddPanelSubFamily]", "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Vendor Profile Sub Family value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Vendor Profile Sub Family value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj
