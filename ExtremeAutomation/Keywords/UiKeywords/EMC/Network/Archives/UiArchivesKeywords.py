from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ArchivesConstants import ArchivesConstants


class UiArchivesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiArchivesKeywords, self).__init__()
        self.api_const = self.constants.API_ARCHIVES
        self.cmd = ArchivesConstants()

    def archives_click_create(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Create' button to display the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_CLICK_CREATE, **kwargs)

    def archives_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Refresh' button to refresh the Archives tree.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_CLICK_REFRESH, **kwargs)

    def archives_tree_expand_node(self, element_name, node_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [node_name] -     Name of the tree node to expand

        Expands the specified node in the Archives tree.
        """
        args = {"node_name": node_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_EXPAND_NODE, **kwargs)

    def archives_tree_collapse_node(self, element_name, node_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [node_name] -     Name of the tree node to collapse

        Collapses the specified node in the Archives tree.
        """
        args = {"node_name": node_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_COLLAPSE_NODE, **kwargs)

    def archives_tree_select_node(self, element_name, node_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [node_name] -     Name of the tree node to select

        Selects the specified node in the Archives tree.
        """
        args = {"node_name": node_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_SELECT_NODE, **kwargs)

    def archives_tree_expand_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to expand the newest version for

        Expands the newest version for the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_EXPAND_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_expand_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to expand the oldest version for

        Expands the oldest version for the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_EXPAND_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_collapse_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to collapse the newest version for

        Collapses the newest version for the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_COLLAPSE_NEWEST_ARCHIVE_VERSION,
                                    **kwargs)

    def archives_tree_collapse_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to collapse the oldest version for

        Collapses the oldest version for the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_COLLAPSE_OLDEST_ARCHIVE_VERSION,
                                    **kwargs)

    def archives_tree_select_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to select the newest version of

        Selects the newest version of the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_SELECT_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_select_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to select the oldest version of

        Selects the oldest version of the specified archive in the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_SELECT_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_create(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Create' button to display the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_TREE_CREATE, **kwargs)

    def archives_tree_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Refresh' button to refresh the Archives tree.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_TREE_REFRESH, **kwargs)

    def archives_tree_delete_archive(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete

        Deletes the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_DELETE_ARCHIVE, **kwargs)

    def archives_tree_delete_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete the newest version of

        Deletes the newest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_DELETE_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_delete_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete the oldest version of

        Deletes the oldest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_DELETE_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_delete_newest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from
        [device_ip] -     IP address of the device to delete

        Deletes the specified device from the newest version of the specified archive via the Archives tree.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_DELETE_NEWEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_tree_delete_oldest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from
        [device_ip] -     IP address of the device to delete

        Deletes the specified device from the oldest version of the specified archive via the Archives tree.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_DELETE_OLDEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_tree_lock_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to lock

        Locks the newest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_LOCK_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_lock_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to lock

        Locks the oldest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_LOCK_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_unlock_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to unlock

        Unlocks the newest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_UNLOCK_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_unlock_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to unlock

        Unlocks the oldest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_UNLOCK_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_rename_archive(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to rename

        Opens the Rename Archive dialog via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_RENAME_ARCHIVE, **kwargs)

    def archives_tree_restore_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore

        Restores the newest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_RESTORE_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_restore_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore

        Restores the oldest version of the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_RESTORE_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_tree_restore_newest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore
        [device_ip] -     IP address of the device to restore

        Restores the specified device from the newest version of the specified archive via the Archives tree.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_RESTORE_NEWEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_tree_restore_oldest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore
        [device_ip] -     IP address of the device to restore

        Restores the specified device from the oldest version of the specified archive via the Archives tree.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_RESTORE_OLDEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_tree_stamp_new_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to stamp a new version on

        Stamps a new version for the specified archive via the Archives tree.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_STAMP_NEW_VERSION, **kwargs)

    def archives_tree_view_config_file(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address to access the configuration file for

        Accesses 'View Configuration File...' from the context menu for the specified device via the Archives tree.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TREE_VIEW_CONFIG_FILE, **kwargs)

    def archives_table_select_archive(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to select

        Select the specified archive in the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_SELECT_ARCHIVE, **kwargs)

    def archives_table_delete_archive(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete

        Deletes the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_DELETE_ARCHIVE, **kwargs)

    def archives_table_delete_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from

        Deletes the newest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_DELETE_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_delete_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from

        Deletes the oldest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_DELETE_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_delete_newest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from
        [device_ip] -     IP address of the device to delete

        Deletes the specified device from the newest version of the specified archive via the Archives table.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_DELETE_NEWEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_table_delete_oldest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to delete from
        [device_ip] -     IP address of the device to delete

        Deletes the specified device from the oldest version of the specified archive via the Archives table.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_DELETE_OLDEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_table_lock_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to lock

        Locks the newest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_LOCK_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_lock_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to lock

        Locks the oldest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_LOCK_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_unlock_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to unlock

        Unlocks the newest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_UNLOCK_NEWEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_unlock_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to unlock

        Unlocks the oldest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_UNLOCK_OLDEST_ARCHIVE_VERSION, **kwargs)

    def archives_table_rename_archive(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to rename

        Opens the Rename Archive dialog via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_RENAME_ARCHIVE, **kwargs)

    def archives_table_restore_newest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore

        Restores the newest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_RESTORE_NEWEST_ARCHIVE_VERSION,
                                    **kwargs)

    def archives_table_restore_oldest_archive_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore

        Restores the oldest version of the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_RESTORE_OLDEST_ARCHIVE_VERSION,
                                    **kwargs)

    def archives_table_restore_newest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore
        [device_ip] -     IP address of the device to restore

        Restores the specified device from the newest version of the specified archive via the Archives table.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_RESTORE_NEWEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_table_restore_oldest_archive_version_device(self, element_name, archive_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to restore
        [device_ip] -     IP address of the device to restore

        Restores the specified device from the oldest version of the specified archive via the Archives table.
        """
        args = {"device_ip": device_ip,
                "archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_RESTORE_OLDEST_ARCHIVE_VERSION_DEVICE,
                                    **kwargs)

    def archives_table_stamp_new_version(self, element_name, archive_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to stamp a new version on

        Stamps a new version for the specified archive via the Archives table.
        """
        args = {"archive_name": archive_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_STAMP_NEW_VERSION, **kwargs)

    def archives_table_view_config_file(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address to access the configuration file for

        Accesses 'View Configuration File...' from the context menu for the specified device via the Archives table.
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_TABLE_VIEW_CONFIG_FILE, **kwargs)

    def archives_details_select_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the details tab to select

        Selects the specified tab in the Details panel.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_SELECT_TAB, **kwargs)

    def archives_details_click_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Save" button in the details panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DETAILS_CLICK_SAVE, **kwargs)

    def archives_details_archive_set_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Description field

        Sets the value of the 'Description' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_DESCRIPTION, **kwargs)

    def archives_details_archive_set_ips_enabled(self, element_name, ip_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_list] -       Comma-separated list of IPs to enable

        Enables the specified IPs in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"ip_list": ip_list}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_IPS_ENABLED, **kwargs)

    def archives_details_archive_set_ips_disabled(self, element_name, ip_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_list] -       Comma-separated list of IPs to disable

        Disables the specified IPs in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"ip_list": ip_list}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_IPS_DISABLED, **kwargs)

    def archives_details_archive_set_process_groups(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Process in Groups Of field

        Sets the value of the 'Process in Groups Of' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_PROCESS_GROUPS, **kwargs)

    def archives_details_archive_set_abort_on_failure(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Abort on Failure field (True/False)

        Sets the selection state of the 'Abort on Failure' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_ABORT_ON_FAILURE,
                                    **kwargs)

    def archives_details_archive_set_max_versions_unlimited(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Selects the 'Unlimited' radio button for the Max Versions field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_MAX_VERSIONS_UNLIMITED,
                                    **kwargs)

    def archives_details_archive_set_max_versions_value(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Description field

        Selects the 'Maximum # of Versions' radio button and sets the associated value for the Max Versions field
        in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_MAX_VERSIONS_VALUE,
                                    **kwargs)

    def archives_details_archive_set_archive_configuration_data(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Archive Configuration Data field (True/False)

        Sets the selection state of the 'Archive Configuration Data' field in the details panel for the selected
        archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_ARCHIVE_CONFIGURATION_DATA, **kwargs)

    def archives_details_archive_set_archive_capacity_planning_data(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Archive Capacity Planning Data field (True/False)

        Sets the selection state of the 'Archive Capacity Planning Data' field in the details panel for the selected
        archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_ARCHIVE_CAPACITY_PLANNING_DATA, **kwargs)

    def archives_details_archive_set_run_governance(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set for the Run Governance field (True/False)

        Sets the selection state of the 'Run Governance' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_RUN_GOVERNANCE, **kwargs)

    def archives_details_archive_select_regime(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to select in the Regime field

        Sets the value of the 'Regime' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SELECT_REGIME, **kwargs)

    def archives_details_archive_set_frequency(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Frequency field

        Sets the value of the 'Frequency' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_FREQUENCY, **kwargs)

    def archives_details_archive_set_date(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Date field

        Sets the value of the 'Date' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_DATE, **kwargs)

    def archives_details_archive_set_start_time(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to set in the Start Time field

        Sets the value of the 'Start Time' field in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_ARCHIVE_SET_START_TIME, **kwargs)

    def archives_details_archive_click_configure_devices(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Configure Devices..." button in the details panel for the selected archive.
        Assumes the details panel is already displaying the archive to configure devices for.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DETAILS_ARCHIVE_CLICK_CONFIGURE_DEVICES,
                                    **kwargs)

    def archives_details_version_set_locked(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Locked field (True/False)

        Sets the value of the 'Locked' field in the details panel for the selected archive version.
        Assumes the details panel is already displaying the archive version to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_VERSION_SET_LOCKED, **kwargs)

    def archives_details_version_set_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Description field

        Sets the value of the 'Description' field in the details panel for the selected archive version.
        Assumes the details panel is already displaying the archive version to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_VERSION_SET_DESCRIPTION, **kwargs)

    def archives_details_device_set_memo(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Memo field

        Sets the value of the 'Memo' field in the details panel for the selected device.
        Assumes the details panel is already displaying the archive version to modify.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DETAILS_DEVICE_SET_MEMO, **kwargs)

    def archives_dialog_configure_devices_add_archive_member_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Device/group which should be moved to the Archive Members list

        Adds the specified device to the Archive Members list in the Configure Device dialog.
        This is different than adding a group because an exact match on the IP address will be made, as opposed to the
        partial match which is made on the group name (which is necessary since the group name nodes contain the number
        of children nodes as a suffix).
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_ADD_ARCHIVE_MEMBER_DEVICE, **kwargs)

    def archives_dialog_configure_devices_add_archive_member_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Comma-separated list of groups to add to the archive

        Adds the specified groups to the 'Archive Members' list in the Configure Devices dialog.
        Assumes the Configure Devices dialog is already displayed.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_ADD_ARCHIVE_MEMBER_GROUP, **kwargs)

    def archives_dialog_configure_devices_remove_archive_member_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     IP of the device which should be removed from the Archive Members list

        Removes the specified device from the Archive Members list in the Configure Devices dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_REMOVE_ARCHIVE_MEMBER_DEVICE, **kwargs)

    def archives_dialog_configure_devices_remove_archive_member_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the group which should be removed from the Archive Members list

        Removes the specified device group from the Archive Members list in the Configure Devices dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_REMOVE_ARCHIVE_MEMBER_GROUP, **kwargs)

    def archives_dialog_configure_devices_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks OK in the Configure Devices dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_CLICK_OK, **kwargs)

    def archives_dialog_configure_devices_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Cancel in the Configure Devices dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIGURE_DEVICES_CLICK_CANCEL, **kwargs)

    def archives_dialog_confirm_delete_archive_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_ARCHIVE_CLICK_YES,
                                    **kwargs)

    def archives_dialog_confirm_delete_archive_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_ARCHIVE_CLICK_NO,
                                    **kwargs)

    def archives_dialog_confirm_delete_version_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete Version dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_VERSION_CLICK_YES,
                                    **kwargs)

    def archives_dialog_confirm_delete_version_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete Version dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_VERSION_CLICK_NO,
                                    **kwargs)

    def archives_dialog_confirm_delete_device_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete Device dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_DEVICE_CLICK_YES,
                                    **kwargs)

    def archives_dialog_confirm_delete_device_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete Device dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CONFIRM_DELETE_DEVICE_CLICK_NO, **kwargs)

    def archives_dialog_create_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Name field

        Sets the value of the 'Name' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_NAME, **kwargs)

    def archives_dialog_create_set_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Description field

        Sets the value of the 'Description' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_DESCRIPTION, **kwargs)

    def archives_dialog_create_set_max_versions_unlimited(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Sets the Max Versions to 'Unlimited' in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_SET_MAX_VERSIONS_UNLIMITED,
                                    **kwargs)

    def archives_dialog_create_set_max_versions_value(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Max Versions field

        Sets the Max Versions to the specified value in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_MAX_VERSIONS_VALUE,
                                    **kwargs)

    def archives_dialog_create_set_archive_configuration_data(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Indicates whether to select or deselect the Archive Configuration Data check box (True/False)

        Sets the value of the 'Archive Configuration Data' checkbox in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_ARCHIVE_CONFIGURATION_DATA,
                                    **kwargs)

    def archives_dialog_create_set_archive_capacity_planning_data(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value]     - Indicates whether to select or deselect the Archive Capacity Planning Data check box
                          (True/False)

        Sets the value of the 'Archive Capacity Planning Data' checkbox in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_DIALOG_CREATE_SET_ARCHIVE_CAPACITY_PLANNING_DATA, **kwargs)

    def archives_dialog_create_add_archive_member_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Device/group which should be moved to the Archive Members list

        Adds the specified device to the Archive Members list in the Create Archive dialog.
        This is different than adding a group because an exact match on the IP address will be made, as opposed to the
        partial match which is made on the group name (which is necessary since the group name nodes contain the number
        of children nodes as a suffix).
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_ADD_ARCHIVE_MEMBER_DEVICE,
                                    **kwargs)

    def archives_dialog_create_add_archive_member_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Device/group which should be moved to the Archive Members list

        Adds the specified group to the Archive Members list in the Configure Device dialog.
        This is different than adding a device because a partial match is made on the group name (which is necessary
        since the group name nodes contain the number of children nodes as a suffix), as opposed to the exact match
        made on the device IP address.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_ADD_ARCHIVE_MEMBER_GROUP,
                                    **kwargs)

    def archives_dialog_create_remove_archive_member_device(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     IP of the device which should be removed from the Archive Members list

        Removes the specified device from the Archive Members list in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_REMOVE_ARCHIVE_MEMBER_DEVICE,
                                    **kwargs)

    def archives_dialog_create_remove_archive_member_group(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Name of the group which should be removed from the Archive Members list

        Removes the specified device group from the Archive Members list in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_REMOVE_ARCHIVE_MEMBER_GROUP,
                                    **kwargs)

    def archives_dialog_create_set_frequency(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Frequency field

        Sets the value of the 'Frequency' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_FREQUENCY, **kwargs)

    def archives_dialog_create_set_date(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Date field

        Sets the value of the 'Date' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_DATE, **kwargs)

    def archives_dialog_create_set_start_time(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Start Time field

        Sets the value of the 'Start Time' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_START_TIME, **kwargs)

    def archives_dialog_create_set_process_groups(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to use in the Process in Groups Of field

        Sets the value of the 'Process in Groups Of' field in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_PROCESS_GROUPS, **kwargs)

    def archives_dialog_create_set_abort_on_failure(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Indicates whether to select or deselect the Abort on Failure check box (True/False)

        Sets the value of the 'Abort on Failure' checkbox in the Create Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_ABORT_ON_FAILURE, **kwargs)

    def archives_dialog_create_set_ip_sort_ascending(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Sets the value of the 'Archive Capacity Planning Data' checkbox in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_SET_IP_SORT_ASCENDING, **kwargs)

    def archives_dialog_create_set_ip_sort_descending(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Sets the device list in the Create Archive dialog to be sorted ascending by the IP Address column.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_SET_IP_SORT_DESCENDING, **kwargs)

    def archives_dialog_create_set_ips_disabled(self, element_name, ip_list, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_list] -       Comma-separated list of IP addreses to disable

        Disables the specified IP addresses in the device list of the Create Archive dialog.
        """
        args = {"ip_list": ip_list}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_CREATE_SET_IPS_DISABLED, **kwargs)

    def archives_dialog_create_click_next(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Next' button in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_CLICK_NEXT, **kwargs)

    def archives_dialog_create_click_previous(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Previous' button in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_CLICK_PREVIOUS, **kwargs)

    def archives_dialog_create_click_finish(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Finish' button in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_CLICK_FINISH, **kwargs)

    def archives_dialog_create_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Cancel' button in the Create Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_CREATE_CLICK_CANCEL, **kwargs)

    def archives_dialog_rename_set_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to enter for the archive's new name

        Enters the new name in the Rename Archive dialog.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_RENAME_SET_NAME, **kwargs)

    def archives_dialog_rename_click_ok(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'OK' button in the Rename Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_RENAME_CLICK_OK, **kwargs)

    def archives_dialog_rename_click_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the 'Cancel' button in the Rename Archive dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_RENAME_CLICK_CANCEL, **kwargs)

    def archives_dialog_view_config_file_find(self, element_name, the_value, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     String to search for in the configuration file
        [exists] -        Indicates whether the value is expected to be found or not (True/False)

        Searches for the specified string in the configuration file.
        Passes/fails the test based on the expected value indicated by the "exists" argument.
        NOTE: The 'View Configuration File' dialog must already be open.
        """
        args = {"exists": exists,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_FIND, **kwargs)

    def archives_dialog_view_config_file_find_in_named_block(self, element_name, block_name, the_value, exists,
                                                             **kwargs):
        """Returns the result of archives_dialog_view_config_file_find_in_named_block."""
        args = {"block_name": block_name,
                "exists": exists,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_FIND_IN_NAMED_BLOCK,
                                    **kwargs)

    def archives_dialog_view_config_file_line_contains(self, element_name, value_list, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [value_list] -    Comma-separated list of strings to search for on a line in the configuration file
        [exists] -        Indicates whether the value is expected to be found or not (True/False)

        Checks whether or not a line in the configuration file contains the specified string(s).
        Passes/fails the test based on the expected value indicated by the "exists" argument.
        NOTE: The 'View Configuration File' dialog must already be open.
        """
        args = {"value_list": value_list,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_LINE_CONTAINS,
                                    **kwargs)

    def archives_dialog_view_config_click_close(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks 'Close' in the View Configuration File dialog.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_DIALOG_VIEW_CONFIG_CLICK_CLOSE, **kwargs)

    def archives_confirm_archive_exists(self, element_name, archive_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [archive_name] -  Name of the archive to search for
        [exists] -        Indicates whether the archive is expected to be found or not (True/False)

        Searches for the specified archive in the Archives tree.
        Passes/fails the test based on the expected value indicated by the "exists" argument.
        """
        args = {"archive_name": archive_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_ARCHIVE_EXISTS, **kwargs)

    def archives_confirm_archive_version_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of versions the archive is expected to have

        Verifies if the currently-selected archive has the specified number of versions.
        NOTE: the archive to check must already be selected.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_ARCHIVE_VERSION_COUNT, **kwargs)

    def archives_confirm_archive_version_success(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Verifies if the currently-selected archive version was successful for all devices.
        NOTE: the archive version to check must already be selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_CONFIRM_ARCHIVE_VERSION_SUCCESS, **kwargs)

    def archives_confirm_archive_version_aborted(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Verifies if the currently-selected archive version aborted correctly;  the number of successes should be less
        than the number of devices, the number of failures should be one, and the number of successe, failures, and
        aborts should be the same as the number of devices.
        NOTE: the archive version to check must already be selected.
        """
        return self.execute_keyword(element_name, {}, self.cmd.ARCHIVES_CONFIRM_ARCHIVE_VERSION_ABORTED, **kwargs)

    def archives_confirm_archive_contains_devices(self, element_name, device_list, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_list] -   Comma-separated list of devices to check for
        [exists] -        Indicates if the devices are expected to be present or not (True/False)

        Verifies if the currently-selected archive contains the specified devices or not.
        Passes/fails the test based on the expected value indicated by the "exists" argument:  the test passes
        if the devices are expected to be found and ALL devices are found, or if the devices are expected to be
        found and NONE of the devices are found - if some are found/some are not found, the test will fail.
        NOTE: the archive to check must already be selected.
        """
        args = {"exists": exists,
                "device_list": device_list}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_ARCHIVE_CONTAINS_DEVICES, **kwargs)

    def archives_confirm_details_archive_name(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the archive name to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected name.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_NAME, **kwargs)

    def archives_confirm_details_archive_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the description to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected description.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DESCRIPTION, **kwargs)

    def archives_confirm_details_archive_description_contains(self, element_name, the_value, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the description to verify
        [exists] -        Indicates whether or not the value is expected to exist in the description (True/False)

        Confirms whether or not the details panel for the currently-selected archive contains the specified string in
        the description.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"exists": exists,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DESCRIPTION_CONTAINS,
                                    **kwargs)

    def archives_confirm_details_archive_ips_enabled(self, element_name, ip_list, is_enabled, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [ip_list] -       Comma-separated list of IPs to verify
        [is_enabled] -    Indicates whether or not the specified IPs should be enabled or disabled (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected enabled state for
        the specified devices.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"is_enabled": is_enabled,
                "ip_list": ip_list}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_IPS_ENABLED, **kwargs)

    def archives_confirm_details_archive_process_groups(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the process groups to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected process groups.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_PROCESS_GROUPS,
                                    **kwargs)

    def archives_confirm_details_archive_abort_on_failure(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the abort on failure setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected abort on failure
        setting.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_ABORT_ON_FAILURE,
                                    **kwargs)

    def archives_confirm_details_archive_max_versions_value(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the max versions to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected max versions
        value.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_MAX_VERSIONS_VALUE,
                                    **kwargs)

    def archives_confirm_details_archive_max_versions_unlimited(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the unlimited max versions setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected unlimited max
        versions setting.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args,
                                    self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_MAX_VERSIONS_UNLIMITED, **kwargs)

    def archives_confirm_details_archive_configuration_data(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the configuration data setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected configuration data
        setting.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_CONFIGURATION_DATA,
                                    **kwargs)

    def archives_confirm_details_archive_capacity_planning(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the capacity planning setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected capacity planning
        setting.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_CAPACITY_PLANNING,
                                    **kwargs)

    def archives_confirm_details_archive_run_governance(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the capacity planning setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected Run Governance
        setting.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_RUN_GOVERNANCE,
                                    **kwargs)

    def archives_confirm_details_archive_regime(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the capacity planning setting to verify (True/False)

        Confirms whether or not the details panel for the currently-selected archive has the expected regime selected.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_REGIME, **kwargs)

    def archives_confirm_details_archive_frequency(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the frequency to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected frequency.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_FREQUENCY, **kwargs)

    def archives_confirm_details_archive_date(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the date to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected date.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DATE, **kwargs)

    def archives_confirm_details_archive_start_time(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the start time to verify

        Confirms whether or not the details panel for the currently-selected archive has the expected start time.
        NOTE: the details panel must already be displaying the archive to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_START_TIME, **kwargs)

    def archives_confirm_details_version_device_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of devices the archive version is expected to have

        Verifies if the currently-selected archive version has the specified number of devices.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_DEVICE_COUNT,
                                    **kwargs)

    def archives_confirm_details_version_success_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of successes the archive version is expected to have

        Verifies if the currently-selected archive version has the specified number of successes.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_SUCCESS_COUNT,
                                    **kwargs)

    def archives_confirm_details_version_failed_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of failures the archive version is expected to have

        Verifies if the currently-selected archive version has the specified number of failures.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_FAILED_COUNT,
                                    **kwargs)

    def archives_confirm_details_version_aborted_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of aborts the archive version is expected to have

        Verifies if the currently-selected archive version has the specified number of aborts.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_ABORTED_COUNT,
                                    **kwargs)

    def archives_confirm_details_version_different_count(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Number of aborts the archive version is expected to have

        Verifies if the currently-selected archive version has the specified number of differences.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_DIFFERENT_COUNT,
                                    **kwargs)

    def archives_confirm_details_version_locked(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Lock state the archive version is expected to have (True/False)

        Verifies if the currently-selected archive version has the specified lock state.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_LOCKED, **kwargs)

    def archives_confirm_details_version_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the description to verify

        Confirms whether or not the details panel for the currently-selected version has the expected description.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_DESCRIPTION, **kwargs)

    def archives_confirm_details_version_description_contains(self, element_name, the_value, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to look for in the device's description

        Confirms whether or not the description in the details panel for the currently-selected archive version contains
        the specified string.
        NOTE: the details panel must already be displaying the archive version to check.
        """
        args = {"exists": exists,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_VERSION_DESCRIPTION_CONTAINS,
                                    **kwargs)

    def archives_confirm_details_device_description(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value of the description to verify

        Confirms whether or not the details panel for the currently-selected device has the expected description.
        NOTE: the details panel must already be displaying the device to check.
        """
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_DEVICE_DESCRIPTION, **kwargs)

    def archives_confirm_details_device_description_contains(self, element_name, the_value, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     Value to look for in the device's description

        Confirms whether or not the description in the details panel for the currently-selected device contains
        the specified string.
        NOTE: the details panel must already be displaying the device to check.
        """
        args = {"exists": exists,
                "the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.ARCHIVES_CONFIRM_DETAILS_DEVICE_DESCRIPTION_CONTAINS,
                                    **kwargs)
