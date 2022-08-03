# A3Inventory module


### _class_ extauto.a3.flows.a3.A3Inventory.A3Inventory()
Bases: `A3InventoryWebElements`


#### verify_a3_server_login_on_xiq(a3_host_name, a3_login_username, a3_login_password)

* This keyword will verify A3 Server Access from XIQ UI using Go To A3 Button and Check A3 Login via XIQ


* Assume that navigated to the A3 –> Inventory


* Keyword Usage:

> 
> * `Verify A3 Server Login On XIQ   ${A3_IP_ADDR}   ${A3_USERNAME}  ${A3_PASSWORD}`


* **Parameters**

    
    * **a3_host_name** – A3 Server Host Name


    * **a3_login_username** – A3 Login Name to Access A3 UI


    * **a3_login_password** – A3 Login Password Access A3 UI



* **Returns**

    A3 UI Page Title if Able to Login Successfully
