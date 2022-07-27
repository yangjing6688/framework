# flows.network.archives package

## flows.network.archives.XIQSE_NetworkArchives module


### _class_ flows.network.archives.XIQSE_NetworkArchives.XIQSE_NetworkArchives()
Bases: `NetworkArchivesWebElements`


#### xiqse_archives_click_create()
> 
> * This keyword clicks the Create button on the Network> Archives Tab


> * It is assumed the view is already navigated to the Archives tab.


> * Keyword Usage

> > 
> > * `XIQSE Archives Click Create`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_click_refresh()
> 
> * This keyword clicks the Refresh button on the Network> Archives Tab


> * It is assumed the view is already navigated to the Archives tab.


> * Keyword Usage

> > 
> > * `XIQSE Archives Click Refresh`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_archive(name, device_ips, frequency=None)
> 
> * This keyword creates an archive with the specified name for the specified device.


> * It is assumed the Network> Archives view is currently displayed.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4`


> > * `XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4  Daily`


> > * `XIQSE Archives Create Archive    MY_ARCHIVE  1.2.3.4  Never`


* **Parameters**

    
    * **name** – name to use when creating the archive


    * **device_ips** – comma-separated list of IP addresses to add to the archive


    * **frequency** – value to select in the Frequency field



* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_delete_archive(name)
> 
> * This keyword deletes the specified archive in the Archives tree.


> * It is assumed the Network> Archives view is currently displayed.


> * Keyword Usage

> > 
> > * `XIQSE Archives Delete Archive    MY_ARCHIVE`


* **Parameters**

    **name** – name of the archive to delete



* **Returns**

    1 if action was successful, 2 if archive was not found (already deleted?), else -1



#### xiqse_archives_select_archive(name)
> 
> * This keyword selects the specified archive in the Archives tree.


> * It is assumed the Network> Archives view is currently displayed.


> * Keyword Usage

> > 
> > * `XIQSE Archives Select Archive    MY_ARCHIVE`


* **Parameters**

    **name** – name of the archive to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_stamp_new_version(name)
> 
> * This keyword selects “Stamp New Version” from the context menu of the specified archive in the Archives tree.


> * It is assumed the Network> Archives view is currently displayed.


> * Keyword Usage

> > 
> > * `XIQSE Archives Stamp New Version    MY_ARCHIVE`


* **Parameters**

    **name** – name of the archive to stamp a new version on



* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_archive_exists(name, exists='true')
> 
> * This keyword confirms the specified archive is present in the Archives tree.


> * It is assumed the Network> Archives view is currently displayed.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Archive Exists    MY_ARCHIVE`


* **Parameters**

    
    * **name** – name of the archive to look for


    * **exists** – indicates whether the archive should be present or not (true/false)



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_archive_added(name, retry_duration=5, retry_count=24)

* This keyword is used to wait for the archive to show up in the Archives tree.


* This keyword by default loops 24 times every 5 seconds to check if the archive exists.


* It is assumed the Network> Archives tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Archive Added    ${ARCHIVE_MAME}    retry_duration=15    retry_count=10`


* **Parameters**

    
    * **name** – name of the archive to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if archive added within time; else -1



#### xiqse_wait_until_archive_complete(retry_duration=30, retry_count=10)
> 
> * This keyword waits until the archive has completed by checking the Inventory Audit entry in the


> * Operations panel for progress value of 100%.


> * Keyword Usage

> > 
> > * `XIQSE Wait Until Archive Complete`


> > * `XIQSE Wait Until Archive Complete    retry_duration=10  retry_count=60`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_archive_removed(name, retry_duration=5, retry_count=24)

* This keyword is used to wait for the archive to be removed from the Archives tree.


* This keyword by default loops 24 times every 5 seconds to check if the archive exists.


* It is assumed the Network> Archives tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Archive Removed    ${ARCHIVE_MAME}    retry_duration=15    retry_count=10`


* **Parameters**

    
    * **name** – name of the archive to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if archive removed within time; else -1



#### xiqse_wait_until_restore_complete(retry_duration=30, retry_count=20)
> 
> * This keyword waits until the restore has completed by checking the Inventory Audit entry in the


> * Operations panel for progress value of 100%.


> * Keyword Usage

> > 
> > * `XIQSE Wait Until Restore Complete`


> > * `XIQSE Wait Until Restore Complete    retry_duration=10  retry_count=60`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if action was successful, else -1


## flows.network.archives.XIQSE_NetworkArchivesCreateArchive module


### _class_ flows.network.archives.XIQSE_NetworkArchivesCreateArchive.XIQSE_NetworkArchivesCreateArchive()
Bases: `NetworkArchivesCreateArchiveWebElements`


#### xiqse_archives_create_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Create Archive dialog


> * It is assumed the Create Archive dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_click_finish()
> 
> * This keyword clicks Finish in the Create Archive dialog


> * It is assumed the Create Archive dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Click Finish`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_click_next()
> 
> * This keyword clicks Next in the Create Archive dialog


> * It is assumed the Create Archive dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Click Next`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_enter_name(value)
> 
> * This keyword populates the Name field of the Create Archive dialog


> * It is assumed the Create Archive dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Enter Name  MY_ARCHIVE`


* **Parameters**

    **value** – name of the archive to create



* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_expand_all_devices()
> 
> * This keyword expands the All Devices node in the Select Devices tree of the Create Archive dialog


> * It is assumed the Create Archive dialog is already open and on the device selection page.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Expand All Devices`


* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_move_device_to_archive_members(ip)
> 
> * This keyword moves the specified device in the Select Devices tree of the Create Archive dialog to


> * the Archive Members list.


> * It is assumed the Create Archive dialog is already open and on the device selection page.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Move Device to Archive Members    1.2.3.4`


* **Parameters**

    **ip** – IP address of the device to select and move to the Archive Members list



* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_select_device_and_move_to_archive_members(ip)
> 
> * This keyword selects the specified device in the Create Archive dialog and moves it to the


> * Archive Members list.


> * It is assumed the Create Archive dialog is already open and on the device selection page.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Select Device and Move to Archive Members    1.2.3.4`


* **Parameters**

    **ip** – IP address of the device to select and move to the Archive Members list



* **Returns**

    1 if action was successful, else -1



#### xiqse_archives_create_dialog_select_frequency(the_value)
> 
> * This keyword selects the value in the Frequency dropdown of the Create Archive dialog.


> * It is assumed the Create Archive dialog is already open and on the page containing the Frequency field.


> * Keyword Usage

> > 
> > * `XIQSE Archives Create Dialog Select Frequency    Daily`


> > * `XIQSE Archives Create Dialog Select Frequency    Never`


> > * `XIQSE Archives Create Dialog Select Frequency    Now`


> > * `XIQSE Archives Create Dialog Select Frequency    On Startup`


> > * `XIQSE Archives Create Dialog Select Frequency    Once`


> > * `XIQSE Archives Create Dialog Select Frequency    Weekly`


* **Parameters**

    **the_value** – frequency to select



* **Returns**

    1 if action was successful, else -1


## Module contents
