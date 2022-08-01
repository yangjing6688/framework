# extauto.xiq.flows.mlinsights package

## Submodules

## extauto.xiq.flows.mlinsights.MLInsightClient360 module


### _class_ extauto.xiq.flows.mlinsights.MLInsightClient360.MLInsightClient360()
Bases: `MLInsightsClients360WebElements`


#### get_client360_current_connection_status(search_string)

* Get the client360 current connection status


* FLow: ML Insights –> Client 360 –> Click on either device MAC hyper link or Host name hyper link


* Client Details include “STATUS HEALTH”, “HOST-NAME”, “SSID” etc


* Keyword Usage:

> 
> * `Get Client360 Current Connection Status        search_string`


* **Parameters**

    **search_string** – string parameter to search the client in client grid ie. client mac, hostname etc



* **Returns**

    current connection status



#### get_real_time_client360_details(search_string)

* Get the client360 details in client grid


* Client Details include “STATUS HEALTH”, “HOST-NAME”, “SSID” etc


* Keyword Usage:

> 
> * `Get Real Time Client360 Details`


* **Parameters**

    **search_string** – string parameter to search the client in client grid ie. client mac, hostname etc



* **Returns**

    client360 details dict


## extauto.xiq.flows.mlinsights.MLInsights module


### _class_ extauto.xiq.flows.mlinsights.MLInsights.MLInsights()
Bases: `object`


#### create_location_in_ml_insights(\*\*kwargs)

* Create the Location on ML Insights Network 360 Plan using Name,address and city information


* Flow: ML Insights–> Network 360 Plan


* **Parameters**

    **kwargs** – Name ,Address,city


:return:1 if successfully created Location on ML Insights–> Network 360 Plan

## extauto.xiq.flows.mlinsights.Network360Monitor module


### _class_ extauto.xiq.flows.mlinsights.Network360Monitor.Network360Monitor()
Bases: `object`


#### get_clients_from_network360monitor_floor(floor_name='default', device_type='default')

* This keyword gets clients MACs from Network360 Monitor page in a floor


* Keyword Usage:

> 
> * `${CLIENT_MATCHES}=          Get APs From Network360Monitor Floor           floor_name=floor_02`


* **Parameters**

    
    * **floor_name** – floor of the location where devices has been assigned


    * **device_type** – optional - type of device - AP/switch/router/VGVA/router



* **Returns**

    clients MAC on the floor



#### get_devices_from_network360monitor_floor(floor_name='default', device_type='default')

* This keyword gets  devices name from Network360 Monitor page


* Keyword Usage:

> 
> * `${AP_MATCHES}=          Get APs From Network360Monitor Floor           floor_name=floor_02`


* **Parameters**

    
    * **floor_name** – floor of the location where devices has been assigned


    * **device_type** – optional - type of device - AP/switch/router/VGVA/router



* **Returns**

    devices names on the floor



#### get_network360monitor_clients_health_client_count(floor_name='default')

* This keyword returns the CLIENTS card -> Client Count


* Keyword Usage:

> 
> * `Get Network360Monitor Clients Health Client Count          floor_name=floor_01`


> * `Get Network360Monitor Clients Health Client Count`


* **Parameters**

    **floor_name** – floor_name. if no floor_name passed, returns the values for Global View



* **Returns**

    returns client_count_2G, client_count_5G, client_count_6G



#### get_network360monitor_device_health_overall_score(floor_name='default')

* This keyword returns the DEVICES card -> Overall Score


* Device Availability Score


* Device Hardware Health


* Config & Firmware Score


* Keyword Usage:

> 
> * `Get Network360Monitor Device Health Overall Score          floor_name=floor_01`


> * `Get Network360Monitor Device Health Overall Score`


* **Parameters**

    **floor_name** – floor_name. if no floor_name passed, returns the values for Global View



* **Returns**

    returns availability_score, hw_health, fw_health



#### get_network360monitor_devices_score(floor_name='default')

* This keyword returns the DEVICES card’s health score


* Keyword Usage:

> 
> * `Get Network360Monitor Devices Score             floor_name=floor_03`


> * `Get Network360Monitor Devices Score`


* **Parameters**

    **floor_name** – floor_name. if no floor_name passed, returns the values for Global View



* **Returns**

    returns the devices score Ex: 94/100 EXCELLENT



#### search_floor_in_network360monitor(floor_name='default')

* This keyword searches for the floor in Network360 Monitor


* Keyword Usage:

> 
> * `${SEARCH_MATCHES}=     Search Floor in Network360Monitor              floor_name=floor_02`


* **Parameters**

    **floor_name** – floor of the location where devices has been assigned



* **Returns**

    returns list of search matches. -1 if no matches


## extauto.xiq.flows.mlinsights.Network360Plan module


### _class_ extauto.xiq.flows.mlinsights.Network360Plan.Network360Plan()
Bases: `object`


#### get_aps_from_network360plan_floor(floor_name='default', device_type='default')

* This keyword gets devices name from Network360 Plan page


* Keyword Usage:

> 
> * `${AP_MATCHES}=          Get APs From Network360Plan Floor           floor_name=floor_02`


* **Parameters**

    
    * **floor_name** – floor of the location where devices has been assigned


    * **device_type** – optional - type of device - AP/switch/router/VGVA/router



* **Returns**

    devices name



#### import_map_in_network360plan(map_file_name)

* This keyword will Import Map file in Network360 Plan page


* Keyword Usage:

> 
> * Import Map In Network360Plan    ${MAP_FILE_NAME}


* **Parameters**

    **map_file_name** – Map File Name to import from /testsuites/xiq/functional/import_map_files directory



* **Returns**

    1 if map uploaded successfully on Network360 Plan else -1



#### n360_elements()
Need to build a string that represents the location of the map files
In a VM the path would be:
‘/automation/framework/extreme_automation_framework/extauto/xiq/configs/maps’
Since not everyone is using a VM the begining of the path can be different.
To handle this condition, we will get the path of this file and split it into variables.
Then remove 3 directories from the end, and rebuild the path to include configs/maps/


#### search_floor_in_network360plan(floor_name='default')

* This keyword searches for the floor in Network360 Plan


* Keyword Usage:

> 
> * `${SEARCH_MATCHES}=     Search Floor in Network360Plan              floor_name=floor_02`


* **Parameters**

    **floor_name** – floor of the location where devices has been assigned



* **Returns**

    returns list of search matches. -1 if no matches


## extauto.xiq.flows.mlinsights.Network360ScoreCard module


### _class_ extauto.xiq.flows.mlinsights.Network360ScoreCard.Network360ScoreCard()
Bases: `object`


#### goto_ml_insights_score_card()

* This keyword navigates to Network360 Plan page


* **Returns**

    returns 1 if successful



#### score_card_details()

* This keyword gets details of N360 Score Card page


* **Returns**

    dictionary of Score Card details


## Module contents
