from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devicegroups.v8dot1dot1.devicegroups import \
    Devicegroups as DevicegroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


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
                                                      "addDeviceGroupWindow[title=Create Device Group] button[text=OK]",
                                                      "[0].disabled")

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "addDeviceGroupWindow[title=Create Device Group] "
                                                          "textfield[name=name]", "[0].lastActiveError")

            # FAIL
            self.logger.log_info("\nCould not create device group: '" + ui_cmd_obj.return_data + "'.\n")
            ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Create Device Group] button[actionId=cancel] => '
                                   '.x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceGroupWindow[title=Create Device Group] button[text=OK] => '
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
                               'menuitem[text=Delete Device Group] => .x-menu-item-text')

        # Confirm the deletion
        self.ext_builder.click(ui_cmd_obj,
                               'deleteDeviceGroupWindow[title=Delete Device Group Confirmation] button[text=Yes] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devicegroups_wait_for_device_group_add(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview', '[0]',
                                                'name', arg_dict['group_name'], None, False, 60)
        return ui_cmd_obj

    def devicegroups_wait_for_device_group_remove(self, ui_cmd_obj, arg_dict):
        # keyword is named "table" but works for checking trees as well
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview', '[0]',
                                                    'name', arg_dict['group_name'], None, False, 60)
        return ui_cmd_obj
