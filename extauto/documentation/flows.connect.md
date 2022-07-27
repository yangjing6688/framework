# extauto.xiqse.flows.connect package


* [extauto.xiqse.flows.connect.configuration package](flows.connect.configuration.md)


    * [extauto.xiqse.flows.connect.configuration.XIQSE_ConnectConfiguration module](flows.connect.configuration.md#module-extauto.xiqse.flows.connect.configuration.XIQSE_ConnectConfiguration)


* [extauto.xiqse.flows.connect.diagnostics package](flows.connect.diagnostics.md)


    * [extauto.xiqse.flows.connect.diagnostics.XIQSE_ConnectDiagnostics module](flows.connect.diagnostics.md#module-extauto.xiqse.flows.connect.diagnostics.XIQSE_ConnectDiagnostics)


* [extauto.xiqse.flows.connect.services_api package](flows.connect.services_api.md)


## extauto.xiqse.flows.connect.XIQSE_Connect module


### _class_ extauto.xiqse.flows.connect.XIQSE_Connect.XIQSE_Connect()
Bases: `ConnectWebElements`


#### xiqse_connect_select_configuration_tab()
> 
> * This keyword selects the Configuration tab of the Connect page


> * Keyword Usage

> > 
> > * `XIQSE Connect Select Configuration Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_connect_select_diagnostics_tab()
> 
> * This keyword selects the Diagnostics tab of the Connect page


> * Keyword Usage

> > 
> > * `XIQSE Connect Select Diagnostics Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_connect_select_services_api_tab()
> 
> * This keyword selects the Services API tab of the Connect page


> * Keyword Usage

> > 
> > * `XIQSE Connect Select Services API Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_connect_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Connect page


> * Keyword Usage

> > 
> > * `XIQSE Connect Select Tab    Configuration`


> > * `XIQSE Connect Select Tab    Diagnostics`


> > * `XIQSE Connect Select Tab    Services API`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1
