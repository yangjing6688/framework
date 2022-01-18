from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ArchivesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Archives(ArchivesBase):

    def archives_click_create(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkArchivesTab #mainArchiveTree "
                               "button[actionId=archiveArchiveWizard] => .x-btn-button")
        return ui_cmd_obj

    def archives_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkArchivesTab #mainArchiveTree button[text=Refresh] => "
                               ".x-btn-button")
        return ui_cmd_obj

    def archives_tree_expand_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def archives_tree_collapse_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.collapse_tree_node(ui_cmd_obj,
                                            '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                            '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def archives_tree_select_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.select_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def archives_tree_expand_newest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to expand, and expand it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "newest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.expand_tree_node(ui_cmd_obj,
                                              '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                              '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_expand_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to expand, and expand it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "oldest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.expand_tree_node(ui_cmd_obj,
                                              '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                              '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_collapse_newest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to collapse, and collapse it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "newest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.collapse_tree_node(ui_cmd_obj,
                                                '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                                '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_collapse_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to collapse, and collapse it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "oldest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.collapse_tree_node(ui_cmd_obj,
                                                '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                                '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_select_newest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to select, and select it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "newest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.select_tree_node(ui_cmd_obj,
                                              '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                              '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_select_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', arg_dict['archive_name'])

        # Determine the name of the version to select, and select it
        self.get_archive_version_name(ui_cmd_obj, arg_dict['archive_name'], "oldest")
        if ui_cmd_obj.error_state is False:
            self.ext_builder.select_tree_node(ui_cmd_obj,
                                              '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                              '[0]', 'text', ui_cmd_obj.return_data)
        return ui_cmd_obj

    def archives_tree_create(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree treeview => "
                                     ".x-grid-tree-node-expanded .x-grid-cell-inner-treecolumn")
        self.ext_builder.click(ui_cmd_obj, "menuitem[text=Create...] => .x-menu-item-text")
        return ui_cmd_obj

    def archives_tree_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree treeview => "
                                     ".x-grid-tree-node-expanded .x-grid-cell-inner-treecolumn")
        self.ext_builder.click(ui_cmd_obj, "menuitem[text=Refresh] => .x-menu-item-text")
        return ui_cmd_obj

    def archives_tree_delete_archive(self, ui_cmd_obj, arg_dict):
        # Right click on the archive in the tree to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree => "
                                     ".x-tree-node-text:textEquals(" +
                                     arg_dict['archive_name'] + ")")
        # Select "Delete" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#firmwareTreeMenu{isVisible()} menuitem[actionId=archiveDeleteArchive] => "
                               ".x-menu-item-text")

        return ui_cmd_obj

    def archives_tree_delete_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Delete")

        return ui_cmd_obj

    def archives_tree_delete_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Delete")

        return ui_cmd_obj

    def archives_tree_delete_newest_archive_version_device(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest",
                                                                 arg_dict['device_ip'], "Delete")

        return ui_cmd_obj

    def archives_tree_delete_oldest_archive_version_device(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldest",
                                                                 arg_dict['device_ip'], "Delete")

        return ui_cmd_obj

    def archives_tree_lock_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Lock")

        return ui_cmd_obj

    def archives_tree_lock_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Lock")

        return ui_cmd_obj

    def archives_tree_unlock_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Unlock")

        return ui_cmd_obj

    def archives_tree_unlock_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Unlock")

        return ui_cmd_obj

    def archives_tree_rename_archive(self, ui_cmd_obj, arg_dict):
        # Right click on the archive in the tree to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree => "
                                     ".x-tree-node-text:textEquals(" +
                                     arg_dict['archive_name'] + ")")

        # Select "Rename" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#firmwareTreeMenu{isVisible()} menuitem[actionId=archiveRename] => .x-menu-item-text")

        return ui_cmd_obj

    def archives_tree_restore_newest_archive_version(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Restore...")

        # Perform the restore
        self.restore_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest")

        return ui_cmd_obj

    def archives_tree_restore_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Restore...")

        # Perform the restore
        self.restore_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest")

        return ui_cmd_obj

    def archives_tree_restore_newest_archive_version_device(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.tree_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest",
                                                                 arg_dict['device_ip'], "Restore...")

        # Perform the restore
        self.restore_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest", arg_dict['device_ip'])

        return ui_cmd_obj

    def archives_tree_restore_oldest_archive_version_device(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.tree_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldest",
                                                                 arg_dict['device_ip'], "Restore...")

        # Perform the restore
        self.restore_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldest", arg_dict['device_ip'])

        return ui_cmd_obj

    def archives_tree_stamp_new_version(self, ui_cmd_obj, arg_dict):
        # Right click on the archive in the tree to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree => "
                                     ".x-tree-node-text:textEquals(" +
                                     arg_dict['archive_name'] + ")")

        # Select "Stamp New Version" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#firmwareTreeMenu{isVisible()} menuitem[actionId=archiveStampNewVersion] => "
                               ".x-menu-item-text")

        return ui_cmd_obj

    def archives_tree_view_config_file(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab #mainArchiveTree => "
                                     ".x-tree-node-text:textEquals(" +
                                     arg_dict['device_ip'] + ")")

        # Check if the specified menu is enabled - the query returns True if the menu is DISABLED
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      r'#firmwareTreeMenu menuitem[text=View Configuration File\.\.\.]',
                                                      r'[0].disabled')

        # Log the result
        if ui_cmd_obj.return_data is True:
            # Close the right click menu by clicking the Archives sub tab again
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel tab[text=Archives] => .x-tab-inner-extr-main-tab-panel')

            self.logger.log_info("\nMenu 'View Configuration File' is disabled.\n")
            ui_cmd_obj.error_state = True
        else:
            self.ext_builder.click(ui_cmd_obj,
                                   r"#firmwareTreeMenu{isVisible()} menuitem[text=View Configuration File\.\.\.] => "
                                   r".x-menu-item-text")

        return ui_cmd_obj

    def archives_table_select_archive(self, ui_cmd_obj, arg_dict):
        # Select the root 'Archives' node in the tree
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkArchivesTab #mainArchiveTree => "
                               ".x-tree-node-text:textEquals(Archives)")

        # Select the specified archive in the table
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkArchivesTab archiveGrid[viewId=Archive_Details] tableview => "
                               ".x-grid-cell-inner:textEquals(" +
                               arg_dict["archive_name"] + ")")

        return ui_cmd_obj

    def archives_table_delete_archive(self, ui_cmd_obj, arg_dict):
        # Right click the specified archive in the table to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#networkTabPanel #networkArchivesTab archiveGrid[viewId=Archive_Details] "
                                     "tableview => .x-grid-cell-inner:textEquals(" +
                                     arg_dict["archive_name"] + ")")

        # Select "Delete" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               "#archiveGridMenu{isVisible()} menuitem[actionId=archiveDeleteArchive] => "
                               ".x-menu-item-text")

        return ui_cmd_obj

    def archives_table_delete_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Delete")

        return ui_cmd_obj

    def archives_table_delete_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Delete")

        return ui_cmd_obj

    def archives_table_delete_newest_archive_version_device(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest",
                                                                  arg_dict['device_ip'], "Delete")

        return ui_cmd_obj

    def archives_table_delete_oldest_archive_version_device(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldest",
                                                                  arg_dict['device_ip'], "Delete")

        return ui_cmd_obj

    def archives_table_lock_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Lock")

        return ui_cmd_obj

    def archives_table_lock_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Lock")

        return ui_cmd_obj

    def archives_table_unlock_newest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Unlock")

        return ui_cmd_obj

    def archives_table_unlock_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Unlock")

        return ui_cmd_obj

    def archives_table_rename_archive(self, ui_cmd_obj, arg_dict):
        # Select the root Archives node in the tree so the archives will be listed in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #mainArchiveTree => '
                               '.x-tree-node-text:textEquals(Archives)')

        # Right click on the archive in the table to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab archiveGrid[viewId=Archive_Details] '
                                     'tableview => .x-grid-cell-inner:textEquals(' +
                                     arg_dict['archive_name'] + ')')

        # Select "Rename..." from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveGridMenu{isVisible()} menuitem[actionId=archiveRename] => .x-menu-item-text')

        return ui_cmd_obj

    def archives_table_restore_newest_archive_version(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest", "Restore...")

        # Perform the restore
        self.restore_archive_version(ui_cmd_obj, arg_dict['archive_name'], "newest")

        return ui_cmd_obj

    def archives_table_restore_oldest_archive_version(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.table_select_context_menu_for_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest", "Restore...")

        # Perform the restore
        self.restore_archive_version(ui_cmd_obj, arg_dict['archive_name'], "oldest")

        return ui_cmd_obj

    def archives_table_restore_newest_archive_version_device(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.table_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest",
                                                                  arg_dict['device_ip'], "Restore...")

        # Perform the restore
        self.restore_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "newest", arg_dict['device_ip'])

        return ui_cmd_obj

    def archives_table_restore_oldest_archive_version_device(self, ui_cmd_obj, arg_dict):
        # Display the Restore dialog
        self.table_select_context_menu_for_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldst",
                                                                  arg_dict['device_ip'], "Restore...")

        # Perform the restore
        self.restore_archive_version_device(ui_cmd_obj, arg_dict['archive_name'], "oldest", arg_dict['device_ip'])

        return ui_cmd_obj

    def archives_table_stamp_new_version(self, ui_cmd_obj, arg_dict):
        # Select the root Archives node in the tree so the archives will be listed in the table
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #mainArchiveTree => '
                               '.x-tree-node-text:textEquals(Archives)')

        # Right click on the archive in the table to access the context menu
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab archiveGrid[viewId=Archive_Details] '
                                     'tableview => .x-grid-cell-inner:textEquals(' +
                                     arg_dict['archive_name'] + ')')

        # Select "Stamp New Version" from the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveGridMenu{isVisible()} menuitem[actionId=archiveStampNewVersion] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def archives_details_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab archiveDetailsPanel tab[text=' +
                               arg_dict['tab_name'] + '] => .x-tab-inner')
        return ui_cmd_obj

    def archives_details_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab panel[title=Details] archiveDetailsPanel '
                               'button[text=Save] => .x-btn-button')
        return ui_cmd_obj

    def archives_details_archive_set_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab #archiveDetailsGeneralPanel textarea => '
                                    '.x-form-text')
        return ui_cmd_obj

    def archives_details_archive_set_ips_enabled(self, ui_cmd_obj, arg_dict):
        self.archive_details_enable_disable_ips(ui_cmd_obj, arg_dict["ip_list"], True)

        return ui_cmd_obj

    def archives_details_archive_set_ips_disabled(self, ui_cmd_obj, arg_dict):
        self.archive_details_enable_disable_ips(ui_cmd_obj, arg_dict["ip_list"], False)

        return ui_cmd_obj

    def archives_details_archive_set_process_groups(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                    'numberfield[name=processNumGroups] => .x-form-text')
        return ui_cmd_obj

    def archives_details_archive_set_abort_on_failure(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Abort on Failure" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                         'checkbox[name=abortOnFail]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                   'checkbox[name=abortOnFail] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Abort on Failure' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_details_archive_set_max_versions_unlimited(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel #maxVersions '
                               'radio[boxLabel=Unlimited] => .x-form-cb-input')
        return ui_cmd_obj

    def archives_details_archive_set_max_versions_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r'#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel #maxVersions '
                               r'radio[boxLabel=Maximum \# of Versions] => .x-form-cb-input')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                    'numberfield[name=maxVersions] => .x-form-text')
        return ui_cmd_obj

    def archives_details_archive_set_archive_configuration_data(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Archive Configuration Data" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                         'checkbox[name=isConfig]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                   'checkbox[name=isConfig] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Archive Configuration Data' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_details_archive_set_archive_capacity_planning_data(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Archive Capacity Planning Data" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                         'checkbox[name=isCapacity]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                   'checkbox[name=isCapacity] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Archive Capacity Planning Data' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_details_archive_set_run_governance(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Run Governance" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                         'checkbox[name=govEnabled]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                                   'checkbox[name=govEnabled] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Run Governance' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_details_archive_select_regime(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                               'combo[name=govRegimeId] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #archiveDetailsSetupPanel '
                               'combo[name=govRegimeId] boundlist => ' +
                               '.x-boundlist-item:textEquals(' + arg_dict['the_value'] + ')')
        return ui_cmd_obj

    def archives_details_archive_set_frequency(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #archiveDetailsSchedulePanel '
                               'combo[name=saveFrequency] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #archiveDetailsSchedulePanel '
                               'combo[name=saveFrequency] boundlist => ' +
                               '.x-boundlist-item:textEquals(' + arg_dict['the_value'] + ')')
        return ui_cmd_obj

    def archives_details_archive_set_date(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab #archiveDetailsSchedulePanel datefield => '
                                    '.x-form-text')
        return ui_cmd_obj

    def archives_details_archive_set_start_time(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab #archiveDetailsSchedulePanel timefield => '
                                    '.x-form-text')
        return ui_cmd_obj

    def archives_details_archive_click_configure_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab button[actionId=editDevicesArchiveDetails] => '
                               '.x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_details_version_set_locked(self, ui_cmd_obj, arg_dict):
        if arg_dict["the_value"] == "True":
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab radio[boxLabel=Locked] => .x-form-cb-input')
        else:
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkArchivesTab radio[boxLabel=Unlocked] => .x-form-cb-input')

        return ui_cmd_obj

    def archives_details_version_set_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab archiveVersionDetailsPanel '
                                    'textarea[name=memo] => .x-form-text')
        return ui_cmd_obj

    def archives_details_device_set_memo(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#networkTabPanel #networkArchivesTab textarea[fieldLabel=Memo] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_configure_devices_add_archive_member_device(self, ui_cmd_obj, arg_dict):
        # Expand the All Devices tree node first so we can find the device to select
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          "archiveEditDeviceWindow[title=Configure Devices] #runScriptDeviceSelector "
                                          "treeview", "[0]", "groupname", "All Devices")

        # Select the specified device.  This does an exact match for the IP address.
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] #runScriptDeviceSelector treeview => '
                               '.x-tree-node-text:textEquals(' + arg_dict['the_value'] + ')')

        # Click the right arrow to move the selection to the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] treeGridDeviceAndGroupSelectionPanel '
                               'panel button[text=&#9658;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_configure_devices_add_archive_member_group(self, ui_cmd_obj, arg_dict):
        # Select the specified group.
        # This does a partial match since the group name contains the number of children nodes as a suffix.
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] #runScriptDeviceSelector treeview => '
                               '.x-tree-node-text:contains(' + arg_dict['the_value'] + ')')

        # Click the right arrow to move the selection to the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] treeGridDeviceAndGroupSelectionPanel '
                               'panel button[text=&#9658;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_configure_devices_remove_archive_member_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] #selectionPanel treeview => '
                               '.x-tree-node-text:textEquals(' + arg_dict['the_value'] + ')')

        # Click the left arrow to remove the selection from the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] treeGridDeviceAndGroupSelectionPanel '
                               'panel button[text=&#9668;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_configure_devices_remove_archive_member_group(self, ui_cmd_obj, arg_dict):
        # This does a partial match since the group name contains the number of children nodes as a suffix.
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] #selectionPanel treeview => '
                               '.x-tree-node-text:textEquals(' + arg_dict['the_value'] + ')')

        # Click the left arrow to remove the selection from the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices] treeGridDeviceAndGroupSelectionPanel '
                               'panel button[text=&#9668;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_configure_devices_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices]  '
                               'button[actionId=archiveEditDeviceOk] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def archives_dialog_configure_devices_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'archiveEditDeviceWindow[title=Configure Devices]  '
                               'button[actionId=archiveEditDeviceCancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_archive_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_archive_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_version_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_version_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_device_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def archives_dialog_confirm_delete_device_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_dialog_create_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardDetails textfield[name=archiveName] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardDetails textareafield[name=archiveMemo] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_max_versions_unlimited(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDetails #archiveMaxVersions radiofield[boxLabel=Unlimited] => '
                               '.x-form-cb-input')
        return ui_cmd_obj

    def archives_dialog_create_set_max_versions_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r'#archiveWizardDetails #archiveMaxVersions radiofield[boxLabel=Maximum \# of Versions] '
                               r'=> .x-form-cb-input')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardDetails numberfield[name=archiveMaxVersions] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_archive_configuration_data(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Archive Configuration Data" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#archiveWizardDetails checkboxfield[name=archiveIsConfig]', '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#archiveWizardDetails checkboxfield[name=archiveIsConfig] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Archive Configuration Data' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_dialog_create_set_archive_capacity_planning_data(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Archive Capacity Planning Data" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#archiveWizardDetails checkboxfield[name=archiveIsCapacity]', '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#archiveWizardDetails checkboxfield[name=archiveIsCapacity] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Archive Capacity Planning Data' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_dialog_create_add_archive_member_device(self, ui_cmd_obj, arg_dict):
        # Expand the All Devices tree node first so we can find the device to select
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          "#archiveWizardDevices #runScriptDeviceSelector treeview", "[0]",
                                          "groupname", "All Devices")

        # Select the specified device.  This does an exact match for the IP address.
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices #runScriptDeviceSelector treeview => '
                               '.x-tree-node-text:textEquals(' + arg_dict['the_value'] + ')')

        # Click the right arrow to move the selection to the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices treeGridDeviceAndGroupSelectionPanel panel '
                               'button[text=&#9658;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_add_archive_member_group(self, ui_cmd_obj, arg_dict):
        # Select the specified group.
        # This does a partial match since the group name contains the number of children nodes as a suffix.
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices #runScriptDeviceSelector treeview => '
                               '.x-tree-node-text:contains(' + arg_dict['the_value'] + ')')

        # Click the right arrow to move the selection to the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices treeGridDeviceAndGroupSelectionPanel panel '
                               'button[text=&#9658;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_remove_archive_member_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices #selectionPanel treeview => .x-tree-node-text:textEquals(' +
                               arg_dict['the_value'] + ')')

        # Click the left arrow to remove the selection from the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices treeGridDeviceAndGroupSelectionPanel panel '
                               'button[text=&#9668;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_remove_archive_member_group(self, ui_cmd_obj, arg_dict):
        # This does a partial match since the group name contains the number of children nodes as a suffix.
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices #selectionPanel treeview => .x-tree-node-text:contains(' +
                               arg_dict['the_value'] + ')')

        # Click the left arrow to remove the selection from the Archive Members list
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardDevices treeGridDeviceAndGroupSelectionPanel panel '
                               'button[text=&#9668;] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_set_frequency(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardSchedule combobox[name=archiveSaveFrequency] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#archiveWizardSchedule combobox[name=archiveSaveFrequency] boundlist => ' +
                               '.x-boundlist-item:textEquals(' + arg_dict['the_value'] + ')')
        return ui_cmd_obj

    def archives_dialog_create_set_date(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardSchedule datefield[name=archiveDate] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_start_time(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardSchedule timefield[name=archiveStartTime] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_process_groups(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    '#archiveWizardSchedule numberfield[name=archiveProcessNumGroups] => .x-form-text')
        return ui_cmd_obj

    def archives_dialog_create_set_abort_on_failure(self, ui_cmd_obj, arg_dict):
        # Set the state of the "Abort on Failure" check button, if it isn't already at the desired state
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#archiveWizardSchedule checkboxfield[name=archiveAbortOnFail]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#archiveWizardSchedule checkboxfield[name=archiveAbortOnFail] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Abort on Failure' check button is already at desired value.\n")

        return ui_cmd_obj

    def archives_dialog_create_set_ip_sort_ascending(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#archiveWizardSchedule #archiveArchiveDevicesGrid gridcolumn[text=IP Address] => '
                                     '.x-leaf-column-header')
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardSchedule #archiveArchiveDevicesGrid gridcolumn[text=IP Address] => '
                               '.x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardSchedule #archiveArchiveDevicesGrid menu #ascItem => .x-menu-item-text')

        return ui_cmd_obj

    def archives_dialog_create_set_ip_sort_descending(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#archiveWizardSchedule #archiveArchiveDevicesGrid gridcolumn[text=IP Address] => '
                                     '.x-leaf-column-header')
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardSchedule #archiveArchiveDevicesGrid gridcolumn[text=IP Address] => '
                               '.x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveWizardSchedule #archiveArchiveDevicesGrid menu #descItem => .x-menu-item-text')

        return ui_cmd_obj

    def archives_dialog_create_set_ips_disabled(self, ui_cmd_obj, arg_dict):
        ip_str_list = str(arg_dict["ip_list"]).split(",")
        for ip_str in ip_str_list:
            # Set the state of the check button if it isn't already at the desired state

            # Figure out how many items are in the table
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#archiveWizardSchedule #archiveArchiveDevicesGrid gridview',
                                                          '[0].store.data.items.length')
            item_count = int(ui_cmd_obj.return_data)
            item_count += 1

            # Loop through the table items, searching for the node to act on
            for item_index in range(0, item_count):
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#archiveWizardSchedule #archiveArchiveDevicesGrid '
                                                              'gridview', '[0].store.data.items[' +
                                                              str(item_index) + '].data.ipAddress')
                if ui_cmd_obj.return_data == ip_str:
                    # Check the current checked state of the node
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#archiveWizardSchedule #archiveArchiveDevicesGrid '
                                                                  'gridview', '[0].store.data.items[' +
                                                                  str(item_index) + '].data.enabled')
                    node_checked = ui_cmd_obj.return_data
                    if node_checked is True:
                        self.ext_builder.click(ui_cmd_obj,
                                               '#archiveWizardSchedule #archiveArchiveDevicesGrid gridview => '
                                               '.x-grid-item:contains(' + ip_str + ') .x-grid-checkcolumn')
                    else:
                        self.logger.log_info("\nIP '" + ip_str + "' is already disabled.\n")
                    break

        return ui_cmd_obj

    def archives_dialog_create_click_next(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=next] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_click_previous(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=prev] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_create_click_finish(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=finish] => .x-btn-button')

        # Handle an error
        self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Error]", "[0]")
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Error]", "[0].hidden")
            if ui_cmd_obj.return_data is False:
                self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Error]", "[0].msg.html")
                self.logger.log_info("\nCREATE ARCHIVE FAILED:\n" + ui_cmd_obj.return_data + "\n")
                ui_cmd_obj.error_state = True

                # Click OK in the error dialog
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

                # Click Cancel in the Create Archive dialog
                self.archives_dialog_create_click_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def archives_dialog_create_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=cancel] => .x-btn-button')

        return ui_cmd_obj

    def archives_dialog_rename_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Rename Archive]', '[0]')
        if ui_cmd_obj.return_data is not None:
            self.ext_builder.component_query(ui_cmd_obj, 'messagebox[title=Rename Archive]', '[0].down("textfield")')
            if ui_cmd_obj.return_data is not None:
                self.logger.log_info("\nTO DO: Need to set name to '" + arg_dict['the_value'] + "'.\n")
            else:
                self.logger.log_info("\nCould not find text field to set new name.\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find Rename Archive dialog.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_dialog_rename_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def archives_dialog_rename_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#cancel => .x-btn-inner-default-small')

        return ui_cmd_obj

    def archives_dialog_view_config_file_find(self, ui_cmd_obj, arg_dict):
        # Ensure config file dialog box is in focus
        self.ext_builder.click(ui_cmd_obj,
                               "viewArchiveConfigWindow[title=Configuration File Viewer] "
                               "title[text=Configuration File Viewer] => .x-title-text")

        # Type control+F to enter the search mechanism
        self.ext_builder.enter_text(ui_cmd_obj, 'F', "codemirror[name=configFileContent] => textarea", ctrl=True)

        # Search for the specified string so it is highlighted.
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'] + '[RETURN]',
                                    "codemirror[name=configFileContent] => .CodeMirror-search-field")

        # Get the config file text
        self.ext_builder.component_query(ui_cmd_obj, 'codemirror[name=configFileContent]', '[0].value')
        config_text = str(ui_cmd_obj.return_data)

        # Determine if the value exists in the config file and log the result
        found_value = False
        if config_text:
            if config_text.find(arg_dict['the_value']) != -1:
                found_value = True
                self.logger.log_info("\nFound '" + arg_dict['the_value'] + "' in configuration text.\n")
            else:
                self.logger.log_info("\nDid not find '" + arg_dict['the_value'] + "' in configuration text.\n")
        else:
            self.logger.log_error("\nConfiguration file is empty.\n")

        # Pass or fail the test, based on what was expected
        if found_value is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_dialog_view_config_file_find_in_named_block(self, ui_cmd_obj, arg_dict):
        # Ensure config file dialog box is in focus
        self.ext_builder.click(ui_cmd_obj,
                               "viewArchiveConfigWindow[title=Configuration File Viewer] "
                               "title[text=Configuration File Viewer] => .x-title-text")

        # Type control+F to enter the search mechanism
        self.ext_builder.enter_text(ui_cmd_obj, 'F', "codemirror[name=configFileContent] => textarea", ctrl=True)

        # Search for the specified string so it is highlighted.
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'] + '[RETURN]',
                                    "codemirror[name=configFileContent] => .CodeMirror-search-field")

        # Get the config file text
        self.ext_builder.component_query(ui_cmd_obj, 'codemirror[name=configFileContent]', '[0].value')
        config_text = str(ui_cmd_obj.return_data)

        # Determine if the value is in the specified block, and log the results
        found_value = False
        if config_text:
            # Split the text into blocks, splitting on the word "exit" which ends each block
            block_list = config_text.split('exit')
            for block in block_list:
                block.lstrip()
                if block.startswith(arg_dict['block_name']):
                    if block.find(arg_dict['the_value']) != -1:
                        found_value = True
                        self.logger.log_info("\nFound '" + arg_dict['the_value'] + "' in config block '" +
                                             arg_dict['block_name'] + "'.\n")
                        break
                    else:
                        self.logger.log_info("\nDid not find '" + arg_dict['the_value'] + "' in config block '" +
                                             arg_dict['block_name'] + "'.\n")
        else:
            self.logger.log_error("\nConfiguration file is empty.\n")

        # Pass or fail the test, based on what was expected
        if found_value is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_dialog_view_config_click_close(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "viewArchiveConfigWindow[title=Configuration File Viewer] button[text=Close] => "
                               ".x-btn-inner-default-small")

        return ui_cmd_obj

    def archives_confirm_archive_exists(self, ui_cmd_obj, arg_dict):
        # Refresh the Archives tree
        self.archives_click_refresh(ui_cmd_obj, arg_dict)

        # Look for the archive in the tree
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                         '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Assume we won't find the archive
        found_item = False

        # Loop through the table and see if the specified archive exists
        item_index = 0
        for x in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                             '[0].store.data.items[' + str(item_index) + '].data.text')
            if ui_cmd_obj.return_data == arg_dict['archive_name']:
                self.logger.log_info(
                    "\nFound archive '" + arg_dict['archive_name'] + "' at index " + str(item_index) + "\n")
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

    def archives_confirm_archive_version_count(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         'archiveVersionGrid[viewId=Archive_Versions]',
                                         '[0].store.data.length')
        if str(ui_cmd_obj.return_data) == str(arg_dict["the_value"]):
            self.logger.log_info(
                "\nThe archive has the expected number of versions '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have the expected number of versions '" +
                                 str(arg_dict["the_value"]) + "'.\nThe archive has '" +
                                 str(ui_cmd_obj.return_data) + "' versions.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_archive_version_success(self, ui_cmd_obj, arg_dict):
        # Find the number of devices
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numDevices]',
                                         '[0].value')
        num_devices = ui_cmd_obj.return_data

        # Find the number successful
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numSuccess]',
                                         '[0].value')
        num_success = ui_cmd_obj.return_data

        if num_success == num_devices:
            self.logger.log_info("\nThe archive was successful for all devices.\n")
        else:
            # Find the number failed
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                             'archiveVersionDetailsPanel ovdisplayfield[name=numFailed]',
                                             '[0].value')
            num_failed = ui_cmd_obj.return_data

            # Find the number aborted
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                             'archiveVersionDetailsPanel ovdisplayfield[name=numAborted]',
                                             '[0].value')
            num_aborted = ui_cmd_obj.return_data

            self.logger.log_info("\nThe archive was not successful for all devices:\n\ndevices = " +
                                 str(num_devices) + "\nsuccess = " + str(num_success) + "\nfailed = " +
                                 str(num_failed) + "\naborted = " + str(num_aborted) + "\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_archive_version_aborted(self, ui_cmd_obj, arg_dict):
        # Find the number of devices
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numDevices]',
                                         '[0].value')
        num_devices = ui_cmd_obj.return_data

        # Find the number successful
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numSuccess]',
                                         '[0].value')
        num_success = ui_cmd_obj.return_data

        # Find the number failed
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numFailed]',
                                         '[0].value')
        num_failed = ui_cmd_obj.return_data

        # Find the number aborted
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numAborted]',
                                         '[0].value')
        num_aborted = ui_cmd_obj.return_data

        total = int(num_success) + int(num_failed) + int(num_aborted)
        if (int(num_success) < int(num_devices)) and (int(num_failed) == 1) and (int(total) == int(num_devices)):
            self.logger.log_info("\nThe archive had the correct number of failures and aborts.\n")
        else:
            self.logger.log_info("\nThe archive did not have the correct number of failures and aborts:\n\ndevices = " +
                                 str(num_devices) + "\nsuccess = " + str(num_success) + "\nfailed = " +
                                 str(num_failed) + "\naborted = " + str(num_aborted) + "\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_archive_contains_devices(self, ui_cmd_obj, arg_dict):
        # Split the comma-separated list of devices into each individual device to search for
        device_list = arg_dict['device_list'].split(',')

        # Look for each device IP in the table
        all_found = True
        none_found = True
        for device_ip in device_list:
            self.ext_builder.is_item_in_component(ui_cmd_obj, '#archiveDevicesGrid', '[0]', 'ipAddress', device_ip)

            # Log the result
            if ui_cmd_obj.return_data is True:
                none_found = False
                self.logger.log_info("\nArchive contains device '" + device_ip + "'.\n")
            else:
                all_found = False
                self.logger.log_info("\nArchive does not contain device '" + device_ip + "'.\n")

        # Pass the test only if all devices were either found or not found, depending on what was expected
        if (all_found is StringUtils.string_to_boolean(arg_dict["exists"])) and \
                (none_found is not StringUtils.string_to_boolean(arg_dict["exists"])):
            # PASS - all of the devices were found, as expected
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsGeneralPanel ovdisplayfield[name=name]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info("\nThe archive has expected Name value '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Name value '" + arg_dict[
                "the_value"] + "'.\nThe archive Name value is '" + ui_cmd_obj.return_data + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_description(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsGeneralPanel textarea[name=memo]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info("\nThe archive has expected Description value '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Description value '" + arg_dict[
                "the_value"] + "'.\nThe archive Description value is '" + ui_cmd_obj.return_data + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_description_contains(self, ui_cmd_obj, arg_dict):
        contains_string = False

        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsGeneralPanel textarea[name=memo]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data.find(arg_dict["the_value"]) != -1:
            contains_string = True
            self.logger.log_info("\nThe archive Description value contains '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info("\nThe archive Description value does not contain '" + arg_dict["the_value"] + "'.\n")

        if contains_string is StringUtils.string_to_boolean(arg_dict["exists"]):
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_ips_enabled(self, ui_cmd_obj, arg_dict):
        all_match = True

        desired_state = StringUtils.string_to_boolean(arg_dict["is_enabled"])
        ip_str_list = arg_dict["ip_list"].split(",")
        for ip_str in ip_str_list:
            # Set the state of the check button if it isn't already at the desired state

            # Figure out how many items are in the table
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#networkTabPanel #networkArchivesTab '
                                                          '#archiveDetailsGeneralPanel #archiveDevicesGrid gridview',
                                                          '[0].store.data.items.length')
            item_count = int(ui_cmd_obj.return_data)
            item_count += 1

            # Loop through the table items, searching for the node to check
            for item_index in range(0, item_count):
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#networkTabPanel #networkArchivesTab '
                                                              '#archiveDetailsGeneralPanel #archiveDevicesGrid '
                                                              'gridview', '[0].store.data.items[' + str(item_index) +
                                                              '].data.ipAddress')
                if ui_cmd_obj.return_data == ip_str:
                    # Check the current checked state of the node
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#networkTabPanel #networkArchivesTab '
                                                                  '#archiveDetailsGeneralPanel #archiveDevicesGrid '
                                                                  'gridview', '[0].store.data.items[' +
                                                                  str(item_index) + '].data.enabled')
                    node_checked = ui_cmd_obj.return_data
                    if node_checked is desired_state:
                        self.logger.log_info("\nIP '" + ip_str + "' is at desired state.")
                    else:
                        all_match = False
                        self.logger.log_info("\nIP '" + ip_str + "' is not at desired state.")
                    break

        # Pass the test only if all IPs were either enabled or not, depending on what was expected
        if all_match is True:
            # PASS - all of the IPs were at the expected state
            ui_cmd_obj.error_state = False
            self.logger.log_info("\nAll IPs were at the desired state.\n")
        else:
            # FAIL
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nNot all IPs were at the desired state.\n")

        return ui_cmd_obj

    def archives_confirm_details_archive_process_groups(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel '
                                         'numberfield[name=processNumGroups]', '[0].value')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info(
                "\nThe archive has expected Process Groups value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Process Groups value '" +
                                 str(arg_dict["the_value"]) + "'.\nThe archive Process Groups value is '" +
                                 str(ui_cmd_obj.return_data) + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_abort_on_failure(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel checkbox[name=abortOnFail]',
                                         '[0].value')
        if str(ui_cmd_obj.return_data).lower() == str(arg_dict["the_value"]).lower():
            self.logger.log_info(
                "\nThe archive has expected Abort on Failure value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Abort on Failure value '" + str(
                arg_dict["the_value"]).lower() + "'.\nThe archive Abort on Failure value is '" + str(
                ui_cmd_obj.return_data).lower() + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_max_versions_value(self, ui_cmd_obj, arg_dict):
        # Make sure the Max Versions is no set to Unlimited
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel radiofield[boxLabel=Unlimited]',
                                         '[0].value')
        if not ui_cmd_obj.return_data:
            # Check the value of the Maximum # of Versions field
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                             'archiveDetailsPanel #archiveDetailsSetupPanel '
                                             'numberfield[name=maxVersions]', '[0].value')
            if ui_cmd_obj.return_data == arg_dict["the_value"]:
                self.logger.log_info(
                    "\nThe archive has expected Maximum # of Versions value '" + str(arg_dict["the_value"]) + "'.\n")
            else:
                self.logger.log_info(
                    "\nThe archive does not have expected Maximum # of Versions value '" + str(arg_dict["the_value"]) +
                    "'.\nThe archive Maximum # of Versions value is '" + str(ui_cmd_obj.return_data) + "'.\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nThe archive Max Versions is set to Unlimited.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_max_versions_unlimited(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel radiofield[boxLabel=Unlimited]',
                                         '[0].value')
        if str(ui_cmd_obj.return_data).lower() == str(arg_dict["the_value"]).lower():
            self.logger.log_info(
                "\nThe archive has expected Max Versions Unlimited value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Max Versions Unlimited value '" +
                                 str(arg_dict["the_value"]).lower() +
                                 "'.\nThe archive Max Versions Unlimited value is '" +
                                 str(ui_cmd_obj.return_data).lower() + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_configuration_data(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel checkbox[name=isConfig]',
                                         '[0].value')
        if str(ui_cmd_obj.return_data).lower() == str(arg_dict["the_value"]).lower():
            self.logger.log_info(
                "\nThe archive has expected Archive Configuration Data value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Archive Configuration Data value '" + str(
                arg_dict["the_value"]).lower() + "'.\nThe Archive Configuration Data value is '" + str(
                ui_cmd_obj.return_data).lower() + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_capacity_planning(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSetupPanel checkbox[name=isCapacity]',
                                         '[0].value')
        if str(ui_cmd_obj.return_data).lower() == str(arg_dict["the_value"]).lower():
            self.logger.log_info("\nThe archive has expected Archive Capacity Planning Data value '" +
                                 str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Archive Capacity Planning Data value '" +
                                 str(arg_dict["the_value"]).lower() +
                                 "'.\nThe Archive Capacity Planning Data value is '" +
                                 str(ui_cmd_obj.return_data).lower() + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_frequency(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSchedulePanel combo[name=saveFrequency]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info("\nThe archive has expected Frequency value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Frequency value '" +
                                 str(arg_dict["the_value"]) + "'.\nThe archive Frequency value is '" +
                                 str(ui_cmd_obj.return_data) + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_date(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSchedulePanel datefield[name=date]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info("\nThe archive has expected Date value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Date value '" +
                                 str(arg_dict["the_value"]) + "'.\nThe archive Date value is '" +
                                 str(ui_cmd_obj.return_data) + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_archive_start_time(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveDetailsPanel #archiveDetailsSchedulePanel timefield[name=startTime]',
                                         '[0].rawValue')
        if ui_cmd_obj.return_data == arg_dict["the_value"]:
            self.logger.log_info("\nThe archive has expected Start Time value '" + str(arg_dict["the_value"]) + "'.\n")
        else:
            self.logger.log_info("\nThe archive does not have expected Start Time value '" +
                                 str(arg_dict["the_value"]) + "'.\nThe archive Start Time value is '" +
                                 str(ui_cmd_obj.return_data) + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_version_device_count(self, ui_cmd_obj, arg_dict):
        # Find the number of devices
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numDevices]',
                                         '[0].value')
        num_devices = ui_cmd_obj.return_data

        if str(num_devices) == str(arg_dict["the_value"]):
            self.logger.log_info("\nThe archive had the expected number of devices '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info("\nThe archive did not have the expected number of devices '" + arg_dict["the_value"] +
                                 "'.\nThe number of devices in the archive version is '" + num_devices + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_version_success_count(self, ui_cmd_obj, arg_dict):
        # Find the number successful
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numSuccess]',
                                         '[0].value')
        num_success = ui_cmd_obj.return_data

        if str(num_success) == str(arg_dict["the_value"]):
            self.logger.log_info(
                "\nThe archive had the expected number of successes '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info(
                "\nThe archive did not have the expected number of successes '" + arg_dict["the_value"] +
                "'.\nThe number of successes in the archive version is '" + num_success + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_version_failed_count(self, ui_cmd_obj, arg_dict):
        # Find the number failed
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numFailed]',
                                         '[0].value')
        num_failed = ui_cmd_obj.return_data

        if str(num_failed) == str(arg_dict["the_value"]):
            self.logger.log_info("\nThe archive had the expected number of failures '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info(
                "\nThe archive did not have the expected number of failures '" + arg_dict["the_value"] +
                "'.\nThe number of failures in the archive version is '" + num_failed + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_version_aborted_count(self, ui_cmd_obj, arg_dict):
        # Find the number aborted
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab panel[title=Details] '
                                         'archiveVersionDetailsPanel ovdisplayfield[name=numAborted]',
                                         '[0].value')
        num_aborted = ui_cmd_obj.return_data

        if str(num_aborted) == str(arg_dict["the_value"]):
            self.logger.log_info("\nThe archive had the expected number of aborts '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info("\nThe archive did not have the expected number of aborts '" + arg_dict["the_value"] +
                                 "'.\nThe number of aborts in the archive version is '" + num_aborted + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_version_locked(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab radiofield[boxLabel=Locked]',
                                         '[0].value')

        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.logger.log_info(
                "\nThe archive version had the expected Lock Status '" + arg_dict["the_value"] + "'.\n")
        else:
            self.logger.log_info(
                "\nThe archive version did not have the expected Lock Status '" + arg_dict["the_value"] +
                "'.\nThe archive version Lock Status is '" + str(ui_cmd_obj.return_data) + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    # HELPER METHODS

    def archives_confirm_details_device_description(self, ui_cmd_obj, arg_dict):
        # Find the device description field
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab ovdisplayfield[name=description]', '[0]')
        if ui_cmd_obj.return_data is not None:
            # Get the value of the device description field
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab ovdisplayfield[name=description]',
                                             '[0].rawValue')
            if ui_cmd_obj.return_data is not None:
                if ui_cmd_obj.return_data == arg_dict['the_value']:
                    ui_cmd_obj.error_state = False
                    self.logger.log_info("\nDevice has expected description '" + arg_dict['the_value'] + "'.\n")
                else:
                    ui_cmd_obj.error_state = True
                    self.logger.log_info(
                        "\nDevice does not have expected description '" + arg_dict['the_value'] + "'.\n" +
                        "The description is '" + ui_cmd_obj.return_data + "'.\n")
            else:
                self.logger.log_info("\nCould not get value of Device Description field\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find Device Description field\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def archives_confirm_details_device_description_contains(self, ui_cmd_obj, arg_dict):
        # Find the device description field
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab ovdisplayfield[name=description]', '[0]')
        if ui_cmd_obj.return_data is not None:
            # Get the value of the device description field
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab ovdisplayfield[name=description]',
                                             '[0].rawValue')

            if ui_cmd_obj.return_data is not None:
                if arg_dict['the_value'] in ui_cmd_obj.return_data:
                    self.logger.log_info("\nDevice description contains '" + arg_dict['the_value'] + "'.\n")
                    if StringUtils.string_to_boolean(arg_dict['exists']) is True:
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True
                else:
                    self.logger.log_info("\nDevice description does not contain '" + arg_dict['the_value'] + "'.\n" +
                                         "The description is '" + ui_cmd_obj.return_data + "'.\n")
                    if StringUtils.string_to_boolean(arg_dict['exists']) is False:
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nCould not get value of Device Description field\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find Device Description field\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def restore_archive_version(self, ui_cmd_obj, archive_name, oldest_or_newest):
        # Display the Restore dialog
        self.tree_select_context_menu_for_archive_version(ui_cmd_obj, archive_name, oldest_or_newest, "Restore...")

        # Expand the archive in the Restore dialog
        self.ext_builder.double_click(ui_cmd_obj,
                                      'archiveRestoreSelectionPanel treeview => .x-tree-node-text:textEquals(' +
                                      archive_name + ')')

        # Get the name of the version to restore
        self.get_archive_version_name(ui_cmd_obj, archive_name, oldest_or_newest)
        version_name = ui_cmd_obj.return_data
        if ui_cmd_obj.error_state is False:
            # Select the version in the Restore dialog
            self.ext_builder.click(ui_cmd_obj,
                                   'archiveRestoreSelectionPanel treeview => .x-tree-node-text:textEquals(' +
                                   version_name + ')')

            # Click the arrow to move the version to the restore list
            self.ext_builder.click(ui_cmd_obj,
                                   r'#restoreSelectionButtonPanel button[text=\&\#9658\;] => .x-btn-inner-gray-small')

            # Click the Start button
            self.ext_builder.click(ui_cmd_obj, 'button[actionId=archiveRestoreStart] => .x-btn-inner-blue-small')
        else:
            # Close the dialog and record the error
            self.ext_builder.click(ui_cmd_obj, 'button[text=Close] => .x-btn-inner-default-small')
            self.logger.log_info("\nCould not find version to restore.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def restore_archive_version_device(self, ui_cmd_obj, archive_name, oldest_or_newest, device_ip):
        # Expand the archive in the Restore dialog
        self.ext_builder.double_click(ui_cmd_obj,
                                      'archiveRestoreSelectionPanel treeview => .x-tree-node-text:textEquals(' +
                                      archive_name + ')')

        # Get the name of the version to restore
        self.get_archive_version_name(ui_cmd_obj, archive_name, oldest_or_newest)
        version_name = ui_cmd_obj.return_data
        if ui_cmd_obj.error_state is False:
            # Expand the version in the Restore dialog
            self.ext_builder.double_click(ui_cmd_obj,
                                          'archiveRestoreSelectionPanel treeview => .x-tree-node-text:textEquals(' +
                                          version_name + ')')

            # Select the device in the Restore dialog
            self.ext_builder.click(ui_cmd_obj,
                                   'archiveRestoreSelectionPanel treeview => .x-tree-node-text:textEquals(' +
                                   device_ip + ')')

            # Click the arrow to move the version to the restore list
            self.ext_builder.click(ui_cmd_obj,
                                   r'#restoreSelectionButtonPanel button[text=\&\#9658\;] => .x-btn-inner-gray-small')

            # Click the Start button
            self.ext_builder.click(ui_cmd_obj, 'button[actionId=archiveRestoreStart] => .x-btn-inner-blue-small')
        else:
            # Close the dialog and record the error
            self.ext_builder.click(ui_cmd_obj, 'button[text=Close] => .x-btn-inner-default-small')
            self.logger.log_info("\nCould not find version to restore device from.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def get_archive_version_name(self, ui_cmd_obj, archive_name, oldest_or_newest):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', archive_name)

        # Find the index of the archive
        self.ext_builder.get_component_index(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                             '[0]', 'text', archive_name)
        archive_index = ui_cmd_obj.return_data
        if archive_index != -1:
            # Determine the number of versions this archive has
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                             '[0].store.data.items[' + str(archive_index) + '].childNodes.length')
            version_count = int(ui_cmd_obj.return_data)
            if version_count > 0:
                # Get the name of the desired version (indexing is 0-based): oldest is first, newest is last
                version_index = 0
                if oldest_or_newest == "newest":
                    version_index = version_count - 1
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                                 '[0].store.data.items[' + str(archive_index) + '].childNodes[' +
                                                 str(version_index) + '].data.text')
            else:
                self.logger.log_info("\nArchive '" + archive_name + "' does not contain any versions.\n")
                ui_cmd_obj.return_data = ""
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find archive '" + archive_name + "'.\n")
            ui_cmd_obj.return_data = ""
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def tree_select_context_menu_for_archive_version(self, ui_cmd_obj, archive_name, oldest_or_newest, menu_name):
        # Make sure the archive is expanded
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkArchivesTab #mainArchiveTree',
                                          '[0]', 'text', archive_name)

        # Determine the name of the version to access the context menu for
        self.get_archive_version_name(ui_cmd_obj, archive_name, oldest_or_newest)
        if ui_cmd_obj.error_state is False:
            # Access the context menu for the node with the version name we just found
            self.ext_builder.right_click(ui_cmd_obj,
                                         '#networkTabPanel #networkArchivesTab #mainArchiveTree treeview => '
                                         '.x-tree-node-text:contains(' + ui_cmd_obj.return_data + ')')
            # Select the menu
            self.ext_builder.click(ui_cmd_obj,
                                   '#firmwareTreeMenu{isVisible()} menuitem[text=' + menu_name +
                                   '] => .x-menu-item-text')
        return ui_cmd_obj

    def tree_select_context_menu_for_archive_version_device(self, ui_cmd_obj, archive_name, oldest_or_newest, device_ip,
                                                            menu_name):
        # Make sure the correct version is expanded
        arg_dict = {"archive_name": archive_name}
        if oldest_or_newest == "oldest":
            self.archives_tree_expand_oldest_archive_version(ui_cmd_obj, arg_dict)
        else:
            self.archives_tree_expand_newest_archive_version(ui_cmd_obj, arg_dict)

        # Select the context menu for the specified device
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab #mainArchiveTree treeview => '
                                     '.x-tree-node-text:textEquals(' + device_ip + ')')

        # Select the desired menu
        self.ext_builder.click(ui_cmd_obj,
                               '#firmwareTreeMenu{isVisible()} menuitem[text=' + menu_name + '] => .x-menu-item-text')

        return ui_cmd_obj

    def table_select_context_menu_for_archive_version(self, ui_cmd_obj, archive_name, oldest_or_newest, menu_name):
        # Select the archive in the tree
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab #mainArchiveTree => '
                               '.x-tree-node-text:textEquals(' + archive_name + ')')

        sort_direction = "#descItem"
        if oldest_or_newest == "oldest":
            sort_direction = "#ascItem"

        # Sort the table by the Version column, descending for newest, ascending for oldest, so the correct archive
        # is at the top
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab panel '
                                     'archiveVersionGrid[viewId=Archive_Versions] gridcolumn[text=Version] => '
                                     '.x-column-header-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab panel '
                               'archiveVersionGrid[viewId=Archive_Versions] gridcolumn[text=Version] => '
                               '.x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab '
                               'archiveVersionGrid[viewId=Archive_Versions] menu ' + sort_direction + ' => '
                               '.x-menu-item-text')

        # Select the first row in the table, which should be the correct row based on the sort direction
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkArchivesTab panel '
                               'archiveVersionGrid[viewId=Archive_Versions] => table.x-grid-item:nth-child(1)')

        # Access the context menu for the first item in the table
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab panel '
                                     'archiveVersionGrid[viewId=Archive_Versions] => table.x-grid-item:nth-child(1)')

        # Select the menu
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveVersionGridMenu{isVisible()} menuitem[text=' + menu_name + '] => '
                               '.x-menu-item-text')

        return ui_cmd_obj

    def table_select_context_menu_for_archive_version_device(self, ui_cmd_obj, archive_name, oldest_or_newest,
                                                             device_ip, menu_name):
        # Make sure the correct version is expanded
        arg_dict = {"archive_name": archive_name}
        if oldest_or_newest == "oldest":
            self.archives_tree_select_oldest_archive_version(ui_cmd_obj, arg_dict)
        else:
            self.archives_tree_select_newest_archive_version(ui_cmd_obj, arg_dict)

        # Select the context menu for the specified device
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkArchivesTab '
                                     'archiveConfigurationGrid[panelId=mainConfigGrid] tableview => '
                                     '.x-grid-cell-inner:textEquals(' + device_ip + ')')

        # Select the desired menu
        self.ext_builder.click(ui_cmd_obj,
                               '#archiveConfigGridMenu{isVisible()} menuitem[text=' + menu_name +
                               '] => .x-menu-item-text')

        return ui_cmd_obj

    def archive_details_enable_disable_ips(self, ui_cmd_obj, ip_list, desired_state):
        ip_str_list = ip_list.split(",")
        for ip_str in ip_str_list:
            # Set the state of the check button if it isn't already at the desired state

            # Figure out how many items are in the table
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#networkTabPanel #networkArchivesTab '
                                                          '#archiveDetailsGeneralPanel #archiveDevicesGrid gridview',
                                                          '[0].store.data.items.length')
            item_count = int(ui_cmd_obj.return_data)
            item_count += 1

            # Loop through the table items, searching for the node to act on
            for item_index in range(0, item_count):
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#networkTabPanel #networkArchivesTab '
                                                              '#archiveDetailsGeneralPanel #archiveDevicesGrid '
                                                              'gridview', '[0].store.data.items[' +
                                                              str(item_index) + '].data.ipAddress')
                if ui_cmd_obj.return_data == ip_str:
                    # Check the current checked state of the node
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#networkTabPanel #networkArchivesTab '
                                                                  '#archiveDetailsGeneralPanel #archiveDevicesGrid '
                                                                  'gridview', '[0].store.data.items[' +
                                                                  str(item_index) + '].data.enabled')
                    node_checked = ui_cmd_obj.return_data
                    if node_checked is not desired_state:
                        self.ext_builder.click(ui_cmd_obj,
                                               '#networkTabPanel #networkArchivesTab #archiveDetailsGeneralPanel '
                                               '#archiveDevicesGrid gridview => .x-grid-item:contains(' +
                                               ip_str + ') .x-grid-checkcolumn')
                    else:
                        self.logger.log_info("\nIP '" + ip_str + "' is already at desired state.\n")
                    break

        return ui_cmd_obj
