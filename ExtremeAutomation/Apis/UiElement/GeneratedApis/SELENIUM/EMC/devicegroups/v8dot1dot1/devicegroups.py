from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DevicegroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devicegroups(DevicegroupsBase):
    def devicegroups_create_device_group(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               'menuitem[text=Device Groups] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               'menuitem[text=Create Device Group...] => .x-menu-item-text')

        # Populate the dialog with the group name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['group_name']), 'textfield[name=name] => .x-form-text')

        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "addDeviceGroupWindow[title=Add Device Group] button[text=OK]",
                                                      "[0].disabled")

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "addDeviceGroupWindow[title=Add Device Group] "
                                                          "textfield[name=name]", "[0].lastActiveError")

            # FAIL
            self.logger.log_info("\nCould not add device group: '" + ui_cmd_obj.return_data + "'.\n")
            ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Add Device Group] button[actionId=cancel] => '
                                   '.x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Add Device Group] button[text=OK] => '
                                   '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devicegroups_delete_device_group(self, ui_cmd_obj, arg_dict):
        # Select the group to delete
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => '
                               '.x-tree-node-text :contains(' + str(arg_dict['group_name']) + ')')

        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               'menuitem[text=Device Groups] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               'menuitem[text=Delete Device Group...] => .x-menu-item-text')

        # Confirm the deletion
        self.ext_builder.click(ui_cmd_obj,
                               'deleteDeviceGroupWindow[title=Delete Device Group Confirmation] button[text=Yes] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devicegroups_rename_device_group(self, ui_cmd_obj, arg_dict):
        # Select the group to rename
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text :contains(' +
                               str(arg_dict['group_name']) + ')')

        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                               'menuitem[text=Device Groups] => .x-menu-item-arrow')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                               'menuitem[text=Rename Device Group...] => .x-menu-item-text')

        # Enter the new name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['new_name']), 'textfield[name=name] => .x-form-text')

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "addDeviceGroupWindow[title=Rename Device Group] "
                                                          "textfield[name=name]", "[0].lastActiveError")

            # FAIL
            self.logger.log_info("\nCould not rename device group: '" + ui_cmd_obj.return_data + "'.\n")
            ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Rename Device Group] button[actionId=cancel] => '
                                   '.x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Rename Device Group] button[text=OK] => '
                                   '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devicegroups_confirm_device_group_exists(self, ui_cmd_obj, arg_dict):
        # Look for the device group in the tree
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDevicesTab treeview', '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Assume we won't find the device group
        found_item = False

        # Loop through the table and see if the specified device group exists
        item_index = 0
        for x in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkDevicesTab treeview',
                                             '[0].store.data.items[' + str(item_index) + '].data.groupname')
            if ui_cmd_obj.return_data == arg_dict['group_name']:
                self.logger.log_info("\nFound device group '" + arg_dict['group_name'] +
                                     "' at index " + str(item_index) + "\n")
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
