# extauto.xiqse.flows.alarms_events.events package

## extauto.xiqse.flows.alarms_events.events.XIQSE_AlarmsEventsEvents module


### _class_ extauto.xiqse.flows.alarms_events.events.XIQSE_AlarmsEventsEvents.XIQSE_AlarmsEventsEvents()
Bases: `AlarmsEventsEventsWebElements`


#### xiqse_events_clear_search()
> 
> * This keyword clicks the clear button in the search box on the Alarms & Events> Events Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Events Clear Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_events_enter_search_text(value)
> 
> * This keyword enters text into the search field on the Alarms & Events> Events Tab


> * Keyword Usage

> > 
> > * `XIQSE Events Enter Search Text    My Event To Find`


* **Parameters**

    **value** – string to enter in the search box



* **Returns**

    1 if action was successful, else -1



#### xiqse_events_open_search()
> 
> * This keyword opens the search box on the Alarms & Events> Events Tab


> * Keyword Usage

> > 
> > * `XIQSE Events Open Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_events_perform_search(value, retry_duration=10, retry_count=30)
> 
> * This keyword performs a search on the Alarms & Events> Events Tab


> * Keyword Usage

> > 
> > * `XIQSE Events Perform Search   My Search String`


> > * `XIQSE Events Perform Search   My Search String  retry_duration=5  retry_count=10`


* **Parameters**

    
    * **value** – string to search for


    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_events_select_time_range(value)
> 
> * This keyword selects the time range on the Alarms & Events> Events Tab


> * Keyword Usage

> > 
> > * `XIQSE Events Select Time Range    Custom`


> > * `XIQSE Events Select Time Range    All`


> > * `XIQSE Events Select Time Range    Today`


> > * `XIQSE Events Select Time Range    Yesterday`


> > * `XIQSE Events Select Time Range    Last 30 Minutes`


> > * `XIQSE Events Select Time Range    Last Hour`


> > * `XIQSE Events Select Time Range    Last 2 Hours`


> > * `XIQSE Events Select Time Range    Last 6 Hours`


> > * `XIQSE Events Select Time Range    Last 12 Hours`


> > * `XIQSE Events Select Time Range    Last 24 Hours`


> > * `XIQSE Events Select Time Range    Last 3 Days`


> > * `XIQSE Events Select Time Range    Last Week`


> > * `XIQSE Events Select Time Range    Last 2 Weeks`


> > * `XIQSE Events Select Time Range    Last 4 Weeks`


* **Parameters**

    **value** – item to select in the time range dropdown



* **Returns**

    1 if action was successful, else -1



#### xiqse_events_select_type(values)
> 
> * This keyword selects the specified types on the Alarms & Events> Events Tab.


> * NOTE: to clear existing selections, first select “All”; otherwise, each call to this method will


> * select the additional values in addition to the current selections.


> * Keyword Usage

> > 
> > * `XIQSE Events Select Type    All`


> > * `XIQSE Events Select Type    Console,Console View,Inventory`


> > * `XIQSE Events Select Type    Admin`


* **Parameters**

    **values** – comma-separated list of items to select in the Type dropdown



* **Returns**

    1 if action was successful, else -1



#### xiqse_events_trigger_search()
> 
> * This keyword clicks the search button in the search box on the Alarms & Events> Events Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Events Trigger Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_events_wait_for_search_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the search to complete on the Alarms & Events> Events Tab


> * Keyword Usage

> > 
> > * `XIQSE Events Wait For Search To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_event_with_text(value)

* Searches for an event containing the specified value


* **Parameters**

    **value** – Value to search for in the event row



* **Returns**

    return 1 if event with specified value is found, else -1
