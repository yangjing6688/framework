from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.FirmwareConstants import FirmwareConstants


class UiFirmwareKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiFirmwareKeywords, self).__init__()
        self.api_const = self.constants.API_FIRMWARE
        self.cmd = FirmwareConstants()

    def firmware_tab_tree_expand_node(self, element_name, node_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [node_name] -     Name of the tree node to expand

        Expands the specified node in the firmware tree.
        """
        args = {"node_name": node_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_TREE_EXPAND_NODE, **kwargs)

    def firmware_tab_tree_select_node(self, element_name, node_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [node_name] -     Name of the tree node to select

        Selects the specified node in the firmware tree.
        """
        args = {"node_name": node_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_TREE_SELECT_NODE, **kwargs)

    def firmware_tab_tree_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Refresh" button under the firmware tree.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_TAB_TREE_REFRESH, **kwargs)

    def firmware_tab_tree_upload_file(self, element_name, upload_file, upload_type, upload_dir, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [upload_file] -   Name of the file to upload
        [upload_type] -   Type of upload (TFTP, FTP, SCP, SFTP)
        [upload_dir] -    Name of the sub directory to place the uploaded files in

        Clicks the "Upload" button under the firmware tree to display and populate the Upload Firmware To Server dialog.
        """
        args = {"upload_dir": upload_dir,
                "upload_type": upload_type,
                "upload_file": upload_file}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_TREE_UPLOAD_FILE, **kwargs)

    def firmware_tab_table_select_image(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select in the table

        Selects the specified image in the firmware table.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_TABLE_SELECT_IMAGE, **kwargs)

    def firmware_tab_table_select_all_images(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects all images currently displayed in the firmware table.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_TAB_TABLE_SELECT_ALL_IMAGES, **kwargs)

    def firmware_tab_menu_set_as_reference_image_table(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select in the table

        Rights clicks the specified image in the firmware table and selects "Set as Reference Image" from the context
        menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_SET_AS_REFERENCE_IMAGE_TABLE,
                                    **kwargs)

    def firmware_tab_menu_set_as_reference_image_tree(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select in the tree

        Rights clicks the specified image in the firmware tree and selects "Set as Reference Image" from the context
        menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_SET_AS_REFERENCE_IMAGE_TREE,
                                    **kwargs)

    def firmware_tab_menu_unset_as_reference_image_table(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select in the table

        Rights clicks the specified image in the firmware table and selects "Set as Reference Image" from the context
        menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_UNSET_AS_REFERENCE_IMAGE_TABLE,
                                    **kwargs)

    def firmware_tab_menu_unset_as_reference_image_tree(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select in the tree

        Rights clicks the specified image in the firmware tree and selects "Set as Reference Image" from the context
        menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_UNSET_AS_REFERENCE_IMAGE_TREE,
                                    **kwargs)

    def firmware_tab_menu_delete_image_tree(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] -      List of elements the keyword will be run against
        [image_name] -         Name of the image to delete
        [delete_from_server] - Indicates whether or not the "Delete image from server" check button should be selected
                               (True/False)

        Accesses the context menu for the specified image in the firmware tree and selects "Delete Image" from the
        context menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_DELETE_IMAGE_TREE, **kwargs)

    def firmware_tab_menu_delete_image_table(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] -      List of elements the keyword will be run against
        [image_name] -         Name of the image to delete
        [delete_from_server] - Indicates whether or not the "Delete image from server" check button should be selected
                               (True/False)

        Accesses the context menu for the specified image in the firmware table and selects "Delete Image" from the
        context menu.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_MENU_DELETE_IMAGE_TABLE, **kwargs)

    def firmware_tab_delete_all_images_from_table(self, element_name, delete_from_server, **kwargs):
        """
        Keyword Arguments:
        [element_names] -      List of elements the keyword will be run against
        [delete_from_server] - Indicates whether or not the "Delete image from server" check button should be selected
                               (True/False)

        Selects all images in the firmware table and selects "Delete Image" from the context menu.
        """
        args = {"delete_from_server": delete_from_server}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_TAB_DELETE_ALL_IMAGES_FROM_TABLE, **kwargs)

    def firmware_tab_dialog_confirm_delete_image_set_delete_from_server(self, element_name, delete_from_server,
                                                                        **kwargs):
        """Returns the result of firmware_tab_dialog_confirm_delete_image_set_delete_from_server."""
        args = {"delete_from_server": delete_from_server}

        return self.execute_keyword(element_name, args,
                                    self.cmd.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_SET_DELETE_FROM_SERVER, **kwargs)

    def firmware_tab_dialog_confirm_delete_image_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the "Delete Image" confirmation dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_CLICK_OK,
                                    **kwargs)

    def firmware_tab_dialog_confirm_delete_image_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the "Delete Image" confirmation dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_CLICK_CANCEL,
                                    **kwargs)

    def firmware_menu_backup_configuration(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Backup Configuration" from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_BACKUP_CONFIGURATION, **kwargs)

    def firmware_menu_restore_configuration(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Restore Configuration..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_RESTORE_CONFIGURATION, **kwargs)

    def firmware_menu_compare_last_configurations(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Compare Last Configurations..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_COMPARE_LAST_CONFIGURATIONS, **kwargs)

    def firmware_menu_upgrade_firmware(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Upgrade Firmware..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_UPGRADE_FIRMWARE, **kwargs)

    def firmware_menu_set_configuration(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Set Configuration..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_SET_CONFIGURATION, **kwargs)

    def firmware_menu_restart_device(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Restart Device..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_RESTART_DEVICE, **kwargs)

    def firmware_menu_check_for_updates(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Check for Updates..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_CHECK_FOR_UPDATES, **kwargs)

    def firmware_menu_view_available_releases(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "View Available Releases..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_VIEW_AVAILABLE_RELEASES, **kwargs)

    def firmware_menu_register_export_serial_numbers(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects "Register/Export Serial Numbers..." from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_MENU_REGISTER_EXPORT_SERIAL_NUMBERS, **kwargs)

    def firmware_dialog_assign_image_set_show_all_images(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether or not the "Show All Images" check button should be selected (True/False)

        Sets the value of the "Show All Images" check button in the Firmware Selection dialog, which is accessed by
        clicking "Assign Image" in the Upgrade Firmware dialog.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_SET_SHOW_ALL_IMAGES,
                                    **kwargs)

    def firmware_dialog_assign_image_set_bootprom_download(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Indicates whether or not the "BootPROM Download" check button should be selected (True/False)

        Sets the value of the "BootPROM Download" check button in the Firmware Selection dialog, which is accessed by
        clicking "Assign Image" in the Upgrade Firmware dialog.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_SET_BOOTPROM_DOWNLOAD,
                                    **kwargs)

    def firmware_dialog_assign_image_select_image(self, element_name, image_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [image_name] -    Name of the image to select

        Selects the specified image in the Firmware Selection dialog, which is accessed by clicking "Assign Image" in
        the Upgrade Firmware dialog.
        """
        args = {"image_name": image_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_SELECT_IMAGE, **kwargs)

    def firmware_dialog_assign_image_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Refresh Images" in the Firmware Selection dialog, which is accessed by clicking "Assign Image" in
        the Upgrade Firmware dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_REFRESH, **kwargs)

    def firmware_dialog_assign_image_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "OK" in the Firmware Selection dialog, which is accessed by clicking "Assign Image" in
        the Upgrade Firmware dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_OK, **kwargs)

    def firmware_dialog_assign_image_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "Cancel" in the Firmware Selection dialog, which is accessed by clicking "Assign Image" in
        the Upgrade Firmware dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_CANCEL, **kwargs)

    def firmware_dialog_compare_last_configs_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "OK" in the Configuration File Compare dialog, which is accessed by selecting
        "Compare Last Configurations" from the device context menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_COMPARE_LAST_CONFIGS_CLICK_OK, **kwargs)

    def firmware_dialog_current_firmware_releases_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the Current Firmware Releases dialog, which is accessed from the Check for Updates and View
        Available Releases menu picks from the device context Configuration/Firmware menu.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_CURRENT_FIRMWARE_RELEASES_CLICK_OK,
                                    **kwargs)

    def firmware_dialog_restart_confirm_timed_restart_supported(self, element_name, is_supported, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_supported] -  Indicates if timed restart is expected to be supported or not (True/False)

        Confirms if the Restart Device dialog supports timed restart or not, depending on what is expected based on the
        "is_supported" argument passed in.
        It is assumed the Restart Device dialog is already displayed.
        """
        args = {"is_supported": is_supported}

        return self.execute_keyword(element_name, args,
                                    self.cmd.FIRMWARE_DIALOG_RESTART_CONFIRM_TIMED_RESTART_SUPPORTED, **kwargs)

    def firmware_dialog_restart_set_show_devices_not_supporting_timed_restart(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -     Selection state of the "Show Devices Not Supporting Timed Restart" check button (True/False)

        Sets the state of the "Show Devices Not Supporting Timed Restart" check button in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args,
                                    self.cmd.FIRMWARE_DIALOG_RESTART_SET_SHOW_DEVICES_NOT_SUPPORTING_TIMED_RESTART,
                                    **kwargs)

    def firmware_dialog_restart_set_device_selected(self, element_name, device_list, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_list] -   List of devices to set the selection state on
        [btn_state] -     Selection state of the specified devices (True/False)

        Sets the state of the "Selected" check button in the Restart Device dialog for the specified list of devices.
        It is assumed the Restart Device dialog is already displayed.
        """
        args = {"btn_state": btn_state,
                "device_list": device_list}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTART_SET_DEVICE_SELECTED, **kwargs)

    def firmware_dialog_restart_set_restart_time(self, element_name, restart_date, restart_time, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [restart_date] -  Date the restart should be performed
        [restart_time] -  Time the restart should be performed

        Sets the date and time values for the "Restart Time" field in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        args = {"restart_time": restart_time,
                "restart_date": restart_date}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTART_SET_RESTART_TIME, **kwargs)

    def firmware_dialog_restart_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Refresh Devices" toolbar button in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTART_CLICK_REFRESH, **kwargs)

    def firmware_dialog_restart_click_start(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Start" button in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTART_CLICK_START, **kwargs)

    def firmware_dialog_restart_click_abort(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Abort" button in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTART_CLICK_ABORT, **kwargs)

    def firmware_dialog_restart_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Cancel" button in the Restart Device dialog.
        It is assumed the Restart Device dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTART_CLICK_CANCEL, **kwargs)

    def firmware_dialog_restore_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the tab to select

        Selects the specified tab in the Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_TAB, **kwargs)

    def firmware_dialog_restore_click_start(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTORE_CLICK_START, **kwargs)

    def firmware_dialog_restore_select_configuration_to_restore(self, element_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name] -   Name of the configuration to restore

        Selects the specified configuration in the "Configuration to Restore" drop down on the Restore tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args,
                                    self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE, **kwargs)

    def firmware_dialog_restore_select_configuration_to_restore_newest(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name] -   Name of the configuration to restore

        Selects the specified configuration in the "Configuration to Restore" drop down on the Restore tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        return self.execute_keyword(element_name, {},
                                    self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE_NEWEST, **kwargs)

    def firmware_dialog_restore_select_configuration_to_restore_oldest(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name] -   Name of the configuration to restore

        Selects the specified configuration in the "Configuration to Restore" drop down on the Restore tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        return self.execute_keyword(element_name, {},
                                    self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE_OLDEST, **kwargs)

    def firmware_dialog_restore_select_source_device(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the source device to select

        Selects the specified device in the "Source Device" drop down on the Clone tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_SOURCE_DEVICE, **kwargs)

    def firmware_dialog_restore_select_configuration_to_clone(self, element_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [config_name] -   Name of the configuration to clone

        Selects the specified configuration in the "Configuration to Clone" drop down on the Clone tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE,
                                    **kwargs)

    def firmware_dialog_restore_select_configuration_to_clone_newest(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects the newest configuration in the "Configuration to Clone" drop down on the Clone tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        return self.execute_keyword(element_name, {},
                                    self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE_NEWEST, **kwargs)

    def firmware_dialog_restore_select_configuration_to_clone_oldest(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects the oldest configuration in the "Configuration to Clone" drop down on the Clone tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        return self.execute_keyword(element_name, {},
                                    self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE_OLDEST, **kwargs)

    def firmware_dialog_restore_select_template(self, element_name, template_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [template_name] - Name of the template to select

        Selects the specified template in the "Template" drop down on the Template tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"template_name": template_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_TEMPLATE, **kwargs)

    def firmware_dialog_restore_select_profile(self, element_name, profile_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [profile_name] -  Name of the profile to select

        Selects the specified profile in the "Model Using Profile" drop down on the Template tab of the
        Restore Configuration dialog.
        It is assumed the Restore Configuration dialog is already displayed.
        """
        args = {"profile_name": profile_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_RESTORE_SELECT_PROFILE, **kwargs)

    def firmware_dialog_restore_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Restore Configuration dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_RESTORE_CLICK_CANCEL, **kwargs)

    def firmware_dialog_serial_numbers_click_register(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Register in the Register/Export Serial Numbers dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_REGISTER, **kwargs)

    def firmware_dialog_serial_numbers_click_export_to_file(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Export to File in the Register/Export Serial Numbers dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_EXPORT_TO_FILE,
                                    **kwargs)

    def firmware_dialog_serial_numbers_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Register/Export Serial Numbers dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_CANCEL, **kwargs)

    def firmware_dialog_serial_numbers_register_set_refresh(self, element_name, btn_state, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [btn_state] -   Desired selection state of the "Refresh the Devices before registering" check button
                        (True/False)

        Sets the state of the "Refresh the Devices before registering" check button in the Register Device
        Serial Numbers dialog, which is accessed by clicking the Register button in the Register/Export Serial Numbers
        dialog.
        It is assumed the Register Device Serial Numbers dialog is already displayed.
        """
        args = {"btn_state": btn_state}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_SET_REFRESH,
                                    **kwargs)

    def firmware_dialog_serial_numbers_register_click_register(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Register in the Register Device Serial Numbers dialog, which is accessed by clicking the Register button
        in the Register/Export Serial Numbers dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_CLICK_REGISTER,
                                    **kwargs)

    def firmware_dialog_serial_numbers_register_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Register Device Serial Numbers dialog, which is accessed by clicking the Register button
        in the Register/Export Serial Numbers dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_CLICK_CANCEL,
                                    **kwargs)

    def firmware_dialog_configuration_set_file_transfer_mode(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to enter in the File Transfer Mode field

        Sets the File Transfer Mode field in the Set Firmware and Configuration Settings dialog.
        It is assumed the Set Firmware and Configuration Settings dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_SET_FILE_TRANSFER_MODE,
                                    **kwargs)

    def firmware_dialog_configuration_set_server(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to enter in the Server for Firmware Downloads field

        Sets the Server for Firmware Downloads field in the Set Firmware and Configuration Settings dialog.
        It is assumed the Set Firmware and Configuration Settings dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_SET_SERVER, **kwargs)

    def firmware_dialog_configuration_set_firmware_mib(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to select in the Firmware Download MIB field

        Sets the Firmware Download MIB field in the Set Firmware and Configuration Settings dialog.
        It is assumed the Set Firmware and Configuration Settings dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_SET_FIRMWARE_MIB,
                                    **kwargs)

    def firmware_dialog_configuration_set_configuration_mib(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to select in the Configuration Download MIB field

        Sets the Configuration Download MIB field in the Set Firmware and Configuration Settings dialog.
        It is assumed the Set Firmware and Configuration Settings dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_SET_CONFIGURATION_MIB,
                                    **kwargs)

    def firmware_dialog_configuration_set_script_file_name(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to select in the Device Family Definition Filename field

        Sets the Device Family Definition Filename field in the Set Firmware and Configuration Settings dialog.
        It is assumed the Set Firmware and Configuration Settings dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_SET_SCRIPT_FILE_NAME,
                                    **kwargs)

    def firmware_dialog_configuration_click_view(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks View next to the Device Family Definition Filename field in the Set Firmware and Configuration Settings
        dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_CLICK_VIEW, **kwargs)

    def firmware_dialog_configuration_view_click_ok(self, element_name, script_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [script_name] -   Name of the script being viewed;  used to access the window the OK button lives in

        Clicks OK in the View Device Family Definition Filename dialog accessed from the Set Firmware and Configuration
        Settings dialog.  The name of the script needs to be passed in so the dialog window can be queried (using the
        script name as the window title) to obtain the OK button.
        """
        args = {"script_name": script_name}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_VIEW_CLICK_OK, **kwargs)

    def firmware_dialog_configuration_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the Set Firmware and Configuration Settings dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_CLICK_OK, **kwargs)

    def firmware_dialog_configuration_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Set Firmware and Configuration Settings dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_CONFIGURATION_CLICK_CANCEL, **kwargs)

    def firmware_dialog_upgrade_select_devices(self, element_name, device_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_list] -   Comma-separated list of devices to select

        Selects the devices in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"device_list": device_list}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SELECT_DEVICES, **kwargs)

    def firmware_dialog_upgrade_click_assign_image(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Assign Image in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_ASSIGN_IMAGE, **kwargs)

    def firmware_dialog_upgrade_click_set_configuration(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Set Configuration in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_SET_CONFIGURATION,
                                    **kwargs)

    def firmware_dialog_upgrade_set_restart_devices_after_upgrade(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Selection state of the "Restart Devices After Upgrade" check button (True/False)

        Sets the selection state of the Restart Devices After Upgrade check button in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_RESTART_DEVICES_AFTER_UPGRADE, **kwargs)

    def firmware_dialog_upgrade_set_schedule_upgrade(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Selection state of the "Schedule Upgrade" check button (True/False)

        Sets the selection state of the Schedule Upgrade check button in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_UPGRADE, **kwargs)

    def firmware_dialog_upgrade_set_schedule_name(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to set in the Schedule Name field

        Sets the Schedule Name field in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_NAME, **kwargs)

    def firmware_dialog_upgrade_set_schedule_date_time(self, element_name, the_date, the_time, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [sched_date] -    Value to set in the Schedule Date field
        [sched_time] -    Value to set in the Schedule Time field

        Sets the Select Date field's date and time values in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"the_date": the_date,
                "the_time": the_time}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_DATE_TIME,
                                    **kwargs)

    def firmware_dialog_upgrade_set_schedule_abort_on_failure(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Selection state of the "Abort on Failure" check button (True/False)

        Sets the selection state of the Abort on Failure check button in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_ABORT_ON_FAILURE,
                                    **kwargs)

    def firmware_dialog_upgrade_set_device_upgrade_group_size(self, element_name, field_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [field_value] -   Value to set in the Device Upgrade Group Size field

        Sets the Device Upgrade Group Size field in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        args = {"field_value": field_value}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_SET_DEVICE_UPGRADE_GROUP_SIZE,
                                    **kwargs)

    def firmware_dialog_upgrade_click_start(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Start in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_START, **kwargs)

    def firmware_dialog_upgrade_click_schedule(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Schedule in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_SCHEDULE, **kwargs)

    def firmware_dialog_upgrade_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_CANCEL, **kwargs)

    def firmware_dialog_upgrade_click_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Close in the Upgrade Firmware dialog.
        It is assumed the Upgrade Firmware dialog is already displayed.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CLICK_CLOSE, **kwargs)

    def firmware_dialog_upgrade_confirm_start_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Firmware Download confirmation dialog, which is displayed when clicking "Start" in the
        Upgrade Firmware dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CONFIRM_START_CLICK_YES,
                                    **kwargs)

    def firmware_dialog_upgrade_confirm_start_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Firmware Download confirmation dialog, which is displayed when clicking "Start" in the
        Upgrade Firmware dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.FIRMWARE_DIALOG_UPGRADE_CONFIRM_START_CLICK_NO, **kwargs)

    def firmware_dialog_upgrade_wait_for_completion(self, element_name, wait_time, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [wait_time] -     Number of seconds to wait before timing out

        Waits for the "Overll Progress" field of the Upgrade Status panel in the Upgrade Firmware dialog to reach 100%.
        Times out at the specified "wait_time" value (in seconds).
        It is assumed the Upgrade Firmware dialog is displayed and the upgrade has been started.
        """
        args = {"wait_time": wait_time}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_DIALOG_UPGRADE_WAIT_FOR_COMPLETION, **kwargs)

    def firmware_confirm_config_fw_menu_exists(self, element_name, menu_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_name] -     Name of the menu to check
        [exists] -        Indicates if the menu should exist or not (True/False)

        Checks the Configuration/Firmware device context menu for the existence of the specified menu.
        """
        args = {"menu_name": menu_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_CONFIRM_CONFIG_FW_MENU_EXISTS, **kwargs)

    def firmware_confirm_config_fw_menu_enabled(self, element_name, menu_name, is_enabled, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [menu_name] -     Name of the menu to check
        [is_enabled] -    Indicates if the menu is expected to be enabled or not (True/False)

        Checks the if the specified menu on the Configuration/Firmware device context menu is enabled.
        """
        args = {"menu_name": menu_name,
                "is_enabled": is_enabled}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_CONFIRM_CONFIG_FW_MENU_ENABLED, **kwargs)

    def firmware_confirm_upgrade_success(self, element_name, device_ip, is_success, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to check the upgrade status of
        [is_success] -    Indicates if the upgrade is expected to be successful or not (True/False)

        Checks the if the upgrade was successful, by checking the Status column in the Upgrade Firmware dialog.
        """
        args = {"is_success": is_success,
                "device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.FIRMWARE_CONFIRM_UPGRADE_SUCCESS, **kwargs)
