from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.firmware.v8dot1dot3.firmware import Firmware as \
    FirmwareBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Firmware(FirmwareBase):
    def firmware_menu_set_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Inventory Settings...] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_backup_configuration(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     r'#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     r'.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                               '.x-menu-item-text')

        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
            self.ext_builder.click(ui_cmd_obj,
                                   r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                                   r'.x-menu-item-text')
            self.ext_builder.move_cursor(ui_cmd_obj,
                                         '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                         '.x-menu-item-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                   '.x-menu-item-text')

        # Handle the question dialog, if applicable
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'button[itemId=yes]', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'button[itemId=yes]', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        # Click OK in the Information dialog about checking the event log
        self.ext_builder.click(ui_cmd_obj, '#ok{isVisible()} => .x-btn-button')

        return ui_cmd_obj

    def firmware_menu_restore_configuration(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Restore Configuration...] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_compare_last_configurations(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Compare Last Configurations...] => '
                               '.x-menu-item-text')

        # Handle the case where two configuration files do not exist
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Configuration File Compare]', '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj.error_state = True
            self.logger.log_info(r"\nTwo configuration files do not exist, so cannot perform comparison.\n")
            self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

        # Click Yes if presented with a confirmation asking if you want to compare applicable data
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Configuration File Comparison]',
                                                      '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_menu_upgrade_firmware(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Upgrade Firmware...] => '
                               r'.x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_restart_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Restart Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Restart Device...] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_check_for_updates(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               r'#networkPrimaryDeviceGrid button[text=Check for Firmware Updates\.\.\.] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def firmware_menu_register_export_serial_numbers(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Restart Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Other] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Overwrite Local Changes] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Register/\Export Serial Numbers...] => '
                               r'.x-menu-item-text')

        return ui_cmd_obj

    def firmware_confirm_config_fw_menu_exists(self, ui_cmd_obj, arg_dict):
        # Check if the context menu has been built yet
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu', '[0]')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        if arg_dict["menu_name"] == 'Restart Device...':
            if ui_cmd_obj.return_data is None:
                # Context menu has not been built yet, so display it then hide it so we can query the menu picks

                self.ext_builder.click(ui_cmd_obj,
                                       r'#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                       r'.x-menu-item-text')

            # Check if the specified menu is enabled - the query returns True if the menu is DISABLED
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#activeContextMenu '
                                                          'menuitem[text=' + arg_dict["menu_name"] + ']',
                                                          '[0].disabled')
        elif arg_dict["menu_name"] == 'Inventory Settings...':
            if ui_cmd_obj.return_data is None:
                self.ext_builder.click(ui_cmd_obj,
                                       r'#activeContextMenu{isVisible()} menuitem[text=Archives] => '
                                       r'.x-menu-item-text')
                self.ext_builder.move_cursor(ui_cmd_obj,
                                             '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                             '.x-menu-item-text')

                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#activeContextMenu '
                                                              'menuitem[text=' + arg_dict["menu_name"] + ']',
                                                              '[0].disabled')
        # Log the result
        if ui_cmd_obj.return_data == 'Component query returned a value that could not be converted by selenium.':
            ui_cmd_obj.return_data = True
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
