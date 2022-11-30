from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.archives.NetworkArchivesWebElements import NetworkArchivesWebElements
from xiqse.elements.common.CommonErrorWebElements import CommonErrorWebElements
from xiqse.flows.common.XIQSE_CommonOperationsPanel import XIQSE_CommonOperationsPanel
from xiqse.flows.network.archives.XIQSE_NetworkArchivesCreateArchive import XIQSE_NetworkArchivesCreateArchive


class XIQSE_NetworkArchives(NetworkArchivesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.error_web_elements = CommonErrorWebElements()
        self.operations_panel = XIQSE_CommonOperationsPanel()
        self.create_dlg = XIQSE_NetworkArchivesCreateArchive()

    def xiqse_archives_click_create(self):
        """
        - This keyword clicks the Create button on the Network> Archives Tab
        - It is assumed the view is already navigated to the Archives tab.
        - Keyword Usage
        - ``XIQSE Archives Click Create``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_create_button()
        if the_button:
            self.utils.print_info("Clicking Create Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Create button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_click_refresh(self):
        """
        - This keyword clicks the Refresh button on the Network> Archives Tab
        - It is assumed the view is already navigated to the Archives tab.
        - Keyword Usage
        - ``XIQSE Archives Click Refresh``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_refresh_button()
        if the_button:
            self.utils.print_info("Clicking Refresh Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Refresh button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_archives_create_archive(self, name, device_ips, frequency=None):
        """
        - This keyword creates an archive with the specified name for the specified device.
        - It is assumed the Network> Archives view is currently displayed.
        - Keyword Usage
        - ``XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4``
        - ``XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4  Daily``
        - ``XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4  Never``

        :param name:          name to use when creating the archive
        :param device_ips:    comma-separated list of IP addresses to add to the archive
        :param frequency:     value to select in the Frequency field
        :return: 1 if action was successful, else -1
        """
        ret_val = self.xiqse_archives_click_create()
        if ret_val != -1:
            # Enter Name
            ret_val = self.create_dlg.xiqse_archives_create_dialog_enter_name(name)

            # Click Next
            if ret_val != -1:
                ret_val = self.create_dlg.xiqse_archives_create_dialog_click_next()

            # Move specified device to the Archive Members list
            if ret_val != -1:
                ip_list = device_ips.split(',')
                ip_count = len(ip_list)
                added_count = 0
                self.utils.print_info(f"Adding {ip_count} devices")
                for ip in ip_list:
                    if self.create_dlg.xiqse_archives_create_dialog_select_device_and_move_to_archive_members(ip) == 1:
                        added_count += 1
                if added_count == 0:
                    self.utils.print_info("Unable to add any devices to archive")
                    ret_val = -1
                else:
                    # As long as at least one device was added, we can continue with the archive creation
                    self.utils.print_info(f"Added {added_count} devices of the {ip_count} devices specified")

            # Click Next
            if ret_val != -1:
                ret_val = self.create_dlg.xiqse_archives_create_dialog_click_next()

            # Select the Frequency
            if ret_val != -1 and frequency:
                ret_val = self.create_dlg.xiqse_archives_create_dialog_select_frequency(frequency)

            # Click Finish
            if ret_val != -1:
                ret_val = self.create_dlg.xiqse_archives_create_dialog_click_finish()

            # Check for errors
            if ret_val == -1:
                self.utils.print_info(f"Unable to create archive {name} for device {ip}")
                self.create_dlg.xiqse_archives_create_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Create button")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_archives_select_archive(self, name):
        """
        - This keyword selects the specified archive in the Archives tree.
        - It is assumed the Network> Archives view is currently displayed.
        - Keyword Usage
        - ``XIQSE Archives Select Archive    MY_ARCHIVE``

        :param name: name of the archive to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_archives_click_refresh():
            tree_node = self.get_archive_tree_node(name)
            if tree_node:
                self.utils.print_info(f"Selecting archive tree node with name '{name}'")
                self.auto_actions.click(tree_node)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find archive tree node with name '{name}'")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_archives_stamp_new_version(self, name):
        """
        - This keyword selects "Stamp New Version" from the context menu of the specified archive in the Archives tree.
        - It is assumed the Network> Archives view is currently displayed.
        - Keyword Usage
        - ``XIQSE Archives Stamp New Version    MY_ARCHIVE``

        :param name: name of the archive to stamp a new version on
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_archives_click_refresh():
            tree_node = self.get_archive_tree_node(name)
            if tree_node:
                self.utils.print_info(f"Selecting archive tree node with name '{name}'")
                self.auto_actions.click(tree_node)

                self.utils.print_info(f"Accessing right click menu for '{name}'")
                self.auto_actions.right_click(tree_node)

                stamp_menu = self.get_archive_stamp_new_version_menu()
                if stamp_menu:
                    self.utils.print_info(f"Clicking Stamp New Version on context menu for '{name}'")
                    self.auto_actions.click(stamp_menu)
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to find Stamp New Version menu for archive '{name}'")
            else:
                self.utils.print_info(f"Unable to find archive tree node with name '{name}'")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_archives_delete_archive(self, name):
        """
        - This keyword deletes the specified archive in the Archives tree.
        - It is assumed the Network> Archives view is currently displayed.
        - Keyword Usage
        - ``XIQSE Archives Delete Archive    MY_ARCHIVE``

        :param name: name of the archive to delete
        :return: 1 if action was successful, 2 if archive was not found (already deleted?), else -1
        """
        ret_val = -1
        if self.xiqse_archives_click_refresh():
            tree_node = self.get_archive_tree_node(name)
            if tree_node:
                self.utils.print_info(f"Selecting archive tree node with name '{name}'")
                self.auto_actions.click(tree_node)

                self.utils.print_info(f"Accessing right click menu for '{name}'")
                self.auto_actions.right_click(tree_node)

                del_menu = self.get_archive_delete_menu()
                if del_menu:
                    self.utils.print_info(f"Clicking Delete on context menu for '{name}'")
                    self.auto_actions.click(del_menu)

                    # Confirm the delete
                    yes_btn = self.error_web_elements.get_message_box_yes_button()
                    if yes_btn:
                        self.utils.print_info(f"Clicking Yes button to confirm the delete")
                        self.auto_actions.click(yes_btn)
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Unable to find Yes button to confirm the delete")
                else:
                    self.utils.print_info(f"Unable to find Delete menu for archive '{name}'")
            else:
                self.utils.print_info(f"Unable to find archive tree node with name '{name}' - already deleted?")
                ret_val = 2

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_archive_exists(self, name, exists="true"):
        """
        - This keyword confirms the specified archive is present in the Archives tree.
        - It is assumed the Network> Archives view is currently displayed.
        - Keyword Usage
        - ``XIQSE Confirm Archive Exists    MY_ARCHIVE``

        :param name:   name of the archive to look for
        :param exists: indicates whether the archive should be present or not (true/false)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_archives_click_refresh():
            tree_node = self.get_archive_tree_node(name)
            if tree_node:
                self.utils.print_info(f"Archive '{name}' is present")
                if exists == "true":
                    self.utils.print_info("  matches expected")
                    ret_val = 1
                else:
                    self.utils.print_info("  does not match expected")
            else:
                self.utils.print_info(f"Archive '{name}' is not present")
                if exists == "false":
                    self.utils.print_info("  matches expected")
                    ret_val = 1
                else:
                    self.utils.print_info("  does not match expected")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_archive_added(self, name, retry_duration=5, retry_count=24):
        """
        - This keyword is used to wait for the archive to show up in the Archives tree.
        - This keyword by default loops 24 times every 5 seconds to check if the archive exists.
        - It is assumed the Network> Archives tab is already selected.
        - Keyword Usage:
        - ``XIQSE Wait Until Archive Added    ${ARCHIVE_MAME}    retry_duration=15    retry_count=10``

        :param name: name of the archive to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if archive added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for archive {name}: loop {count}")
            if self.xiqse_confirm_archive_exists(name) == 1:
                self.utils.print_info(f"Archive {name} has been added")
                return 1
            else:
                self.utils.print_info(f"Archive is not yet present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        # Check for archive one last time
        if self.xiqse_confirm_archive_exists(name) == 1:
            self.utils.print_info(f"Archive {name} has been added")
            return 1

        self.utils.print_info(f"Archive {name} does not exist. Please check.")
        self.screen.save_screen_shot()

        return -1

    def xiqse_wait_until_archive_removed(self, name, retry_duration=5, retry_count=24):
        """
        - This keyword is used to wait for the archive to be removed from the Archives tree.
        - This keyword by default loops 24 times every 5 seconds to check if the archive exists.
        - It is assumed the Network> Archives tab is already selected.
        - Keyword Usage:
        - ``XIQSE Wait Until Archive Removed    ${ARCHIVE_MAME}    retry_duration=15    retry_count=10``

        :param name: name of the archive to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if archive removed within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for archive {name}: loop {count}")
            if self.xiqse_confirm_archive_exists(name, "false") == 1:
                self.utils.print_info(f"Archive {name} has been removed")
                return 1
            else:
                self.utils.print_info(f"Archive is still present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        # Check for archive one last time
        if self.xiqse_confirm_archive_exists(name, "false") == 1:
            self.utils.print_info(f"Archive {name} has been removed")
            return 1

        self.utils.print_info(f"Archive {name} still exists. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_until_archive_complete(self, retry_duration=30, retry_count=10):
        """
        - This keyword waits until the archive has completed by checking the Inventory Audit entry in the
        - Operations panel for progress value of 100%.
        - Keyword Usage
        - ``XIQSE Wait Until Archive Complete``
        - ``XIQSE Wait Until Archive Complete    retry_duration=10  retry_count=60``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if action was successful, else -1
        """
        return self.operations_panel.xiqse_operations_wait_until_operation_complete("Inventory Audit",
                                                                                    retry_duration, retry_count)

    def xiqse_wait_until_restore_complete(self, retry_duration=30, retry_count=20):
        """
        - This keyword waits until the restore has completed by checking the Inventory Audit entry in the
        - Operations panel for progress value of 100%.
        - Keyword Usage
        - ``XIQSE Wait Until Restore Complete``
        - ``XIQSE Wait Until Restore Complete    retry_duration=10  retry_count=60``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if action was successful, else -1
        """
        return self.operations_panel.xiqse_operations_wait_until_operation_complete("Inventory Audit",
                                                                                    retry_duration, retry_count)
