from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot2dot4.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
import time
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devices(DevicesBase):
    def devices_add_device(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[text=Add Device...] => '
                               '.x-btn-inner-default-toolbar-small')

        # Populate the IP Address field
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ip_address']),
                                    '#addDeviceAddressText => .x-form-text')

        # Select the profile
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           'combobox[name=profile_id]', '[0]', 'profileName',
                                                           arg_dict['snmp_profile'], exact_match=True)
        if ui_cmd_obj.return_data is True:
            # It's in the drop down, so select it
            self.ext_builder.click(ui_cmd_obj, 'combobox[name=profile_id] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combobox[name=profile_id] boundlist => :textEquals(' + str(
                arg_dict['snmp_profile']) + ')')

            # Populate the Nickname field
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['nickname']),
                                        'textfield[name=nickname] => .x-form-text')

            # Handle the case where the OK button is disabled
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "addDeviceWindow[title=Add Device] "
                                                          "button[actionId=addDevice]",
                                                          "[0].disabled")

            # If OK is disabled click Cancel/Close;  otherwise, click OK
            if ui_cmd_obj.return_data is True:
                # Check if there was an error
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "#addDeviceAddressText",
                                                              "[0].lastActiveError")
                if "address exists" in ui_cmd_obj.return_data:
                    # PASS
                    self.logger.log_info("\nA device with IP '" + str(arg_dict['ip_address']) + "' already exists.\n")
                    ui_cmd_obj.error_state = False
                else:
                    # FAIL
                    self.logger.log_info("\nCould not add device: '" + ui_cmd_obj.return_data + "'.\n")
                    ui_cmd_obj.error_state = True

                # Click Cancel
                self.ext_builder.click(ui_cmd_obj,
                                       'addDeviceWindow[title=Add Device] button[actionId=cancel] => '
                                       '.x-btn-inner-default-small')
            else:
                # Click OK
                self.ext_builder.click(ui_cmd_obj,
                                       'addDeviceWindow[title=Add Device] button[text=OK] => .x-btn-inner-blue-small')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nProfile '" + arg_dict[
                'snmp_profile'] + "' does not exist in the drop down - device cannot be created.\n")

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj,
                                   'addDeviceWindow[title=Add Device] button[actionId=cancel] => '
                                   '.x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_delete_device(self, ui_cmd_obj, arg_dict):
        # Select the Devices tab
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'tab[text=Devices] => .x-tab-inner-extr-sec-tab-panel')

        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Delete Device menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Delete Device] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               'checkbox[boxLabel=Delete Extreme Management Center Data] => .x-form-cb-input')
        self.ext_builder.click(ui_cmd_obj,
                               'deleteDeviceWindow[title=Confirm Delete] button[text=Yes] => '
                               '.x-btn-inner-blue-small')
        return ui_cmd_obj

    def devices_register_trap_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Register Trap Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Register Trap Receiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_unregister_trap_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Register Trap Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Unregister Trap Receiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_register_syslog_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Register Trap Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Register SysLog Receiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_unregister_syslog_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Register Trap Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Unregister SysLog Receiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_refresh_rediscover_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')

        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Rediscover] => '
                               '.x-menu-item-text')

        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_delete_selected_devices(self, ui_cmd_obj, arg_dict):
        # Access the Delete Device menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Delete Device] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               'checkbox[boxLabel=Delete Extreme Management Center Data] => .x-form-cb-input')
        self.ext_builder.click(ui_cmd_obj,
                               'deleteDeviceWindow[title=Confirm Delete] button[text=Yes] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_configure_device(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Configure Device menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Configure...] '
                                           '=> .x-menu-item-text')

        return ui_cmd_obj

    def devices_set_device_profile(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Select the Set Device Profile... menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel{isVisible()} '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=More Actions] => '
                                           '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Set Device Profile...] => '
                               '.x-menu-item-text')

        # Select the profile
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           'combobox[name=profile_id]', '[0]', 'profileName',
                                                           arg_dict['snmp_profile'], exact_match=True)
        if ui_cmd_obj.return_data is True:
            # It's in the drop down, so select it
            self.ext_builder.click(ui_cmd_obj, 'combobox[name=profile_id] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combobox[name=profile_id] boundlist => :textEquals(' +
                                   str(arg_dict['snmp_profile']) + ')')

            # Click OK
            self.ext_builder.click(ui_cmd_obj,
                                   'setProfileWindow[title=Set Device Profile] button[text=OK] => '
                                   '.x-btn-inner-blue-small')
        else:
            # It's not in the drop down, so report the error
            self.logger.log_info("\nCould not find profile '" + arg_dict['snmp_profile'] + "'.\n")
            ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj,
                                   'setProfileWindow[title=Set Device Profile] button[text=Cancel] => '
                                   '.x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_confirm_firmware_version_and_rediscover(self, ui_cmd_obj, arg_dict):
        iterate_table = 0
        attempts = 0
        self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                     '#networkPrimaryDeviceGrid gridview', '[0].store.data.length')
        table_length = ui_cmd_obj.return_data
        while attempts <= int(arg_dict['max_attempts']):
            while iterate_table <= int(table_length):
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 '#networkPrimaryDeviceGrid gridview', '[0].store.data.items[' +
                                                 str(iterate_table) + '].data.ip')
                ip_address = ui_cmd_obj.return_data
                if arg_dict['ip_address'] == ip_address:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                     '#networkPrimaryDeviceGrid gridview', '[0].store.data.items[' +
                                                     str(iterate_table) + '].data.firmware')
                    version = ui_cmd_obj.return_data
                    if arg_dict['version'] == version:
                        return ui_cmd_obj

                    else:
                        attempts += 1
                        self.ext_builder.click(ui_cmd_obj,
                                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                                               str(arg_dict['ip_address']) + ')')
                        self.ext_builder.click(ui_cmd_obj,
                                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
                        self.ext_builder.click(ui_cmd_obj,
                                               '#activeContextMenu{isVisible()} menuitem[text=Rediscover] => '
                                               '.x-menu-item-text')

                        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
                        time.sleep(int(arg_dict['delay_rediscover']))
                        break
                elif table_length == (iterate_table + 1):
                    attempts += 1
                else:
                    iterate_table += 1

        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_edit_device_enforce_preview(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Enforce Preview...] => .x-btn-inner-default-small')
        self.ext_builder.wait_for_attribute(ui_cmd_obj, "button[text=Enforce]", '[0].ariaEl.dom.attributes[6].value',
                                            "false")
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Enforce] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Enforce] boundlist => :textEquals(Custom)')
        self.ext_builder.delay(ui_cmd_obj, 2000)

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceSystem]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_system"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceSystem] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce System check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforceVlan]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_vlan"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforceVlan] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce VLAN check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforcePortAlias]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_port_alias"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforcePortAlias] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce Port Alias check button already at desired state.\n")

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=enforcePortVlan]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_port_vlan"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=enforcePortVlan] => .x-form-cb-input")
        else:
            self.logger.log_info("\nEnforce Port VLAN check button already at desired state.\n")

        self.ext_builder.click(ui_cmd_obj,
                               "button[text=Enforce] => .x-btn-inner-blue-small")
        self.ext_builder.click(ui_cmd_obj,
                               "button[itemId=yes] => .x-btn-inner-blue-small")
        self.ext_builder.delay(ui_cmd_obj, 5000)
        self.ext_builder.click(ui_cmd_obj,
                               "compareDeviceDataWindow[name=compareDeviceDataWindow] button[text=Cancel] => "
                               ".x-btn-inner-default-small")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid button[text=Delete] => .x-btn-button")
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj
