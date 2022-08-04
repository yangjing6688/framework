# extauto.xiqse.flows.analytics.configuration package

## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfiguration module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfiguration.XIQSE_AnalyticsConfiguration()
Bases: `AnalyticsConfigurationWebElements`


#### xiqse_add_analytics_engine(engine_ip, engine_name, engine_profile)
> 
> * This keyword adds an analytics engine to the Analytics Configuration panel.


> * It is assumed the user is already on the Analytics> Configuration> tab.


> * Keyword Usage

> > 
> > * `XIQSE Add Analytics Engine    ${NEXTGEN_IP}  ${NEXTGEN_NAME}  ${APPLIANCE_PROFILE}`


* **Parameters**

    
    * **engine_ip** – IP address of the analytics engine to add


    * **engine_name** – Value to enter into the Name field


    * **engine_profile** – Value to enter into the Profile field



* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_add_engine_button()
> 
> * This keyword clicks the Add button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Add Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_delete_engine_button()
> 
> * This keyword clicks the Delete button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Delete Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_enforce_all_engine_button()
> 
> * This keyword clicks the Enforce All button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Enforce All Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_enforce_engine_button()
> 
> * This keyword clicks the Enforce button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Enforce Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_poll_engine_button()
> 
> * This keyword clicks the Poll button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Poll Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_click_restart_collector_engine_button()
> 
> * This keyword clicks the Restart Collector button in the Analytics->Configuration panel.


> * It is assumed the user is already in the Analytics> Configuration panel.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Click Restart Collector Engine Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_configuration_refresh_panel()
> 
> * This keyword clicks the refresh icon on the toolbar.


> * Keyword Usage

> > 
> > * `XIQSE Analytics Configuration Refresh Panel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_close_add_application_analytics_engine_dialog()
> 
> * This keyword closes the Add Application Analytics Engine dialog which may appear when first navigating to Analytics -> Configuration panel and no engines exist


> * Keyword Usage

> > 
> > * `XIQSE Close Add Application Analytics Engine Dialog`


* **Returns**

    1 if action successful, else -1



#### xiqse_delete_selected_engine(engine_ip)
> 
> * This keyword deletes the currently-selected engine.


> * It is assumed the user is already on the Analytics> Configuration tab and the engine to delete is selected.


> * Keyword Usage
> - `XIQSE Delete Engine    ${NEXTGEN_IP}`
> - `XIQSE Delete Engine    ${NEXTGEN_IP}    false`


* **Parameters**

    **engine_ip** – IP address of the engine to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_enforce_all_engines()
> 
> * This keyword enforces all engines.


> * It is assumed the user is already on the Analytics> Configuration tab


> * Keyword Usage
> - `XIQSE Enforce All Engines`


* **Returns**

    1 if action was successful, else -1



#### xiqse_enforce_selected_engine(engine_ip)
> 
> * This keyword enforces the currently-selected engine.


> * It is assumed the user is already on the Analytics> Configuration tab and the engine to enforce is selected.


> * Keyword Usage
> - `XIQSE Enforce Selected Engine    ${NEXTGEN_IP}`


* **Parameters**

    **engine_ip** – IP address of the engine to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_engine_with_ip(engine_ip)

* Searches for Engine matching Engine’s IP Address


* **Parameters**

    **engine_ip** – Engine IP Address to search for



* **Returns**

    return 1 if engine with specified IP address is found, else -1



#### xiqse_get_engine_row(engine_ip)

* This keyword returns the row for the engine matching the IP address


* **Parameters**

    **engine_ip** – IP address of the engine to obtain the row for



* **Returns**

    returns the row object



#### xiqse_poll_selected_engine(engine_ip)
> 
> * This keyword polls the currently-selected engine.


> * It is assumed the user is already on the Analytics> Configuration tab and the engine to poll is selected.


> * Keyword Usage
> - `XIQSE Poll Selected Engine    ${NEXTGEN_IP}`


* **Parameters**

    **engine_ip** – IP address of the engine to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_restart_collector_selected_engine(engine_ip)
> 
> * This keyword restarts collector on the currently-selected engine.


> * It is assumed the user is already on the Analytics> Configuration tab and the engine to restart is selected.


> * Keyword Usage
> - `XIQSE Restart Collector Selected Engine    ${NEXTGEN_IP}`


* **Parameters**

    **engine_ip** – IP address of the engine to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_select_engine(engine_ip)
> 
> * This keyword selects the specified engine.


> * It is assumed the user is already on the Analytics> Configuration tab.


> * Keyword Usage

> > 
> > * `XIQSE Select Engine    ${NEXTGEN_IP}`


* **Parameters**

    **engine_ip** – IP address of the engine to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_for_enforce_all_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the Enforce All action to complete.


> * Keyword Usage

> > 
> > * `XIQSE Wait For Enforce All To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the enforce all action to be complete


    * **retry_count** – number of times to check for the enforce all action to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_for_enforce_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the Enforce action to complete.


> * Keyword Usage

