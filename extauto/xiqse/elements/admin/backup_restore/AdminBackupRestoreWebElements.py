from extauto.common.WebElementHandler import *
from xiqse.defs.admin.backup_restore.AdminBackupRestoreWebElementsDefinitions import *


class AdminBackupRestoreWebElements(AdminBackupRestoreWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_text_input_backup_name(self):
        """
        :return: 'File Name' text box for Backup File Name
        """
        return self.weh.get_element(self.text_input_backup_name)

    def get_backup_alarm_checkbox(self):
        """
        :return: 'Back Up Alarm, End-System Event, and Reporting Database' checkbox
        """
        return self.weh.get_element(self.backup_alarm_checkbox)

    def get_restore_initial_database_radio_button(self):
        """
        :return: 'Restore Initial Database" radio button as Restore option
        """
        return self.weh.get_element(self.restore_initial_database_radio_button)

    def get_restore_saved_backup_radio_button(self):
        """
        :return: 'Restore Saved Backup' radio button
        """
        return self.weh.get_element(self.restore_saved_backup_radio_button)

    def get_restore_button(self):
        """
        :return: 'Restore' action button to begin Restore process
        """
        return self.weh.get_element(self.restore_button)

    def get_advanced_button(self):
        """
        :return: 'Advanced' button to open Advanced database options
        """
        return self.weh.get_element(self.advanced_button)

    def get_connection_url_text_field(self):
        """
        :return: 'Connection URL' text field for mysql URL
        """
        return self.weh.get_element(self.connection_url_text_field)

    def get_db_password_text_field(self):
        """
        :return: 'DB Password' text field
        """
        return self.weh.get_element(self.db_password_text_field)

    def get_advanced_options_save_button(self):
        """
        :return: 'Save' button for Advanced Options
        NOTE: this will only activate when options have been changed
        """
        return self.weh.get_element(self.advanced_options_save_button)

    def get_advanced_options_reset_button(self):
        """
        :return: 'Reset' button for Advanced Options
        NOTE: this will only activate when options have been changed
        """
        return self.weh.get_element(self.advanced_options_reset_button)

    def get_advanced_options_restore_defaults_button(self):
        """
        :return: 'Restore Defaults' button for Advanced Options
        NOTE: this will only activate when options have been changed
        """
        return self.weh.get_element(self.advanced_options_restore_defaults_button)

    def get_backup_button(self):
        """
        :return: 'Back Up' button to start backup process
        """
        return self.weh.get_element(self.backup_button)

    def get_working_backup_load_mask(self):
        """
        :return: load 'Working' refresh mask if displayed, else None
        """
        elements = self.weh.get_elements(self.working_backup_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_file_exists_dialog(self):
        """
        :return: 'Overwrite File' dialog if existing backup file with same name exists
        """
        return self.weh.get_element(self.file_exists_dialog)

    def get_overwrite_existing_file_yes_button(self):
        """
        :return: 'Yes' button in Overwrite File dialog to overwrite existing file and start backup
        """
        return self.weh.get_element(self.overwrite_existing_file_yes_button)

    def get_overwrite_existing_file_no_button(self):
        """
        :return: 'No' button in Overwrite File dialog to not overwrite and spawn 'Backup Aborted' dialog
        """
        return self.weh.get_element(self.overwrite_existing_file_no_button)

    def get_backup_aborted_dialog(self):
        """
        :return: 'Backup Aborted' dialog with OK button
        """
        return self.weh.get_element(self.backup_aborted_dialog)

    def get_backup_aborted_ok_button(self):
        """
        :return: 'OK' button to close all backup operations
        """
        return self.weh.get_element(self.backup_aborted_ok_button)

    def get_restore_initial_database_yes_button(self):
        """
        :return: 'Yes' button to start initial database restore on Confirmation dialog
        """
        return self.weh.get_element(self.restore_initial_database_confirmation_yes_button)

    def get_restore_initial_database_no_button(self):
        """
        :return: 'No' button to cancel restore of initial database on Confirmation dialog
        """
        return self.weh.get_element(self.restore_initial_database_confirmation_no_button)

    def get_restore_initial_database_dialog(self):
        """
        :return: 'Restore Initial Database' dialog to confirm function of database reinitialization
        """
        return self.weh.get_element(self.restore_initial_database_dialog)

    def get_restore_initial_database_load_mask(self):
        """
        :return: load 'Restoring Initial Database' refresh mask if displayed, else None
        """
        elements = self.weh.get_elements(self.restore_initial_database_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_connection_to_server_lost_dialog(self):
        """
        :return: 'Connection to server lost' dialog when server restarts after restoring database
        """
        return self.weh.get_element(self.connection_to_server_lost_dialog)

    def get_connection_to_server_lost_ok_button(self):
        """
        :return: 'OK' button to close 'Connection to server lost' dialog
        """
        return self.weh.get_element(self.connection_to_server_lost_ok_button)

