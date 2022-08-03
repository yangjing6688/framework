# extauto.xiqse.flows.analytics.flows package

## extauto.xiqse.flows.analytics.flows.XIQSE_AnalyticsApplicationFlows module


### _class_ extauto.xiqse.flows.analytics.flows.XIQSE_AnalyticsApplicationFlows.XIQSE_AnalyticsApplicationFlows()
Bases: `AnalyticsApplicationFlowsWebElements`


#### xiqse_application_flows_find_with_text(value)

* Searches for an event containing the specified value


* **Parameters**

    **value** – Value to search for in the event row



* **Returns**

    return 1 if event with specified value is found, else -1



#### xiqse_application_flows_perform_search(value, retry_duration=10, retry_count=30)
> 
> * This keyword performs a search on the Application Flows Tab


> * Keyword Usage

> > 
> > * `XIQSE Application Flows Perform Search   My Search String`


> > * `XIQSE Application Flows Perform Search   My Search String  retry_duration=5  retry_count=10`


* **Parameters**

    
    * **value** – string to search for


    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_applicationflows_clear_search()
> 
> * This keyword clicks the clear button in the search box on the Application Flows tab to clear the search


> * Keyword Usage

> > 
> > * `XIQSE ApplicationFlows Clear Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_applicationflows_enter_search_text(value)
> 
> * This keyword enters text into the search field on the Analytics Application Flows Tab


> * Keyword Usage

> > 
> > * `XIQSE ApplicationFlows Enter Search Text    My Event To Find`


* **Parameters**

    **value** – string to enter in the search box



* **Returns**

    1 if action was successful, else -1



#### xiqse_applicationflows_open_search()
> 
> * This keyword opens the search box on the Analytics > Application Flows Tab


> * Keyword Usage

> > 
> > * `XIQSE ApplicationFlows Open Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_applicationflows_trigger_search()
> 
> * This keyword clicks the search button in the search box on the Analytics> Application Flows Tab to perform the search


> * Keyword Usage

> > 
> > * `XIQSE ApplicationFlows Trigger Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_applicationflows_wait_for_search_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the search to complete on the Application Flows Tab


> * Keyword Usage

> > 
> > * `XIQSE ApplicationFlows Wait For Search To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1
