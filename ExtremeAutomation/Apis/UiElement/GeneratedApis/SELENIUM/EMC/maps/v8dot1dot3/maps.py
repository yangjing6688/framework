from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.maps.v8dot1dot1.maps import Maps as MapsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Maps(MapsBase):
    def maps_create_map(self, ui_cmd_obj, arg_dict):
        # Access the menu to create the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Create Map...] => .x-menu-item-text')

        # Populate the dialog and click OK
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['map_name'],
                                    '#mapCreationRenameWindow #mapName => .x-form-text')

        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#mapCreationRenameWindow #mapCreateOkButton', '[0].disabled')

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "#mapCreationRenameWindow #mapName",
                                                          "[0].lastActiveError")
            if "already exists" in ui_cmd_obj.return_data:
                # PASS
                self.logger.log_info("\nA map with name '" + str(arg_dict['map_name']) + "' already exists.\n")
                ui_cmd_obj.error_state = False
            else:
                # FAIL
                self.logger.log_info("\nCould not create map: '" + ui_cmd_obj.return_data + "'.\n")
                ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj, '#mapCreationRenameWindow button[text=Cancel] => '
                                               '.x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj, '#mapCreationRenameWindow #mapCreateOkButton => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def maps_wait_for_map_add(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj,
                                                '#networkTabPanel #networkDevicesTab treeview',
                                                '[0]', 'name', arg_dict['map_name'], None, 60)
        return ui_cmd_obj

    def maps_wait_for_map_remove(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj,
                                                    '#networkTabPanel #networkDevicesTab treeview',
                                                    '[0]', 'name', arg_dict['map_name'], None, 60)
        return ui_cmd_obj
