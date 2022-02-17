from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.backup_restore.AdminBackupRestoreWebElements import AdminBackupRestoreWebElements
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator


class XIQSE_Backup(AdminBackupRestoreWebElements):
    def __init__(self):
        super().__init__()
        self.overwrite_file = AdminBackupRestoreWebElements()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = AdminBackupRestoreWebElements()
        self.xiqse_nav = XIQSE_CommonNavigator()

    def xiqse_backup_database_set_name(self, the_value):
        """
         - This keyword sets the Backup File Name value in the File Name text field.
         - It is assumed the Backup/Restore tab is already opened.
         - Keyword Usage
          - ``XIQSE Backup Database Set Name  ${BACKUP_NAME}``

        :param the_value:  Value entered into backup file name dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        file_name = self.get_text_input_backup_name()
        if file_name:
            self.utils.print_info(f"Entering {the_value} into the File Name field of the Backup Panel")
            self.auto_actions.send_keys(file_name, the_value)
        else:
            self.utils.print_info("Could not find File Name field in the Backup panel")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_overwrite_existing_backup_file(self):
        """
        - This keyword clicks the "yes" button on the Overwrite File dialog to overwrite the file and start the backup
        - Keyword Usage
        - XIQSE Overwrite Existing Backup File
        :return: 1 if action successful, else -1
        """
        ret_val = 1

        the_dialog = self.get_file_exists_dialog()
        if the_dialog and the_dialog.is_displayed:
            self.utils.print_info("Overwrite File dialog is displayed")
            yes_button = self.get_overwrite_existing_file_yes_button()
            if yes_button:
                self.utils.print_info("File exists - overwriting file")
                self.auto_actions.click(yes_button)
                sleep(1)
            else:
                self.utils.print_info("Yes button not displayed")
                ret_val = -1
        else:
            self.utils.print_info("Overwrite File dialog not displayed")
            ret_val = -1

        return ret_val

    def xiqse_wait_for_backup_to_complete(self, retry_duration=10, retry_count=30):
        """
        - This keyword waits for the "Backing Up Database" loading mask to complete before continuing
        - Keyword Usage
        - ''XIQSE Wait For Backup to Complete''
        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Backup to complete: loop {count}")
            load_mask = self.view_el.get_working_backup_load_mask()
            if load_mask:
                self.utils.print_info(f"Backup still in progress")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Backup has completed")
                return 1
            count += 1

        self.utils.print_info("Backup did not complete within specified time")
        self.screen.save_screen_shot()

        return -1

    def xiqse_start_backup(self):
        """
        This keyword starts the backup of the XIQSE database by selecting the "Backup" button on the Backup/Restore tab
        :return: 1 if successful, else -1
        """
        ret_val = 1

        the_backup_button = self.get_backup_button()
        if the_backup_button:
            self.utils.print_info("Clicking 'Back Up' button")
            self.auto_actions.click(the_backup_button)
            sleep(1)

            self.xiqse_overwrite_existing_backup_file()

            self.xiqse_wait_for_backup_to_complete()

        else:
            self.utils.print_info("Unable to find Back Up Button")
            ret_val = -1

        return ret_val

    def xiqse_get_working_backup_load_mask(self):
        """
        - This keyword looks for the "Working" dialog when the backup is successful
        - Keyword usage: XIQSE Get Working Backup Load Mask
        :return: 1 if successful, else -1
        """
        load_mask = self.view_el.get_working_backup_load_mask()
        if load_mask:
            self.utils.print_info("Backup Started")
            ret_val = 1
        else:
            self.utils.print_info("Backup not started")
            ret_val = -1

        return ret_val

    def xiqse_get_file_exists_dialog(self):
        """
        - This Keyword checks for the existence of "Overwrite File - File Exists" dialog
        - Keyword Usage: XIQSE Get File Exists Dialog
        :return: 1 if successful, else -1
        """
        file_exists_dialog = self.view_el.get_file_exists_dialog()
        if file_exists_dialog:
            self.utils.print_info("File Exists, being prompted to overwrite to continue")
            ret_val = 1
        else:
            self.utils.print_info("File does not already exist, continuing with backup")
            ret_val = -1

        return ret_val

    def xiqse_perform_backup(self, name):
        """
         - This keyword initiates the backup with the specified name and waits for the action to complete.
         - It is assumed the Backup/Restore tab is already opened.
         - Keyword Usage
          - ``XIQSE Perform Backup ${BACKUP_NAME}``

        :param name:  Value to use for the backup file name 
        :return: 1 if action was successful, else -1
        """

        ret_val = self.xiqse_backup_database_set_name(name)
        if ret_val != -1:
            ret_val = self.xiqse_start_backup()

        if ret_val == -1:
            self.utils.print_info("Unable to perform the backup")
            self.screen.save_screen_shot()

        return ret_val
