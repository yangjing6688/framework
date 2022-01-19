

class AlarmsEventsWebElementsDefinitions:

    alarms_tab = \
        {
            'DESC': 'Alarms & Events> Alarms Tab',
            'XPATH': '//span[text()="Alarms" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    alarm_config_tab = \
        {
            'DESC': 'Alarms & Events> Alarm Configuration Tab',
            'XPATH': '//span[text()="Alarm Configuration" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    events_tab = \
        {
            'DESC': 'Alarms & Events> Events Tab',
            'XPATH': '//span[text()="Events" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    event_config_tab = \
        {
            'DESC': 'Alarms & Events> Event Configuration Tab',
            'XPATH': '//span[text()="Event Configuration" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
