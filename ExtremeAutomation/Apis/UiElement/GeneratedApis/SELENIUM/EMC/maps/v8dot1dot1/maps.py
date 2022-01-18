from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as MapsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Maps(MapsBase):
    def maps_create_map(self, ui_cmd_obj, arg_dict):
        # Access the menu to create the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Create Map...] => .x-menu-item-text')

        # Populate the dialog and click OK
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['map_name'], '#mapCreationWindow #mapName => .x-form-text')

        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#mapCreationWindow #mapCreateOkButton', '[0].disabled')

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "#mapCreationWindow #mapName",
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
            self.ext_builder.click(ui_cmd_obj, '#mapCreationWindow button[text=Cancel] => .x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj, '#mapCreationWindow #mapCreateOkButton => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def maps_delete_map(self, ui_cmd_obj, arg_dict):
        # Select the specified map in the tree
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                                           'span:textEquals(' + arg_dict['map_name'] + ')')

        # Access the menu to delete the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Delete Map] => .x-menu-item-text')

        # Confirm the delete
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def maps_confirm_map_exists(self, ui_cmd_obj, arg_dict):
        # Look for the map in the tree
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDevicesTab treeview', '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Assume we won't find the map
        found_item = False

        # Loop through the table and see if the specified map exists
        item_index = 0
        for x in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkDevicesTab treeview',
                                             '[0].store.data.items[' + str(item_index) + '].data.name')
            if ui_cmd_obj.return_data == arg_dict['map_name']:
                self.logger.log_info("\nFound map '" + arg_dict['map_name'] + "' at index " + str(item_index) + "\n")
                found_item = True
                break
            else:
                item_index += 1

        # Determine if we passed or failed the test, depending on what we expected (exists/not)
        if found_item is StringUtils.string_to_boolean(arg_dict["exists"]):
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
