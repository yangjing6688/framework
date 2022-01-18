from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
import time
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Devices(DevicesBase):

    def devices_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel tab[text=' + str(
                                   arg_dict['tab_name']) + '] => .x-tab-inner-extr-sec-tab-panel')
        return ui_cmd_obj

    def devices_select_devices_summary_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel tab[text=' + str(
                                   arg_dict['tab_name']) + '] => .x-tab-inner')
        return ui_cmd_obj

    def devices_select_device_tree_context(self, ui_cmd_obj, arg_dict):
        self.ext_builder.delay(ui_cmd_obj, "1000")
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab otreeselectorcombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab otreeselectorcombo boundlist => '
                                           ':textEquals(' + arg_dict['tree_context'] + ')')
        self.ext_builder.delay(ui_cmd_obj, "2000")
        return ui_cmd_obj

    def devices_expand_device_tree_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.double_click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                                                  ':contains(' + arg_dict['tree_node'] + ')')
        return ui_cmd_obj

    def devices_select_device_tree_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.get_component_index(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview', '[0]', 'name',
                                             arg_dict['tree_node'], False)
        if ui_cmd_obj.return_data != -1:
            self.ext_builder.scroll_to_index(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview', '[0]',
                                             ui_cmd_obj.return_data)
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                                               ':contains(' + arg_dict['tree_node'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nCould not find tree node '" + arg_dict['tree_node'] + "'")

        return ui_cmd_obj

    def devices_select_device_in_table(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' + str(
                                   arg_dict['device_ip']) + ')')
        return ui_cmd_obj

    def devices_select_all_devices_in_table(self, ui_cmd_obj, arg_dict):
        # get the number of device table entries
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                         'deviceGrid[viewId=DeviceTable]', '[0].store.data.items.length')
        item_count = int(ui_cmd_obj.return_data)
        # check if the table is empty
        if item_count > 0:
            # click on the first element and shift click on the last element in the table
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid gridview' +
                                   '=> .x-grid-item:nth-of-type(1) :nth-of-type(5) .x-grid-cell-inner')
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid gridview' +
                                   '=> .x-grid-item:nth-of-type(' + str(item_count) +
                                   ') :nth-of-type(5) .x-grid-cell-inner', shift=True)
            self.logger.log_info("\nSelected " + str(item_count) + " rows.\n")
        else:
            self.logger.log_info("\nTable is empty.\n")
        return ui_cmd_obj

    def devices_refresh_devices_table(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel'
                                           ' deviceGrid #refresh => .x-btn-icon-el')
        self.ext_builder.delay(ui_cmd_obj, "3000")
        return ui_cmd_obj

    def devices_refresh_device_tree_my_network(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => '
                               '.x-tree-node-text :contains(My Network)')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'deviceGrid[title=Devices] #refresh => .x-btn-icon-el')

        return ui_cmd_obj

    def devices_add_device(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=addDevice] => .x-menu-item-text')

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
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=editDevices] => .x-menu-item-text')

        return ui_cmd_obj

    def devices_open_device_terminal(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' + str(
                                   arg_dict['ip_address']) + ')')

        # Select the Open Device Terminal... menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel{isVisible()} '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Open Device Terminal...] => '
                               '.x-menu-item-text')
        return ui_cmd_obj

    def devices_close_device_terminal(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'tool[type=close] => .x-tool-tool-el')

        return ui_cmd_obj

    def devices_confirm_device_terminal_enters_device_prompt(self, ui_cmd_obj, arg_dict):
        # Component query for the prompt from the device if successfully logged in
        self.ext_builder.component_query(ui_cmd_obj,
                                         'window[title="Extreme WebShell - ' + arg_dict['ip_address'] + '"]',
                                         '[0].body.dom.childNodes["0"].childNodes["0"].childNodes["0"].childNodes["0"]'
                                         '.childNodes["0"].childNodes["0"].childNodes["0"].contentDocument.'
                                         'childNodes["0"].childNodes[1].childNodes["0"].childNodes["0"].childNodes[4]'
                                         '.innerHTML')

        # Verify the prompt found matches what user provided
        if ui_cmd_obj.return_data.strip() == arg_dict['prompt']:
            self.logger.log_info('A prompt of "' + ui_cmd_obj.return_data +
                                 '" was seen, which matches what user provided.')
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info('A prompt of "' + ui_cmd_obj.return_data +
                                 '" was seen, which does not match the value that the user povided of "' +
                                 arg_dict['prompt'] + '".')
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_launch_webview(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Select the Launch WebView menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel{isVisible()} '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=View] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Device Details] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Device Details] => '
                               '.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Launch WebView] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Launch WebView] => '
                               '.x-menu-item-text')
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
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Delete Device] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               'checkbox[boxLabel=Delete Extreme Management Center Data] => .x-form-cb-input')
        self.ext_builder.click(ui_cmd_obj,
                               'deleteDeviceWindow[title=Delete Confirmation] button[text=Yes] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_delete_selected_devices(self, ui_cmd_obj, arg_dict):
        # get the number of device table entries
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                         'deviceGrid[viewId=DeviceTable]',
                                         '[0].store.data.items.length')
        item_count = int(ui_cmd_obj.return_data)
        # check if the table is empty
        if item_count > 0:
            # delete all selected items from table
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
            self.ext_builder.click(ui_cmd_obj,
                                   '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
            self.ext_builder.move_cursor(ui_cmd_obj,
                                         '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                         '.x-menu-item-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#activeContextMenu{isVisible()} menuitem[text=Delete Device] => .x-menu-item-text')
            self.ext_builder.click(ui_cmd_obj,
                                   'checkbox[boxLabel=Delete Extreme Management Center Data] => .x-form-cb-input')
            self.ext_builder.click(ui_cmd_obj,
                                   'deleteDeviceWindow[title=Delete Confirmation] button[text=Yes] => '
                                   '.x-btn-inner-blue-small')
        else:
            self.logger.log_info("\nTable is empty.\n")
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
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
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

    def devices_add_device_to_group(self, ui_cmd_obj, arg_dict):
        # Select the Devices tab
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'tab[text=Devices] => .x-tab-inner-extr-sec-tab-panel')

        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'deviceGrid[title=Devices] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Add Device to Group menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Add Device to Group...] => '
                               '.x-menu-item-link')

        # Populate the dialog
        self.ext_builder.click(ui_cmd_obj, 'addToDeviceGroupWindow[title=Select Destination Group] '
                                           'treeview => .x-tree-node-text:textEquals(' +
                               str(arg_dict['group_name']) + ')')
        self.ext_builder.click(ui_cmd_obj,
                               'addToDeviceGroupWindow[title=Select Destination Group] button[text=OK] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_remove_device_from_group(self, ui_cmd_obj, arg_dict):
        # Select the Devices tab
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'tab[text=Devices] => .x-tab-inner-extr-sec-tab-panel')

        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'deviceGrid[title=Devices] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Remove Device from Group menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Remove Device from Group] => '
                               '.x-menu-item-link')

        return ui_cmd_obj

    def devices_refresh_rediscover_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')

        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Refresh (Rediscover) Device] => '
                               '.x-menu-item-text')

        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

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
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=registerTrapReceiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_unregister_trap_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Unregister Trap Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=unregisterTrapReceiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_register_syslog_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Register SysLog Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=registerSysLogReceiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_unregister_syslog_receiver(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] tableview => :textEquals(' +
                               str(arg_dict['ip_address']) + ')')

        # Access the Unregister SysLog Receiver menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[actionId=unregisterSysLogReceiver] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def devices_collect_device_statistics(self, ui_cmd_obj, arg_dict):
        # Select the device in the table
        self.ext_builder.click(
            ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel deviceGrid[title=Devices] '
                        'tableview => :textEquals(' + str(arg_dict['ip_address']) + ')')

        # Select the Collect Device Statistics menu item from the context menu
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'deviceGrid[title=Devices] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Collect Device Statistics...] => '
                               '.x-menu-item-text')

        # Select the statistic to collect
        self.ext_builder.click(ui_cmd_obj, "#" + str(arg_dict['stat_name']) + " => [data-ref='displayEl']")
        self.ext_builder.click(ui_cmd_obj,
                               'collectStatisticsWindow[title=Collect Device Statistics] button[text=OK] => '
                               '.x-btn-button')
        if arg_dict['stat_name'] == "Monitor":
            self.ext_builder.click(ui_cmd_obj,
                                   'button[text=' + arg_dict['monitor_selection'] + '] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_collect_interface_statistics(self, ui_cmd_obj, arg_dict):

        # Select the device in the tree (note: the node must be visible/parent already expanded)
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                                           ':contains(' + arg_dict['ip_address'] + ')')

        # Make sure the correct tab is selected
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'tab[text=Summary] => .x-tab-inner-extr-sec-tab-panel')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'deviceViewDataPanel tab[title=Ports] => .x-tab-inner')

        # Expand the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        # Select the specified port
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')

        # Access the context menu for the specified port
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                                     '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')

        # Select the Collect Interface Statistics menu
        self.ext_builder.click(ui_cmd_obj,
                               '#portTreeMenu{isVisible()} menuitem[text=Collect Interface Statistics...] => '
                               '.x-menu-item-text')

        # Populate the dialog
        self.ext_builder.click(ui_cmd_obj, "#ifHistorical => [data-ref='displayEl']")
        self.ext_builder.click(ui_cmd_obj,
                               'ifCollectionWindow[title=Collect Interface Statistics] button[text=OK] => '
                               '.x-btn-inner-blue-small')

        # Collapse the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        return ui_cmd_obj

    def devices_enable_port(self, ui_cmd_obj, arg_dict):

        # Select the device in the tree (the parent node must already be expanded so the device is visible)
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text :contains(' +
                               str(arg_dict['ip_address']) + ')')

        # Make sure the correct tab is selected
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'tab[text=Summary] => .x-tab-inner-extr-sec-tab-panel')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceViewDataPanel tab[title=Ports] => .x-tab-inner')

        # Expand the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        # Enable the port
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                                     '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#portTreeMenu{isVisible()} menuitem[text=Enable Port] => .x-menu-item-text')

        # Collapse the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        return ui_cmd_obj

    def devices_disable_port(self, ui_cmd_obj, arg_dict):

        # Select the device in the tree (the parent node must already be expanded so the device is visible)
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                               ':contains(' + arg_dict['ip_address'] + ')')

        # Make sure the correct tab is selected
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'tab[text=Summary] => .x-tab-inner-extr-sec-tab-panel')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceViewDataPanel tab[title=Ports] => .x-tab-inner')

        # Expand the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        # Disable the port
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                                     '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')
        self.ext_builder.click(ui_cmd_obj,
                               '#portTreeMenu{isVisible()} menuitem[text=Disable Port] => .x-menu-item-text')

        # Collapse the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        return ui_cmd_obj

    def devices_open_device_view(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[title=Devices] tableview => .x-grid-cell:textEquals(' +
                               str(arg_dict['ip_address']) + ')')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[title=Devices] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} '
                               'menuitem[text=View] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device Details]'
                                           ' => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()}'
                                     ' menuitem[text=Launch WebView] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()}'
                               ' menuitem[text=DeviceView] => .x-menu-item-text')

        return ui_cmd_obj

    def devices_edit_device_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel tab[text=" + str(arg_dict['tab_name']) + "] => .x-tab-inner")
        return ui_cmd_obj

    def devices_edit_device_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] button[text=Save] => "
                               ".x-btn-inner-blue-small")
        return ui_cmd_obj

    def devices_edit_device_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] button[text=Cancel] => "
                               ".x-btn-inner-default-small")

        return ui_cmd_obj

    def devices_edit_device_set_system_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['sys_name']),
                                    "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_contact(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['contact']),
                                    "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_location(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['location']),
                                    "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_admin_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=profileName] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=profileName].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['profile']) + ")")
        return ui_cmd_obj

    def devices_edit_device_remove_from_service(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=outOfService]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=outOfService] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")

        return ui_cmd_obj

    def devices_edit_device_set_default_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['site_name']) + ")")

        if str(arg_dict['import_site']) == "True" or str(arg_dict['import_site']) == "Yes":
            self.ext_builder.click(ui_cmd_obj, "messagebox[title=Import Site] #yes => .x-btn-inner-blue-small")
        else:
            self.ext_builder.click(ui_cmd_obj,
                                   "messagebox[title=Import Site] #no => .x-btn-inner-default-small")

        return ui_cmd_obj

    def devices_edit_device_set_poll_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollGroup] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollGroup].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['poll_group']) + ")")
        return ui_cmd_obj

    def devices_edit_device_set_poll_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollType].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['poll_type']) + ")")
        return ui_cmd_obj

    def devices_edit_device_set_snmp_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['snmp_timeout']),
                                    "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_snmp_retries(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['snmp_retries']),
                                    "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_topology_layer(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=topologyRole] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=topologyRole].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['topology_layer']) + ")")
        return ui_cmd_obj

    def devices_edit_device_set_nickname(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['nick_name']),
                                    "deviceDetailsPanel textfield[name=nickname] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_asset_tag(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=assetTag] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['asset_tag']),
                                    "deviceDetailsPanel textfield[name=assetTag] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_user_data(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel textfield[name=" + "userData" +
                               str(arg_dict['the_field']) + "] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_data']),
                                    "deviceDetailsPanel textfield[name=" + "userData" +
                                    str(arg_dict['the_field']) + "] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_set_note(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textarea[name=note] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_note']),
                                    "deviceDetailsPanel textarea[name=note] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid button[text=Add] => .x-btn-button")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid button[text=Edit] => .x-btn-button")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid button[text=Delete] => .x-btn-button")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_update(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text_no_target(ui_cmd_obj, '[RETURN]')
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVlanName] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_set_vid(self, ui_cmd_obj, arg_dict):

        self.ext_builder.click(ui_cmd_obj, "numberfield[name=deviceDetailsVid] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "numberfield[name=deviceDetailsVid] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_set_always_write_to_devices(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsWrite]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=deviceDetailsWrite] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def devices_edit_device_vlan_definition_select_row(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Selecting VLAN Name " + str(arg_dict['vlan_name']))
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid gridview => .x-grid-cell-inner:textEquals(" +
                               str(arg_dict['vlan_name']) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_select_row(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[title=Configure Device] "
                               "deviceDetailPortsPanel[name=deviceDetailPortsPanel] tableview => "
                               ".x-grid-cell-inner:textEquals(" + str(arg_dict['port_name']) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_select_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                                     '.x-column-header-text')
        self.ext_builder.double_click(ui_cmd_obj,
                                      "editDeviceDataWindow[title=Configure Device] "
                                      "deviceDetailPortsPanel[name=deviceDetailPortsPanel] tableview => "
                                      ".x-grid-cell-inner:textEquals(" + str(arg_dict['port_name']) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[title=Configure Device] "
                               "deviceDetailPortsPanel[name=deviceDetailPortsPanel] button[actionId=deviceEditPort] => "
                               ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def devices_edit_device_ports_row_editor_update(self, ui_cmd_obj, arg_dict):
        type_string = "[RETURN]"
        self.ext_builder.enter_text(ui_cmd_obj, str(type_string),
                                    "textfield[name=deviceDetailsPortAlias] => .x-form-text",
                                    clear_existing=False)
        return ui_cmd_obj

    def devices_edit_device_ports_row_editor_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "roweditorbuttons [itemId=cancel] => .x-btn-inner-default-small")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_alias(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsPortAlias] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsPortAlias] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_nickname(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsPortNickname] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsPortNickname] => .x-form-text")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_enabled(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name =deviceDetailsPortAdminState]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name =deviceDetailsPortAdminState] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_auto_negotiation(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name =deviceDetailsPortAutoNegotiation]",
                                                      "[0].rawValue")

        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name =deviceDetailsPortAutoNegotiation] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")

        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_speed(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortConfigSpeed] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combo[name=deviceDetailsPortConfigSpeed] boundlist => :textEquals(" + str(
                                   arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_duplex(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortDuplex] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combo[name=deviceDetailsPortDuplex] boundlist => :textEquals(" +
                               str(arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsRole] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combo[name=deviceDetailsRole] boundlist => :textEquals(" +
                               str(arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_pvid(self, ui_cmd_obj, arg_dict):
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            self.ext_builder.click(ui_cmd_obj, "combo[name=devicePortPvidEditor] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "combo[name=devicePortPvidEditor].getPicker() => .x-boundlist-item:contains(" +
                                   str(arg_dict["the_value"]) + ")")
            if ui_cmd_obj.error_state is True:
                ui_cmd_obj.error_state = False
                attempts += 1
            else:
                return ui_cmd_obj
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_lag(self, ui_cmd_obj, arg_dict):
        iteration = 0
        self.ext_builder.click(ui_cmd_obj,
                               "selectActionField[dataIndex=deviceLagMembership] => .fa-ellipsis-h")
        self.ext_builder.click(ui_cmd_obj,
                               "selectPortActionDialog[title=Select LAG Ports] checkcolumn => "
                               ".x-column-header-checkbox")
        self.ext_builder.click(ui_cmd_obj,
                               "selectPortActionDialog[title=Select LAG Ports] checkcolumn => "
                               ".x-column-header-checkbox")
        values = str(arg_dict["the_value"]).split(",")
        for value in values:
            self.ext_builder.component_query(
                ui_cmd_obj, 'selectPortActionDialog[title=Select LAG Ports] gridview', '[0].store.data.length')
            length = ui_cmd_obj.return_data
            while iteration < length:
                self.ext_builder.component_query(ui_cmd_obj, 'selectPortActionDialog[title=Select LAG Ports] gridview',
                                                 '[0].store.data.items[' + str(iteration) + '].data.portName')
                if value == ui_cmd_obj.return_data:
                    location_in_table = iteration
                    self.ext_builder.component_query(
                        ui_cmd_obj, 'selectPortActionDialog[title=Select LAG Ports] gridview',
                        '[0].body.dom.childNodes[' + str(location_in_table) + '].id')
                    self.ext_builder.click(ui_cmd_obj, '#' + str(ui_cmd_obj.return_data) + ' > tbody > tr > td')
                    break
                else:
                    iteration += 1

        self.ext_builder.click(ui_cmd_obj,
                               "selectPortActionDialog[title=Select LAG Ports] button[text=OK] => "
                               ".x-btn-inner-default-small")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_authentication(self, ui_cmd_obj, arg_dict):
        # THIS DOES NOT WORK... NEED HELPER FUNCTIONS
        self.ext_builder.click(ui_cmd_obj, "multicombo[name=deviceAuthType] => .x-form-arrow-trigger")
        self.ext_builder.click(ui_cmd_obj, "multicombobox[name=deviceAuthType] boundlist => :textEquals(" + str(
            arg_dict["the_value"]) + ")")
        # self.ext_builder.click(ui_cmd_obj,"multicombobox[name=deviceAuthType].getPicker() =>
        #                        .x-boundlist-item:contains(" + str(arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_tagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-clear-trigger")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-arrow-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "vlanmulticombobox[dataIndex=tagged] boundlist => :textEquals(" + str(
                                   arg_dict["the_value"]) + ")")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-arrow-trigger")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_untagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-clear-trigger")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-arrow-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "vlanmulticombobox[dataIndex=untagged] boundlist => :textEquals(" + str(
                                   arg_dict["the_value"]) + ")")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-arrow-trigger")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_node_alias(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortNodeAlias]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortNodeAlias] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired value.\n")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_span_guard(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortSpanGuard]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortSpanGuard] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_loop_protect(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortLoopProtect]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name=deviceDetailsPortLoopProtect] => .x-form-cb-input")
        else:
            self.logger.log_info("\ncheck button already at desired state.\n")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_mvrp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortMvrp]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['the_value']):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortMvrp] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
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

        # Make sure the menu exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu '
                                                      '#columnItem', '[0].menu')

        if ui_cmd_obj.return_data is not None:
            # Make sure the menu contains items
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu '
                                                          '#columnItem', '[0].menu.items.length')
            menu_count = int(ui_cmd_obj.return_data)
            if menu_count != 0:
                # Loop through each of the column names in the comma-separated list and toggle each column checkbox
                # appropriately
                columns = arg_dict['col_list'].split(',')
                for col_name in columns:
                    menu_count += 1

                    # Loop through the items, searching for the node to act on
                    menu_index = 0
                    for x in range(0, menu_count):
                        ui_cmd_obj = self.ext_builder.component_query(
                            ui_cmd_obj, 'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem',
                            '[0].menu.items.items[' + str(menu_index) + '].text')
                        if ui_cmd_obj.return_data == col_name:
                            # Check the current selection state of the node
                            ui_cmd_obj = self.ext_builder.component_query(
                                ui_cmd_obj,
                                'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem',
                                '[0].menu.items.items[' + str(menu_index) + '].checked')
                            if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['show_col']):
                                self.ext_builder.click(
                                    ui_cmd_obj,
                                    'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem '
                                    'menucheckitem[text=' + col_name + '] => .x-menu-item-icon')
                            else:
                                self.logger.log_info(
                                    "\nColumn '" + col_name + "' is already at desired selection state (" +
                                    arg_dict['show_col'] + ").\n")
                            break
                        else:
                            menu_index += 1
            else:
                self.logger.log_info("\nColumn menu is empty.\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find column menu.\n")
            ui_cmd_obj.error_state = True

        # Close the column menu
        self.ext_builder.click(ui_cmd_obj,
                               'editDeviceDataWindow[title=Configure Device] '
                               'deviceDetailPortsPanel[name=deviceDetailPortsPanel] toolbar => .x-box-inner')

        return ui_cmd_obj

    def devices_edit_device_enforce_preview(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] button[actionId=verifyDeviceData] => "
                               ".x-btn-inner-default-small")
        self.ext_builder.delay(ui_cmd_obj, 3000)

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
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enforce_port"]):
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

    def devices_open_device_view_flexview(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} '
                               'menuitem[text=View] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device Details]'
                                           ' => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()}'
                                     ' menuitem[text=FlexView] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=FlexView] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=flexView] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               'combo[name=flexView] boundlist => :textEquals(' + arg_dict['flexview'] + ')')
        self.ext_builder.click(ui_cmd_obj,
                               'flexViewSelectWindow[title=Open FlexView] button[text=OK] => .x-btn-button')
        return ui_cmd_obj

    def devices_open_device_view_physical_entity_summary(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} '
                               'menuitem[text=View] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device Details]'
                                           ' => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()}'
                                     ' menuitem[text=Launch WebView] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj, '#activeContextMenu{isVisible()}'
                                                 ' menuitem[text=System] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, ' menuitem[text=Physical Entity Summary] => .x-menu-item-text')
        return ui_cmd_obj

    def devices_open_device_view_interface_statistics(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} '
                               'menuitem[text=View] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Device Details]'
                                           ' => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()}'
                                     ' menuitem[text=Launch WebView] => .x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj, '#activeContextMenu{isVisible()}'
                                                 ' menuitem[text=Interface] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, ' menuitem[text=Statistics] => .x-menu-item-text')
        return ui_cmd_obj

    def devices_wait_for_device_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj,
                                                '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                'deviceGrid[viewId=DeviceTable]',
                                                '[0]', 'ip', arg_dict['device_ip'], None, True, arg_dict['timeout'])
        return ui_cmd_obj

    def devices_wait_for_device_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj,
                                                    '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                    'deviceGrid[viewId=DeviceTable]',
                                                    '[0]', 'ip', arg_dict['device_ip'], None, True, 60)
        return ui_cmd_obj

    def devices_wait_for_device_value(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]',
                                                          '[0]', 'ip', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            col_name = arg_dict['col_name']
            self.get_column_attribute(ui_cmd_obj, col_name)
            col_attr = ui_cmd_obj.return_data
            if col_attr != "":
                # Wait for the column's value to be what we expect
                self.ext_builder.wait_for_attribute(ui_cmd_obj,
                                                    '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                    'deviceGrid[viewId=DeviceTable]',
                                                    '[0].store.data.items[' + str(row_index) + '].data.' + col_attr,
                                                    arg_dict['expected_value'], arg_dict['wait_time'])
            else:
                self.logger.log_info("\nColumn '" + col_name + "' did not map to a known column attribute.\n")
                ui_cmd_obj.error_state = True

        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' was not found in the table.\n")

        return ui_cmd_obj

    def devices_confirm_firmware_version(self, ui_cmd_obj, arg_dict):
        table_length = 0
        attempts = 0
        self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                     '#networkPrimaryDeviceGrid gridview', '[0].store.data.length')
        table_length = ui_cmd_obj.return_data
        while attempts <= int(arg_dict['max_attempts']):
            if int(table_length) == 1:
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 '#networkPrimaryDeviceGrid gridview',
                                                 '[0].store.data.items[0].data.ip')
                ip_address = ui_cmd_obj.return_data
                if arg_dict['ip_address'] == ip_address:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                     '#networkPrimaryDeviceGrid gridview',
                                                     '[0].store.data.items[0].data.firmware')
                    version = ui_cmd_obj.return_data
                    if arg_dict['version'] == version:
                        return ui_cmd_obj
                    else:
                        attempts += 1
                        self.ext_builder.delay(ui_cmd_obj, "1000")
            else:
                attempts += 1
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'ip', arg_dict['ip'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_admin_profile(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'adminProfileName', arg_dict['admin_profile'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_stats(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'collectionStatus', str(0))

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_collection_statistics(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'collectionStatus', arg_dict['collection'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_syslog_status(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'deviceSysLogStatus', arg_dict['syslog_status'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_ip_trap_status(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'deviceTrapStatus', arg_dict['trap_status'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict['exists']):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_status(self, ui_cmd_obj, arg_dict):
        table_length = 0
        attempts = 0
        iterate_table = 0
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
                                                     str(iterate_table) + '].data.status')
                    if ui_cmd_obj.return_data == 0:
                        status = "down"
                    else:
                        status = "up"
                    if arg_dict['status'].lower() == status:
                        return ui_cmd_obj
                    else:
                        attempts += 1
                        self.ext_builder.delay(ui_cmd_obj, "1000")
                        break
                else:
                    iterate_table += 1

        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_confirm_system_name(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysName]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device System Name: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device System Name: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))
        return ui_cmd_obj

    def devices_confirm_contact(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysContact]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Contact Name: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Contact Name: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_location(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysLocation]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Location value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Location value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))
        return ui_cmd_obj

    def devices_confirm_admin_profile(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel combo[name=profileName]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Admin Profile value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Admin Profile value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_topology_layer(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel combobox[name=topologyRole]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Topology Layer value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Topology Layer value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))
        return ui_cmd_obj

    def devices_confirm_remove_from_service(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel checkbox[name=outOfService]",
                                                      "[0].rawValue")
        if str(ui_cmd_obj.return_data) == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Out of Service value: " + str(ui_cmd_obj.return_data) +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Out of Service value: " + str(ui_cmd_obj.return_data) +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_default_site(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel combobox[name=defaultSiteId]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Detault Site value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Default Site value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_poll_group(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollGroup]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Poll Group value: " + ui_cmd_obj.return_data + " does match the value provided: " + str(
                    arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Poll Group value: " + ui_cmd_obj.return_data + " does not match the value provided: " + str(
                    arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_poll_type(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           "#networkTabPanel #networkDevicesTab "
                                                           "#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]",
                                                           '[0]', 'pollType', arg_dict['the_value'])

        self.logger.log_info("QUERY RESULT: " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data:
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_snmp_timeout(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpTimeout]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device SNMP Timeout value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device SNMP Timeout value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_snmp_retries(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpRetry]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device SNMP Retries value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device SNMP Retries value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_serial_number(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceDetailsPanel textfield[name=replacementSerialNumber]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Serial Number value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Serial Number value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_nickname(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=nickname]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Nickname value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Nickname value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_asset_tag(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=assetTag]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Asset Tag value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Asset Tag value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_user_data(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=userData" +
                                                      str(arg_dict["data_num"] + "]"), "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device User Data " + str(arg_dict["data_num"]) + " value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device User Data " + str(arg_dict["data_num"]) + " value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_note(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textarea[name=note]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Note value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Note value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

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
                                               '#activeContextMenu{isVisible()} menuitem[text=Device] => '
                                               '.x-menu-item-text')
                        self.ext_builder.move_cursor(ui_cmd_obj,
                                                     '#activeContextMenu{isVisible()} menuitem[text=Add Device...] => '
                                                     '.x-menu-item-text')

                        self.ext_builder.click(ui_cmd_obj,
                                               '#activeContextMenu{isVisible()} menuitem[text=Refresh '
                                               '(Rediscover) Device] => .x-menu-item-text')

                        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
                        time.sleep(int(arg_dict['delay_rediscover']))
                        break
                elif table_length == (iterate_table + 1):
                    attempts += 1
                else:
                    iterate_table += 1

        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_confirm_vlan_name(self, ui_cmd_obj, arg_dict):
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'editDeviceDataWindow[title=Configure Device] #deviceVlanGrid',
                                                     "deviceDetailsVlanName",
                                                     str(arg_dict["vlan_name"]))
        self.logger.log_info("deviceDetailsVlanName " + str(row_index))
        ui_cmd_obj.error_state = False
        if row_index == -1:
            match = False
            self.logger.log_info("Confirmed VLAN Name: " + str(
                arg_dict["vlan_name"]) + " does not exist within the VLAN Definition table.")
        else:
            match = True
            self.logger.log_info("Confirmed VLAN Name: " + str(
                arg_dict["vlan_name"]) + " does exist within the VLAN Definition table at row index: " + str(row_index))

        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_confirm_vlan_vid(self, ui_cmd_obj, arg_dict):
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'editDeviceDataWindow[title=Configure Device] #deviceVlanGrid',
                                                     "deviceDetailsVlanName", str(arg_dict["vlan_name"]))
        self.logger.log_info("deviceDetailsVid " + str(row_index))
        ui_cmd_obj.error_state = False
        if row_index == -1:
            match = False
            self.logger.log_info(
                "Confirmed VID ID: " + str(arg_dict["vlan_name"]) + " does not exist within the VLAN Definition table.")
        else:
            vid_id = str(
                self.devices_get_table(ui_cmd_obj, 'editDeviceDataWindow[title=Configure Device] #deviceVlanGrid',
                                       row_index, "deviceDetailsVid"))

            if vid_id == str(arg_dict["vid_id"]):
                self.logger.log_info("Confirmed VID ID: " + arg_dict['vid_id'] + " matches VID ID: " + vid_id +
                                     " within the devices VLAN Definition table for VLAN ""Name: " +
                                     str(arg_dict["vlan_name"]))
                match = True
            else:
                self.logger.log_info("Confirmed VID ID: " + arg_dict['vid_id'] + " does not match VID ID: " + vid_id +
                                     " within the discovered table for VLAN Name: " +
                                     str(arg_dict["vlan_name"]))
                match = False

        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_confirm_vlan_write_to_device(self, ui_cmd_obj, arg_dict):
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'editDeviceDataWindow[title=Configure Device] #deviceVlanGrid',
                                                     "deviceDetailsVlanName", str(arg_dict["vlan_name"]))
        self.logger.log_info("deviceDetailsWrite " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Confirmed VID ID: " + str(arg_dict["vlan_name"]) + " does not exist within the VLAN Definition table.")
        else:
            write_to_device = str(
                self.devices_get_table(ui_cmd_obj, 'editDeviceDataWindow[title=Configure Device] #deviceVlanGrid',
                                       row_index, "deviceDetailsWrite"))

            if write_to_device == str(arg_dict["write_to_device"]):
                self.logger.log_info("Confirmed Always Write To Device: " + arg_dict['write_to_device'] +
                                     " matches Always Write To Device value: " + write_to_device +
                                     " within the devices VLAN Definition table for VLAN Name: " +
                                     str(arg_dict["vlan_name"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed Always Write To Device: " + arg_dict['write_to_device'] +
                                     " does not match Always Write To Device value: " + write_to_device +
                                     " within the discovered table for VLAN Name: " + str(arg_dict["vlan_name"]))
                ui_cmd_obj.error_state = True

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
                                       row_index, "deviceDetailsPortAlias"))

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

    def devices_confirm_device_port_authentication(self, ui_cmd_obj, arg_dict):

        # get row index of specified port
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'deviceDetailPortsPanel[name=deviceDetailPortsPanel]'
                                                     ' gridview{isVisible()}', "deviceDetailsPortNumber",
                                                     str(arg_dict["port_id"]))
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Provided Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
            return ui_cmd_obj
        else:
            # get length of tagged vlan list
            self.ext_builder.component_query(
                ui_cmd_obj, 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                '[0].store.data.items[' + str(row_index) + '].data.deviceAuthType.length')
            item_count = int(ui_cmd_obj.return_data)
            for item_index in range(0, item_count):
                self.ext_builder.component_query(ui_cmd_obj,
                                                 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] '
                                                 'gridview{isVisible()}', '[0].store.data.items[' + str(row_index) +
                                                 '].data.deviceAuthType[' + str(item_index) + ']')
                self.logger.log_info("VID returned by query: " + str(ui_cmd_obj.return_data))
                if str(ui_cmd_obj.return_data) == str(arg_dict["the_value"]):
                    self.logger.log_info("Provided Auth Type: " + str(arg_dict['the_value']) +
                                         " matches the found Auth Type: " + str(ui_cmd_obj.return_data) +
                                         " within the Device Ports table for port " + str(arg_dict["port_id"]))
                    return ui_cmd_obj

        # The value was not found
        self.logger.log_info("Provided Auth Type: " + str(arg_dict['the_value']) +
                             " was not found within the Device Ports Table for port: " + str(arg_dict["port_id"]))
        ui_cmd_obj.error_state = True

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
                                       row_index, "deviceDetailsPortAdminState"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Enabled: " + arg_dict['the_value'] + " matches the Enabled value: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed Enabled: " + arg_dict['the_value'] + " does not match Enabled: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_mvrp(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortMvrp"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed MVRP: " + arg_dict['the_value'] + " matches the MVRP value: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed MVRP: " + arg_dict['the_value'] + " does not match MVRP: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_pvid(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceVlanPvid"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed PVID: " + arg_dict['the_value'] + " matches the PVID value: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed PVID: " + arg_dict['the_value'] + " does not match PVID: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_tagged(self, ui_cmd_obj, arg_dict):
        # get row index of specified port
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'deviceDetailPortsPanel[name=deviceDetailPortsPanel]'
                                                     ' gridview{isVisible()}', "deviceDetailsPortNumber",
                                                     str(arg_dict["port_id"]))
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Provided Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
            return ui_cmd_obj
        else:
            # get length of tagged vlan list
            self.ext_builder.component_query(
                ui_cmd_obj, 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                '[0].store.data.items[' + str(row_index) + '].data.tagged.length')
            item_count = int(ui_cmd_obj.return_data)
            if item_count == 0 and arg_dict['the_value'] == '':
                return ui_cmd_obj

            for item_index in range(0, item_count):
                self.ext_builder.component_query(ui_cmd_obj,
                                                 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] '
                                                 'gridview{isVisible()}', '[0].store.data.items[' + str(row_index) +
                                                 '].data.tagged[' + str(item_index) + ']')
                self.logger.log_info("VID returned by query: " + str(ui_cmd_obj.return_data))
                if str(ui_cmd_obj.return_data) == str(arg_dict["the_value"]):
                    self.logger.log_info("Provided Tagged VID: " + str(arg_dict['the_value']) +
                                         " matches the found Tagged value: " + str(ui_cmd_obj.return_data) +
                                         " within the Device Ports table for port " + str(arg_dict["port_id"]))
                    return ui_cmd_obj

        # The value was not found
        self.logger.log_info("Provided Tagged VID: " + str(arg_dict['the_value']) +
                             " was not found within the Device Ports Table for port: " + str(arg_dict["port_id"]))
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_untagged(self, ui_cmd_obj, arg_dict):
        # get row index of specified port
        row_index = self.devices_get_table_row_index(ui_cmd_obj,
                                                     'deviceDetailPortsPanel[name=deviceDetailPortsPanel]'
                                                     ' gridview{isVisible()}', "deviceDetailsPortNumber",
                                                     str(arg_dict["port_id"]))
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "Provided Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
            return ui_cmd_obj
        else:
            # get length of tagged vlan list
            self.ext_builder.component_query(
                ui_cmd_obj, 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                '[0].store.data.items[' + str(row_index) + '].data.untagged.length')
            item_count = int(ui_cmd_obj.return_data)
            if item_count == 0 and arg_dict['the_value'] == '':
                return ui_cmd_obj
            for item_index in range(0, item_count):
                self.ext_builder.component_query(ui_cmd_obj,
                                                 'deviceDetailPortsPanel[name=deviceDetailPortsPanel] '
                                                 'gridview{isVisible()}', '[0].store.data.items[' + str(row_index) +
                                                 '].data.untagged[' + str(item_index) + ']')
                self.logger.log_info("VID returned by query: " + str(ui_cmd_obj.return_data))
                if str(ui_cmd_obj.return_data) == str(arg_dict["the_value"]):
                    self.logger.log_info("Provided Untagged VID: " + str(arg_dict['the_value']) +
                                         " matches the found Untagged value: " + str(ui_cmd_obj.return_data) +
                                         " within the Device Ports table for port " + str(arg_dict["port_id"]))
                    return ui_cmd_obj

        # The value was not found
        self.logger.log_info("Provided Untagged VID: " + str(arg_dict['the_value']) +
                             " was not found within the Device Ports Table for port: " + str(arg_dict["port_id"]))
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_nickname(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortNickname"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Nick Name: " + arg_dict['the_value'] + " matches the Nick Name: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Nick Name: " + arg_dict['the_value'] + " does not match  Nick Name: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_device_nickname(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "nickname"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Device Nickname: " + arg_dict['the_value'] +
                                     " matches the Device Nickname: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Device Nickname: " + arg_dict['the_value'] +
                                     " does not match  Device Nickname: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_duplex(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortDuplex"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Duplex: " + arg_dict['the_value'] + " matches the Port Duplex: " +
                                     column_value + " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Duplexe: " + arg_dict['the_value'] +
                                     " does not match  Port Duplex: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_auto_negotiation(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortAutoNegotiation"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Auto Negotiation: " + arg_dict['the_value'] +
                                     " matches the Auto Negotiation: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Auto Negotiation: " + arg_dict['the_value'] +
                                     " does not match  Auto Negotiation: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_speed(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortConfigSpeed"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Configuration Speed: " + arg_dict['the_value'] +
                                     " matches the Port Configuration Speed: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Configuration Speed: " + arg_dict['the_value'] +
                                     " does not match Port Configuration Speed: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_configuration(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsRole"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Configuration: " + arg_dict['the_value'] +
                                     " matches the Port Configuration: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Configuration: " + arg_dict['the_value'] +
                                     " does not match Port Configuration: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_lag(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceLagMembership"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port LAG Configuration: " + arg_dict['the_value'] +
                                     " matches the Port LAG Configuration: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port LAG Configuration: " + arg_dict['the_value'] +
                                     " does not match  Port LAG Configuration: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_policy(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "devicePolicyRole"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Policy Role: " + arg_dict['the_value'] +
                                     " matches the Port Policy Role: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Policy Role: " + arg_dict['the_value'] +
                                     " does not match Port Policy Role: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_node_alias(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortNodeAlias"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Node Alias: " + arg_dict['the_value'] +
                                     " matches the Port Node Alias: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Node Alias: " + arg_dict['the_value'] +
                                     " does notPort Node Alias: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_span_guard(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortSpanGuard"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Span Guard : " + arg_dict['the_value'] +
                                     " matches the Port Span Guard: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Span Guard: " + arg_dict['the_value'] +
                                     " does not Port Span Guard: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_port_loop_protect(self, ui_cmd_obj, arg_dict):
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
                                       row_index, "deviceDetailsPortLoopProtect"))

            if column_value == str(arg_dict["the_value"]):
                self.logger.log_info("Confirmed Port Loop Protect: " + arg_dict['the_value'] +
                                     " matches the Port Loop Protect: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = False
            else:
                self.logger.log_info("Confirmed  Port Loop Protect: " + arg_dict['the_value'] +
                                     " does not Port Loop Protect: " + column_value +
                                     " within the Device Ports table row: " + str(arg_dict["port_id"]))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_confirm_device_ztp_serial_number(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=serialNumber]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Serial Number: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Serial Number: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_ip_address_subnet(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=ipAddress]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                r"The Device IP Address\Subnet: " + ui_cmd_obj.return_data + r" does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                r"The Device IP Address\Subnet: " + ui_cmd_obj.return_data + r" does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_gateway_address(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=gateway]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Gateway: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Gateway: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_management_interface(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=mgmtInterface]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Management Interface: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Management Interface: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_domain_name(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=ztpDomainName]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device Domain Name: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device Domain Name: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_dns_server(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=dnsServer]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device DNS Value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device DNS Value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_ntp_server(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=ntpServer]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            ui_cmd_obj.error_state = False
            self.logger.log_info(
                "The Device NTP Value: " + ui_cmd_obj.return_data + " does match the value provided: " +
                str(arg_dict["the_value"]))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(
                "The Device NTP Value: " + ui_cmd_obj.return_data + " does not match the value provided: " +
                str(arg_dict["the_value"]))

        return ui_cmd_obj

    def devices_confirm_device_ztp_lacp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=lacp]", "[0].rawValue")

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            checkbox_fail = False
            self.logger.log_info(
                "The Device LACP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does match the value provided: " + str(
                    arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device LACP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does not match the value provided: " + str(
                    arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=lacpLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device LACP Value: " + ui_cmd_obj.return_data + " does match the value provided: " + str(
                    arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device LACP Value: " + ui_cmd_obj.return_data + " does not match the value provided: " + str(
                    arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_lldp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=lldp]", "[0].rawValue")

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            checkbox_fail = False
            self.logger.log_info(
                "The Device LLDP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does match the value provided: " + str(
                    arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device LLDP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does not match the value provided: " + str(
                    arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "deviceDetailsPanel textfield[name=lldpLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device LLDP Value: " + ui_cmd_obj.return_data + " does match the value provided: " + str(
                    arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device LLDP Value: " + ui_cmd_obj.return_data + " does not match the value provided: " + str(
                    arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_mstp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=spanningTree]", "[0].rawValue")

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            checkbox_fail = False
            self.logger.log_info(
                "The Device MSTP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does match the value provided: " + str(
                    arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device MSTP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does not match the value provided: " + str(
                    arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceDetailsPanel textfield[name=spanningTreeLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device MSTP Value: " + ui_cmd_obj.return_data + " does match the value provided: " + str(
                    arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device MSTP Value: " + ui_cmd_obj.return_data + " does not match the value provided: " + str(
                    arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_mvrp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=mvrp]", "[0].rawValue")

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            checkbox_fail = False
            self.logger.log_info(
                "The Device MVRP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does match the value provided: " + str(
                    arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device MVRP Checkbox Value: " + str(
                    ui_cmd_obj.return_data) + " does not match the value provided: " + str(
                    arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceDetailsPanel textfield[name=mvrpLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device MVRP Value: " + ui_cmd_obj.return_data + " does match the value provided: " + str(
                    arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device MVRP Value: " + ui_cmd_obj.return_data + " does not match the value provided: " + str(
                    arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_poe(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=poe]", "[0].rawValue")
        is_enabled = arg_dict["is_enabled"]
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(is_enabled.lower()):
            checkbox_fail = False
            self.logger.log_info(
                "The Device POE Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does match the value provided: " + str(arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device POE Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does not match the value provided: " + str(arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceDetailsPanel textfield[name=poeLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device POE Value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device POE Value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_xvlan(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=vxlan]", "[0].rawValue")
        is_enabled = arg_dict["is_enabled"]
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(is_enabled.lower()):
            checkbox_fail = False
            self.logger.log_info(
                "The Device VXLAN Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does match the value provided: " + str(arg_dict["is_enabled"]))
        else:
            checkbox_fail = True
            self.logger.log_info(
                "The Device VXLAN Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does not match the value provided: " + str(arg_dict["is_enabled"]))

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceDetailsPanel textfield[name=vxlanLogging]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data == str(arg_dict["the_value"]):
            object_fail = False
            self.logger.log_info(
                "The Device VXLAN Value: " + ui_cmd_obj.return_data +
                " does match the value provided: " + str(arg_dict["the_value"]))
        else:
            object_fail = True
            self.logger.log_info(
                "The Device VXLAN Value: " + ui_cmd_obj.return_data +
                " does not match the value provided: " + str(arg_dict["the_value"]))

        if checkbox_fail or object_fail:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_device_ztp_configure_device(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=ztpConfigEnable]", "[0].rawValue")

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            self.logger.log_info(
                "The ZTP Configure Device Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does match the value provided: " + str(arg_dict["is_enabled"]))
        else:

            self.logger.log_info(
                "The ZTP Configure Device Checkbox Value: " + str(ui_cmd_obj.return_data) +
                " does not match the value provided: " + str(arg_dict["is_enabled"]))
        return ui_cmd_obj

    def devices_confirm_device_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Devices, self).devices_confirm_device_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def devices_confirm_device_ip_archived(self, ui_cmd_obj, arg_dict):
        arg_dict2 = {'device_ip': arg_dict['device_ip'],
                     'col_name': 'Archived',
                     'the_value': arg_dict['the_value']}
        self.devices_confirm_table_value(ui_cmd_obj, arg_dict2)

        return ui_cmd_obj

    def devices_confirm_device_is_collecting_statistics(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]',
                                                          '[0]', 'ip', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                             'deviceGrid[viewId=DeviceTable]',
                                             '[0].store.data.items[' + str(row_index) + '].data.collectionStatus')
            # A value of "0" (disabled) is not collecting
            if ui_cmd_obj.return_data == "0":
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is not collecting statistics.\n")
                if arg_dict['the_value'] is True:
                    ui_cmd_obj.error_state = False
            # A non-zero value ("2" is historical, "4" is monitored) is collecting
            else:
                self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' is collecting statistics.\n")
                if arg_dict['the_value'] is False:
                    ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_confirm_table_value(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.get_component_index(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]',
                                                          '[0]', 'ip', arg_dict['device_ip'])
        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            col_name = arg_dict['col_name']
            self.get_column_attribute(ui_cmd_obj, col_name)
            col_attr = ui_cmd_obj.return_data
            if col_attr != "":
                # Determine which type of data this column holds (string, boolean, or integer)
                self.get_column_type(ui_cmd_obj, col_name)
                col_type = ui_cmd_obj.return_data

                # Get the column's value
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'deviceGrid[viewId=DeviceTable]',
                                                 '[0].store.data.items[' + str(row_index) + '].data.' + col_attr)
                row_value = ui_cmd_obj.return_data
                expected_value = arg_dict['the_value']

                if col_type == "boolean":
                    if row_value is StringUtils.string_to_boolean(expected_value):
                        self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nDevice '" + arg_dict['device_ip'] + "' does not have expected value '" + expected_value +
                            "' for column '" + col_name + "'. The row value is '" + str(row_value) + "'.\n")
                        ui_cmd_obj.error_state = True
                elif col_type == "integer":
                    if row_value == int(expected_value):
                        self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nDevice '" + arg_dict['device_ip'] + "' does not have expected value '" + expected_value +
                            "' for column '" + col_name + "'. The row value is '" + str(row_value) + "'.\n")
                        ui_cmd_obj.error_state = True
                else:
                    if row_value == expected_value:
                        self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' has expected value '" +
                                             expected_value + "' for column '" + col_name + "'.")
                    else:
                        self.logger.log_info(
                            "\nDevice '" + arg_dict['device_ip'] + "' does not have expected value '" + expected_value +
                            "' for column '" + col_name + "'. The row value is '" + str(row_value) + "'.\n")
                        ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nColumn '" + col_name + "' did not map to a known column attribute.\n")
                ui_cmd_obj.error_state = True

        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' was not found in the table.\n")

        return ui_cmd_obj

    def devices_configure_device_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel tab[text=" + arg_dict['tab_name'] +
                               "] => .x-tab-inner")
        return ui_cmd_obj

    def devices_configure_vlan_definition_add_vlan(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#deviceVlanGrid{isVisible()} => .add')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_name'],
                                    'textfield[name=deviceDetailsVlanName] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_id'], "numberfield[name=deviceDetailsVid] => "
                                                                     ".x-form-text")
        self.ext_builder.click(ui_cmd_obj, '#update{isVisible()} => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_configure_vlan_definition_delete_vlan(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'deviceDetailsPanel #deviceVlanGrid gridview => '
                                           '.x-grid-cell-inner:textEquals(' + arg_dict['vlan_name'] + ')')
        self.ext_builder.click(ui_cmd_obj, '#deviceVlanGrid{isVisible()} => .delete')

        return ui_cmd_obj

    def devices_configure_enforce_preview(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Enforce Preview...] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_configure_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '>>editDeviceDataWindow[name=editDeviceDataWindow] button[text=Cancel]')

        return ui_cmd_obj

    def devices_configure_compare_device_config_enforce_options(self, ui_cmd_obj, arg_dict):
        if arg_dict['enforce_option'].lower() == 'vlan definition':
            self.ext_builder.click(ui_cmd_obj, 'checkbox[name = enforceVlan] => .x-form-cb-input')
        if arg_dict['enforce_option'].lower() == 'port vlan':
            self.ext_builder.click(ui_cmd_obj, 'checkbox[name=enforcePortVlan] => .x-form-cb-input')
        return ui_cmd_obj

    def devices_configure_compare_device_config_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'tab[text=' + arg_dict['tab_name'] + '] => .x-tab-inner')

        return ui_cmd_obj

    def devices_configure_compare_device_config_enforce(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Enforce] => .x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_configure_compare_device_config_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'compareDeviceDataWindow[name=compareDeviceDataWindow] '
                                           'button[text=Refresh] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_configure_compare_device_config_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'compareDeviceDataWindow[name=compareDeviceDataWindow] '
                                           'button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def devices_configure_compare_device_config_verify_device_parameters(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "grid[name=compareDeviceDataWindow_editDeviceSelection] gridview",
                                             '[0].store.data.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['ip_address'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "grid[name=compareDeviceDataWindow_editDeviceSelection] gridview",
                                                     '[0].store.data.items[' + str(item) + '].data.ipAddress')
                    if arg_dict['ip_address'] != ui_cmd_obj.return_data:
                        match = False
                        item += 1
                        continue

                if arg_dict['status_action'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "grid[name=compareDeviceDataWindow_editDeviceSelection] gridview",
                                                     '[0].store.data.items[' + str(item) + '].data.action')
                    if arg_dict['status_action'].lower() not in ui_cmd_obj.return_data.lower():
                        match = False
                        item += 1
                        continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    # Helper Methods

    def get_column_attribute(self, ui_cmd_obj, col_name):
        ui_cmd_obj.return_data = ""

        if col_name == "Admin Profile":
            ui_cmd_obj.return_data = "adminProfileName"
        elif col_name == "Archived":
            ui_cmd_obj.return_data = "archived"
        elif col_name == "Asset Tag":
            ui_cmd_obj.return_data = "assetTag"
        elif col_name == "Client Profile":
            ui_cmd_obj.return_data = "clientProfileName"
        elif col_name == "Config Changed":
            ui_cmd_obj.return_data = "cfgChanged"
        elif col_name == "Contact":
            ui_cmd_obj.return_data = "sysContact"
        elif col_name == "Context":
            ui_cmd_obj.return_data = "snmpContext"
        elif col_name == "Description":
            ui_cmd_obj.return_data = "sysDescriptor"
        elif col_name == "Device Type":
            ui_cmd_obj.return_data = "deviceDisplayType"
        elif col_name == "Display Name":
            ui_cmd_obj.return_data = "deviceDisplayName"
        elif col_name == "Family":
            ui_cmd_obj.return_data = "deviceDisplayFamily"
        elif col_name == "Firmware":
            ui_cmd_obj.return_data = "firmware"
        elif col_name == "IP Address":
            ui_cmd_obj.return_data = "ip"
        elif col_name == "Location":
            ui_cmd_obj.return_data = "sysLocation"
        elif col_name == "Name":
            ui_cmd_obj.return_data = "deviceName"
        elif col_name == "Nickname":
            ui_cmd_obj.return_data = "nickname"
        elif col_name == "Notes":
            ui_cmd_obj.return_data = "note"
        elif col_name == "Policy Domain":
            ui_cmd_obj.return_data = "policyDomain"
        elif col_name == "Poll Group Name":
            ui_cmd_obj.return_data = "pollGroupName"
        elif col_name == "Poll Type":
            ui_cmd_obj.return_data = "pollType"
        elif col_name == "Reference":
            ui_cmd_obj.return_data = "refFirmware"
        elif col_name == "Serial Number":
            ui_cmd_obj.return_data = "chassisId"
        elif col_name == "Stats":
            ui_cmd_obj.return_data = "collectionStatus"
        elif col_name == "Status":
            ui_cmd_obj.return_data = "status"
        elif col_name == "Syslog Status":
            ui_cmd_obj.return_data = "deviceSysLogStatus"
        elif col_name == "System Name":
            ui_cmd_obj.return_data = "sysName"
        elif col_name == "Trap Status":
            ui_cmd_obj.return_data = "deviceTrapStatus"
        elif col_name == "User Data 1":
            ui_cmd_obj.return_data = "userData1"
        elif col_name == "User Data 2":
            ui_cmd_obj.return_data = "userData2"
        elif col_name == "User Data 3":
            ui_cmd_obj.return_data = "userData3"
        elif col_name == "User Data 4":
            ui_cmd_obj.return_data = "userData4"

        return ui_cmd_obj

    def get_column_type(self, ui_cmd_obj, col_name):
        ui_cmd_obj.return_data = "string"

        if col_name == "Archived":
            ui_cmd_obj.return_data = "boolean"
        elif col_name == "Config Changed":
            ui_cmd_obj.return_data = "boolean"
        elif col_name == "Reference":
            ui_cmd_obj.return_data = "boolean"
        elif col_name == "Status":
            ui_cmd_obj.return_data = "integer"

        return ui_cmd_obj

    def devices_get_table(self, ui_cmd_obj, target, row_index, column_name):
        self.ext_builder.component_query(ui_cmd_obj, target,
                                         '[0].store.data.items[' + str(row_index) + '].data.' + column_name)
        return ui_cmd_obj.return_data

    def devices_get_table_row_index(self, ui_cmd_obj, target, column_name, the_value):
        self.logger.log_info("The value to look for: " + the_value + ".")
        self.ext_builder.component_query(ui_cmd_obj, target, '[0].store.data.items.length')

        try:
            item_count = int(ui_cmd_obj.return_data)
        except ValueError:
            self.logger.log_error("Return data is empty. Therefore this keyword will not work.")
            item_count = 0

        self.logger.log_info("The table contains : " + str(item_count) + " rows.")
        item_count += 1
        item_index = 0
        for item_index in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj, target,
                                             '[0].store.data.items[' + str(item_index) + '].data.' + column_name)
            self.logger.log_info(
                "The table row contains : " + str(ui_cmd_obj.return_data) + " in column: " + column_name)
            if str(ui_cmd_obj.return_data) == str(the_value):
                self.logger.log_info("The row index returned: " + str(item_index + 1))
                break
            else:
                item_index = -1
        return item_index

    def devices_get_checkbox_value(self, ui_cmd_obj, target):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, target, '[0].rawValue')
        return ui_cmd_obj.return_data

    def devices_edit_device_ports_edit_row_clear_tagged(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Devices, self).devices_edit_device_ports_edit_row_clear_tagged(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def devices_edit_device_ports_edit_row_clear_untagged(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Devices, self).devices_edit_device_ports_edit_row_clear_untagged(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
