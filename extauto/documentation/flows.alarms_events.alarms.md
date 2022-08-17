# extauto.xiqse.flows.alarms_events.alarms package

## extauto.xiqse.flows.alarms_events.alarms.XIQSE_AlarmsEventsAlarms module


### _class_ extauto.xiqse.flows.alarms_events.alarms.XIQSE_AlarmsEventsAlarms.XIQSE_AlarmsEventsAlarms()
Bases: `AlarmsEventsAlarmsWebElements`


#### xiqse_alarms_clear_search()
> 
> * This keyword clicks the clear button in the search box on the Alarms & Events> Alarms Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Alarms Clear Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarms_enter_search_text(value)
> 
> * This keyword enters text into the search field on the Alarms & Events> Alarms Tab


> * Keyword Usage

> > 
> > * `XIQSE Alarms Enter Search Text    My Alarm To Find`


* **Parameters**

    **value** – string to enter in the search box



* **Returns**

    1 if action was successful, else -1



#### xiqse_alarms_open_search()
> 
> * This keyword opens the search box on the Alarms & Events> Alarms Tab


> * Keyword Usage

> > 
> > * `XIQSE Alarms Open Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarms_perform_search(value, retry_duration=10, retry_count=30)
> 
> * This keyword performs a search on the Alarms & Events> Alarms Tab


> * Keyword Usage

> > 
> > * `XIQSE Alarms Perform Search   My Search String`


> > * `XIQSE Alarms Perform Search   My Search String  retry_duration=5  retry_count=10`


* **Parameters**

    
    * **value** – string to search for


    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_alarms_trigger_search()
> 
> * This keyword clicks the search button in the search box on the Alarms & Events> Alarms Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Alarms Trigger Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarms_wait_for_search_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the search to complete on the Alarms & Events> Alarms Tab


> * Keyword Usage

> > 
> > * `XIQSE Alarms Wait For Search To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_alarm_with_text(value)

* Searches for an alarm containing the specified value


* **Parameters**

    **value** – Value to search for in the alarm row



* **Returns**

    return 1 if alarm with specified value is found, else -1