> > 
> > * `XIQSE Wait For Enforce To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the enforce action to be complete


    * **retry_count** – number of times to check for the enforce action to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_for_poll_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the Poll action to complete.


> * Keyword Usage

> > 
> > * `XIQSE Wait For Poll To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the poll action to be complete


    * **retry_count** – number of times to check for the poll action to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_for_restart_collector_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the Restart Collector action to complete.


> * Keyword Usage

> > 
> > * `XIQSE Wait For Restart Collector To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the restart collector action to be complete


    * **retry_count** – number of times to check for the restart collector action to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_engine_added(engine_ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the engine to show up in the configuration panel.


* This keyword by default loops 10 times every 30 seconds to check if the engine exists.


* It is assumed the Analytics> Configuration tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Engine Added    ${NEXTGEN_IP}    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **engine_ip** – engine IP to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if engine added within time; else -1



#### xiqse_wait_until_engine_deleted(engine_ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the engine to be deleted from the configuration panel.


* This keyword by default loops 10 times every 30 seconds to check if the engine exists.


* It is assumed the Analytics> Configuration tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Engine Deleted    ${NEXTGEN_IP}    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **engine_ip** – engine IP to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if engine added within time; else -1


## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationAddEngine module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationAddEngine.XIQSE_AnalyticsConfigurationAddEngine()
Bases: `AnalyticsConfigurationAddEngineWebElements`


#### xiqse_add_analytics_engine_dialog_set_ip(the_value)
> 
> * This keyword sets the IP Address value in the Add Application Analytics Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Analytics Engine Dialog Set IP  ${IP}`


* **Parameters**

    **the_value** – IP address value to enter in the Add Application Analytics Engine dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_analytics_engine_dialog_set_name(the_value)
> 
> * This keyword sets the Name value in the Add Application Analytics Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Analytics Engine Dialog Set Name  ${IP}`


* **Parameters**

    **the_value** – Name value to enter in the Add Application Analytics Engine dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_analytics_engine_dialog_set_profile(the_value)
> 
> * This keyword sets the Profile value in the Add Application Analytics Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Analytics Engine Dialog Set Profile  ${DEVICE_PROFILE}`


* **Parameters**

    **the_value** – Profile value to enter in the Add Application Analytics Engine dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_engine_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Add Application Analytics Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Engine Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_engine_dialog_click_ok()
> 
> * This keyword clicks OK in the Add Application Analytics Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Engine Dialog Click OK`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationDeleteEngine module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationDeleteEngine.XIQSE_AnalyticsConfigurationDeleteEngine()
Bases: `AnalyticsConfigurationDeleteEngineWebElements`


#### xiqse_delete_engine_dialog_click_no()
> 
> * This keyword clicks No in the Delete Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Delete Engine Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_engine_dialog_click_yes()
> 
> * This keyword clicks Yes in the Delete Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Delete Engine Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceAllEngines module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceAllEngines.XIQSE_AnalyticsConfigurationEnforceAllEngines()
Bases: `AnalyticsConfigurationEnforceAllEnginesWebElements`


#### xiqse_close_enforce_engines_error_dialog()
> 
> * This keyword closes the Enforce Engines Error dialog which may appear when an error has occurred while enforcing an engine


> * Keyword Usage

> > 
> > * `XIQSE Close Enforce Engines Error Dialog`


* **Returns**

    1 if action successful, else -1



#### xiqse_enforce_all_engines_dialog_click_no()
> 
> * This keyword clicks No in the Enforce Engines dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Enforce All Engines Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_enforce_all_engines_dialog_click_yes()
> 
> * This keyword clicks Yes in the Enforce Engines dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Enforce All Engines Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceEngine module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceEngine.XIQSE_AnalyticsConfigurationEnforceEngine()
Bases: `AnalyticsConfigurationEnforceEngineWebElements`


#### xiqse_close_enforce_engine_error_dialog()
> 
> * This keyword closes the Enforce Engine Error dialog which may appear when an error has occurred while enforcing an engine


> * Keyword Usage

> > 
> > * `XIQSE Close Enforce Engine Error Dialog`


* **Returns**

    1 if action successful, else -1



#### xiqse_enforce_engine_dialog_click_no()
> 
> * This keyword clicks No in the Enforce Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Enforce Engine Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_enforce_engine_dialog_click_yes()
> 
> * This keyword clicks Yes in the Enforce Engine dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Enforce Engine Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationRestartCollector module


### _class_ extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationRestartCollector.XIQSE_AnalyticsConfigurationRestartCollector()
Bases: `AnalyticsConfigurationRestartCollectorWebElements`


#### xiqse_close_restart_collector_error_dialog()
> 
> * This keyword closes the Restart Collector Error dialog which may appear when an error has occurred while restarting the collector on an engine


> * Keyword Usage

> > 
> > * `XIQSE Close Restart Collector Error Dialog`


* **Returns**

    1 if action successful, else -1



#### xiqse_restart_collector_dialog_click_no()
> 
> * This keyword clicks No in the Restart Collector dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Restart Collector Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_restart_collector_dialog_click_yes()
> 
> * This keyword clicks Yes in the Restart Collector dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Restart Collector Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1
