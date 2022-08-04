# extauto.xiqse.flows.network.firmware package

## Submodules

## extauto.xiqse.flows.network.firmware.XIQSE_NetworkFirmware module


### _class_ extauto.xiqse.flows.network.firmware.XIQSE_NetworkFirmware.XIQSE_NetworkFirmware()
Bases: `NetworkFirmwareWebElements`


#### xiqse_assign_firmware()

* This keyword selects the Assign Firmware menu item of the selected firmware’s context menu


* It assumes the Firmware Image has already been selected


* Keyword Usage:


* ‘XIQSE Assign Firmware’


* **Returns**

    1 if action is successful, else -1



#### xiqse_click_firmware_refresh_button()

* This keyword refreshes the uploaded firmware images by selecting “Refresh Images…” from the Firmware Page.


* It assumes the Network > Firmware tab is already open.


* Keyword Usage:


* `XIQSE Click Refresh Images`


* **Returns**

    1 if action is successful, else -1



#### xiqse_delete_image()

* This keyword selects the Delete Image menu item of the selected firmware’s context menu


* It assumes the Firmware Image has already been selected


* Keyword Usage:


* ‘XIQSE Delete Image’


* **Returns**

    1 if action is successful, else -1



#### xiqse_find_firmware_with_text(value)

* Searches for firmware containing the specified value


* **Parameters**

    **value** – Value to search for in the firmware row



* **Returns**

    return 1 if firmware with specified value is found, else -1



#### xiqse_firmware_clear_search()
> 
> * This keyword clicks the clear button in the search box on the Network > Firmware Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Firmware Clear Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_firmware_enter_search_text(value)
> 
> * This keyword enters text into the search field on the Network > Firmware Tab


> * Keyword Usage

> > 
> > * `XIQSE Firmware Enter Search Text    My Firmware To Find`


* **Parameters**

    **value** – string to enter in the search box



* **Returns**

    1 if action was successful, else -1



#### xiqse_firmware_open_search()
> 
> * This keyword opens the search box on the Network > Firmware Tab


> * Keyword Usage

> > 
> > * `XIQSE Firmware Open Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_firmware_perform_search(value, retry_duration=10, retry_count=30)
> 
> * This keyword performs a search on the Network > Firmware Tab


> * Keyword Usage

> > 
> > * `XIQSE Firmware Perform Search   My Search String`


> > * `XIQSE Firmware Perform Search   My Search String  retry_duration=5  retry_count=10`


* **Parameters**

    
    * **value** – string to search for


    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_firmware_trigger_search()
> 
> * This keyword clicks the search button in the search box on the Network > Firmware Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Firmware Trigger Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_firmware_wait_for_search_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the search to complete on the Network > Firmware Tab


> * Keyword Usage

> > 
> > * `XIQSE Firmware Wait For Search To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_open_firmware_context_menu(firmware_image_filename)
> 
> * This keyword right-clicks the specified firmware image.


> * It is assumed the user is already on the Network > Firmware tab.


> * Keyword Usage

> > 
> > * `XIQSE Right-Click Firmware Image  My_Firmware_Image_Name`


* **Parameters**

    **firmware_image_filename** – firmware image to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_remove_firmware_from_group()

* This keyword selects the Remove Firmware from Group menu item of the selected firmware’s context menu


* It assumes the Firmware Image has already been selected


* Keyword Usage:


* ‘XIQSE Remove Firmware From Group’


* **Returns**

    1 if action is successful, else -1



#### xiqse_select_firmware_image_filename(firmware_image_filename)
> 
> * This keyword selects the specified firmware image.


> * It is assumed the user is already on the Network > Firmware tab.


> * Keyword Usage

> > 
> > * `XIQSE Select Firmware Image  My_Firmware_Image_Name`


* **Parameters**

    **firmware_image_filename** – firmware image to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_as_reference_image()

* This keyword selects the Set As Reference Image menu item of the selected firmware’s context menu


* It assumes the Firmware Image has already been selected


* Keyword Usage:


* ‘XIQSE Set As Reference Image’


* **Returns**

    1 if action is successful, else -1



#### xiqse_unset_as_reference_image()

* This keyword selects the Unset As Reference Image menu item of the selected firmware’s context menu


* It assumes the Firmware Image has already been selected


* Keyword Usage:


* ‘XIQSE Unset As Reference Image’


* **Returns**

    1 if action is successful, else -1



#### xiqse_wait_for_firmware_refresh_to_complete(retry_duration=10, retry_count=30)

* This keyword waits for the “Firmware Refresh” loading mask to complete before continuing


* Keyword Usage


* ‘’XIQSE Wait For Firmware Refresh to Complete’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the refresh to be complete


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.firmware.XIQSE_NetworkFirmwareTreePanel module


### _class_ extauto.xiqse.flows.network.firmware.XIQSE_NetworkFirmwareTreePanel.XIQSE_NetworkFirmwareTreePanel()
Bases: `NetworkFirmwareWebElements`


#### xiqse_select_firmware_type_node(firmware_type)
> 
> * This keyword selects the specified firmware type node on the Network > Firmware Tab


> * Keyword Usage

> > 
> > * `XIQSE Select Firmware Type Node   ${FIRMWARE_TYPE}`


> > * 

> > ```
> > ``
> > ```

> > XIQSE Select Firmware Type Node   DEVICE TYPE


> > * 

> > ```
> > ``
> > ```

> > XIQSE Select Firmware Type Node   ALL FIRMWARE


* **Parameters**

    **firmware_type** – name of firmware node to select in the tree



* **Returns**

    1 if action was successful, else -1


## Module contents
