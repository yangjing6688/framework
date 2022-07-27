# extauto.xiqse.flows.alarms_events package

## Subpackages


* [extauto.xiqse.flows.alarms_events.alarm_config package](flows.alarms_events.alarm_config.md)


* [extauto.xiqse.flows.alarms_events.alarms package](flows.alarms_events.alarms.md)


    * [extauto.xiqse.flows.alarms_events.alarms.XIQSE_AlarmsEventsAlarms module](flows.alarms_events.alarms.md#module-extauto.xiqse.flows.alarms_events.alarms.XIQSE_AlarmsEventsAlarms)


* [extauto.xiqse.flows.alarms_events.event_config package](flows.alarms_events.event_config.md)


    * [Subpackages](flows.alarms_events.event_config.md#subpackages)


        * [extauto.xiqse.flows.alarms_events.event_config.event_logs package](flows.alarms_events.event_config.event_logs.md)


        * [extauto.xiqse.flows.alarms_events.event_config.event_patterns package](flows.alarms_events.event_config.event_patterns.md)


    * [extauto.xiqse.flows.alarms_events.event_config.XIQSE_AlarmsEventsEventConfig module](flows.alarms_events.event_config.md#module-extauto.xiqse.flows.alarms_events.event_config.XIQSE_AlarmsEventsEventConfig)


* [extauto.xiqse.flows.alarms_events.events package](flows.alarms_events.events.md)


    * [extauto.xiqse.flows.alarms_events.events.XIQSE_AlarmsEventsEvents module](flows.alarms_events.events.md#module-extauto.xiqse.flows.alarms_events.events.XIQSE_AlarmsEventsEvents)


## extauto.xiqse.flows.alarms_events.XIQSE_AlarmsEvents module


### _class_ extauto.xiqse.flows.alarms_events.XIQSE_AlarmsEvents.XIQSE_AlarmsEvents()
Bases: `AlarmsEventsWebElements`


#### xiqse_alarmsevents_select_alarm_configuration_tab()
> 
> * This keyword selects the Alarm Configuration tab of the Alarms & Events page


> * Keyword Usage

> > 
> > * `XIQSE AlarmsEvents Select Alarm Configuration Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarmsevents_select_alarms_tab()
> 
> * This keyword selects the Alarms tab of the Alarms & Events page


> * Keyword Usage

> > 
> > * `XIQSE AlarmsEvents Select Alarms Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarmsevents_select_event_configuration_tab()
> 
> * This keyword selects the Event Configuration tab of the Alarms & Events page


> * Keyword Usage

> > 
> > * `XIQSE AlarmsEvents Select Event Configuration Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarmsevents_select_events_tab()
> 
> * This keyword selects the Events tab of the Alarms & Events page


> * Keyword Usage

> > 
> > * `XIQSE AlarmsEvents Select Events Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_alarmsevents_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Alarms & Events page


> * Keyword Usage

> > 
> > * `XIQSE AlarmsEvents Select Tab    Alarms`


> > * `XIQSE AlarmsEvents Select Tab    Alarm Configuration`


> > * `XIQSE AlarmsEvents Select Tab    Events`


> > * `XIQSE AlarmsEvents Select Tab    Event Configuration`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1
