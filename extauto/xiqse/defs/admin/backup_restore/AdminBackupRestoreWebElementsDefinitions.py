
class AdminBackupRestoreWebElementsDefinitions:

    text_input_backup_name = \
        {
            'DESC': 'Text Area for Backup File Name',
            'XPATH': '//input[contains(@name,"dbName")]',
            'wait_for': 10
        }

    backup_alarm_checkbox = \
        {
            'DESC': 'Checkbox for backing up alarm and reporting database',
            'XPATH': '//input[contains(@name,"backupReportingDbCB")]',
            'wait_for': 10
        }

    restore_initial_database_radio_button = \
        {
            'DESC': 'Radio button to select restoring initial database',
            'XPATH': '//label[text()="Restore Initial Database"]',
            'wait_for': 10
        }

    restore_saved_backup_radio_button = \
        {
            'DESC': 'Radio button to select saved backup',
            'XPATH': '//label[text()="Restore Saved Backup"]',
            'wait_for': 10
        }

    restore_button = \
        {
            'DESC': 'Restore button to begin restore process',
            'XPATH': '//span[text()="Restore"]',
            'wait_for': 10
        }

    advanced_button = \
        {
            'DESC': 'Advanced button on backup/restore tab to open sql options',
            'XPATH': '//span[text()="Advanced..."]',
            'wait_for': 10
        }

    connection_url_text_field = \
        {
            'DESC': 'URL text field for Mysql URL',
            'XPATH': '//input[contains(@name,"connectionUrlId")]',
        }

    db_password_text_field = \
        {
            'DESC': 'Text field for mySql password',
            'XPATH': '//input[contains(@name,"dbPassword")]',
            'wait_for': 10
        }

    advanced_options_save_button = \
        {
            'DESC': 'Save button for changing advanced options',
            'XPATH': '//div[contains(@class,"x-docked-bottom")] //span[text()="Save"]',
            'wait_for': 10
        }

    advanced_options_reset_button = \
        {
            'DESC': 'Reset button for changing advanced options',
            'XPATH': '//div[contains(@class,"x-docked-bottom")] //span[text()="Reset"]',
            'wait_for': 10
        }

    advanced_options_restore_defaults_button = \
        {
            'DESC': 'Reset button for restoring advanced options default values',
            'XPATH': '//div[contains(@class,"x-docked-bottom")] //span[text()="Restore Defaults"]',
            'wait_for': 10
        }

    backup_button = \
        {
            'DESC': 'Back Up button to kick off backup process',
            'XPATH': '//span[text()="Back Up"]',
            'wait_for': 10
        }

    working_backup_load_mask = \
        {
            'DESC': 'Working dialog mask while backup process is running',
            'XPATH': '//div[text()="Backing Up Database"]',
            'wait_for': 10
        }

    file_exists_dialog = \
        {
            'DESC': 'Backup File Exists dialog box with Yes/No choices',
            'XPATH': '//div[text()="Overwrite Backup"]',
            'wait_for': 10
        }

    overwrite_existing_file_yes_button = \
        {
            'DESC': 'Yes button to confirm overwriting of existing backup file with same name',
            'XPATH': '//a[contains(@role, "button")]//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    overwrite_existing_file_no_button = \
        {
            'DESC': 'Yes button to confirm overwriting of existing backup file with same name',
            'XPATH': '//a[contains(@role, "button")]//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

    backup_aborted_dialog = \
        {
            'DESC': 'Backup Aborted dialog with OK button to end backup process',
            'XPATH': '//div[text()="Backup Aborted"]',
            'wait_for': 10
        }

    backup_aborted_ok_button = \
        {
            'DESC': 'OK button to close Backup Aborted dialog and exit backup process',
            'XPATH': '//a[contains(@role, "button")]//span[text()="OK"]/ancestor::a',
            'wait_for': 10
        }

    restore_initial_database_confirmation_yes_button = \
        {
            'DESC': 'Yes button on Restore Initial Database Confirmation Dialog',
            'XPATH': '//a[contains(@role, "button")]//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    restore_initial_database_confirmation_no_button = \
        {
            'DESC': 'No button on Restore Initial Database Confirmation Dialog',
            'XPATH': '//a[contains(@role, "button")]//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

    restore_initial_database_load_mask = \
        {
            'DESC': 'Working load mask while database is reinitializing',
            'XPATH': '//div[text()="Restoring Initial Database"]',
            'wait_for': 10
        }

    connection_to_server_lost_ok_button = \
        {
            'DESC': 'OK button on Connection to Server Lost dialog after restore completes',
            'XPATH': '//div[@role="alertdialog"]//span[text()="OK"]/ancestor::a',
            'wait_for': 10
        }

    restore_initial_database_dialog = \
        {
            'DESC': 'Confirmation of database reinitialization with Yes/No choices',
            'XPATH': '//div[text()="Restore Initial Database Confirmation"]',
            'wait_for': 10
        }

    connection_to_server_lost_dialog = \
        {
            'DESC': 'Connection to Server Lost dialog during reinitialization process/restart of server',
            'XPATH': '//div[text()="Connection to server lost."]',
            'wait_for': 10
        }
