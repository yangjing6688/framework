from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as FirmwareBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Firmware(FirmwareBase):

    def firmware_tab_tree_expand_node(self, ui_cmd_obj, arg_dict):
        # Figure out how many items are in the tree
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkFirmwareTab '
                                                      'firmwareTree[title=Firmware] treeview',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Loop through the items, searching for the option to expand
        item_index = 0
        for x in range(0, item_count):
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#networkTabPanel #networkFirmwareTab '
                                                          'firmwareTree[title=Firmware] treeview',
                                                          '[0].store.data.items[' + str(item_index) + '].data["text"]')
            if ui_cmd_obj.return_data == arg_dict['node_name']:
                # Check if the node is already expanded or not - we only want to double click it if it is not expanded
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#networkTabPanel #networkFirmwareTab '
                                                              'firmwareTree[title=Firmware] treeview',
                                                              '[0].store.data.items[' + str(item_index) +
                                                              '].data["expanded"]')
                if ui_cmd_obj.return_data is False:
                    # The node isn't expanded yet, so double click it to expand it
                    self.ext_builder.double_click(ui_cmd_obj,
                                                  '#networkTabPanel #networkFirmwareTab firmwareTree[title=Firmware] '
                                                  'treeview => .x-tree-node-text:contains(' + arg_dict['node_name'] +
                                                  ')')
                else:
                    self.logger.log_info("\nNode '" + arg_dict['node_name'] + "' is already expanded.\n")
                break
            else:
                item_index += 1

        return ui_cmd_obj

    def firmware_tab_tree_select_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkFirmwareTab treeview => .x-tree-node-text:contains(' +
                               arg_dict['node_name'] + ')')

        return ui_cmd_obj

    def firmware_tab_tree_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkFirmwareTab button[text=Refresh] => '
                               '.x-btn-inner-default-small')
        self.ext_builder.delay(ui_cmd_obj, "2000")

        return ui_cmd_obj

    def firmware_tab_tree_upload_file(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'>>#networkTabPanel #networkFirmwareTab button[text=Upload\.\.\.]')
        self.ext_builder.click(ui_cmd_obj, "radiofield[boxLabel=" + str(arg_dict['upload_type']) +
                                           "] => [data-ref='displayEl']")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['upload_dir']), 'textfield[name=subdir] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, 'button[text=Upload] => .x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, 'button[text=Close] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_tab_table_select_image(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkFirmwareTab firmwareGrid[viewId=Firmware_Details] '
                               'tableview => .x-grid-row :textEquals(' + str(arg_dict['image_name']) + ')')

        return ui_cmd_obj

    def firmware_tab_table_select_all_images(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkFirmwareTab '
                                                      'firmwareGrid[viewId=Firmware_Details] tableview',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkFirmwareTab '
                                               'firmwareGrid[viewId=Firmware_Details] tableview ' +
                                               '=> .x-grid-item:nth-of-type(1) :nth-of-type(3) .x-grid-cell-inner')
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkFirmwareTab firmwareGrid[viewId=Firmware_Details] '
                                   'tableview ' + '=> .x-grid-item:nth-of-type(' + str(item_count) +
                                   ') :nth-of-type(3) .x-grid-cell-inner', shift=True)
            self.logger.log_info("\nSelected " + str(item_count) + " rows.\n")
        else:
            self.logger.log_info("\nTable is empty.\n")

        return ui_cmd_obj

    def firmware_tab_menu_set_as_reference_image_table(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the table
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareGrid[viewId=Firmware_Details] '
                                     'tableview => .x-grid-row :textEquals(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, '#fwGridMenu menuitem[actionId=fwSetReferenceGrid] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_set_as_reference_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree[title=Firmware] => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Set as Reference Image] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_unset_as_reference_image_table(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the table
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareGrid[viewId=Firmware_Details] '
                                     'tableview => .x-grid-row :textEquals(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, '#fwGridMenu menuitem[actionId=fwUnSetReferenceGrid] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_unset_as_reference_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree[title=Firmware] => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Unset as Reference Image] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_delete_image_table(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the table
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareGrid[viewId=Firmware_Details] '
                                     'tableview => .x-grid-row :textEquals(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, '#fwGridMenu menuitem[actionId=fwDeleteGrid] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_delete_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree[title=Firmware] => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Delete Image] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_delete_all_images_from_table(self, ui_cmd_obj, arg_dict):
        # Check if table is empty
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkFirmwareTab '
                                                      'firmwareGrid[viewId=Firmware_Details] tableview',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)

        # Only delete if table is not empty
        if item_count > 0:
            # Select all images in the table
            self.firmware_tab_table_select_all_images(ui_cmd_obj, arg_dict)

            # Access the menu pick from the context menu of the first row in the table
            self.ext_builder.right_click(ui_cmd_obj,
                                         '#networkTabPanel #networkFirmwareTab '
                                         'firmwareGrid[viewId=Firmware_Details] tableview => '
                                         '.x-grid-row :nth-of-type(1)')
            self.ext_builder.click(ui_cmd_obj, '#fwGridMenu menuitem[actionId=fwDeleteGrid] => .x-menu-item-text')

            # Confirm the delete
            self.firmware_tab_dialog_confirm_delete_image_set_delete_from_server(ui_cmd_obj, arg_dict)
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDeleteWindow button[text=OK]{isVisible()} => .x-btn-inner-blue-small')
        # Do not attempt to delete since table is empty
        else:
            self.logger.log_info("\nTable is empty.\n")

        return ui_cmd_obj

    def firmware_tab_dialog_confirm_delete_image_set_delete_from_server(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Delete image from server?" check button, if it isn't already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#firmwareDeleteWindow checkbox[name=deleteFromServer]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["delete_from_server"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDeleteWindow checkbox[name=deleteFromServer] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Delete image from server?' check button already at desired value.\n")

        return ui_cmd_obj

    def firmware_tab_dialog_confirm_delete_image_click_ok(self, ui_cmd_obj, arg_dict):
        # Click OK to delete the image
        self.ext_builder.click(ui_cmd_obj,
                               '#firmwareDeleteWindow button[text=OK]{isVisible()} => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_tab_dialog_confirm_delete_image_click_cancel(self, ui_cmd_obj, arg_dict):
        # Click Cancel to not delete the image
        self.ext_builder.click(ui_cmd_obj,
                               '#firmwareDeleteWindow button[text=Cancel]{isVisible()} => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_menu_backup_configuration(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
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
                                   r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
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
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
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
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
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
            self.logger.log_info("\nTwo configuration files do not exist, so cannot perform comparison.\n")
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
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Upgrade Firmware...] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_set_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Set Configuration...] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_restart_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Restart Device...] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_menu_check_for_updates(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Check for Updates...] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#activeContextMenu{isVisible()} menuitem[text=Check for Updates...] => '
                               '.x-menu-item-text')

        self.ext_builder.wait_for_load_mask(ui_cmd_obj, '#fwUpdateLoadMask', '[0]', 60)
        return ui_cmd_obj

    def firmware_menu_view_available_releases(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\n******* TO DO: implement View Available Releases\n")
        # ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
        #                                               '#networkTabPanel #networkDevicesTab '
        #                                               '#devicesTreeContextTabPanel deviceGrid[viewId=DeviceTable]',
        #                                               '[0].store.data.items.length')
        # item_count = int(ui_cmd_obj.return_data)
        # item_count += 1
        # item_index = 0
        # found_item = False
        # for x in range(0,item_count):
        #     ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
        #                                                   '#networkTabPanel #networkDevicesTab '
        #                                                   '#devicesTreeContextTabPanel '
        #                                                   'deviceGrid[viewId=DeviceTable]',
        #                                                   '[0].store.data.items[' + str(item_index) + '].data.ip')
        #     if ui_cmd_obj.return_data == arg_dict['device_ip']:
        #         self.logger.log_info("FOUND DEVICE " + str(arg_dict['device_ip']) )
        #         found_item = True
        #         break
        #     else:
        #         item_index += 1
        #
        # if found_item is True:
        #     ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
        #                                                   '#networkTabPanel #networkDevicesTab '
        #                                                   '#devicesTreeContextTabPanel '
        #                                                   'deviceGrid[viewId=DeviceTable]',
        #                                                   '[0].store.data.items[' + str(item_index) +
        #                                                   '].data.firmwareStatus' )
        #     if ui_cmd_obj.return_data == "0":
        #         self.logger.log_info("UPDATES AVAILABLE FOR DEVICE" + str(arg_dict['device_ip']))
        #         # Access the menu pick from the context menu
        #         self.ext_builder.click(ui_cmd_obj,
        #                                '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
        #                                '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        #         self.ext_builder.click(ui_cmd_obj,
        #                                '#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
        #                                '.x-menu-item-text')
        #         self.ext_builder.move_cursor(ui_cmd_obj,
        #                                      '#activeContextMenu{isVisible()} menuitem[text=Check for Updates...] => '
        #                                      '.x-menu-item-text')
        #         self.ext_builder.click(ui_cmd_obj,
        #                                '#activeContextMenu{isVisible()} menuitem[text=View Available Releases...] => '
        #                                '.x-menu-item-text')
        #
        #         # TO DO: use wait for #fwUpdateLoadMask gone instead of the delay...
        #         # wait = True
        #         # while wait:
        #         #     cq_result = self.ext_builder.component_query(ui_cmd_obj, '#fwUpdateLoadMask', '')
        #         #     if cq_result is "":
        #         #         wait = False
        #         self.logger.log_info("****** TO DO: USE WAIT INSTEAD OF DELAY *****")
        #         self.ext_builder.delay(ui_cmd_obj, "10000")
        #     else:
        #         self.logger.log_info("NO UPDATES ARE AVAILABLE FOR DEVICE " + str(arg_dict['device_ip']))
        # else:
        #     self.logger.log_info("DID NOT FIND DEVICE " + str(arg_dict['device_ip']) )

        return ui_cmd_obj

    def firmware_menu_register_export_serial_numbers(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                               r'.x-menu-item-text')
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#activeContextMenu{isVisible()} menuitem[text=Backup Configuration] => '
                                     '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               r'#activeContextMenu{isVisible()} menuitem[text=Register/\Export Serial Numbers...] => '
                               r'.x-menu-item-text')

        return ui_cmd_obj

    def firmware_dialog_assign_image_set_show_all_images(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#FirmwareSelectionWindow #FirmwareSelectionGrid "
                                                      "checkbox[name=showAllImages]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['btn_state']):
            self.ext_builder.click(ui_cmd_obj,
                                   '#FirmwareSelectionWindow #FirmwareSelectionGrid checkbox[name=showAllImages] => '
                                   '.x-form-cb-input')
        else:
            self.logger.log_info("\n'Show All Images' check button already at desired state.\n")

        return ui_cmd_obj

    def firmware_dialog_assign_image_set_bootprom_download(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#FirmwareSelectionWindow #FirmwareSelectionGrid "
                                                      "checkbox[name=toggleBootpromDownload]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['btn_state']):
            self.ext_builder.click(ui_cmd_obj,
                                   '#FirmwareSelectionWindow #FirmwareSelectionGrid '
                                   'checkbox[name=toggleBootpromDownload] => .x-form-cb-input')
            self.ext_builder.click(ui_cmd_obj,
                                   '#yes => .x-btn-inner-blue-small')
        else:
            self.logger.log_info("\n'BootPROM Download' check button already at desired state.\n")

        return ui_cmd_obj

    def firmware_dialog_assign_image_select_image(self, ui_cmd_obj, arg_dict):
        # Determine if the imqage is in the table
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, '#FirmwareSelectionWindow #FirmwareSelectionGrid gridview',
                                                '[0]', 'firmwareNickName', arg_dict['image_name'], exact_match=False)
        if ui_cmd_obj.return_data is True:
            # It's in the table, so select it
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj,
                                   '#FirmwareSelectionWindow #FirmwareSelectionGrid tableview => ' +
                                   '.x-grid-cell-first .x-grid-cell-inner:contains(' + arg_dict['image_name'] + ')')
        else:
            # It's not in the table, so report the error
            self.logger.log_info("\nCould not find image '" + arg_dict['image_name'] + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def firmware_dialog_assign_image_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '>>#FirmwareSelectionWindow #FirmwareSelectionGrid button[text=Refresh Images]')
        self.ext_builder.wait_for_load_mask(ui_cmd_obj, 'loadmask[msg=Refreshing Firmware...]', '[0]', 60)

        return ui_cmd_obj

    def firmware_dialog_assign_image_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSelectionWindow button[text=OK] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_assign_image_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSelectionWindow button[name=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_compare_last_configs_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'configFileCompareWindow[title=Configuration File Compare] button[text=OK] => '
                               '.x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_configuration_set_file_transfer_mode(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdFTMcb => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdFTMcb boundlist => :textEquals(' +
                                           arg_dict['field_value'] + ')')

        return ui_cmd_obj

    def firmware_dialog_configuration_set_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdServercb => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdServercb boundlist => :textEquals(' +
                                           arg_dict['field_value'] + ')')

        return ui_cmd_obj

    def firmware_dialog_configuration_set_firmware_mib(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #firmMibcb => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #firmMibcb boundlist => :textEquals(' +
                                           arg_dict['field_value'] + ')')

        return ui_cmd_obj

    def firmware_dialog_configuration_set_configuration_mib(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #configMibcb => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #configMibcb boundlist => :textEquals(' +
                                           arg_dict['field_value'] + ')')

        return ui_cmd_obj

    def firmware_dialog_configuration_set_script_file_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdScriptcb => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow #fdScriptcb boundlist => :textEquals(' +
                                           arg_dict['field_value'] + ')')

        return ui_cmd_obj

    def firmware_dialog_configuration_click_view(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#FirmwareSettingsWindow button[actionId=viewDeviceFamilyScriptFile] => '
                               '.x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_configuration_view_click_ok(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.click(ui_cmd_obj,
                                            "window[title=" + arg_dict['script_name'] +
                                            "] button[text=OK] => .x-btn-button")

        return ui_cmd_obj

    def firmware_dialog_configuration_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow button[text=OK] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_configuration_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#FirmwareSettingsWindow button[name=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_current_firmware_releases_click_ok(self, ui_cmd_obj, arg_dict):
        # Handle the updates dialog
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'firmwareReleasesWindow[title=Current Firmware Releases]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.click(ui_cmd_obj,
                                   'firmwareReleasesWindow[title=Current Firmware Releases] button[text=OK] => '
                                   '.x-btn-inner-blue-small')
        else:
            # Handle the error dialog, which is displayed if the firmware update check failed
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Firmware Update Check Failed]',
                                                          '[0]')
            if ui_cmd_obj.return_data is not None:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              'messagebox[title=Firmware Update Check Failed]',
                                                              '[0].hidden')
                if ui_cmd_obj.return_data is False:
                    self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

            # Handle the message dialog stating no updates are available
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Check For Firmware Updates]',
                                                          '[0]')
            if ui_cmd_obj.return_data is not None:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              'messagebox[title=Check For Firmware Updates]',
                                                              '[0].hidden')
                if ui_cmd_obj.return_data is False:
                    self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_restart_confirm_timed_restart_supported(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#ResetDeviceWindow', '[0].title')
        if ui_cmd_obj.return_data == "Restart Devices - Timed Restart Supported":
            self.logger.log_info("\nTimed Restart Supported\n")
            if StringUtils.string_to_boolean(arg_dict['is_supported']) is True:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        elif ui_cmd_obj.return_data == "Restart Devices - Timed Restart Not Supported":
            self.logger.log_info("\nTimed Restart Not Supported\n")
            if StringUtils.string_to_boolean(arg_dict['is_supported']) is False:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nUnexpected Restart Devices dialog title '" + ui_cmd_obj.return_data + "'\n")

        return ui_cmd_obj

    def firmware_dialog_restart_set_show_devices_not_supporting_timed_restart(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#ResetDeviceWindow #ResetDeviceGrid "
                                                      "checkbox[name=showManualDevices]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['btn_state']):
            self.ext_builder.click(ui_cmd_obj,
                                   '#ResetDeviceWindow #ResetDeviceGrid checkbox[name=showManualDevices] => '
                                   '.x-form-cb-input')
        else:
            self.logger.log_info("\n'Show devices not supporting timed restart' check button is already at desired "
                                 "state.\n")

        return ui_cmd_obj

    def firmware_dialog_restart_set_device_selected(self, ui_cmd_obj, arg_dict):
        devices = arg_dict['device_list'].split(',')
        for device in devices:
            # Figure out how many items are in the table
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#ResetDeviceWindow #ResetDeviceGrid',
                                                          '[0].store.data.length')
            item_count = int(ui_cmd_obj.return_data)
            item_count += 1
            table_index = 1

            # Loop through the items, searching for the node to act on
            item_index = 0
            for x in range(0, item_count):
                table_index = item_index + 1
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#ResetDeviceWindow #ResetDeviceGrid',
                                                              '[0].store.data.items[' + str(item_index) + '].data.ip')
                if ui_cmd_obj.return_data == device:
                    # Check the current selection state of the node
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#ResetDeviceWindow #ResetDeviceGrid',
                                                                  '[0].store.data.items[' + str(item_index) +
                                                                  '].data.selected')
                    if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['btn_state']):
                        self.ext_builder.click(ui_cmd_obj,
                                               '#ResetDeviceWindow #ResetDeviceGrid gridview ' +
                                               '=> .x-grid-item:nth-of-type(' + str(table_index) +
                                               ') .x-grid-checkcolumn')
                    else:
                        self.logger.log_info("\nDevice '" + device + "' is already at desired selection state (" +
                                             arg_dict['btn_state'] + ").\n")
                    break
                else:
                    item_index += 1

        return ui_cmd_obj

    def firmware_dialog_restart_set_restart_time(self, ui_cmd_obj, arg_dict):
        # Enter the Date
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow #startDate => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['restart_date'],
                                    '#ResetDeviceWindow #startDate => .x-form-text')

        # Enter the Time
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow #startTime => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['restart_time'],
                                    '#ResetDeviceWindow #startTime => .x-form-text')

        return ui_cmd_obj

    def firmware_dialog_restart_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#ResetDeviceWindow #ResetDeviceGrid button[name=refreshDevices] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def firmware_dialog_restart_click_start(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow button[actionId=startResetDeviceAction] => '
                                           '.x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_restart_click_abort(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow button[actionId=startResetDeviceAction] => '
                                           '.x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_restart_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow button[text=Cancel] => .x-btn-inner-default-small')

        # Handle the confirmation dialog, which is displayed if the restart action was not performed
        self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Restart Devices]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Restart Devices]', '[0].hidden')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_restore_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "tab[text=" + arg_dict['tab_name'] + "] => .x-tab-inner")
        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_restore(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.logger.log_info("\nTO DO: check that the specified config to restore exists in the drop down.\n")
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] boundlist => ' +
                                               '.x-boundlist-item:textEquals(' + arg_dict['config_name'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_restore_newest(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] boundlist => '
                                               '.x-boundlist-item:nth-of-type(1)')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_restore_oldest(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Restore] boundlist => ' +
                                               '.x-boundlist-item:nth-of-type(' + str(item_count) + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_source_device(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[name=source]', '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj, 'combo[name=source] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=source] boundlist => ' +
                                               '.x-boundlist-item:contains(' + arg_dict['device_ip'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo devices available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_clone(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.logger.log_info("\nTO DO: check that the specified config to clone exists in the drop down.\n")
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] boundlist => ' +
                                               '.x-boundlist-item:textEquals(' + arg_dict['config_name'] + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_clone_newest(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] boundlist => ' +
                                               '.x-boundlist-item:nth-of-type(1)')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_configuration_to_clone_oldest(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone]',
                                                      '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Configuration to Clone] boundlist => ' +
                                               '.x-boundlist-item:nth-of-type(' + str(item_count) + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo configurations available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_template(self, ui_cmd_obj, arg_dict):
        # Get the number of items in the drop down
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'combo[name=templateName]', '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        if item_count > 0:
            ui_cmd_obj.error_state = False
            self.logger.log_info("\nTO DO: check that the specified template exists in the drop down.\n")
            self.ext_builder.click(ui_cmd_obj, 'combo[name=templateName] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=templateName] boundlist => ' +
                                               '.x-boundlist-item:nth-of-type(' + str(item_count) + ')')
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNo templates available to select.\n")

        return ui_cmd_obj

    def firmware_dialog_restore_select_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=temp_profile] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=temp_profile] boundlist => .x-boundlist-item:contains(' +
                                           str(arg_dict['profile_name']) + ')')

        return ui_cmd_obj

    def firmware_dialog_restore_click_start(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Start] => .x-btn-button')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def firmware_dialog_restore_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'loadConfigurationWindow button[actionId=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_click_register(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'RegExportSerialNumbersWindow button[text=Register] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_click_export_to_file(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#csvButton => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'RegExportSerialNumbersWindow button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_register_set_refresh(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#regSerialNumberWindowId checkbox[inputType=checkbox]",
                                                      "[0]")
        if ui_cmd_obj is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "#regSerialNumberWindowId checkbox[inputType=checkbox]",
                                                          "[0].rawValue")
            if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['btn_state']):
                self.ext_builder.click(ui_cmd_obj,
                                       '#regSerialNumberWindowId checkbox[inputType=checkbox] => .x-form-cb-input')
            else:
                self.logger.log_info("\n'Refresh the devices before registering' check button is already at desired "
                                     "state.\n")
        else:
            self.logger.log_info("\nCould not find 'Refresh the devices before registering' check button.\n")

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_register_click_register(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#regSerialNumberWindowId button[text=Register] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_serial_numbers_register_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#regSerialNumberWindowId button[text=Cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_select_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.clear_table_selection(ui_cmd_obj, '#firmwareDownloadWindow #FirmwareDownloadGrid tableview',
                                               '[0]')
        devices = arg_dict['device_list'].split(',')
        for device in devices:
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDownloadWindow #FirmwareDownloadGrid tableview => :textEquals(' +
                                   device + ')', ctrl=True)

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_assign_image(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#firmwareDownloadWindow #FirmwareDownloadGrid button[name=assignImage] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_set_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#firmwareDownloadWindow #FirmwareDownloadGrid button[name=setConfig] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_restart_devices_after_upgrade(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Restart Devices After Upgrade" check button, if it isn't already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#firmwareDownloadWindow checkbox[name=resetDeviceBtn]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["field_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDownloadWindow checkbox[name=resetDeviceBtn] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Restart Devices After Upgrade' check button is already at desired state.\n")

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_schedule_upgrade(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Schedule Upgrade" check button, if it isn't already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#firmwareDownloadWindow checkbox[name=schedUpgrade]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["field_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDownloadWindow checkbox[name=schedUpgrade] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Schedule Upgrade' check button is already at desired state.\n")

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_schedule_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['field_value']),
                                    '#firmwareDownloadWindow textfield[name=schedName] => .x-form-text')

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_schedule_date_time(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_date']),
                                    '#firmwareDownloadWindow #startDate => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_time']),
                                    '#firmwareDownloadWindow #startTime => .x-form-text')

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_schedule_abort_on_failure(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Abort on Failure" check button, if it isn't already at the desired state
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#firmwareDownloadWindow checkbox[name=abortFail]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["field_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareDownloadWindow checkbox[name=abortFail] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Abort on Failure' check button is already at desired state.\n")

        return ui_cmd_obj

    def firmware_dialog_upgrade_set_device_upgrade_group_size(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['field_value']),
                                    '#firmwareDownloadWindow numberfield[name=groupsOf] => .x-form-text')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_schedule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#firmwareDownloadWindow button[name=startAbort] => .x-btn-button')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_start(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#firmwareDownloadWindow button[name=startAbort] => .x-btn-button')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#firmwareDownloadWindow button[name=finishFirmBtn] => '
                                           '.x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_close(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#firmwareDownloadWindow button[name=finishFirmBtn] => '
                                           '.x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_confirm_start_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_confirm_start_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_wait_for_completion(self, ui_cmd_obj, arg_dict):
        # Make sure the Overall Progress field is being displayed (it is located in the 'Upgrade Status' panel
        # in the Upgrade Firmware dialog once an upgrade has been started).
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#overallFieldId', '[0]')
        if ui_cmd_obj.return_data is not None:
            # Wait until the "Overall Progress" is 100%
            self.ext_builder.wait_for_attribute(ui_cmd_obj, '#overallFieldId', '[0].text', '100%',
                                                int(arg_dict['wait_time']))
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\n'Overall Progress' field is not displayed.\n")
            self.logger.log_info("Make sure the Upgrade Firmware dialog is open and the upgrade has been started.\n")

        return ui_cmd_obj

    def firmware_confirm_config_fw_menu_exists(self, ui_cmd_obj, arg_dict):
        # Check if the context menu has been built yet
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu', '[0]')
        if ui_cmd_obj.return_data is None:
            # Context menu has not been built yet, so display it then hide it so we can query the menu picks
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
            self.ext_builder.click(ui_cmd_obj,
                                   r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                                   r'.x-menu-item-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel tab[text=Devices] '
                                   '=> .x-tab-inner-extr-sec-tab-panel')

        # Check if the specified menu is present - the query returns True if the menu is HIDDEN
        self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu menuitem[text=' + arg_dict["menu_name"] + ']',
                                         '[0].hidden')

        # Pass or fail the test, based on what was expected (query info is true if the menu is HIDDEN)
        if ui_cmd_obj.return_data == 'Component query returned a value that could not be converted by selenium.':
            ui_cmd_obj.return_data = True
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def firmware_confirm_config_fw_menu_enabled(self, ui_cmd_obj, arg_dict):
        # Check if the context menu has been built yet
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu', '[0]')
        if ui_cmd_obj.return_data is None:
            # Context menu has not been built yet, so display it then hide it so we can query the menu picks
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
            self.ext_builder.click(ui_cmd_obj,
                                   r'#activeContextMenu{isVisible()} menuitem[text=Configuration\/Firmware] => '
                                   r'.x-menu-item-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel tab[text=Devices] '
                                   '=> .x-tab-inner-extr-sec-tab-panel')

        # Check if the specified menu is enabled - the query returns True if the menu is DISABLED
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#activeContextMenu menuitem[text=' + arg_dict["menu_name"] + ']',
                                                      '[0].disabled')

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nMenu '" + arg_dict['menu_name'] + "' is disabled.\n")
        else:
            self.logger.log_info("\nMenu '" + arg_dict['menu_name'] + "' is enabled.\n")

        # Pass or fail the test, based on what was expected (query info is true if the menu is DISABLED)
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["is_enabled"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def firmware_confirm_upgrade_success(self, ui_cmd_obj, arg_dict):
        # Find the index of the device to check
        self.ext_builder.get_component_index(ui_cmd_obj, '#firmwareDownloadWindow #FirmwareDownloadGrid tableview',
                                             '[0]', 'ip', arg_dict['device_ip'])

        if ui_cmd_obj.return_data is not None and ui_cmd_obj.return_data != -1:
            row_index = ui_cmd_obj.return_data
            # Check the upgrade status
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#firmwareDownloadWindow #FirmwareDownloadGrid tableview',
                                                          '[0].store.data.items[' + str(row_index) + '].data.status')

            # Log the result
            self.logger.log_info("\nUpgrade status: '" + ui_cmd_obj.return_data + "'.\n")

            # Pass or fail the test, based on what was expected
            if ui_cmd_obj.return_data == "Success" and StringUtils.string_to_boolean(arg_dict["is_success"] is True):
                # PASS
                ui_cmd_obj.error_state = False
            elif ui_cmd_obj.return_data != "Success" and StringUtils.string_to_boolean(arg_dict["is_success"] is False):
                # PASS
                ui_cmd_obj.error_state = False
            else:
                # FAIL
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' was not found in Upgrade Firmware dialog.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
