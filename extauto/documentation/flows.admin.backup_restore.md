# extauto.xiqse.flows.admin.backup_restore package

## extauto.xiqse.flows.admin.backup_restore.XIQSE_Backup module


### _class_ extauto.xiqse.flows.admin.backup_restore.XIQSE_Backup.XIQSE_Backup()
Bases: `AdminBackupRestoreWebElements`


#### xiqse_backup_database_set_name(the_value)
> 
> * This keyword sets the Backup File Name value in the File Name text field.


> * It is assumed the Backup/Restore tab is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Backup Database Set Name  ${BACKUP_NAME}`


* **Parameters**

    **the_value** – Value entered into backup file name dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_get_file_exists_dialog()

* This Keyword checks for the existence of “Overwrite File - File Exists” dialog


* Keyword Usage: XIQSE Get File Exists Dialog


* **Returns**

    1 if successful, else -1



#### xiqse_get_working_backup_load_mask()

* This keyword looks for the “Working” dialog when the backup is successful


* Keyword usage: XIQSE Get Working Backup Load Mask


* **Returns**

    1 if successful, else -1



#### xiqse_overwrite_existing_backup_file()

* This keyword clicks the “yes” button on the Overwrite File dialog to overwrite the file and start the backup


* Keyword Usage


* XIQSE Overwrite Existing Backup File


* **Returns**

    1 if action successful, else -1



#### xiqse_perform_backup(name)
> 
> * This keyword initiates the backup with the specified name and waits for the action to complete.


> * It is assumed the Backup/Restore tab is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Perform Backup ${BACKUP_NAME}`


* **Parameters**

    **name** – Value to use for the backup file name



* **Returns**

    1 if action was successful, else -1



#### xiqse_start_backup()
This keyword starts the backup of the XIQSE database by selecting the “Backup” button on the Backup/Restore tab
:return: 1 if successful, else -1


#### xiqse_wait_for_backup_to_complete(retry_duration=10, retry_count=30)

* This keyword waits for the “Backing Up Database” loading mask to complete before continuing


* Keyword Usage


* ‘’XIQSE Wait For Backup to Complete’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the refresh to be complete


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.backup_restore.XIQSE_Restore module


### _class_ extauto.xiqse.flows.admin.backup_restore.XIQSE_Restore.XIQSE_Restore()
Bases: `AdminBackupRestoreWebElements`


#### xiqse_click_restore_button()

* This keyword clicks the “Restore” button on the Backup/Restore File dialog to initiate restoration of database


* Keyword Usage:


* “XIQSE Click Restore Button”


* **Returns**

    1 if action successful, else -1



#### xiqse_close_connection_lost_dialog(retry_duration=30, retry_count=60)

* This keyword waits for the “Connection to server lost” dialog, indicating that the server has shut down after restore and clicks OK to close the UI


* Keyword Usage:


* ‘’XIQSE Close Connection Lost Dialog’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the Connection to Server lost dialog to appear


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_database_reinitialization()

* This Keyword checks for the existence of “Reinitialize Database” dialog and clicks “Yes” to begin restore of initial database


* Keyword Usage:


* “XIQSE Confirm Database Reinitialization”


* **Returns**

    1 if successful, else -1



#### xiqse_force_quit_browser(_driver=None)

* Closes all the browser windows and ends the WebDriver session gracefully.


* if the driver object is passed, quits and returns


* Keyword Usage:


* `XIQSE Force Quit Browser`


* **Parameters**

    **_driver** – specific driver to use; if not specified, default driver will be used



* **Returns**

    None



#### xiqse_select_restore_initial_database()

* This keyword selects the “Restore Initial Database” button on the Backup/Restore tab


* Keyword Usage:


* “XIQSE Select Restore Initial Database”


* **Returns**

    1 if successful, else -1



#### xiqse_start_restore_initial_database()
This keyword starts the restoration of the initial XIQSE database by selecting the “Restore” button on the Backup/Restore tab
and accepts confirmation dialogs to continue.
- Keyword Usage:
- “XIQSE Start Restore Initial Database”
:return: 1 if successful, else -1


#### xiqse_wait_for_restore_to_complete(retry_duration=30, retry_count=60)

* This keyword looks for the “Reinitializing Database” dialog, indicating that the restore is in progress


* Keyword Usage”


* ‘’XIQSE Wait For Restore to Complete’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the Connection to Server lost dialog to appear


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1
