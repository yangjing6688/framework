from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.backup_restore.AdminBackupRestoreWebElements import AdminBackupRestoreWebElements


class XIQSE_Restore(AdminBackupRestoreWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        # self.driver = extauto.common.CloudDriver.cloud_driver

    def xiqse_select_restore_initial_database(self):
        """
        - This keyword selects the "Restore Initial Database" button on the Backup/Restore tab
        - Keyword Usage:
        - "XIQSE Select Restore Initial Database"
        :return: 1 if successful, else -1
        """
        ret_val = 1

        the_reinit_button = self.get_restore_initial_database_radio_button()
        if the_reinit_button:
            self.utils.print_info("Selecting 'Restore Initial Database' radio button")
            self.auto_actions.click(the_reinit_button)

        else:
            self.utils.print_info("Unable to find 'Restore Initial Database' radio button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_click_restore_button(self):
        """
        - This keyword clicks the "Restore" button on the Backup/Restore File dialog to initiate restoration of database
        - Keyword Usage:
        - "XIQSE Click Restore Button"
        :return: 1 if action successful, else -1
        """
        ret_val = 1

        the_restore_button = self.get_restore_button()
        if the_restore_button:
            self.utils.print_info("Clicking 'Restore' button")
            self.auto_actions.click(the_restore_button)

        else:
            self.utils.print_info("Unable to find 'Restore' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_confirm_database_reinitialization(self):
        """
        - This Keyword checks for the existence of "Reinitialize Database" dialog and clicks "Yes" to begin restore of initial database
        - Keyword Usage:
        - "XIQSE Confirm Database Reinitialization"
        :return: 1 if successful, else -1
        """

        ret_val = 1

        restore_initial_db_dialog = self.get_restore_initial_database_dialog()
        if restore_initial_db_dialog and restore_initial_db_dialog.is_displayed:
            self.utils.print_info("Being prompted to restore the initial database")
            yes_button = self.get_restore_initial_database_yes_button()
            if yes_button:
                self.utils.print_info("Choosing 'Yes' to begin database reinitialization")
                self.auto_actions.click(yes_button)
                sleep(1)

            else:
                self.utils.print_info("'Yes' button is not displayed")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("Restore Initial Database dialog is not displayed")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_start_restore_initial_database(self):
        """
        This keyword starts the restoration of the initial XIQSE database by selecting the "Restore" button on the Backup/Restore tab
        and accepts confirmation dialogs to continue.
        - Keyword Usage:
        - "XIQSE Start Restore Initial Database"
        :return: 1 if successful, else -1
        """

        ret_val = 1

        self.xiqse_select_restore_initial_database()

        the_restore_button = self.get_restore_button()
        if the_restore_button:
            self.utils.print_info("Clicking 'Restore' button")
            self.auto_actions.click(the_restore_button)
            sleep(1)

            self.xiqse_confirm_database_reinitialization()

        else:
            self.utils.print_info("Unable to find Restore Button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_wait_for_restore_to_complete(self, retry_duration=30, retry_count=60):
        """
        - This keyword looks for the "Reinitializing Database" dialog, indicating that the restore is in progress
        - Keyword Usage"
        - ''XIQSE Wait For Restore to Complete''
        :param retry_duration: amount of time to wait in between each check for the Connection to Server lost dialog to appear
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Restore of Initial Database to complete: loop {count}")
            load_mask = self.get_restore_initial_database_load_mask()
            if load_mask:
                self.utils.print_info("Restore is still in progress")
                sleep(retry_duration)
            else:
                self.utils.print_info("Restore has completed")
                return 1
            count += 1

        self.utils.print_info("Restore did not complete within specified time")
        self.screen.save_screen_shot()

        return -1

    def xiqse_close_connection_lost_dialog(self, retry_duration=30, retry_count=60):
        """
        - This keyword waits for the "Connection to server lost" dialog, indicating that the server has shut down after restore and clicks OK to close the UI
        - Keyword Usage:
        - ''XIQSE Close Connection Lost Dialog''
        :param retry_duration: amount of time to wait in between each check for the Connection to Server lost dialog to appear
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """

        count = 1
        while count <= retry_count:
            self.utils.print_info("Restore has completed, waiting for server restart")
            connection_lost = self.get_connection_to_server_lost_dialog()
            if connection_lost:
                self.utils.print_info("Connection lost to server dialog visible. Closing browser session.")
                ok_button = self.get_connection_to_server_lost_ok_button()
                self.auto_actions.click(ok_button)
                return 1
            else:
                self.utils.print_info("Connection Lost dialog not visible")
                sleep(retry_duration)
            count += 1

        self.utils.print_info("Could not close UI")
        self.screen.save_screen_shot()

        return -1

    def xiqse_force_quit_browser(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
        - ``XIQSE Force Quit Browser``
        :param _driver: specific driver to use; if not specified, default driver will be used
        :return: None
        """

        if _driver:
            _driver.quit()
            CloudDriver().close_browser()
            # CloudDriver().cloud_driver.quit()
            self.utils.print_info("Resetting cloud driver to -1")
            # extauto.common.CloudDriver.cloud_driver = None
            return 1
        else:
            self.utils.print_info("Could not close Web Driver")

        return -1
