from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.sites.v8dot1dot2.sites import Sites as SitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Sites(SitesBase):
    def sites_create_site(self, ui_cmd_obj, arg_dict):
        # Access the menu to create the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Create Site...] => .x-menu-item-text')

        # Populate the dialog
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['site_name'],
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
                self.logger.log_info("\nA site with name '" + str(arg_dict['site_name']) + "' already exists.\n")
                ui_cmd_obj.error_state = False
            else:
                # FAIL
                self.logger.log_info("\nCould not create site: '" + ui_cmd_obj.return_data + "'.\n")
                ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj, '#mapCreationRenameWindow button[text=Cancel] => '
                                               '.x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj, '#mapCreationRenameWindow #mapCreateOkButton => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def sites_wait_for_site_add(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj,
                                                '#networkTabPanel #networkDevicesTab treeview',
                                                '[0]', 'name', arg_dict['site_name'], None, 60)
        return ui_cmd_obj

    def sites_wait_for_site_remove(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj,
                                                    '#networkTabPanel #networkDevicesTab treeview',
                                                    '[0]', 'name', arg_dict['site_name'], None, 60)
        return ui_cmd_obj

    def sites_configure_devices_select_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'grid[name=editDeviceSelection] gridview => '
                                           '.x-grid-cell-inner:textEquals(' + arg_dict['ip'] + ')')
        return ui_cmd_obj
