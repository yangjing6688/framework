# extauto.xiqse.flows.analytics package

## Subpackages


* [extauto.xiqse.flows.analytics.browser package](flows.analytics.browser.md)


* [extauto.xiqse.flows.analytics.configuration package](flows.analytics.configuration.md)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfiguration module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfiguration)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationAddEngine module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationAddEngine)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationDeleteEngine module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationDeleteEngine)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceAllEngines module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceAllEngines)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceEngine module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceEngine)


    * [extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationRestartCollector module](flows.analytics.configuration.md#module-extauto.xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationRestartCollector)


* [extauto.xiqse.flows.analytics.dashboard package](flows.analytics.dashboard.md)


* [extauto.xiqse.flows.analytics.fingerprints package](flows.analytics.fingerprints.md)


* [extauto.xiqse.flows.analytics.flows package](flows.analytics.flows.md)


    * [extauto.xiqse.flows.analytics.flows.XIQSE_AnalyticsApplicationFlows module](flows.analytics.flows.md#module-extauto.xiqse.flows.analytics.flows.XIQSE_AnalyticsApplicationFlows)


* [extauto.xiqse.flows.analytics.packet_captures package](flows.analytics.packet_captures.md)


* [extauto.xiqse.flows.analytics.reports package](flows.analytics.reports.md)


## extauto.xiqse.flows.analytics.XIQSE_Analytics module


### _class_ extauto.xiqse.flows.analytics.XIQSE_Analytics.XIQSE_Analytics()
Bases: `AnalyticsWebElements`


#### xiqse_analytics_select_application_flows_tab()
> 
> * This keyword selects the Application Flows tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Application Flows Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_browser_tab()
> 
> * This keyword selects the Browser tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Browser Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_configuration_tab()
> 
> * This keyword selects the Configuration tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Configuration Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_dashboard_tab()
> 
> * This keyword selects the Dashboard tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Dashboard Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_fingerprints_tab()
> 
> * This keyword selects the Fingerprints tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Fingerprints Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_packet_captures_tab()
> 
> * This keyword selects the Packet Captures tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Packet Captures Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_reports_tab()
> 
> * This keyword selects the Reports tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Reports Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_analytics_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Analytics page


> * Keyword Usage

> > 
> > * `XIQSE Analytics Select Tab    Dashboard`


> > * `XIQSE Analytics Select Tab    Browser`


> > * `XIQSE Analytics Select Tab    Application Flows`


> > * `XIQSE Analytics Select Tab    Fingerprints`


> > * `XIQSE Analytics Select Tab    Packet Captures`


> > * `XIQSE Analytics Select Tab    Configuration`


> > * `XIQSE Analytics Select Tab    Reports`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1
